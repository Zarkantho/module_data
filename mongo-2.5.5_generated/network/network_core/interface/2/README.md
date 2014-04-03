
# Interface for Listener Interface
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/util/net/listen.cpp

<div></div>

    mongo::Listener::globalConnectionNumber

- Used By:

    - [src/mongo/db/commands/server\_status.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::Listener::setupSockets()

- Used By:

    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)

<div></div>

    mongo::Listener::globalTicketHolder

- Used By:

    - [src/mongo/db/clientcursor.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/db/commands/server\_status.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::Listener::Listener(std::string const&, std::string const&, int, bool)

- Used By:

    - [src/mongo/util/net/miniwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)

<div></div>

    mongo::Listener::accepted(boost::shared_ptr<mongo::Socket>, long long)

- Used By:

    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)

<div></div>

    mongo::Listener::~Listener()

- Used By:

    - [src/mongo/util/net/miniwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)

<div></div>

    mongo::ListeningSockets::get()

- Used By:

    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::Listener::_timeTracker

- Used By:

    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/isself.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/cursors.cpp](../../../../sharding/sharding\_uncategorized)
    - [src/mongo/db/clientcursor.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/curop.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/replication)
    - [src/mongo/db/commands/server\_status.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/s/d\_writeback.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/util/elapsed\_tracker.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Listener::acceptedMP(mongo::MessagingPort*)

- Used By:

    - [src/mongo/util/net/miniwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)

<div></div>

    mongo::Listener::initAndListen()

- Used By:

    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)

<div></div>

    typeinfo for mongo::Listener

- Used By:

    - [src/mongo/util/net/miniwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)
