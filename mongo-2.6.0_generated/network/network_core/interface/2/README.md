
# Interface for Listener Interface
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/util/net/listen.cpp

<div></div>

    mongo::Listener::_timeTracker

- Used By:

    - [src/mongo/db/commands/isself.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/util/elapsed\_tracker.cpp](../../../../utilities/utilities)
    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/server\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/s/d\_writeback.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::Listener::globalConnectionNumber

- Used By:

    - [src/mongo/db/commands/server\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    typeinfo for mongo::Listener

- Used By:

    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)
    - [src/mongo/util/net/miniwebserver.cpp](../../../../network/web\_server)

<div></div>

    mongo::ListeningSockets::get()

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)

<div></div>

    mongo::Listener::~Listener()

- Used By:

    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)
    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/util/net/miniwebserver.cpp](../../../../network/web\_server)

<div></div>

    mongo::Listener::acceptedMP(mongo::MessagingPort*)

- Used By:

    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/util/net/miniwebserver.cpp](../../../../network/web\_server)

<div></div>

    mongo::Listener::Listener(std::string const&, std::string const&, int, bool)

- Used By:

    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)
    - [src/mongo/util/net/miniwebserver.cpp](../../../../network/web\_server)

<div></div>

    mongo::Listener::globalTicketHolder

- Used By:

    - [src/mongo/db/commands/server\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::Listener::accepted(boost::shared_ptr<mongo::Socket>, long long)

- Used By:

    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)

<div></div>

    mongo::Listener::setupSockets()

- Used By:

    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)

<div></div>

    mongo::Listener::initAndListen()

- Used By:

    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)
