# replication

# Module Groups

-------------

Replication code? TODO: verify that this is all replication related and document the architecture.   a part of this i would like to have documented is threads+locks, e.g.   heartbeats are sent in a unique thread (i think?) and maybe listened for   in a unique thread too? what threads get started if replication is being   used?

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

## Interface
### src/mongo/db/repl/bgsync.cpp
<pre>mongo::replset::BackgroundSyncInterface::~BackgroundSyncInterface()</pre>
#### Used By:
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<pre>typeinfo for mongo::replset::BackgroundSyncInterface</pre>
#### Used By:
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
### src/mongo/db/repl/health.cpp
<pre>mongo::rsLog</pre>
#### Used By:
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<pre>mongo::ReplSetImpl::lastOtherOpTime() const</pre>
#### Used By:
- [src/mongo/db/dbcommands.cpp](../database\_commands)
### src/mongo/db/repl/master\_slave.cpp
<pre>mongo::replAllDead</pre>
#### Used By:
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

<pre>mongo::DatabaseIgnorer::ignoreAt(std::string const&, mongo::OpTime const&)</pre>
#### Used By:
- [src/mongo/dbtests/repltests.cpp](../unit\_tests)

<pre>mongo::replInfo</pre>
#### Used By:
- [src/mongo/db/restapi.cpp](../database\_web\_accesss)

<pre>mongo::DatabaseIgnorer::doIgnoreUntilAfter(std::string const&, mongo::OpTime const&)</pre>
#### Used By:
- [src/mongo/dbtests/repltests.cpp](../unit\_tests)

<pre>mongo::ReplSource::ReplSource(mongo::BSONObj)</pre>
#### Used By:
- [src/mongo/dbtests/repltests.cpp](../unit\_tests)

<pre>mongo::ReplSource::applyOperation(mongo::BSONObj const&)</pre>
#### Used By:
- [src/mongo/dbtests/repltests.cpp](../unit\_tests)
### src/mongo/db/repl/oplog.cpp
<pre>mongo::createOplog()</pre>
#### Used By:
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- [src/mongo/dbtests/repltests.cpp](../unit\_tests)

<pre>mongo::oplogCheckCloseDatabase(mongo::Database*)</pre>
#### Used By:
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::logOp(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, bool*, bool, mongo::BSONObj const*)</pre>
#### Used By:
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

<pre>mongo::oldRepl()</pre>
#### Used By:
- [src/mongo/dbtests/repltests.cpp](../unit\_tests)

<pre>mongo::applyOperation_inlock(mongo::BSONObj const&, bool, bool)</pre>
#### Used By:
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)
### src/mongo/db/repl/oplogreader.cpp
<pre>mongo::replAuthenticate(mongo::DBClientBase*)</pre>
#### Used By:
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)

<pre>mongo::OplogReader::connect(std::string const&)</pre>
#### Used By:
- [src/mongo/tools/oplog.cpp](../tools)

<pre>mongo::OplogReader::tailingQueryGTE(char const*, mongo::OpTime, mongo::BSONObj const*)</pre>
#### Used By:
- [src/mongo/tools/oplog.cpp](../tools)

<pre>mongo::OplogReader::OplogReader()</pre>
#### Used By:
- [src/mongo/tools/oplog.cpp](../tools)
### src/mongo/db/repl/repl\_reads\_ok.cpp
<pre>mongo::replVerifyReadsOk(mongo::LiteParsedQuery const*)</pre>
#### Used By:
- [src/mongo/db/query/new\_find.cpp](../query\_system)
### src/mongo/db/repl/repl\_start.cpp
<pre>mongo::startReplication()</pre>
#### Used By:
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
### src/mongo/db/repl/replication\_server\_status.cpp
<pre>mongo::replSettings</pre>
#### Used By:
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

<pre>mongo::anyReplEnabled()</pre>
#### Used By:
- [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/s/d\_migrate.cpp](../sharding)
### src/mongo/db/repl/rs.cpp
<pre>mongo::ReplSetImpl::replPrefetcherThreadCount</pre>
#### Used By:
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<pre>mongo::theReplSet</pre>
#### Used By:
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

<pre>mongo::ReplSetImpl::rss</pre>
#### Used By:
- [src/mongo/db/index\_rebuilder.cpp](../indexing)

<pre>mongo::ReplSet::shutdown()</pre>
#### Used By:
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::ReplSetImpl::replWriterThreadCount</pre>
#### Used By:
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<pre>mongo::ReplSet::ReplSet()</pre>
#### Used By:
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<pre>mongo::ReplSetImpl::_stepDown(int)</pre>
#### Used By:
- [src/mongo/db/dbcommands.cpp](../database\_commands)

