# startup\_initialization

# Module Groups

-------------

Check various expected startup conditions and log warnings to the user if necessary   what uses these? everything? mongod/mongos only? what sort of checks?

- src/mongo/db/startup\_warnings.cpp   (mongod, tools)
- src/mongo/db/startup\_warnings.h

-------------

MONGO\_INITIALIZER startup initialization framework.   what should use these? any tool? mongod/mongos only?

- src/mongo/base/global\_initializer.cpp   (cppclientdriver)
- src/mongo/base/global\_initializer.h
- src/mongo/base/global\_initializer\_registerer.cpp   (mongod, tools, mongos)
- src/mongo/base/global\_initializer\_registerer.h
- src/mongo/base/init.cpp   (cppclientdriver)
- src/mongo/base/init.h
- src/mongo/base/initializer.cpp   (mongod, tools, mongos)
- src/mongo/base/initializer.h
- src/mongo/base/initializer\_context.cpp   (mongod, tools, mongos)
- src/mongo/base/initializer\_context.h
- src/mongo/base/initializer\_dependency\_graph.cpp   (cppclientdriver)
- src/mongo/base/initializer\_dependency\_graph.h
- src/mongo/base/initializer\_dependency\_graph\_test.cpp   ()
- src/mongo/base/initializer\_function.h
- src/mongo/base/initializer\_test.cpp   ()
- src/mongo/base/make\_string\_vector.cpp   (mongod, tools, mongos)
- src/mongo/base/make\_string\_vector.h

-------------

Initialize the global state common to mongod and mongos, such as logging.

- src/mongo/db/initialize\_server\_global\_state.cpp   (mongod, mongos)
- src/mongo/db/initialize\_server\_global\_state.h

-------------

Options parser library (command line and config files)   where do the options get stored / how can people grab options later?   are they set once and immutable or can they be updated?

- src/mongo/util/options\_parser/constraints.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/constraints.h
- src/mongo/util/options\_parser/environment.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/environment.h
- src/mongo/util/options\_parser/environment\_test.cpp   ()
- src/mongo/util/options\_parser/option\_description.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/option\_description.h
- src/mongo/util/options\_parser/option\_section.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/option\_section.h
- src/mongo/util/options\_parser/options\_parser.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/options\_parser.h
- src/mongo/util/options\_parser/options\_parser\_init.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/options\_parser\_test.cpp   ()
- src/mongo/util/options\_parser/startup\_option\_init.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/startup\_option\_init.h
- src/mongo/util/options\_parser/startup\_options.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/startup\_options.h
- src/mongo/util/options\_parser/value.cpp   (mongod, tools, mongos)
- src/mongo/util/options\_parser/value.h

-------------

Command line utilities   can you say a bit more? (give an example?)

- src/mongo/util/cmdline\_utils/censor\_cmdline.cpp   (mongod, tools, mongos)
- src/mongo/util/cmdline\_utils/censor\_cmdline.h
- src/mongo/util/cmdline\_utils/censor\_cmdline\_test.cpp   ()

-------------

Only used to ask user for password at startup. TODO: move into cmdline\_utils directory

- src/mongo/util/password.cpp   (mongod, tools, mongos)
- src/mongo/util/password.h

-------------

Command line options shared between mongod and mongos   give an example (--hostname?)

- src/mongo/db/server\_options.cpp   (mongod, tools, mongos)
- src/mongo/db/server\_options.h
- src/mongo/db/server\_options\_helpers.cpp   (mongod, tools, mongos)
- src/mongo/db/server\_options\_helpers.h
- src/mongo/db/server\_options\_test.cpp   ()

-------------

ServerParameter class used to add new parameters to the "setParameter" command. These can also be  configured to be runtime modifiable.

- src/mongo/db/server\_parameters.cpp   (mongod, tools, mongos)
- src/mongo/db/server\_parameters.h
- src/mongo/db/server\_parameters\_inline.h
- src/mongo/db/server\_parameters\_test.cpp   ()
