
# Interface for Log Domain
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/logger/message\_log\_domain.cpp

<div></div>

    mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>::clearAppenders()

- Used By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/tools/tool\_logger.cpp](../../../../tools/tools)

<div></div>

    mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>::attachAppender(std::auto_ptr<mongo::logger::Appender<mongo::logger::MessageEventEphemeral> >)

- Used By:

    - [src/mongo/tools/tool\_logger.cpp](../../../../tools/tools)
    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>::detachAppender(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>::AppenderHandle)

- Used By:

    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
