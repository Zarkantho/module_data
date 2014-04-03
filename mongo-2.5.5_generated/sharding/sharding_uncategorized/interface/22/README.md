
# Interface for Shard Connection
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/s/shardconnection.cpp

<div></div>

    mongo::ShardConnection::forgetNS(std::string const&)

- Used By:

    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ShardConnection::~ShardConnection()

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::ShardConnection::releaseMyConnections()

- Used By:

    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::ShardConnection::_finishInit()

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/client/parallel.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::ShardConnection::kill()

- Used By:

    - [src/mongo/client/parallel.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::ShardConnection::ShardConnection(std::string const&, std::string const&, boost::shared_ptr<mongo::ChunkManager const>)

- Used By:

    - [src/mongo/client/parallel.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::shardConnectionPool

- Used By:

    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../../network/write\_commands)

<div></div>

    mongo::ShardConnection::ShardConnection(mongo::Shard const&, std::string const&, boost::shared_ptr<mongo::ChunkManager const>)

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/client/parallel.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::ShardConnection::checkMyConnectionVersions(std::string const&)

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::ShardConnection::done()

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