<pre>mongo::isCurrentlyAReplSetPrimary()</pre>
#### Used By:
- [src/mongo/db/compact.cpp](../database\_commands)

<pre>mongo::replSet</pre>
#### Used By:
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

<pre>mongo::ReplSetImpl::setMaintenanceMode(bool)</pre>
#### Used By:
- [src/mongo/db/dbcommands.cpp](../database\_commands)

<pre>mongo::ReplSetImpl::registerSlave(mongo::BSONObj const&, int)</pre>
#### Used By:
- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<pre>mongo::replLocalAuth()</pre>
#### Used By:
- [src/mongo/db/index\_builder.cpp](../indexing)
### src/mongo/db/repl/rs\_config.cpp
<pre>mongo::ReplSetConfig::getMajority() const</pre>
#### Used By:
- [src/mongo/s/d\_migrate.cpp](../sharding)

<pre>mongo::ReplSetConfig::make(mongo::BSONObj, bool)</pre>
#### Used By:
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
### src/mongo/db/repl/rs\_sync.cpp
<pre>mongo::replset::SyncTail::SyncTail(mongo::replset::BackgroundSyncInterface*)</pre>
#### Used By:
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<pre>typeinfo for mongo::replset::InitialSync</pre>
#### Used By:
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<pre>mongo::replset::InitialSync::InitialSync(mongo::replset::BackgroundSyncInterface*)</pre>
#### Used By:
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<pre>mongo::replset::InitialSync::oplogApplication(mongo::BSONObj const&, mongo::BSONObj const&)</pre>
#### Used By:
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<pre>mongo::replset::multiInitialSyncApply(std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const&, mongo::replset::SyncTail*)</pre>
#### Used By:
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<pre>mongo::replset::InitialSync::~InitialSync()</pre>
#### Used By:
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<pre>mongo::replset::SyncTail::oplogApplication()</pre>
#### Used By:
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<pre>mongo::replset::SyncTail::syncApply(mongo::BSONObj const&, bool)</pre>
#### Used By:
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
### src/mongo/db/repl/sync.cpp
<pre>vtable for mongo::Sync</pre>
#### Used By:
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- [src/mongo/dbtests/repltests.cpp](../unit\_tests)

<pre>typeinfo for mongo::Sync</pre>
#### Used By:
- [src/mongo/dbtests/repltests.cpp](../unit\_tests)

<pre>mongo::Sync::shouldRetry(mongo::BSONObj const&)</pre>
#### Used By:
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- [src/mongo/dbtests/repltests.cpp](../unit\_tests)

<pre>mongo::Sync::getMissingDoc(mongo::BSONObj const&)</pre>
#### Used By:
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- [src/mongo/dbtests/repltests.cpp](../unit\_tests)
### src/mongo/db/repl/sync\_source\_feedback.cpp
<pre>vtable for mongo::SyncSourceFeedback</pre>
#### Used By:
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

-------------

Helpers to wait for the appropriate write concern

- src/mongo/db/write\_concern.cpp   (mongod, tools)
- src/mongo/db/write\_concern.h

## Interface
### src/mongo/db/write\_concern.cpp
<pre>mongo::WriteConcernResult::appendTo(mongo::BSONObjBuilder*) const</pre>
#### Used By:
- [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)

<pre>mongo::WriteConcernOptions::parse(mongo::BSONObj const&)</pre>
#### Used By:
- [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)
- [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)

<pre>mongo::waitForWriteConcern(mongo::WriteConcernOptions const&, mongo::OpTime const&, mongo::WriteConcernResult*)</pre>
#### Used By:
- [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)
- [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)

-------------

Actual meat of the waiting for write concern code

- src/mongo/db/repl/write\_concern.cpp   (mongod, tools)
- src/mongo/db/repl/write\_concern.h

## Interface
### src/mongo/db/repl/write\_concern.cpp
<pre>mongo::updateSlaveLocation(mongo::CurOp&, char const*, mongo::OpTime)</pre>
#### Used By:
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<pre>mongo::opReplicatedEnough(mongo::OpTime, int)</pre>
#### Used By:
- [src/mongo/s/d\_migrate.cpp](../sharding)

<pre>mongo::waitForReplication(mongo::OpTime, int, int)</pre>
#### Used By:
- [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
- [src/mongo/s/d\_migrate.cpp](../sharding)

<pre>mongo::opReplicatedEnough(mongo::OpTime, mongo::BSONElement)</pre>
#### Used By:
- [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
