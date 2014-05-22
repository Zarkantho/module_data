
# Interface for Server Options
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/server\_options.cpp

<div></div>

    mongo::serverGlobalParams

- Used By:

    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/index\_stats.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)
    - [src/mongo/util/net/listen.cpp](../../../../network/network\_core)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/util/net/ssl\_options.cpp](../../../../network/ssl)
    - [src/mongo/db/log\_process\_details.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/tools/sniffer.cpp](../../../../tools/tools)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/commands/isself.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/db/repl/rs\_initiate.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/commands/validate.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/db/commands/server\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/authentication\_commands.cpp](../../../../security/authentication)
    - [src/mongo/db/index\_rebuilder.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/util/net/message\_server\_port.cpp](../../../../network/network\_core)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/version\_mongos.cpp](../../../../process\_management/build\_information)
    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/repl/health.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/commands/parameters.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/dbmessage.cpp](../../../../network/network\_core)
    - [src/mongo/util/net/sock.cpp](../../../../network/network\_core)
    - [src/mongo/db/introspect.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/storage\_details.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/auth/security\_key.cpp](../../../../security/authentication)
    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)
    - [src/mongo/shell/shell\_options.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/dbeval.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/stats/snapshots.cpp](../../../../utilities/utilities)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/client/dbclient\_rs.cpp](../../../../network/cpp\_client\_driver)

### src/mongo/db/server\_options\_helpers.cpp

<div></div>

    mongo::printCommandLineOpts()

- Used By:

    - [src/mongo/db/log\_process\_details.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::isMongos()

- Used By:

    - [src/mongo/db/extsort.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/commands/parameters.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
