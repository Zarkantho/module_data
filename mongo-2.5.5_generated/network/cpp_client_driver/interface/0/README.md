
# Interface for Replica Set Monitor
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/client/replica\_set\_monitor.cpp

<div></div>

    mongo::ReplicaSetMonitor::contains(mongo::HostAndPort const&) const

- Used By:

    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::ReplicaSetMonitor::getName() const

- Used By:

    - [src/mongo/s/dbclient\_shard\_resolver.cpp](../../../../sharding/routing)

<div></div>

    mongo::ReplicaSetMonitor::getServerAddress() const

- Used By:

    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::ReplicaSetMonitor::getMasterOrUassert()

- Used By:

    - [src/mongo/s/dbclient\_shard\_resolver.cpp](../../../../sharding/routing)

<div></div>

    mongo::ReplicaSetMonitor::appendInfo(mongo::BSONObjBuilder&) const

- Used By:

    - [src/mongo/shell/shell\_utils.cpp](../../../../mongo\_shell/mongo\_shell)

<div></div>

    mongo::ReplicaSetMonitor::setConfigChangeHook(boost::function<void (std::string const&, std::string const&)>)

- Used By:

    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::ReplicaSetMonitor::remove(std::string const&, bool)

- Used By:

    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::ReplicaSetMonitor::get(std::string const&, bool)

- Used By:

    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/dbclient\_shard\_resolver.cpp](../../../../sharding/routing)
    - [src/mongo/shell/shell\_utils.cpp](../../../../mongo\_shell/mongo\_shell)

<div></div>

    mongo::ReplicaSetMonitor::maxConsecutiveFailedChecks

- Used By:

    - [src/mongo/db/commands/parameters.cpp](../../../../queries/database\_commands)
