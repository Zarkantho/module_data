
# Interface

### src/mongo/client/clientAndShell.cpp

<div></div>

    mongo::dbexitCalled

- Used By:

    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../mongo\_shell)
    - [src/mongo/shell/dbshell.cpp](../../../mongo\_shell)

<div></div>

    mongo::shell_utils::mongoProgramOutputMutex

- Used By:

    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../mongo\_shell)
    - [src/mongo/shell/dbshell.cpp](../../../mongo\_shell)

<div></div>

    mongo::haveLocalShardingInfo(std::string const&)

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../javascript\_libraries)

<div></div>

    mongo::createDirectClient()

- Used By:

    - [src/mongo/scripting/engine.cpp](../../../javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../javascript\_libraries)

<div></div>

    mongo::dbexit(mongo::ExitCode, char const*)

- Used By:

    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/framework.cpp](../../../unit\_tests)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)
    - [src/mongo/util/net/message\_server\_port.cpp](../../../network\_core)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/tools/tool.cpp](../../../tools)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)

<div></div>

    mongo::Shard::isAShardNode(std::string const&)

- Used By:

    - [src/mongo/s/writeback\_listener.cpp](../../../writeback\_listener)

<div></div>

    mongo::Shard::getAllShards(std::vector<mongo::Shard, std::allocator<mongo::Shard> >&)

- Used By:

    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../../../authorization)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/s/balance.cpp](../../../sharding)
    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/s/shardconnection.cpp](../../../sharding)

<div></div>

    mongo::inShutdown()

- Used By:

    - [src/mongo/util/net/listen.cpp](../../../network\_core)
    - [src/mongo/util/assert\_util.cpp](../../../utilities)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../../../authorization)
    - [src/mongo/db/repl/bgsync.cpp](../../../replication)
    - [src/mongo/db/range\_deleter.cpp](../../../sharding)
    - [src/mongo/db/dur\_journal.cpp](../../../journaling)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../journaling)
    - [src/mongo/db/repl/write\_concern.cpp](../../../replication)
    - [src/mongo/db/stats/snapshots.cpp](../../../utilities)
    - [src/mongo/util/concurrency/task.cpp](../../../utilities)
    - [src/mongo/s/writeback\_listener.cpp](../../../writeback\_listener)
    - [src/mongo/db/clientcursor.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/s/balance.cpp](../../../sharding)
    - [src/mongo/s/shardconnection.cpp](../../../sharding)
    - [src/mongo/db/dur.cpp](../../../journaling)
    - [src/mongo/db/ttl.cpp](../../../indexing)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/util/net/message\_server\_port.cpp](../../../network\_core)
    - [src/mongo/s/distlock.cpp](../../../sharding)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/s/config\_server\_checker\_service.cpp](../../../sharding)
    - [src/mongo/db/storage/data\_file.cpp](../../../mmap\_file\_interface)

<div></div>

    mongo::ClientBasic::getCurrent()

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../authentication)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/db/dbeval.cpp](../../../database\_commands)
    - [src/mongo/s/server.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/s/cursors.cpp](../../../sharding)
    - [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../../../authorization)
    - [src/mongo/db/commands/server\_status.cpp](../../../database\_commands)
    - [src/mongo/db/matcher/expression\_where.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../authorization)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication)
    - [src/mongo/db/commands/connection\_status.cpp](../../../database\_commands)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../../../logging\_system)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/db/commands/group.cpp](../../../database\_commands)
    - [src/mongo/s/strategy.cpp](../../../sharding)
