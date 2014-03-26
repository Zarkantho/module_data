
# Interface for Mongos Client State Implementation
This interface information represents symbols thatare defined in this group but used in other modules.  Does not includesymbols defined in this group that are used inside this module.

### src/mongo/s/client\_info.cpp

<div></div>

    mongo::ClientInfo::newRequest()

- Used By:

    - [src/mongo/s/request.cpp](../../../sharding/sharding)

<div></div>

    mongo::ClientInfo::disableForCommand()

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../sharding/sharding)

<div></div>

    mongo::ClientInfo::get(mongo::AbstractMessagingPort*)

- Used By:

    - [src/mongo/s/request.cpp](../../../sharding/sharding)
    - [src/mongo/s/commands\_public.cpp](../../../sharding/sharding)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding/sharding)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../network/write\_commands)

<div></div>

    mongo::ClientInfo::create(mongo::AbstractMessagingPort*)

- Used By:

    - [src/mongo/s/server.cpp](../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::saveGLEStats(mongo::BSONObj const&, std::string const&)

- Used By:

    - [src/mongo/s/shard.cpp](../../../sharding/sharding)

<div></div>

    mongo::ClientInfo::newPeerRequest(mongo::HostAndPort const&)

- Used By:

    - [src/mongo/s/request.cpp](../../../sharding/sharding)

<div></div>

    mongo::ClientInfo::addHostOpTimes(std::map<mongo::ConnectionString, mongo::HostOpTime, mongo::ConnectionStringComp, std::allocator<std::pair<mongo::ConnectionString const, mongo::HostOpTime> > > const&)

- Used By:

    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../network/write\_commands)

<div></div>

    mongo::ClientInfo::exists()

- Used By:

    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../network/write\_commands)

<div></div>

    mongo::ClientBasic::getCurrent()

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../security/authentication)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding/sharding)
    - [src/mongo/db/commands/mr.cpp](../../../queries/database\_commands)
    - [src/mongo/db/dbeval.cpp](../../../queries/database\_commands)
    - [src/mongo/s/server.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/s/cursors.cpp](../../../sharding/sharding)
    - [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../../../security/authorization)
    - [src/mongo/db/commands/server\_status.cpp](../../../queries/database\_commands)
    - [src/mongo/db/matcher/expression\_where.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../security/authorization)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication/replication)
    - [src/mongo/db/commands/connection\_status.cpp](../../../queries/database\_commands)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../../../process\_management/logging\_system)
    - [src/mongo/db/repl/rs.cpp](../../../replication/replication)
    - [src/mongo/db/commands/group.cpp](../../../queries/database\_commands)
    - [src/mongo/s/strategy.cpp](../../../sharding/sharding)
