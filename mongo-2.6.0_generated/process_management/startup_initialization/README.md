# Startup Initialization
TODO: startup\_initialization description


-------------

## Startup Warnings
Check various expected startup conditions, such as whether mongod is running in 32 bit mode or on a numa machine, and log warnings to the startup warnings log if necessary

#### Files
- [src/mongo/db/startup\_warnings.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/startup_warnings.cpp)   (mongod, tools)
- [src/mongo/db/startup\_warnings.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/startup_warnings.h)   (mongod, tools)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Initialization Framework
MONGO\_INITIALIZER startup initialization framework.  Used by anything that shares the server code, which currently includes the tools and the mongo shell

#### Files
- [src/mongo/base/global\_initializer.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/base/global_initializer.cpp)   (mongod, tools, mongos)
- [src/mongo/base/global\_initializer.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/base/global_initializer.h)   (mongod, tools, mongos)
- [src/mongo/base/global\_initializer\_registerer.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/base/global_initializer_registerer.cpp)   (mongod, tools, mongos)
- [src/mongo/base/global\_initializer\_registerer.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/base/global_initializer_registerer.h)   (mongod, tools, mongos)
- [src/mongo/base/init.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/base/init.cpp)   (mongod, tools, mongos)
- [src/mongo/base/init.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/base/init.h)   (mongod, tools, mongos)
- [src/mongo/base/initializer.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/base/initializer.cpp)   (mongod, tools, mongos)
- [src/mongo/base/initializer.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/base/initializer.h)   (mongod, tools, mongos)
- [src/mongo/base/initializer\_context.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/base/initializer_context.cpp)   (mongod, tools, mongos)
- [src/mongo/base/initializer\_context.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/base/initializer_context.h)   (mongod, tools, mongos)
- [src/mongo/base/initializer\_dependency\_graph.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/base/initializer_dependency_graph.cpp)   (mongod, tools, mongos)
- [src/mongo/base/initializer\_dependency\_graph.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/base/initializer_dependency_graph.h)   (mongod, tools, mongos)
- [src/mongo/base/initializer\_dependency\_graph\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/base/initializer_dependency_graph_test.cpp)   ()
- [src/mongo/base/initializer\_function.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/base/initializer_function.h)   (mongod, tools, mongos)
- [src/mongo/base/initializer\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/base/initializer_test.cpp)   ()
- [src/mongo/base/make\_string\_vector.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/base/make_string_vector.cpp)   (mongod, tools, mongos)
- [src/mongo/base/make\_string\_vector.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/base/make_string_vector.h)   (mongod, tools, mongos)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Global State Initialization
Initialize the global state common to mongod and mongos, such as logging.

#### Files
- [src/mongo/db/initialize\_server\_global\_state.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/initialize_server_global_state.cpp)   (mongod, mongos)
- [src/mongo/db/initialize\_server\_global\_state.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/initialize_server_global_state.h)   (mongod, mongos)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Options Parser
Options parser library (command line and config files)

#### Files
- [src/mongo/util/options\_parser/constraints.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/options_parser/constraints.cpp)   (mongod, tools, mongos)
- [src/mongo/util/options\_parser/constraints.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/options_parser/constraints.h)   (mongod, tools, mongos)
- [src/mongo/util/options\_parser/environment.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/options_parser/environment.cpp)   (mongod, tools, mongos)
- [src/mongo/util/options\_parser/environment.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/options_parser/environment.h)   (mongod, tools, mongos)
- [src/mongo/util/options\_parser/environment\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/options_parser/environment_test.cpp)   ()
- [src/mongo/util/options\_parser/option\_description.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/options_parser/option_description.cpp)   (mongod, tools, mongos)
- [src/mongo/util/options\_parser/option\_description.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/options_parser/option_description.h)   (mongod, tools, mongos)
- [src/mongo/util/options\_parser/option\_section.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/options_parser/option_section.cpp)   (mongod, tools, mongos)
- [src/mongo/util/options\_parser/option\_section.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/options_parser/option_section.h)   (mongod, tools, mongos)
- [src/mongo/util/options\_parser/options\_parser.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/options_parser/options_parser.cpp)   (mongod, tools, mongos)
- [src/mongo/util/options\_parser/options\_parser.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/options_parser/options_parser.h)   (mongod, tools, mongos)
- [src/mongo/util/options\_parser/options\_parser\_init.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/options_parser/options_parser_init.cpp)   (mongod, tools, mongos)
- [src/mongo/util/options\_parser/options\_parser\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/options_parser/options_parser_test.cpp)   ()
- [src/mongo/util/options\_parser/startup\_option\_init.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/options_parser/startup_option_init.cpp)   (mongod, tools, mongos)
- [src/mongo/util/options\_parser/startup\_option\_init.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/options_parser/startup_option_init.h)   (mongod, tools, mongos)
- [src/mongo/util/options\_parser/startup\_options.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/options_parser/startup_options.cpp)   (mongod, tools, mongos)
- [src/mongo/util/options\_parser/startup\_options.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/options_parser/startup_options.h)   (mongod, tools, mongos)
- [src/mongo/util/options\_parser/value.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/options_parser/value.cpp)   (mongod, tools, mongos)
- [src/mongo/util/options\_parser/value.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/options_parser/value.h)   (mongod, tools, mongos)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Command Line Censorship
Utilities to censor passwords read in at startup

#### Files
- [src/mongo/util/cmdline\_utils/censor\_cmdline.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/cmdline_utils/censor_cmdline.cpp)   (mongod, tools, mongos)
- [src/mongo/util/cmdline\_utils/censor\_cmdline.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/cmdline_utils/censor_cmdline.h)   (mongod, tools, mongos)
- [src/mongo/util/cmdline\_utils/censor\_cmdline\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/cmdline_utils/censor_cmdline_test.cpp)   ()

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## Password Prompt
Only used to ask user for password at startup. TODO: move into cmdline\_utils directory

#### Files
- [src/mongo/util/password.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/password.cpp)   (mongod, tools, mongos)
- [src/mongo/util/password.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/password.h)   (mongod, tools, mongos)

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

## Server Parameters
ServerParameter class used to add new parameters to the "setParameter" command. These can also be  configured to be runtime modifiable.

#### Files
- [src/mongo/db/server\_parameters.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/server_parameters.cpp)   (mongod, tools, mongos)
- [src/mongo/db/server\_parameters.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/server_parameters.h)   (mongod, tools, mongos)
- [src/mongo/db/server\_parameters\_inline.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/server_parameters_inline.h)   (mongod, tools, mongos)
- [src/mongo/db/server\_parameters\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/server_parameters_test.cpp)   ()

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)
