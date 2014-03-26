# Startup Initialization

# Module Groups

-------------

# TODO: Name this group
Check various expected startup conditions and log warnings to the user if necessary   what uses these? everything? mongod/mongos only? what sort of checks?

## Files
- src/mongo/db/startup\_warnings.cpp   (mongod, tools)
- src/mongo/db/startup\_warnings.h   (mongod, tools)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

# TODO: Name this group
MONGO\_INITIALIZER startup initialization framework.   what should use these? any tool? mongod/mongos only?

## Files
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

# TODO: Name this group
Initialize the global state common to mongod and mongos, such as logging.

## Files
- src/mongo/db/initialize\_server\_global\_state.cpp   (mongod, mongos)
- src/mongo/db/initialize\_server\_global\_state.h   (mongod, mongos)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

# TODO: Name this group
Options parser library (command line and config files)   where do the options get stored / how can people grab options later?   are they set once and immutable or can they be updated?

## Files
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

# TODO: Name this group
Command line utilities   can you say a bit more? (give an example?)

## Files
- src/mongo/util/cmdline\_utils/censor\_cmdline.cpp   (mongod, tools, mongos)
- src/mongo/util/cmdline\_utils/censor\_cmdline.h   (mongod, tools, mongos)
- src/mongo/util/cmdline\_utils/censor\_cmdline\_test.cpp   ()

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

# TODO: Name this group
Only used to ask user for password at startup. TODO: move into cmdline\_utils directory

## Files
- src/mongo/util/password.cpp   (mongod, tools, mongos)
- src/mongo/util/password.h   (mongod, tools, mongos)

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

# TODO: Name this group
Command line options shared between mongod and mongos   give an example (--hostname?)

## Files
- src/mongo/db/server\_options.cpp   (mongod, tools, mongos)
- src/mongo/db/server\_options.h   (mongod, tools, mongos)
- src/mongo/db/server\_options\_helpers.cpp   (mongod, tools, mongos)
- src/mongo/db/server\_options\_helpers.h   (mongod, tools, mongos)
- src/mongo/db/server\_options\_test.cpp   ()

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)

-------------

# TODO: Name this group
ServerParameter class used to add new parameters to the "setParameter" command. These can also be  configured to be runtime modifiable.

## Files
- src/mongo/db/server\_parameters.cpp   (mongod, tools, mongos)
- src/mongo/db/server\_parameters.h   (mongod, tools, mongos)
- src/mongo/db/server\_parameters\_inline.h   (mongod, tools, mongos)
- src/mongo/db/server\_parameters\_test.cpp   ()

#### [Interface](interface/7)

#### [Dependencies](dependencies/7)
