# Startup Initialization
TODO: startup\_initialization description


-------------

## Startup Warnings
Check various expected startup conditions, such as whether mongod is running in 32 bit mode or on a numa machine, and log warnings to the startup warnings log if necessary

#### Files
- src/mongo/db/startup\_warnings.cpp   (mongod, tools)
- src/mongo/db/startup\_warnings.h   (mongod, tools)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Initialization Framework
MONGO\_INITIALIZER startup initialization framework.  Used by anything that shares the server code, which currently includes the tools and the mongo shell

#### Files
- src/mongo/base/global\_initializer.cpp   (mongod, tools, mongos)
- src/mongo/base/global\_initializer.h   (mongod, tools, mongos)
- src/mongo/base/global\_initializer\_registerer.cpp   (mongod, tools, mongos)
- src/mongo/base/global\_initializer\_registerer.h   (mongod, tools, mongos)
- src/mongo/base/init.cpp   (mongod, tools, mongos)
- src/mongo/base/init.h   (mongod, tools, mongos)
- src/mongo/base/initializer.cpp   (mongod, tools, mongos)
- src/mongo/base/initializer.h   (mongod, tools, mongos)
- src/mongo/base/initializer\_context.cpp   (mongod, tools, mongos)
- src/mongo/base/initializer\_context.h   (mongod, tools, mongos)
- src/mongo/base/initializer\_dependency\_graph.cpp   (mongod, tools, mongos)
- src/mongo/base/initializer\_dependency\_graph.h   (mongod, tools, mongos)
- src/mongo/base/initializer\_dependency\_graph\_test.cpp   ()
- src/mongo/base/initializer\_function.h   (mongod, tools, mongos)
- src/mongo/base/initializer\_test.cpp   ()
- src/mongo/base/make\_string\_vector.cpp   (mongod, tools, mongos)
- src/mongo/base/make\_string\_vector.h   (mongod, tools, mongos)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Global State Initialization
Initialize the global state common to mongod and mongos, such as logging.

#### Files
- src/mongo/db/initialize\_server\_global\_state.cpp   (mongod, mongos)
- src/mongo/db/initialize\_server\_global\_state.h   (mongod, mongos)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Options Parser
Options parser library (command line and config files)

#### Files
- src/mongo/util/options\_parser/constraints.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/constraints.h   (mongod, tools, mongos)
- src/mongo/util/options\_parser/environment.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/environment.h   (mongod, tools, mongos)
- src/mongo/util/options\_parser/environment\_test.cpp   ()
- src/mongo/util/options\_parser/option\_description.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/option\_description.h   (mongod, tools, mongos)
- src/mongo/util/options\_parser/option\_section.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/option\_section.h   (mongod, tools, mongos)
- src/mongo/util/options\_parser/options\_parser.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/options\_parser.h   (mongod, tools, mongos)
- src/mongo/util/options\_parser/options\_parser\_init.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/options\_parser\_test.cpp   ()
- src/mongo/util/options\_parser/startup\_option\_init.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/startup\_option\_init.h   (mongod, tools, mongos)
- src/mongo/util/options\_parser/startup\_options.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/startup\_options.h   (mongod, tools, mongos)
- src/mongo/util/options\_parser/value.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/value.h   (mongod, tools, mongos)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Command Line Censorship
Utilities to censor passwords read in at startup

#### Files
- src/mongo/util/cmdline\_utils/censor\_cmdline.cpp   (mongod, tools, mongos)
- src/mongo/util/cmdline\_utils/censor\_cmdline.h   (mongod, tools, mongos)
- src/mongo/util/cmdline\_utils/censor\_cmdline\_test.cpp   ()

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## Password Prompt
Only used to ask user for password at startup. TODO: move into cmdline\_utils directory

#### Files
- src/mongo/util/password.cpp   (mongod, tools, mongos)
- src/mongo/util/password.h   (mongod, tools, mongos)

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

## Server Parameters
ServerParameter class used to add new parameters to the "setParameter" command. These can also be  configured to be runtime modifiable.

#### Files
- src/mongo/db/server\_parameters.cpp   (mongod, tools, mongos)
- src/mongo/db/server\_parameters.h   (mongod, tools, mongos)
- src/mongo/db/server\_parameters\_inline.h   (mongod, tools, mongos)
- src/mongo/db/server\_parameters\_test.cpp   ()

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)
