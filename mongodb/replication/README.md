# replication

# Module Groups

-------------

# Group Description
Replication code? TODO: verify that this is all replication related and document the architecture.   a part of this i would like to have documented is threads+locks, e.g.   heartbeats are sent in a unique thread (i think?) and maybe listened for   in a unique thread too? what threads get started if replication is being   used?

# Files
- src/mongo/db/repl/bgsync.cpp   (mongod, tools)
- src/mongo/db/repl/bgsync.h
- src/mongo/db/repl/connections.h
- src/mongo/db/repl/consensus.cpp   (mongod, tools)
- src/mongo/db/repl/health.cpp   (mongod, tools)
- src/mongo/db/repl/health.h
- src/mongo/db/repl/heartbeat.cpp   (mongod, tools)
- src/mongo/db/repl/is\_master.h
- src/mongo/db/repl/manager.cpp   (mongod, tools)
- src/mongo/db/repl/master\_slave.cpp   (mongod, tools)
- src/mongo/db/repl/master\_slave.h
- src/mongo/db/repl/multicmd.h
- src/mongo/db/repl/oplog.cpp   (mongod, tools)
- src/mongo/db/repl/oplog.h
- src/mongo/db/repl/oplogreader.cpp   (mongod, tools)
- src/mongo/db/repl/oplogreader.h
- src/mongo/db/repl/repl\_reads\_ok.cpp   (mongod, tools)
- src/mongo/db/repl/repl\_reads\_ok.h
- src/mongo/db/repl/repl\_start.cpp   (mongod, tools)
- src/mongo/db/repl/repl\_start.h
- src/mongo/db/repl/replication\_server\_status.cpp   (mongod, tools)
- src/mongo/db/repl/replication\_server\_status.h
- src/mongo/db/repl/replset\_commands.cpp   (mongod, tools)
- src/mongo/db/repl/replset\_web\_handler.cpp   (mongod)
- src/mongo/db/repl/resync.cpp   (mongod, tools)
- src/mongo/db/repl/rs.cpp   (mongod, tools)
- src/mongo/db/repl/rs.h
- src/mongo/db/repl/rs\_config.cpp   (mongod, tools)
- src/mongo/db/repl/rs\_config.h
- src/mongo/db/repl/rs\_exception.h
- src/mongo/db/repl/rs\_initialsync.cpp   (mongod, tools)
- src/mongo/db/repl/rs\_initiate.cpp   (mongod, tools)
- src/mongo/db/repl/rs\_member.h
- src/mongo/db/repl/rs\_rollback.cpp   (mongod, tools)
- src/mongo/db/repl/rs\_sync.cpp   (mongod, tools)
- src/mongo/db/repl/rs\_sync.h
- src/mongo/db/repl/sync.cpp   (mongod, tools)
- src/mongo/db/repl/sync.h
- src/mongo/db/repl/sync\_source\_feedback.cpp   (mongod, tools)
- src/mongo/db/repl/sync\_source\_feedback.h

# Interface

### src/mongo/db/repl/bgsync.cpp

<div></div>

    mongo::replset::BackgroundSyncInterface::~BackgroundSyncInterface()

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::replset::BackgroundSyncInterface

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

### src/mongo/db/repl/health.cpp

<div></div>

    mongo::rsLog

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<div></div>

    mongo::ReplSetImpl::lastOtherOpTime() const

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)

### src/mongo/db/repl/master\_slave.cpp

<div></div>

    mongo::replAllDead

- Used By:

    - [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)
    - src/mongo/db/modules/subscription/src/snmp/snmp.cpp
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/restapi.cpp](../database\_web\_accesss)

<div></div>

    mongo::DatabaseIgnorer::ignoreAt(std::string const&, mongo::OpTime const&)

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)

<div></div>

    mongo::replInfo

- Used By:

    - [src/mongo/db/restapi.cpp](../database\_web\_accesss)

<div></div>

    mongo::DatabaseIgnorer::doIgnoreUntilAfter(std::string const&, mongo::OpTime const&)

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)

<div></div>

    mongo::ReplSource::ReplSource(mongo::BSONObj)

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)

<div></div>

    mongo::ReplSource::applyOperation(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)

### src/mongo/db/repl/oplog.cpp

<div></div>

    mongo::createOplog()

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)

<div></div>

    mongo::oplogCheckCloseDatabase(mongo::Database*)

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::logOp(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, bool*, bool, mongo::BSONObj const*)

- Used By:

    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
    - [src/mongo/db/ops/delete.cpp](../query\_system)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::oldRepl()

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)

<div></div>

    mongo::applyOperation_inlock(mongo::BSONObj const&, bool, bool)

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)

### src/mongo/db/repl/oplogreader.cpp

<div></div>

    mongo::replAuthenticate(mongo::DBClientBase*)

- Used By:

    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)

<div></div>

    mongo::OplogReader::connect(std::string const&)

