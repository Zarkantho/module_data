
# Interface

### src/mongo/client/replica\_set\_monitor.cpp

<div></div>

    mongo::ReplicaSetMonitor::contains(mongo::HostAndPort const&) const

- Used By:

    - [src/mongo/s/shard.cpp](../sharding)

<div></div>

    mongo::ReplicaSetMonitor::getName() const

- Used By:

    - [src/mongo/s/dbclient\_shard\_resolver.cpp](../sharding)

<div></div>

    mongo::ReplicaSetMonitor::getServerAddress() const

- Used By:

    - [src/mongo/s/grid.cpp](../sharding)

<div></div>

    mongo::ReplicaSetMonitor::getMasterOrUassert()

- Used By:

    - [src/mongo/s/dbclient\_shard\_resolver.cpp](../sharding)

<div></div>

    mongo::ReplicaSetMonitor::appendInfo(mongo::BSONObjBuilder&) const

- Used By:

    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)

<div></div>

    mongo::ReplicaSetMonitor::setConfigChangeHook(boost::function<void (std::string const&, std::string const&)>)

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::ReplicaSetMonitor::remove(std::string const&, bool)

- Used By:

    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/s/commands\_admin.cpp](../sharding)

<div></div>

    mongo::ReplicaSetMonitor::get(std::string const&, bool)

- Used By:

    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/s/dbclient\_shard\_resolver.cpp](../sharding)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)

<div></div>

    mongo::ReplicaSetMonitor::maxConsecutiveFailedChecks

- Used By:

    - [src/mongo/db/commands/parameters.cpp](../database\_commands)
