
# Interface for Shared Client State Interface
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/client\_basic.cpp

<div></div>

    mongo::ClientBasic::hasAuthorizationSession() const

- Used By:

    - [src/mongo/db/server\_extra\_log\_context.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::ClientBasic::resetAuthenticationSession(mongo::AuthenticationSession*)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../../security/authentication)

<div></div>

    mongo::ClientBasic::swapAuthenticationSession(boost::scoped_ptr<mongo::AuthenticationSession>&)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../../security/authentication)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Used By:

    - [src/mongo/s/request.cpp](../../../../network/network\_core)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../../network/write\_commands)
    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/db/dbeval.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../../core\_query\_system/query\_system\_commands)
    - [src/mongo/db/commands/authentication\_commands.cpp](../../../../security/authentication)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/commands/group.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/s/commands/cluster\_index\_filter\_cmd.cpp](../../../../core\_query\_system/query\_system\_commands)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../../security/authorization)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../../core\_query\_system/query\_system\_commands)
    - [src/mongo/s/commands/cluster\_plan\_cache\_cmd.cpp](../../../../core\_query\_system/query\_system\_commands)
    - [src/mongo/db/restapi.cpp](../../../../network/web\_server)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../../network/write\_commands)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/index\_rebuilder.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/commands/copydb\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/server\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/matcher/expression\_where.cpp](../../../../core\_query\_system/query\_preprocessing)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/oplog\_note.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/connection\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
