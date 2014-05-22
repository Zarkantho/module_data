# Logging System
System for managing log output from the server.  Currently this is also shared by the tools since the tools share much of the server code.


-------------

## Log System Interface
Helper functions that hide the more complex details of the logging function and provide a simple interface with which to log messages.  This is what you will be using if you are logging a message.

#### Files
- [src/mongo/util/log.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/log.cpp)   (mongod, tools, mongos)
- [src/mongo/util/log.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/log.h)   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Log System Globals Access
Free functions to get access to the global instances of the various components of the logging system.

#### Files
- [src/mongo/logger/logger.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/logger.cpp)   (mongod, tools, mongos)
- [src/mongo/logger/logger.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/logger.h)   (mongod, tools, mongos)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Log Appender
Interface for an object that logs can be appended to.  This is what allows us to plug different log sinks into the logging system.

#### Files
- [src/mongo/logger/appender.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/appender.h)   (mongod, tools, mongos)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Console Appender
Implementation of an appender that sends messages to a console.  For example, this is the appender that gets used when log messages are sent to stdout.

#### Files
- [src/mongo/logger/console.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/console.cpp)   (mongod, tools, mongos)
- [src/mongo/logger/console.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/console.h)   (mongod, tools, mongos)
- [src/mongo/logger/console\_appender.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/console_appender.h)   (mongod, tools, mongos)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Syslog Appender
Implementation of an appender that sends messages to syslog.

#### Files
- [src/mongo/logger/syslog\_appender.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/syslog_appender.h)   (mongod, mongos)

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## Ram Log
In memory log that can be accessed using the "getLog" command.  See http://docs.mongodb.org/manual/reference/command/getLog/.

#### Files
- [src/mongo/logger/ramlog.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/ramlog.cpp)   (mongod, tools, mongos)
- [src/mongo/logger/ramlog.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/ramlog.h)   (mongod, tools, mongos)

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

## Log Tee
Class that can be streamed to a log builder to add another output location for whatever gets sent to that log builder.

#### Files
- [src/mongo/logger/tee.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/tee.h)   (mongod, tools, mongos)

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)

-------------

## Log Domain
A class to manage appenders.  A single log domain can have many appenders (log sinks) attached to it.

#### Files
- [src/mongo/logger/log\_domain-impl.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/log_domain-impl.h)   (mongod, tools, mongos)
- [src/mongo/logger/log\_domain.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/log_domain.h)   (mongod, tools, mongos)
- [src/mongo/logger/message\_log\_domain.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/message_log_domain.cpp)   (mongod, tools, mongos)
- [src/mongo/logger/message\_log\_domain.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/message_log_domain.h)   (mongod, tools, mongos)

#### [Interface](interface/7)

#### [Dependencies](dependencies/7)

-------------

## Log Manager
Class to manage log domains.  Allows access to log domains by name.

#### Files
- [src/mongo/logger/log\_manager.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/log_manager.cpp)   (mongod, tools, mongos)
- [src/mongo/logger/log\_manager.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/log_manager.h)   (mongod, tools, mongos)

#### [Interface](interface/8)

#### [Dependencies](dependencies/8)

-------------

## Log Level
Classes representing the severity of log messages.  Currently, we log messages if they have a severity above the threshold set by the user, or if they are unconditional.

#### Files
- [src/mongo/logger/labeled\_level.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/labeled_level.h)   (mongod, tools, mongos)
- [src/mongo/logger/log\_severity-inl.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/log_severity-inl.h)   (mongod, tools, mongos)
- [src/mongo/logger/log\_severity.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/log_severity.cpp)   (mongod, tools, mongos)
- [src/mongo/logger/log\_severity.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/log_severity.h)   (mongod, tools, mongos)

#### [Interface](interface/9)

#### [Dependencies](dependencies/9)

-------------

## Message Event
Class containing all the details behind a log event, such as the date and the severity.

#### Files
- [src/mongo/logger/logstream\_builder.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/logstream_builder.cpp)   (mongod, tools, mongos)
- [src/mongo/logger/logstream\_builder.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/logstream_builder.h)   (mongod, tools, mongos)

#### [Interface](interface/10)

#### [Dependencies](dependencies/10)

-------------

## Message Event
Class containing all the details behind a log event, such as the date and the severity.

#### Files
- [src/mongo/logger/message\_event.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/message_event.h)   (mongod, tools, mongos)

#### [Interface](interface/11)

#### [Dependencies](dependencies/11)

-------------

## Encoder Interface
Interface for classes that take event objects and convert them to streams of data suitable for output to some log stream.

#### Files
- [src/mongo/logger/encoder.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/encoder.h)   (mongod, tools, mongos)

#### [Interface](interface/12)

#### [Dependencies](dependencies/12)

-------------

## Message Encoder
Classes that take message event objects, convert them to a form suitable to being output to a stream, and outputs them to a stream.  This is where the the format of the log messages and log message timestamps is handled.

#### Files
- [src/mongo/logger/message\_event\_utf8\_encoder.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/message_event_utf8_encoder.cpp)   (mongod, tools, mongos)
- [src/mongo/logger/message\_event\_utf8\_encoder.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/message_event_utf8_encoder.h)   (mongod, tools, mongos)

#### [Interface](interface/13)

#### [Dependencies](dependencies/13)

-------------

## Log Unittests
Some basic unittests of the logging system.

#### Files
- [src/mongo/logger/log\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/log_test.cpp)   ()

#### [Interface](interface/14)

#### [Dependencies](dependencies/14)

-------------

## Log File Rotation
Classes to allow MongoDB to support logfile rotation.

#### Files
- [src/mongo/logger/rotatable\_file\_appender.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/rotatable_file_appender.h)   (mongod, mongos)
- [src/mongo/logger/rotatable\_file\_manager.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/rotatable_file_manager.cpp)   (mongod, tools, mongos)
- [src/mongo/logger/rotatable\_file\_manager.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/rotatable_file_manager.h)   (mongod, tools, mongos)
- [src/mongo/logger/rotatable\_file\_writer.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/rotatable_file_writer.cpp)   (mongod, tools, mongos)
- [src/mongo/logger/rotatable\_file\_writer.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/rotatable_file_writer.h)   (mongod, tools, mongos)
- [src/mongo/logger/rotatable\_file\_writer\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/logger/rotatable_file_writer_test.cpp)   ()

#### [Interface](interface/15)

#### [Dependencies](dependencies/15)

-------------

## Process Info Loggers
Helpers to dump a bunch of information about the current process

#### Files
- [src/mongo/db/log\_process\_details.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/log_process_details.cpp)   (mongod, tools, mongos)
- [src/mongo/db/log\_process\_details.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/log_process_details.h)   (mongod, tools, mongos)

#### [Interface](interface/16)

#### [Dependencies](dependencies/16)

-------------

## Extra Log Context
MONGO\_INITIALIZERs to add extra information to the server logs.

#### Files
- [src/mongo/db/server\_extra\_log\_context.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/server_extra_log_context.cpp)   (mongod, mongos)

#### [Interface](interface/17)

#### [Dependencies](dependencies/17)

-------------

## Query Log
Helper for verbose query logging.  Should be unified with the logging system once it supports logging based on module.

#### Files
- [src/mongo/db/query/qlog.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/qlog.cpp)   (mongod, tools, mongos)
- [src/mongo/db/query/qlog.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/qlog.h)   (mongod, tools, mongos)

#### [Interface](interface/18)

#### [Dependencies](dependencies/18)
