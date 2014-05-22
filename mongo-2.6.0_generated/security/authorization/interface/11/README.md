
# Interface for Authorization Session
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/auth/authorization\_session.cpp

<div></div>

    mongo::AuthorizationSession::grantInternalAuthorization()

- Used By:

    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/index\_rebuilder.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/commands/authentication\_commands.cpp](../../../../security/authentication)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForPrivileges(std::vector<mongo::Privilege, std::allocator<mongo::Privilege> > const&)

- Used By:

    - [src/mongo/db/commands/server\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../../../../network/write\_commands)

<div></div>

    mongo::AuthorizationSession::AuthorizationSession(mongo::AuthzSessionExternalState*)

- Used By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/client\_info.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::AuthorizationSession::logoutDatabase(std::string const&)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../../security/authentication)

<div></div>

    mongo::AuthorizationSession::checkAuthForInsert(mongo::NamespaceString const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnResource(mongo::ResourcePattern const&, mongo::ActionType)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/commands/cluster\_plan\_cache\_cmd.cpp](../../../../core\_query\_system/query\_system\_commands)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../../core\_query\_system/query\_system\_commands)
    - [src/mongo/s/commands/cluster\_index\_filter\_cmd.cpp](../../../../core\_query\_system/query\_system\_commands)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/db/commands/oplog\_note.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../../core\_query\_system/query\_system\_commands)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::AuthorizationSession::checkAuthForQuery(mongo::NamespaceString const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::AuthorizationSession::isImpersonating() const

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForPrivilege(mongo::Privilege const&)

- Used By:

    - [src/mongo/db/commands/create\_indexes.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::AuthorizationSession::~AuthorizationSession()

- Used By:

    - [src/mongo/db/client\_basic.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::AuthorizationSession::checkAuthForDelete(mongo::NamespaceString const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnNamespace(mongo::NamespaceString const&, mongo::ActionType)

- Used By:

    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/group.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnResource(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Used By:

    - [src/mongo/db/commands/copydb\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::AuthorizationSession::getAuthenticatedUserNames()

- Used By:

    - [src/mongo/db/introspect.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/db/commands/connection\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::AuthorizationSession::getAuthenticatedUserNamesToken()

- Used By:

    - [src/mongo/db/matcher/expression\_where.cpp](../../../../core\_query\_system/query\_preprocessing)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/group.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/dbeval.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::AuthorizationSession::checkAuthForUpdate(mongo::NamespaceString const&, mongo::BSONObj const&, mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::AuthorizationSession::addAndAuthorizeUser(mongo::UserName const&)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../../security/authentication)
    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)

<div></div>

    mongo::AuthorizationSession::getAuthorizationManager()

- Used By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/db/restapi.cpp](../../../../network/web\_server)

<div></div>

    mongo::AuthorizationSession::setImpersonatedUserNames(std::vector<mongo::UserName, std::allocator<mongo::UserName> > const&)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::AuthorizationSession::startRequest()

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/request.cpp](../../../../network/network\_core)

<div></div>

    mongo::AuthorizationSession::checkAuthForGetMore(mongo::NamespaceString const&, long long)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnNamespace(mongo::NamespaceString const&, mongo::ActionSet const&)

- Used By:

    - [src/mongo/db/commands/copydb\_common.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::AuthorizationSession::clearImpersonatedUserNames()

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
