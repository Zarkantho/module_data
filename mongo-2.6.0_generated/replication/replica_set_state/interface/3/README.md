
# Interface for Top Level Replica Set Classes
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/repl/rs.cpp

<div></div>

    mongo::ScopedConn::keepOpen

- Used By:

    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../../security/authorization)
    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replica\_set\_configuration)

<div></div>

    mongo::ReplSetImpl::replPrefetcherThreadCount

- Used By:

    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::ReplSetImpl::clearInitialSyncFlag()

- Used By:

    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::startReplSets(mongo::ReplSetCmdline*)

- Used By:

    - [src/mongo/db/repl/repl\_start.cpp](../../../../replication/replication\_initialization)

<div></div>

    mongo::ReplSetImpl::setMinValid(mongo::BSONObj)

- Used By:

    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::ReplSetImpl::getMinValid()

- Used By:

    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::ReplSetImpl::changeState(mongo::MemberState)

- Used By:

    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::theReplSet

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_initiate.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/catalog/collection.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/prefetch.cpp](../../../../storage/page\_fault\_utilities)
    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/commands/get\_last\_error.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/db/ops/update.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/repl/oplogreader.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/replset\_web\_handler.cpp](../../../../replication/replication\_web\_interface)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/resync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)
    - [src/mongo/db/ops/delete\_executor.cpp](../../../../core\_query\_system/delete\_operations)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../../security/authorization)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::ReplSetImpl::assumePrimary()

- Used By:

    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)

<div></div>

    mongo::ReplSetImpl::rss

- Used By:

    - [src/mongo/db/index\_rebuilder.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::ReplSet::shutdown()

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::ReplSetImpl::_freeze(int)

- Used By:

    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)

<div></div>

    mongo::ReplSetImpl::setInitialSyncFlag()

- Used By:

    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::ReplSetImpl::replWriterThreadCount

- Used By:

    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::ReplSet::ReplSet()

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::ReplSetImpl::_fatal()

- Used By:

    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::ReplSetImpl::getInitialSyncFlag()

- Used By:

    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::ReplSetImpl::_stepDown(int)

- Used By:

    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ReplSet::haveNewConfig(mongo::ReplSetConfig&, bool)

- Used By:

    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)

<div></div>

    mongo::isCurrentlyAReplSetPrimary()

- Used By:

    - [src/mongo/db/commands/compact.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::replSet

- Used By:

    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)
    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/db/repl/repl\_start.cpp](../../../../replication/replication\_initialization)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/ops/update.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/repl/rs\_initiate.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/db/restapi.cpp](../../../../network/web\_server)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/ops/delete\_executor.cpp](../../../../core\_query\_system/delete\_operations)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::ReplSetImpl::setMaintenanceMode(bool)

- Used By:

    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ReplSetImpl::goStale(mongo::Member const*, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::ReplSetImpl::startupStatusMsg

- Used By:

    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)
    - [src/mongo/db/repl/rs\_initiate.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/db/repl/replset\_web\_handler.cpp](../../../../replication/replication\_web\_interface)

<div></div>

    mongo::ReplSetImpl::registerSlave(mongo::BSONObj const&, int)

- Used By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::replset::sethbmsg(std::string const&, int)

- Used By:

    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)
    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::ReplSetImpl::startupStatus

- Used By:

    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)
    - [src/mongo/db/repl/rs\_initiate.cpp](../../../../replication/replica\_set\_configuration)

<div></div>

    mongo::ReplSetImpl::sethbmsg(std::string const&, int)

- Used By:

    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::ReplSetImpl::getMostElectable()

- Used By:

    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)

<div></div>

    mongo::parseReplsetCmdLine(std::string const&, std::string&, std::vector<mongo::HostAndPort, std::allocator<mongo::HostAndPort> >&, std::set<mongo::HostAndPort, std::less<mongo::HostAndPort>, std::allocator<mongo::HostAndPort> >&)

- Used By:

    - [src/mongo/db/repl/repl\_start.cpp](../../../../replication/replication\_initialization)
    - [src/mongo/db/repl/rs\_initiate.cpp](../../../../replication/replica\_set\_configuration)

<div></div>

    mongo::replLocalAuth()

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/index\_builder.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::ReplSetImpl::loadLastOpTimeWritten(bool)

- Used By:

    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
