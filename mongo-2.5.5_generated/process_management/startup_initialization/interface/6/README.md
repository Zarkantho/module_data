
# Interface for TODO: Name this group
This interface information represents symbols thatare defined in this group but used in other modules.  Does not includesymbols defined in this group that are used inside this module.

### src/mongo/db/server\_options.cpp

<div></div>

    mongo::serverGlobalParams

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../security/authentication)
    - [src/mongo/util/net/listen.cpp](../../../network/network\_core)
    - [src/mongo/db/repl/consensus.cpp](../../../replication/replication)
    - [src/mongo/tools/bridge.cpp](../../../tools/tools)
    - [src/mongo/db/mongod\_options.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/tools/sniffer.cpp](../../../tools/tools)
    - [src/mongo/db/write\_concern.cpp](../../../replication/replication)
    - [src/mongo/db/dbmessage.cpp](../../../network/network\_core)
    - [src/mongo/db/cloner.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/introspect.cpp](../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../queries/database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication/replication)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../queries/database\_commands)
    - [src/mongo/s/strategy.cpp](../../../sharding/sharding)
    - [src/mongo/db/stats/snapshots.cpp](../../../utilities/utilities)
    - [src/mongo/shell/shell\_options.cpp](../../../mongo\_shell/mongo\_shell)
    - [src/mongo/dbtests/replsettests.cpp](../../../tests/unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../../../network/cpp\_client\_driver)
    - [src/mongo/util/net/sock.cpp](../../../network/network\_core)
    - [src/mongo/db/commands/validate.cpp](../../../queries/database\_commands)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../sharding/sharding)
    - [src/mongo/s/version\_mongos.cpp](../../../sharding/sharding)
    - [src/mongo/s/server.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/clientcursor.cpp](../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/dbwebserver.cpp](../../../network/web\_server)
    - [src/mongo/s/balance.cpp](../../../sharding/sharding)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../network/cpp\_client\_driver)
    - [src/mongo/db/repl/health.cpp](../../../replication/replication)
    - [src/mongo/s/mongos\_options.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding/sharding)
    - [src/mongo/db/commands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/commands/isself.cpp](../../../queries/database\_commands)
    - [src/mongo/db/catalog/database.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/index\_stats.cpp](../../../queries/database\_commands)
    - [src/mongo/db/instance.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/log\_process\_details.cpp](../../../process\_management/logging\_system)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../network/write\_commands)
    - [src/mongo/util/net/message\_server\_port.cpp](../../../network/network\_core)
    - [src/mongo/s/distlock.cpp](../../../sharding/sharding)
    - [src/mongo/db/dbeval.cpp](../../../queries/database\_commands)
    - [src/mongo/s/d\_split.cpp](../../../sharding/sharding)
    - [src/mongo/db/commands/storage\_details.cpp](../../../queries/database\_commands)
    - [src/mongo/db/pdfile.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../replication/replication)
    - [src/mongo/util/net/ssl\_options.cpp](../../../network/ssl)
    - [src/mongo/db/repl/rs\_initiate.cpp](../../../replication/replication)
    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/server\_status.cpp](../../../queries/database\_commands)
    - [src/mongo/shell/dbshell.cpp](../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/dbcommands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/index\_rebuilder.cpp](../../../queries/indexing)
    - [src/mongo/db/auth/security\_key.cpp](../../../security/authentication)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../network/write\_commands)
    - [src/mongo/db/commands/parameters.cpp](../../../queries/database\_commands)

### src/mongo/db/server\_options\_helpers.cpp

<div></div>

    mongo::addGeneralServerOptions(mongo::optionenvironment::OptionSection*)

- Used By:

    - [src/mongo/s/mongos\_options.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/mongod\_options.cpp](../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::storeServerOptions(mongo::optionenvironment::Environment const&, std::vector<std::string, std::allocator<std::string> > const&)

- Used By:

    - [src/mongo/s/mongos\_options.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/mongod\_options.cpp](../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::printCommandLineOpts()

- Used By:

    - [src/mongo/db/log\_process\_details.cpp](../../../process\_management/logging\_system)

<div></div>

    mongo::isMongos()

- Used By:

    - [src/mongo/db/extsort.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/s/grid.cpp](../../../sharding/sharding)
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/db/commands/parameters.cpp](../../../queries/database\_commands)
