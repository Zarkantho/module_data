
# Interface for Message Port
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/util/net/message\_port.cpp

<div></div>

    mongo::MessagingPort::MessagingPort(double, mongo::logger::LogSeverity)

- Used By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::MessagingPort::say(mongo::Message&, int)

- Used By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/tools/sniffer.cpp](../../../../tools/tools)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)

<div></div>

    mongo::MessagingPort::recv(mongo::Message&)

- Used By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)

<div></div>

    mongo::MessagingPort::shutdown()

- Used By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)

<div></div>

    mongo::MessagingPort::closeAllSockets(unsigned int)

- Used By:

    - [src/mongo/db/repl/rs.cpp](../../../../replication/replication)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::MessagingPort::piggyBack(mongo::Message&, int)

- Used By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::MessagingPort::setSocketTimeout(double)

- Used By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::MessagingPort::call(mongo::Message&, mongo::Message&)

- Used By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/tools/sniffer.cpp](../../../../tools/tools)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)
