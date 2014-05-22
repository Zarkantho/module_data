
# Interface for Message Encoder
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/logger/message\_event\_utf8\_encoder.cpp

<div></div>

    mongo::logger::MessageEventDetailsEncoder::setDateFormatter(std::string (*)(mongo::Date_t))

- Used By:

    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    vtable for mongo::logger::MessageEventUnadornedEncoder

- Used By:

    - [src/mongo/tools/tool\_logger.cpp](../../../../tools/tools)
    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)

<div></div>

    vtable for mongo::logger::MessageEventWithContextEncoder

- Used By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    vtable for mongo::logger::MessageEventDetailsEncoder

- Used By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/tools/tool\_logger.cpp](../../../../tools/tools)
    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)
