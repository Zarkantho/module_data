# database\_commands

# Module Groups

-------------

Base class for mongodb commands. Has a big std::map with the keys of the command name and the  values as the Command itself. These are the commands that you run using  "db.$cmd.findOne({ "serverStatus" : true }).

- src/mongo/db/commands.cpp   (mongod, tools, mongos)
- src/mongo/db/commands.h

## Interface


### src/mongo/db/commands.cpp

<pre>mongo::Command::Command(mongo::StringData, bool, mongo::StringData)</pre>

#### Used By:

- [src/mongo/db/repl/heartbeat.cpp](../replication)
- [src/mongo/db/repl/consensus.cpp](../replication)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
- src/mongo/db/modules/subscription/src/audit/audit\_command.cpp
- [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
- [src/mongo/s/d\_writeback.cpp](../sharding)
- [src/mongo/db/repl/resync.cpp](../replication)
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/geo/haystack.cpp](../geo\_queries)
- [src/mongo/s/d\_state.cpp](../sharding)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/s/shardconnection.cpp](../sharding)
- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
- [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- [src/mongo/s/shard.cpp](../sharding)
- [src/mongo/s/d\_split.cpp](../sharding)
- [src/mongo/db/repl/replset\_commands.cpp](../replication)
- [src/mongo/s/cursors.cpp](../sharding)
- [src/mongo/db/stats/top.cpp](../utilities)
- [src/mongo/db/repl/rs\_initiate.cpp](../replication)
- [src/mongo/db/fts/fts\_command.cpp](../full\_text\_search\_module)
- [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)

<pre>mongo::Command::parseNsFullyQualified(std::string const&, mongo::BSONObj const&) const</pre>

#### Used By:

- [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
- [src/mongo/s/d\_state.cpp](../sharding)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/s/d\_split.cpp](../sharding)
- [src/mongo/s/d\_migrate.cpp](../sharding)

<pre>mongo::Command::findCommand(std::string const&)</pre>

#### Used By:

- [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<pre>mongo::Command::_checkAuthorization(mongo::Command*, mongo::ClientBasic*, std::string const&, mongo::BSONObj const&, bool)</pre>

#### Used By:

- [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<pre>mongo::Command::parseResourcePattern(std::string const&, mongo::BSONObj const&) const</pre>

#### Used By:

- [src/mongo/db/geo/haystack.cpp](../geo\_queries)
- [src/mongo/db/fts/fts\_command.cpp](../full\_text\_search\_module)
- [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)
- [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
- [src/mongo/s/d\_split.cpp](../sharding)

<pre>vtable for mongo::Command</pre>

#### Used By:

- [src/mongo/db/repl/heartbeat.cpp](../replication)
- [src/mongo/db/repl/consensus.cpp](../replication)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
- src/mongo/db/modules/subscription/src/audit/audit\_command.cpp
- [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
- [src/mongo/s/d\_writeback.cpp](../sharding)
- [src/mongo/db/repl/resync.cpp](../replication)
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/geo/haystack.cpp](../geo\_queries)
- [src/mongo/s/d\_state.cpp](../sharding)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/s/shardconnection.cpp](../sharding)
- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
- [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
- [src/mongo/s/shard.cpp](../sharding)
- [src/mongo/s/d\_split.cpp](../sharding)
- [src/mongo/db/repl/replset\_commands.cpp](../replication)
- [src/mongo/s/cursors.cpp](../sharding)
- [src/mongo/db/stats/top.cpp](../utilities)
- [src/mongo/db/repl/rs\_initiate.cpp](../replication)
- [src/mongo/db/fts/fts\_command.cpp](../full\_text\_search\_module)
- [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)

<pre>mongo::Command::testCommandsEnabled</pre>

#### Used By:

- [src/mongo/dbtests/dbtests.cpp](../unit\_tests)
- [src/mongo/db/repl/replset\_commands.cpp](../replication)

<pre>mongo::Command::parseNs(std::string const&, mongo::BSONObj const&) const</pre>

#### Used By:

- [src/mongo/db/repl/heartbeat.cpp](../replication)
- [src/mongo/db/repl/consensus.cpp](../replication)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
- src/mongo/db/modules/subscription/src/audit/audit\_command.cpp
- [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
- [src/mongo/s/d\_writeback.cpp](../sharding)
- [src/mongo/db/repl/resync.cpp](../replication)
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/geo/haystack.cpp](../geo\_queries)
- [src/mongo/s/d\_state.cpp](../sharding)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/s/shardconnection.cpp](../sharding)
- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
- [src/mongo/s/shard.cpp](../sharding)
- [src/mongo/s/d\_split.cpp](../sharding)
- [src/mongo/db/repl/replset\_commands.cpp](../replication)
- [src/mongo/s/cursors.cpp](../sharding)
- [src/mongo/db/stats/top.cpp](../utilities)
- [src/mongo/db/repl/rs\_initiate.cpp](../replication)
- [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)

<pre>mongo::Command::stopIndexBuilds(std::string const&, mongo::BSONObj const&)</pre>

#### Used By:

- [src/mongo/db/repl/heartbeat.cpp](../replication)
- [src/mongo/db/repl/consensus.cpp](../replication)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
- src/mongo/db/modules/subscription/src/audit/audit\_command.cpp
- [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
- [src/mongo/s/d\_writeback.cpp](../sharding)
- [src/mongo/db/repl/resync.cpp](../replication)
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/geo/haystack.cpp](../geo\_queries)
- [src/mongo/s/d\_state.cpp](../sharding)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/s/shardconnection.cpp](../sharding)
- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
- [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
- [src/mongo/s/shard.cpp](../sharding)
- [src/mongo/s/d\_split.cpp](../sharding)
- [src/mongo/db/repl/replset\_commands.cpp](../replication)
- [src/mongo/s/cursors.cpp](../sharding)
- [src/mongo/db/stats/top.cpp](../utilities)
- [src/mongo/db/repl/rs\_initiate.cpp](../replication)
- [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)

<pre>typeinfo for mongo::Command</pre>

#### Used By:

- [src/mongo/db/repl/heartbeat.cpp](../replication)
- [src/mongo/db/repl/consensus.cpp](../replication)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
- src/mongo/db/modules/subscription/src/audit/audit\_command.cpp
- [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
- [src/mongo/s/d\_writeback.cpp](../sharding)
- [src/mongo/db/repl/resync.cpp](../replication)
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/geo/haystack.cpp](../geo\_queries)
- [src/mongo/s/d\_state.cpp](../sharding)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/s/shardconnection.cpp](../sharding)
- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
- [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
- [src/mongo/s/shard.cpp](../sharding)
- [src/mongo/s/d\_split.cpp](../sharding)
- [src/mongo/db/repl/replset\_commands.cpp](../replication)
- [src/mongo/s/cursors.cpp](../sharding)
- [src/mongo/db/stats/top.cpp](../utilities)
- [src/mongo/db/repl/rs\_initiate.cpp](../replication)
- [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)

<pre>mongo::Command::_commandsByBestName</pre>

#### Used By:

- [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)

<pre>mongo::Command::checkAuthForCommand(mongo::ClientBasic*, std::string const&, mongo::BSONObj const&)</pre>

#### Used By:

- [src/mongo/db/repl/heartbeat.cpp](../replication)
- [src/mongo/db/repl/consensus.cpp](../replication)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
- [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
- [src/mongo/s/d\_writeback.cpp](../sharding)
- [src/mongo/db/repl/resync.cpp](../replication)
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/geo/haystack.cpp](../geo\_queries)
- [src/mongo/s/d\_state.cpp](../sharding)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/s/shardconnection.cpp](../sharding)
- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
- [src/mongo/s/shard.cpp](../sharding)
- [src/mongo/s/d\_split.cpp](../sharding)
- [src/mongo/db/repl/replset\_commands.cpp](../replication)
- [src/mongo/s/cursors.cpp](../sharding)
- [src/mongo/db/stats/top.cpp](../utilities)
- [src/mongo/db/repl/rs\_initiate.cpp](../replication)
- [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)

<pre>mongo::Command::_webCommands</pre>

#### Used By:

- [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)

<pre>mongo::Command::redactForLogging(mongo::mutablebson::Document*)</pre>

#### Used By:

- [src/mongo/db/repl/heartbeat.cpp](../replication)
- [src/mongo/db/repl/consensus.cpp](../replication)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
- src/mongo/db/modules/subscription/src/audit/audit\_command.cpp
- [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
- [src/mongo/s/d\_writeback.cpp](../sharding)
- [src/mongo/db/repl/resync.cpp](../replication)
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/geo/haystack.cpp](../geo\_queries)
- [src/mongo/s/d\_state.cpp](../sharding)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/s/shardconnection.cpp](../sharding)
- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
- [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
- [src/mongo/s/shard.cpp](../sharding)
- [src/mongo/s/d\_split.cpp](../sharding)
- [src/mongo/db/repl/replset\_commands.cpp](../replication)
- [src/mongo/s/cursors.cpp](../sharding)
- [src/mongo/db/stats/top.cpp](../utilities)
- [src/mongo/db/repl/rs\_initiate.cpp](../replication)
- [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)

<pre>mongo::Command::appendCommandStatus(mongo::BSONObjBuilder&, bool, std::string const&)</pre>

#### Used By:

- [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<pre>mongo::Command::appendCommandStatus(mongo::BSONObjBuilder&, mongo::Status const&)</pre>

#### Used By:

- [src/mongo/db/query/new\_find.cpp](../query\_system)
- [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/s/strategy\_single.cpp](../sharding)
- [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<pre>mongo::Command::help(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&) const</pre>

#### Used By:

- [src/mongo/s/d\_state.cpp](../sharding)
- [src/mongo/db/geo/haystack.cpp](../geo\_queries)
- [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
- [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)
- [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)

<pre>mongo::Command::htmlHelp(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&) const</pre>

#### Used By:

- [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)

-------------

A bunch of commands for mongod. However, this ALSO has the definition of Command::execCommand for  mongod (the function that actually runs commands registered using the Command class, which gets  called whenever a query against the "$cmd" collection is made)

- src/mongo/db/dbcommands.cpp   (mongod, tools)

## Interface


### src/mongo/db/dbcommands.cpp

<pre>mongo::Command::execCommand(mongo::Command*, mongo::Client&, int, char const*, mongo::BSONObj&, mongo::BSONObjBuilder&, bool)</pre>

#### Used By:

- [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)

<pre>mongo::_runCommands(char const*, mongo::BSONObj&, mongo::_BufBuilder<mongo::TrivialAllocator>&, mongo::BSONObjBuilder&, bool, int)</pre>

#### Used By:

- [src/mongo/db/repl/oplog.cpp](../replication)
- [src/mongo/db/query/new\_find.cpp](../query\_system)

-------------

Commands (run using db.$cmd.findOne(...))

- src/mongo/db/commands/apply\_ops.cpp   (mongod, tools)
- src/mongo/db/commands/authentication\_commands.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/authentication\_commands.h
- src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp   (mongod, tools)
- src/mongo/db/commands/collection\_to\_capped.cpp   (mongod, tools)
- src/mongo/db/commands/connection\_status.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/copydb.h
- src/mongo/db/commands/copydb\_common.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/dbhash.cpp   (mongod, tools)
- src/mongo/db/commands/dbhash.h
- src/mongo/db/commands/distinct.cpp   (mongod, tools)
- src/mongo/db/commands/drop\_indexes.cpp   (mongod, tools)
- src/mongo/db/commands/fail\_point\_cmd.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/find\_and\_modify.cpp   (mongod, tools)
- src/mongo/db/commands/find\_and\_modify.h
- src/mongo/db/commands/find\_and\_modify\_common.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/geonear.cpp   (mongod, tools)
- src/mongo/db/commands/get\_last\_error.cpp   (mongod, tools)
- src/mongo/db/commands/group.cpp   (mongod, tools)
- src/mongo/db/commands/hashcmd.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/index\_stats.cpp   (mongod, tools)
- src/mongo/db/commands/isself.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/merge\_chunks\_cmd.cpp   (mongod, tools)
- src/mongo/db/commands/mr.cpp   (mongod, tools)
- src/mongo/db/commands/mr.h
- src/mongo/db/commands/mr\_common.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/parameters.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/pipeline\_command.cpp   (mongod, tools)
- src/mongo/db/commands/rename\_collection.cpp   (mongod, tools)
- src/mongo/db/commands/rename\_collection.h
- src/mongo/db/commands/rename\_collection\_common.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/server\_status.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/server\_status.h
- src/mongo/db/commands/shutdown.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/shutdown.h
- src/mongo/db/commands/storage\_details.cpp   (mongod, tools)
- src/mongo/db/commands/test\_commands.cpp   (mongod, tools)
- src/mongo/db/commands/touch.cpp   (mongod)
- src/mongo/db/commands/user\_management\_commands.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/validate.cpp   (mongod, tools)
- src/mongo/db/compact.cpp   (mongod, tools)
- src/mongo/db/dbcommands\_admin.cpp   (mongod, tools)
- src/mongo/db/dbcommands\_generic.cpp   (mongod, tools, mongos)
- src/mongo/db/dbeval.cpp   (mongod, tools)
- src/mongo/s/commands\_admin.cpp   (mongos)
- src/mongo/s/commands\_public.cpp   (mongos)
- src/mongo/db/driverHelpers.cpp   (mongod, tools)

## Interface


### src/mongo/db/commands/authentication\_commands.cpp

<pre>mongo::CmdAuthenticate::disableAuthMechanism(std::string)</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp

### src/mongo/db/commands/copydb\_common.cpp

<pre>mongo::copydb::checkAuthForCopydbCommand(mongo::ClientBasic*, std::string const&, mongo::BSONObj const&)</pre>

#### Used By:

- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)

### src/mongo/db/commands/dbhash.cpp

<pre>mongo::logOpForDbHash(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, mongo::BSONObj const*, bool)</pre>

#### Used By:

- [src/mongo/db/repl/oplog.cpp](../replication)

### src/mongo/db/commands/get\_last\_error.cpp

<pre>mongo::getLastErrorDefault</pre>

#### Used By:

- [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/repl/rs.cpp](../replication)

### src/mongo/db/commands/isself.cpp

<pre>mongo::HostAndPort::isSelf() const</pre>

#### Used By:

- [src/mongo/db/repl/rs\_config.cpp](../replication)
- [src/mongo/dbtests/socktests.cpp](../unit\_tests)
- [src/mongo/db/repl/rs\_initiate.cpp](../replication)
- [src/mongo/db/repl/manager.cpp](../replication)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/rs.cpp](../replication)

### src/mongo/db/commands/server\_status.cpp

<pre>mongo::ServerStatusSection::ServerStatusSection(std::string const&)</pre>

#### Used By:

- [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
- [src/mongo/db/dur.cpp](../journaling)
- [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
- [src/mongo/util/tcmalloc\_server\_status\_section.cpp](../utilities)
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/d\_concurrency.cpp](../concurrency)
- [src/mongo/db/structure/btree/btree\_stats.cpp](../storage\_layer\_structure)

<pre>mongo::OpCounterServerStatusSection::OpCounterServerStatusSection(std::string const&, mongo::OpCounters*)</pre>

#### Used By:

- [src/mongo/db/repl/replication\_server\_status.cpp](../replication)

<pre>mongo::ServerStatusMetric::ServerStatusMetric(std::string const&)</pre>

#### Used By:

- [src/mongo/db/repl/bgsync.cpp](../replication)
- [src/mongo/db/ttl.cpp](../indexing)
- [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)
- [src/mongo/db/write\_concern.cpp](../replication)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
- [src/mongo/db/repl/oplogreader.cpp](../replication)
- [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/repl/rs\_sync.cpp](../replication)
- [src/mongo/s/d\_writeback.cpp](../sharding)
- [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

### src/mongo/db/dbeval.cpp

<pre>mongo::dbEval(std::string const&, mongo::BSONObj&, mongo::BSONObjBuilder&, std::string&)</pre>

#### Used By:

- [src/mongo/dbtests/jstests.cpp](../unit\_tests)

### src/mongo/s/commands\_public.cpp

<pre>mongo::Command::runAgainstRegistered(char const*, mongo::BSONObj&, mongo::BSONObjBuilder&, int)</pre>

#### Used By:

- [src/mongo/s/strategy\_single.cpp](../sharding)
- [src/mongo/s/strategy\_shard.cpp](../sharding)

-------------

Commands + code for fsync of data files

- src/mongo/db/commands/fsync.cpp   (mongod, tools)
- src/mongo/db/commands/fsync.h

## Interface


### src/mongo/db/commands/fsync.cpp

<pre>mongo::_unlockFsync()</pre>

#### Used By:

- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::lockedForWriting()</pre>

#### Used By:

- [src/mongo/db/repl/write\_concern.cpp](../replication)
- [src/mongo/db/ttl.cpp](../indexing)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::filesLockedFsync</pre>

#### Used By:

- [src/mongo/db/dur.cpp](../journaling)
- [src/mongo/db/repl/rs\_sync.cpp](../replication)
