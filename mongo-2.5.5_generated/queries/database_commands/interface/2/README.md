
# Interface for Uncategorized Commands
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/commands/copydb\_common.cpp

<div></div>

    mongo::copydb::checkAuthForCopydbCommand(mongo::ClientBasic*, std::string const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)

### src/mongo/db/commands/dbhash.cpp

<div></div>

    mongo::logOpForDbHash(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, mongo::BSONObj const*, bool)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)

### src/mongo/db/commands/find\_and\_modify\_common.cpp

<div></div>

    mongo::find_and_modify::addPrivilegesRequiredForFindAndModify(mongo::Command*, std::string const&, mongo::BSONObj const&, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> >*)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

### src/mongo/db/commands/get\_last\_error.cpp

<div></div>

    mongo::getLastErrorDefault

- Used By:

    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../../network/write\_commands)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

### src/mongo/db/commands/isself.cpp

<div></div>

    mongo::HostAndPort::isSelf() const

- Used By:

    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/dbtests/socktests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_initiate.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/db/repl/manager.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

### src/mongo/db/commands/mr\_common.cpp

<div></div>

    mongo::mr::addPrivilegesRequiredForMapReduce(mongo::Command*, std::string const&, mongo::BSONObj const&, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> >*)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

### src/mongo/db/commands/rename\_collection\_common.cpp

<div></div>

    mongo::rename_collection::checkAuthForRenameCollectionCommand(mongo::ClientBasic*, std::string const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

### src/mongo/db/commands/server\_status.cpp

<div></div>

    mongo::ServerStatusSection::ServerStatusSection(std::string const&)

- Used By:

    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/util/tcmalloc\_server\_status\_section.cpp](../../../../utilities/utilities)
    - [src/mongo/db/clientcursor.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/d\_concurrency.cpp](../../../../queries/concurrency)
    - [src/mongo/db/structure/btree/btree\_stats.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::OpCounterServerStatusSection::OpCounterServerStatusSection(std::string const&, mongo::OpCounters*)

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::ServerStatusMetric::ServerStatusMetric(std::string const&)

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/ttl.cpp](../../../../queries/indexing)
    - [src/mongo/db/catalog/collection.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/clientcursor.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/prefetch.cpp](../../../../storage/page\_fault\_utilities)
    - [src/mongo/s/client\_info.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/repl/oplogreader.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/s/d\_writeback.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/db/curop.cpp](../../../../queries/client\_and\_operation\_tracking)

### src/mongo/db/commands/shutdown.cpp

<div></div>

    vtable for mongo::CmdShutdown

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

### src/mongo/db/dbcommands\_generic.cpp

<div></div>

    mongo::CmdShutdown::shutdownHelper()

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

### src/mongo/db/dbeval.cpp

<div></div>

    mongo::dbEval(std::string const&, mongo::BSONObj&, mongo::BSONObjBuilder&, std::string&)

- Used By:

    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
