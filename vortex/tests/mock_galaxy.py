import os

from galaxy.job_metrics import JobMetrics
from galaxy.jobs import JobConfiguration
from galaxy.util import bunch
from galaxy.web_stack import ApplicationStack


# Job mock and helpers=======================================
class Job:
    def __init__(self):
        self.input_datasets = []
        self.input_library_datasets = []
        self.param_values = dict()
        self.parameters = []

    def get_param_values(self, app, ignore_errors=False):
        return self.param_values

    def set_arg_value(self, key, value):
        self.param_values[key] = value

    def add_input_dataset(self, dataset):
        self.input_datasets.append(dataset)

    def get_parameters(self):
        return self.parameters


class InputDataset:
    def __init__(self, name, dataset):
        self.name = name
        self.dataset = dataset


class Dataset:
    def __init__(self, file_name, file_ext, value):
        self.file_name = file_name
        self.datatype = Datatype(file_ext)
        self.ext = file_ext
        self.metadata = dict()
        self.metadata['sequences'] = value

    def get_metadata(self):
        return self.metadata


class Datatype:
    def __init__(self, file_ext):
        self.file_ext = file_ext


# Tool mock and helpers=========================================
class Tool:
    def __init__(self, id):
        self.id = id
        self.old_id = id
        self.installed_tool_dependencies = []

    def add_tool_dependency(self, dependency):
        self.installed_tool_dependencies.append(dependency)


class ToolDependency:
    def __init__(self, name, dir_name):
        self.name = name
        self.dir_name = dir_name

    def installation_directory(self, app):
        return self.dir_name


# App mock=======================================================
class App:
    def __init__(self):
        self.config = bunch.Bunch(
            job_config_file=os.path.join(os.path.dirname(__file__), 'fixtures/job_conf.yml'),
            use_tasked_jobs=False,
            job_resource_params_file="/tmp/fake_absent_path",
            config_dict={},
            default_job_resubmission_condition="",
            track_jobs_in_database=True,
            server_name="main",
        )
        self.application_stack = ApplicationStack()
        self.job_metrics = JobMetrics()
        self.job_config = JobConfiguration(self)


# JobMappingException mock=======================================
class JobMappingException(Exception):
    pass


class JobDestination:
    def __init__(self, **kwd):
        self.id = kwd.get('id')
        self.nativeSpec = kwd.get('params')['nativeSpecification']
        self.runner = kwd.get('runner')


class User:
    def __init__(self, username, email, roles=[]):
        self.username = username
        self.email = email
        self.roles = roles

    def all_roles(self):
        """
        Return a unique list of Roles associated with this user or any of their groups.
        """
        return self.roles