- Used By:

    - [src/mongo/tools/oplog.cpp](../tools)

<div></div>

    mongo::OplogReader::tailingQueryGTE(char const*, mongo::OpTime, mongo::BSONObj const*)

- Used By:

    - [src/mongo/tools/oplog.cpp](../tools)

<div></div>

    mongo::OplogReader::OplogReader()

- Used By:

    - [src/mongo/tools/oplog.cpp](../tools)

### src/mongo/db/repl/repl\_reads\_ok.cpp

<div></div>

    mongo::replVerifyReadsOk(mongo::LiteParsedQuery const*)

- Used By:

    - [src/mongo/db/query/new\_find.cpp](../query\_system)

### src/mongo/db/repl/repl\_start.cpp

<div></div>

    mongo::startReplication()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/db/repl/replication\_server\_status.cpp

<div></div>

    mongo::replSettings

- Used By:

    - [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/db/restapi.cpp](../database\_web\_accesss)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - src/mongo/db/modules/subscription/src/snmp/snmp.cpp
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

<div></div>

    mongo::anyReplEnabled()

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

### src/mongo/db/repl/rs.cpp

<div></div>

    mongo::ReplSetImpl::replPrefetcherThreadCount

- Used By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::theReplSet

- Used By:

    - [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - src/mongo/db/modules/subscription/src/snmp/snmp.cpp
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ReplSetImpl::rss

- Used By:

    - [src/mongo/db/index\_rebuilder.cpp](../indexing)

<div></div>

    mongo::ReplSet::shutdown()

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ReplSetImpl::replWriterThreadCount

- Used By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::ReplSet::ReplSet()

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<div></div>

    mongo::ReplSetImpl::_stepDown(int)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    mongo::isCurrentlyAReplSetPrimary()

- Used By:

    - [src/mongo/db/compact.cpp](../database\_commands)

<div></div>

    mongo::replSet

- Used By:

    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)
    - src/mongo/db/modules/subscription/src/snmp/snmp.cpp
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/restapi.cpp](../database\_web\_accesss)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)

<div></div>

    mongo::ReplSetImpl::setMaintenanceMode(bool)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    mongo::ReplSetImpl::registerSlave(mongo::BSONObj const&, int)

- Used By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::replLocalAuth()

- Used By:

    - [src/mongo/db/index\_builder.cpp](../indexing)

### src/mongo/db/repl/rs\_config.cpp

<div></div>

    mongo::ReplSetConfig::getMajority() const

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::ReplSetConfig::make(mongo::BSONObj, bool)

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

### src/mongo/db/repl/rs\_sync.cpp

<div></div>

    mongo::replset::SyncTail::SyncTail(mongo::replset::BackgroundSyncInterface*)

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::replset::InitialSync

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<div></div>

    mongo::replset::InitialSync::InitialSync(mongo::replset::BackgroundSyncInterface*)

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<div></div>

    mongo::replset::InitialSync::oplogApplication(mongo::BSONObj const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<div></div>

    mongo::replset::multiInitialSyncApply(std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const&, mongo::replset::SyncTail*)

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<div></div>

    mongo::replset::InitialSync::~InitialSync()

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<div></div>

    mongo::replset::SyncTail::oplogApplication()

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<div></div>

    mongo::replset::SyncTail::syncApply(mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

### src/mongo/db/repl/sync.cpp

<div></div>

    vtable for mongo::Sync

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::Sync

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)

<div></div>

    mongo::Sync::shouldRetry(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)

<div></div>

    mongo::Sync::getMissingDoc(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)

### src/mongo/db/repl/sync\_source\_feedback.cpp

<div></div>

    vtable for mongo::SyncSourceFeedback

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

-------------

# Group Description
Helpers to wait for the appropriate write concern

# Files
- src/mongo/db/write\_concern.cpp   (mongod, tools)
- src/mongo/db/write\_concern.h

# Interface

### src/mongo/db/write\_concern.cpp

<div></div>

    mongo::WriteConcernResult::appendTo(mongo::BSONObjBuilder*) const

- Used By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)

<div></div>

    mongo::WriteConcernOptions::parse(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::waitForWriteConcern(mongo::WriteConcernOptions const&, mongo::OpTime const&, mongo::WriteConcernResult*)

- Used By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)

-------------

# Group Description
Actual meat of the waiting for write concern code

# Files
- src/mongo/db/repl/write\_concern.cpp   (mongod, tools)
- src/mongo/db/repl/write\_concern.h

# Interface

### src/mongo/db/repl/write\_concern.cpp

<div></div>

    mongo::updateSlaveLocation(mongo::CurOp&, char const*, mongo::OpTime)

- Used By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::opReplicatedEnough(mongo::OpTime, int)

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::waitForReplication(mongo::OpTime, int, int)

- Used By:

    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::opReplicatedEnough(mongo::OpTime, mongo::BSONElement)

- Used By:

    - [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
