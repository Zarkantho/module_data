# logging\_system

# Module Groups

-------------

jesus, i hope this becomes a library :)   can you say a bit about what kind of logging we do? is there any sort of   ordering or atomicity (maybe per-call-to-log, or per log line?) our   logging guarantees? 'log lines are emitted in-order with respect to each   process thread?' maybe?)  Logging system (NOTE: The first two actually aren't part of the "logger" library, but I see no  reason why they should not be)

- src/mongo/util/log.cpp   (mongod, tools, mongos)
- src/mongo/util/log.h
- src/mongo/logger/appender.h
- src/mongo/logger/console.cpp   (cppclientdriver)
- src/mongo/logger/console.h
- src/mongo/logger/console\_appender.h
- src/mongo/logger/encoder.h
- src/mongo/logger/labeled\_level.h
- src/mongo/logger/log\_domain-impl.h
- src/mongo/logger/log\_domain.h
- src/mongo/logger/log\_manager.cpp   (mongod, tools, mongos)
- src/mongo/logger/log\_manager.h
- src/mongo/logger/log\_severity-inl.h
- src/mongo/logger/log\_severity.cpp   (mongod, tools, mongos)
- src/mongo/logger/log\_severity.h
- src/mongo/logger/log\_test.cpp   ()
- src/mongo/logger/logger.cpp   (cppclientdriver)
- src/mongo/logger/logger.h
- src/mongo/logger/logstream\_builder.cpp   (cppclientdriver)
- src/mongo/logger/logstream\_builder.h
- src/mongo/logger/message\_event.h
- src/mongo/logger/message\_event\_utf8\_encoder.cpp   (mongod, tools, mongos)
- src/mongo/logger/message\_event\_utf8\_encoder.h
- src/mongo/logger/message\_log\_domain.cpp   (cppclientdriver)
- src/mongo/logger/message\_log\_domain.h
- src/mongo/logger/ramlog.cpp   (mongod, tools, mongos)
- src/mongo/logger/ramlog.h
- src/mongo/logger/rotatable\_file\_appender.h
- src/mongo/logger/rotatable\_file\_manager.cpp   (mongod, tools, mongos)
- src/mongo/logger/rotatable\_file\_manager.h
- src/mongo/logger/rotatable\_file\_writer.cpp   (cppclientdriver)
- src/mongo/logger/rotatable\_file\_writer.h
- src/mongo/logger/rotatable\_file\_writer\_test.cpp   ()
- src/mongo/logger/syslog\_appender.h
- src/mongo/logger/tee.h

-------------

Helpers to dump a bunch of information about the current process   at crash time only? at any time? can you give an example of when   this is used?

- src/mongo/db/log\_process\_details.cpp   (mongod, tools, mongos)
- src/mongo/db/log\_process\_details.h

-------------

MONGO\_INITIALIZERs to add extra information to the server logs.

- src/mongo/db/server\_extra\_log\_context.cpp   (mongod, mongos)
