
# Interface

### src/mongo/db/server\_options.cpp

<div></div>

    mongo::serverGlobalParams

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../database\_commands)
    - [src/mongo/util/net/listen.cpp](../../../network)
    - [src/mongo/db/repl/consensus.cpp](../../../replication)
    - [src/mongo/tools/bridge.cpp](../../../tools)
    - [src/mongo/db/mongod\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/sniffer.cpp](../../../tools)
    - [src/mongo/db/write\_concern.cpp](../../../replication)
    - [src/mongo/db/dbmessage.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/cloner.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/introspect.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../../../core\_query\_system)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../database\_commands)
    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/db/stats/snapshots.cpp](../../../utilities)
    - [src/mongo/shell/shell\_options.cpp](../../../mongo\_shell)
    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../../../cpp\_client\_driver)
    - [src/mongo/util/net/sock.cpp](../../../network)
    - [src/mongo/db/commands/validate.cpp](../../../database\_commands)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../sharding)
    - [src/mongo/s/version\_mongos.cpp](../../../sharding)
    - [src/mongo/s/server.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/clientcursor.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/dbwebserver.cpp](../../../web\_server)
    - [src/mongo/s/balance.cpp](../../../sharding)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/repl/health.cpp](../../../replication)
    - [src/mongo/s/mongos\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/db/commands.cpp](../../../database\_commands)
    - [src/mongo/db/commands/isself.cpp](../../../database\_commands)
    - [src/mongo/db/catalog/database.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/commands/index\_stats.cpp](../../../database\_commands)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/log\_process\_details.cpp](../../../logging\_system)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/util/net/message\_server\_port.cpp](../../../network)
    - [src/mongo/s/distlock.cpp](../../../sharding)
    - [src/mongo/db/dbeval.cpp](../../../database\_commands)
    - [src/mongo/s/d\_split.cpp](../../../sharding)
    - [src/mongo/db/commands/storage\_details.cpp](../../../database\_commands)
    - [src/mongo/db/pdfile.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../replication)
    - [src/mongo/util/net/ssl\_options.cpp](../../../network)
    - [src/mongo/db/repl/rs\_initiate.cpp](../../../replication)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/server\_status.cpp](../../../database\_commands)
    - [src/mongo/shell/dbshell.cpp](../../../mongo\_shell)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/index\_rebuilder.cpp](../../../indexing)
    - [src/mongo/db/auth/security\_key.cpp](../../../authentication)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/parameters.cpp](../../../database\_commands)

### src/mongo/db/server\_options\_helpers.cpp

<div></div>

    mongo::addGeneralServerOptions(mongo::optionenvironment::OptionSection*)

- Used By:

    - [src/mongo/s/mongos\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/mongod\_options.cpp](../../../mongos\_and\_mongod\_mains)

<div></div>

    mongo::storeServerOptions(mongo::optionenvironment::Environment const&, std::vector<std::string, std::allocator<std::string> > const&)

- Used By:

    - [src/mongo/s/mongos\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/mongod\_options.cpp](../../../mongos\_and\_mongod\_mains)

<div></div>

    mongo::printCommandLineOpts()

- Used By:

    - [src/mongo/db/log\_process\_details.cpp](../../../logging\_system)

<div></div>

    mongo::isMongos()

- Used By:

    - [src/mongo/db/extsort.cpp](../../../aggregation\_framework)
    - [src/mongo/s/grid.cpp](../../../sharding)
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../../../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../../../aggregation\_framework)
    - [src/mongo/db/commands/parameters.cpp](../../../database\_commands)
