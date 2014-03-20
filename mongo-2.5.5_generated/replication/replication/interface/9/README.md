
# Interface

### src/mongo/db/repl/rs.cpp

<div></div>

    mongo::ScopedConn::keepOpen

- Used By:

    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../database\_commands)

<div></div>

    mongo::ReplSetImpl::replPrefetcherThreadCount

- Used By:

    - [src/mongo/db/clientcursor.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::theReplSet

- Used By:

    - [src/mongo/db/structure/btree/btreebuilder.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_create.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)
    - [src/mongo/db/clientcursor.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/s/d\_state.cpp](../../../sharding)
    - [src/mongo/db/commands/get\_last\_error.cpp](../../../database\_commands)
    - [src/mongo/db/ttl.cpp](../../../indexing)
    - [src/mongo/db/catalog/collection.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/prefetch.cpp](../../../page\_fault\_utilities)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../indexing)
    - [src/mongo/db/structure/btree/btree.cpp](../../../storage\_layer\_structure)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::ReplSetImpl::rss

- Used By:

    - [src/mongo/db/index\_rebuilder.cpp](../../../indexing)

<div></div>

    mongo::ReplSet::shutdown()

- Used By:

    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::ReplSetImpl::replWriterThreadCount

- Used By:

    - [src/mongo/db/clientcursor.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::ReplSet::ReplSet()

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)

<div></div>

    mongo::ReplSetImpl::_stepDown(int)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)

<div></div>

    mongo::isCurrentlyAReplSetPrimary()

- Used By:

    - [src/mongo/db/commands/compact.cpp](../../../database\_commands)

<div></div>

    mongo::replSet

- Used By:

    - [src/mongo/db/structure/btree/btreebuilder.cpp](../../../storage\_layer\_structure)
    - [src/mongo/s/d\_state.cpp](../../../sharding)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_create.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/ttl.cpp](../../../indexing)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/structure/btree/btree.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/db/restapi.cpp](../../../web\_server)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../sharding)

<div></div>

    mongo::ReplSetImpl::setMaintenanceMode(bool)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)

<div></div>

    mongo::ReplSetImpl::registerSlave(mongo::BSONObj const&, int)

- Used By:

    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::replLocalAuth()

- Used By:

    - [src/mongo/db/index\_builder.cpp](../../../indexing)