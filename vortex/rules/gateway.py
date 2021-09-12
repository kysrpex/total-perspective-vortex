import logging

from galaxy.util.watcher import get_watcher
from vortex.core.resources import ResourceDestinationParser
from vortex.core.mapper import ResourceToDestinationMapper

log = logging.getLogger(__name__)


ACTIVE_DESTINATION_MAPPER = None


def load_destination_mapper(mapper_config_file):
    log.info(f"loading vortex rules from: {mapper_config_file}")
    parser = ResourceDestinationParser.from_file_path(mapper_config_file)
    return ResourceToDestinationMapper(parser.tools, parser.users, parser.roles, parser.destinations)


def reload_destination_mapper(path=None):
    log.info(f"reloading vortex rules from: {path}")
    global ACTIVE_DESTINATION_MAPPER
    ACTIVE_DESTINATION_MAPPER = load_destination_mapper(path)


def setup_destination_mapper(app, mapper_config_file):
    mapper = load_destination_mapper(mapper_config_file)
    job_rule_watcher = get_watcher(app.config, 'watch_job_rules', monitor_what_str='job rules')
    job_rule_watcher.watch_file(mapper_config_file, callback=reload_destination_mapper)
    job_rule_watcher.start()
    return mapper


def map_tool_to_destination(app, job, tool, user, mapper_config_file):
    global ACTIVE_DESTINATION_MAPPER
    if not ACTIVE_DESTINATION_MAPPER:
        ACTIVE_DESTINATION_MAPPER = setup_destination_mapper(app, mapper_config_file)
    return ACTIVE_DESTINATION_MAPPER.map_to_destination(app, tool, user, job)
