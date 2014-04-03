# Logging System
TODO: logging\_system description


-------------

## TODO: Name this group
TODO: Divide this into sections and document

#### Files
- src/mongo/util/log.cpp   (mongod, tools, mongos)
- src/mongo/util/log.h   (mongod, tools, mongos)
- src/mongo/logger/appender.h   (mongod, tools, mongos)
- src/mongo/logger/console.cpp   (mongod, tools, mongos)
- src/mongo/logger/console.h   (mongod, tools, mongos)
- src/mongo/logger/console\_appender.h   (mongod, tools, mongos)
- src/mongo/logger/encoder.h   (mongod, tools, mongos)
- src/mongo/logger/labeled\_level.h   (mongod, tools, mongos)
- src/mongo/logger/log\_domain-impl.h   (mongod, tools, mongos)
- src/mongo/logger/log\_domain.h   (mongod, tools, mongos)
- src/mongo/logger/log\_manager.cpp   (mongod, tools, mongos)
- src/mongo/logger/log\_manager.h   (mongod, tools, mongos)
- src/mongo/logger/log\_severity-inl.h   (mongod, tools, mongos)
- src/mongo/logger/log\_severity.cpp   (mongod, tools, mongos)
- src/mongo/logger/log\_severity.h   (mongod, tools, mongos)
- src/mongo/logger/log\_test.cpp   ()
- src/mongo/logger/logger.cpp   (mongod, tools, mongos)
- src/mongo/logger/logger.h   (mongod, tools, mongos)
- src/mongo/logger/logstream\_builder.cpp   (mongod, tools, mongos)
- src/mongo/logger/logstream\_builder.h   (mongod, tools, mongos)
- src/mongo/logger/message\_event.h   (mongod, tools, mongos)
- src/mongo/logger/message\_event\_utf8\_encoder.cpp   (mongod, tools, mongos)
- src/mongo/logger/message\_event\_utf8\_encoder.h   (mongod, tools, mongos)
- src/mongo/logger/message\_log\_domain.cpp   (mongod, tools, mongos)
- src/mongo/logger/message\_log\_domain.h   (mongod, tools, mongos)
- src/mongo/logger/ramlog.cpp   (mongod, tools, mongos)
- src/mongo/logger/ramlog.h   (mongod, tools, mongos)
- src/mongo/logger/rotatable\_file\_appender.h   (mongod, mongos)
- src/mongo/logger/rotatable\_file\_manager.cpp   (mongod, tools, mongos)
- src/mongo/logger/rotatable\_file\_manager.h   (mongod, tools, mongos)
- src/mongo/logger/rotatable\_file\_writer.cpp   (mongod, tools, mongos)
- src/mongo/logger/rotatable\_file\_writer.h   (mongod, tools, mongos)
- src/mongo/logger/rotatable\_file\_writer\_test.cpp   ()
- src/mongo/logger/syslog\_appender.h   (mongod, mongos)
- src/mongo/logger/tee.h   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## TODO: Name this group
Helpers to dump a bunch of information about the current process
TODO: at crash time only? at any time? can you give an example of when this is used?

#### Files
- src/mongo/db/log\_process\_details.cpp   (mongod, tools, mongos)
- src/mongo/db/log\_process\_details.h   (mongod, tools, mongos)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## TODO: Name this group
MONGO\_INITIALIZERs to add extra information to the server logs.

#### Files
- src/mongo/db/server\_extra\_log\_context.cpp   (mongod, mongos)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)