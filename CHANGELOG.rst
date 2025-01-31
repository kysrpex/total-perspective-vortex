2.2.2 - Apr 25, 2023. (sha 3ab3f209ffdf3117a2efcc8cf70ebbf4c57efc6f)
--------------------------------------------------------------------
* Fix formatter ordering of inherits field by @nuwang (PR #90)
* Add helpers for tool version comparison by @cat-bro (PR #91)
* Fix dry run user by @cat-bro (PR #92)
* Failing test for pulsar user scenario by @cat-bro and @nuwang (PR #93)

2.2.1 - Mar 30, 2023. (sha 060ff9e411b35a2fed444b19b61bbedfe2d2cc4d)
--------------------------------------------------------------------
* A role rule has no access to a tool's scheduling tags by @cat-bro (PR #89)

2.2.0 - Mar 22, 2023. (sha 129c65b58998661da325294fa8461f0a48fcebb0)
--------------------------------------------------------------------
* Add helper for checking entity tags within a tpv rule by @cat-bro (PR #86)
* Remove condition from tpv packaging by @nuwang (PR #87)
* refactor: remove unnecessary overrides of superclass __init__ by @nuwang (PR #88)

2.1.0 - Mar 06, 2023. (sha 0f47032a1faf416b34969fb26c332428cb74209a)
--------------------------------------------------------------------
* Automatically convert envs to string, but make sure params are preserved by @nuwang (PR #73)
* Fix indentation by @bernt-matthias in (PR #76)
* Convert env to a list compatible with Galaxy job conf by @natefoo in (PR #79)
* Fix missing app.config.is_set() in mock config for dry-run by @natefoo in (PR #80)
* Refactor and fix dryrun by @nuwang in (PR #82)
* Add initializer to handle empty sequence when reducing by @nuwang in (PR #84)

2.0.1 - Jan 11, 2023. (sha 8860c1d570ed94310f5ed57b2166390124d9bbf8)
--------------------------------------------------------------------
* create __init__.py in tpv core test folder by @bgruening (PR #70)

2.0.0 - Dec 24, 2022. (sha b593d5527bce51a7070684569dc8f19aff3d24e0)
--------------------------------------------------------------------
* Add a `tpv dry-run` subcommand by @natefoo (PR #52)
* Simplify TPV by disambiguating terms by @nuwang (PR #58)
* Additional context params by @nuwang (PR #62)
* Use only TPV defined destinations, ignoring job_conf by @nuwang (PR #63)
* Add support for abstract entities by @nuwang (PR #64)
* Add destination min accepted by @nuwang (PR #67)
* Shared rules inheritance test by @cat-bro (PR #68)
* Update github actions by @nuwang (PR #69)


1.4.1 - Nov 21, 2022. (sha 396afc17d0ba2f78e0827e6f8319246977994172)
--------------------------------------------------------------------
* Avoid deepcopying loader when cloning entities  (PR #54)
* Change remaining uses of pyyaml to ruaml.yaml (PR #51)
* Automatic PyPi deployment action (#43)


1.4.0 - Oct 12, 2022. (sha c4a49330a55f02107a9ece4ac84fd74f956f7017)
--------------------------------------------------------------------
* Added support for the execute block to change entity properties
* Added link to TPV shared database.


1.3.0 - Sep 28, 2022. (sha 3e9342622ab8bb2b6b18ef1fd32625e246eec66a)
--------------------------------------------------------------------
* Added tpv format command for prettying and ordering tpv tool lists
* Support for overriding destination name
* Fix some bugs in context variable handling
* Misc. bug fixes and refactoring


1.2.0 - Jun 15, 2022. (sha 872d200f3bfeb7356ba76bb1ee14134a50608d92)
--------------------------------------------------------------------
* vortex package and cli renamed to tpv for consistency.
* All matching entity regexes are applied, not just the first. Order of application is in the order of definition.
* When a particular entity type is matched, its definitions are cached, so that future lookups are O(1).
* Support for job resubmission handling, with integration tests for Galaxy,
* Allow destinations to be treated as regular entities, with support for rules and expressions.
* Support for global and local context variables that can be referenced in expressions.
* Improved support for complex jobs param types like dicts and lists, which are now recursively evaluated.


1.1.0 - Mar 25, 2022. (sha 0e65d9a6a16bbbfd463031677067e1af9f4dac64)
--------------------------------------------------------------------
* The "match" clause has been deprecated and renamed to "if", for easier readability of rules.
* When no default mapping for a tool exists, choose the first available destination for a simpler initial experience.
* A sample config file has been added to provide a starting point for new TPV users.


1.0.0 - Mar 07, 2022. (sha 2e082a4ec0868e03df1b902562810873421823e5)
--------------------------------------------------------------------
* Initial PyPi release of total-perspective-vortex.
* Basic usage docs and examples.
* 94% test coverage.
