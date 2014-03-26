
# Interface

### src/mongo/db/auth/authorization\_session.cpp

<div></div>

    mongo::AuthorizationSession::startRequest()

- Used By:

    - [src/mongo/s/request.cpp](../../../sharding)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::AuthorizationSession::grantInternalAuthorization()

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../authentication)
    - [src/mongo/db/ttl.cpp](../../../indexing)
    - [src/mongo/db/dbwebserver.cpp](../../../web\_server)
    - [src/mongo/db/repl/write\_concern.cpp](../../../replication)
    - [src/mongo/db/index\_rebuilder.cpp](../../../indexing)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnResource(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Used By:

    - [src/mongo/db/commands/copydb\_common.cpp](../../../database\_commands)
    - [src/mongo/db/cloner.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../../../database\_commands)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForPrivileges(std::vector<mongo::Privilege, std::allocator<mongo::Privilege> > const&)

- Used By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)
    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/server\_status.cpp](../../../database\_commands)

<div></div>

    mongo::AuthorizationSession::getAuthorizationManager()

- Used By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)
    - [src/mongo/db/dbwebserver.cpp](../../../web\_server)
    - [src/mongo/db/restapi.cpp](../../../web\_server)

<div></div>

    mongo::AuthorizationSession::setImpersonatedUserNames(std::vector<mongo::UserName, std::allocator<mongo::UserName> > const&)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)

<div></div>

    mongo::AuthorizationSession::AuthorizationSession(mongo::AuthzSessionExternalState*)

- Used By:

    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/s/client\_info.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForPrivilege(mongo::Privilege const&)

- Used By:

    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../database\_commands)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../database\_commands)

<div></div>

    mongo::AuthorizationSession::getAuthenticatedUserNamesToken()

- Used By:

    - [src/mongo/db/matcher/expression\_where.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/db/dbeval.cpp](../../../database\_commands)
    - [src/mongo/db/commands/group.cpp](../../../database\_commands)

<div></div>

    mongo::AuthorizationSession::getAuthenticatedUserNames()

- Used By:

    - [src/mongo/db/commands/connection\_status.cpp](../../../database\_commands)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../../../logging\_system)
    - [src/mongo/db/introspect.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::AuthorizationSession::logoutDatabase(std::string const&)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../authentication)

<div></div>

    mongo::AuthorizationSession::checkAuthForQuery(mongo::NamespaceString const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::AuthorizationSession::checkAuthForInsert(mongo::NamespaceString const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::AuthorizationSession::checkAuthForGetMore(mongo::NamespaceString const&, long long)

- Used By:

    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnResource(mongo::ResourcePattern const&, mongo::ActionType)

- Used By:

    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../../../sharding)
    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../../../database\_commands)
    - [src/mongo/s/commands/cluster\_plan\_cache\_cmd.cpp](../../../sharding)
    - [src/mongo/s/commands\_public.cpp](../../../sharding)
    - [src/mongo/db/commands/oplog\_note.cpp](../../../database\_commands)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../database\_commands)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/s/d\_state.cpp](../../../sharding)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../sharding)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../database\_commands)
    - [src/mongo/s/d\_split.cpp](../../../sharding)
    - [src/mongo/s/commands/cluster\_index\_filter\_cmd.cpp](../../../sharding)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)

<div></div>

    mongo::AuthorizationSession::~AuthorizationSession()

- Used By:

    - [src/mongo/db/client\_basic.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnNamespace(mongo::NamespaceString const&, mongo::ActionSet const&)

- Used By:

    - [src/mongo/db/commands/copydb\_common.cpp](../../../database\_commands)

<div></div>

    mongo::AuthorizationSession::checkAuthForDelete(mongo::NamespaceString const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::AuthorizationSession::checkAuthForUpdate(mongo::NamespaceString const&, mongo::BSONObj const&, mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::AuthorizationSession::isImpersonating() const

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnNamespace(mongo::NamespaceString const&, mongo::ActionType)

- Used By:

    - [src/mongo/s/cursors.cpp](../../../sharding)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/commands/group.cpp](../../../database\_commands)

<div></div>

    mongo::AuthorizationSession::addAndAuthorizeUser(mongo::UserName const&)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../authentication)
    - [src/mongo/db/dbwebserver.cpp](../../../web\_server)

<div></div>

    mongo::AuthorizationSession::clearImpersonatedUserNames()

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
