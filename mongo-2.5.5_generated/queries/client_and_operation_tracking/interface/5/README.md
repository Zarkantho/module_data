
# Interface for Shared Client State Interface
This interface information represents symbols thatare defined in this group but used in other modules.  Does not includesymbols defined in this group that are used inside this module.

### src/mongo/db/client\_basic.cpp

<div></div>

    mongo::ClientBasic::hasAuthorizationSession() const

- Used By:

    - [src/mongo/db/server\_extra\_log\_context.cpp](../../../process\_management/logging\_system)

<div></div>

    mongo::ClientBasic::resetAuthenticationSession(mongo::AuthenticationSession*)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../security/authentication)

<div></div>

    mongo::ClientBasic::swapAuthenticationSession(boost::scoped_ptr<mongo::AuthenticationSession>&)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../security/authentication)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../security/authentication)
    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../../../queries/database\_commands)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/repl/write\_concern.cpp](../../../replication/replication)
    - [src/mongo/db/cloner.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../../../process\_management/logging\_system)
    - [src/mongo/s/d\_split.cpp](../../../sharding/sharding)
    - [src/mongo/db/commands/group.cpp](../../../queries/database\_commands)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../../../sharding/sharding)
    - [src/mongo/s/strategy.cpp](../../../sharding/sharding)
    - [src/mongo/db/commands/copydb\_common.cpp](../../../queries/database\_commands)
    - [src/mongo/db/dbwebserver.cpp](../../../network/web\_server)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../queries/database\_commands)
    - [src/mongo/s/d\_state.cpp](../../../sharding/sharding)
    - [src/mongo/db/repl/rs.cpp](../../../replication/replication)
    - [src/mongo/db/restapi.cpp](../../../network/web\_server)
    - [src/mongo/db/commands.cpp](../../../queries/database\_commands)
    - [src/mongo/s/commands\_public.cpp](../../../sharding/sharding)
    - [src/mongo/db/ttl.cpp](../../../queries/indexing)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../queries/database\_commands)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../sharding/sharding)
    - [src/mongo/db/instance.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/s/request.cpp](../../../sharding/sharding)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../security/authorization)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../queries/database\_commands)
    - [src/mongo/db/commands/connection\_status.cpp](../../../queries/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding/sharding)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding/sharding)
    - [src/mongo/db/dbeval.cpp](../../../queries/database\_commands)
    - [src/mongo/s/cursors.cpp](../../../sharding/sharding)
    - [src/mongo/s/commands/cluster\_plan\_cache\_cmd.cpp](../../../sharding/sharding)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../network/write\_commands)
    - [src/mongo/db/commands/server\_status.cpp](../../../queries/database\_commands)
    - [src/mongo/db/matcher/expression\_where.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/commands/oplog\_note.cpp](../../../queries/database\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/index\_rebuilder.cpp](../../../queries/indexing)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../network/write\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../queries/database\_commands)
    - [src/mongo/s/commands/cluster\_index\_filter\_cmd.cpp](../../../sharding/sharding)
