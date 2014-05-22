
# Interface for Top Level Cluster Configuration
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/s/grid.cpp

<div></div>

    mongo::Grid::getDBConfig(mongo::StringData const&, bool, std::string const&)

- Used By:

    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/version\_manager.cpp](../../../../sharding/metadata\_versioning)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/routing)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../../sharding/routing)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/request.cpp](../../../../network/network\_core)

<div></div>

    mongo::Grid::addShard(std::string*, mongo::ConnectionString const&, long long, std::string&)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::Grid::shouldBalance(std::string const&, mongo::BSONObj*) const

- Used By:

    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::Grid::getConfigSetting(std::string const&) const

- Used By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::Grid::allowLocalHost() const

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::Grid::removeDBIfExists(mongo::DBConfig const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::Grid::setAllowLocalHost(bool)

- Used By:

    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::grid

- Used By:

    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/version\_manager.cpp](../../../../sharding/metadata\_versioning)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/routing)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../../sharding/routing)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/request.cpp](../../../../network/network\_core)

<div></div>

    mongo::Grid::flushConfig()

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::Grid::knowAboutShard(std::string const&) const

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
