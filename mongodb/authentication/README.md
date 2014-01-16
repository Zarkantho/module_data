# authentication

# Module Groups

-------------

# Group Description
Authapalooza! TODO: actually separate this logically.

# Files
- src/mongo/db/auth/action\_set.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/action\_set.h
- src/mongo/db/auth/action\_set\_test.cpp   ()
- src/mongo/db/auth/action\_types.txt
- src/mongo/db/auth/auth\_index\_d.cpp   (mongod, tools)
- src/mongo/db/auth/auth\_index\_d.h
- src/mongo/db/auth/auth\_server\_parameters.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/authentication\_session.h
- src/mongo/db/auth/authorization\_manager.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/authorization\_manager.h
- src/mongo/db/auth/authorization\_manager\_global.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/authorization\_manager\_global.h
- src/mongo/db/auth/authorization\_manager\_test.cpp   ()
- src/mongo/db/auth/authorization\_session.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/authorization\_session.h
- src/mongo/db/auth/authorization\_session\_test.cpp   ()
- src/mongo/db/auth/authz\_documents\_update\_guard.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/authz\_documents\_update\_guard.h
- src/mongo/db/auth/authz\_manager\_external\_state.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/authz\_manager\_external\_state.h
- src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp   (mongod, tools)
- src/mongo/db/auth/authz\_manager\_external\_state\_d.h
- src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/authz\_manager\_external\_state\_local.h
- src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/authz\_manager\_external\_state\_mock.h
- src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp   (mongos)
- src/mongo/db/auth/authz\_manager\_external\_state\_s.h
- src/mongo/db/auth/authz\_session\_external\_state.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/authz\_session\_external\_state.h
- src/mongo/db/auth/authz\_session\_external\_state\_d.cpp   (mongod, tools)
- src/mongo/db/auth/authz\_session\_external\_state\_d.h
- src/mongo/db/auth/authz\_session\_external\_state\_mock.h
- src/mongo/db/auth/authz\_session\_external\_state\_s.cpp   (mongos)
- src/mongo/db/auth/authz\_session\_external\_state\_s.h
- src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/authz\_session\_external\_state\_server\_common.h
- src/mongo/db/auth/generate\_action\_types.py
- src/mongo/db/auth/mongo\_authentication\_session.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/mongo\_authentication\_session.h
- src/mongo/db/auth/privilege.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/privilege.h
- src/mongo/db/auth/privilege\_parser.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/privilege\_parser.h
- src/mongo/db/auth/privilege\_parser\_test.cpp   ()
- src/mongo/db/auth/resource\_pattern.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/resource\_pattern.h
- src/mongo/db/auth/role\_graph.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/role\_graph.h
- src/mongo/db/auth/role\_graph\_builtin\_roles.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/role\_graph\_test.cpp   ()
- src/mongo/db/auth/role\_graph\_update.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/role\_name.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/role\_name.h
- src/mongo/db/auth/security\_key.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/security\_key.h
- src/mongo/db/auth/user.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/user.h
- src/mongo/db/auth/user\_cache\_invalidator\_job.cpp   (mongos)
- src/mongo/db/auth/user\_cache\_invalidator\_job.h
- src/mongo/db/auth/user\_document\_parser.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/user\_document\_parser.h
- src/mongo/db/auth/user\_document\_parser\_test.cpp   ()
- src/mongo/db/auth/user\_management\_commands\_parser.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/user\_management\_commands\_parser.h
- src/mongo/db/auth/user\_name.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/user\_name.h
- src/mongo/db/auth/user\_name\_hash.h
- src/mongo/db/auth/user\_set.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/user\_set.h
- src/mongo/db/auth/user\_set\_test.cpp   ()

# Interface

### src/mongo/db/auth/action\_set.cpp

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Used By:

    - [src/mongo/db/compact.cpp](../database\_commands)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../database\_commands)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/db/commands/find\_and\_modify\_common.cpp](../database\_commands)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/s/d\_writeback.cpp](../sharding)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)
    - [src/mongo/db/commands/fsync.cpp](../database\_commands)
    - [src/mongo/db/repl/resync.cpp](../replication)
    - [src/mongo/db/commands/copydb\_common.cpp](../database\_commands)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/geo/haystack.cpp](../geo\_queries)
    - [src/mongo/db/commands/mr\_common.cpp](../database\_commands)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/commands/geonear.cpp](../database\_commands)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/db/stats/top.cpp](../utilities)
    - [src/mongo/db/repl/rs\_initiate.cpp](../replication)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/db/commands/shutdown.cpp](../database\_commands)
    - [src/mongo/db/fts/fts\_command.cpp](../full\_text\_search\_module)
    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/commands/distinct.cpp](../database\_commands)
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

<div></div>

    mongo::ActionSet::removeAllActions()

- Used By:

    - [src/mongo/db/commands/copydb\_common.cpp](../database\_commands)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../database\_commands)

### src/mongo/db/auth/auth\_index\_d.cpp

<div></div>

    mongo::authindex::createSystemIndexes(mongo::NamespaceString const&)

- Used By:

    - [src/mongo/db/database.cpp](../storage\_layer\_structure)

### src/mongo/db/auth/authorization\_manager.cpp

<div></div>

    mongo::AuthorizationManager::updateAuthzDocuments(mongo::NamespaceString const&, mongo::BSONObj const&, mongo::BSONObj const&, bool, bool, mongo::BSONObj const&, int*) const

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::internalSecurity

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationManager::ROLE_NAME_FIELD_NAME

- Used By:

    - src/mongo/db/modules/subscription/src/audit/audit\_user\_management.cpp
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

<div></div>

    mongo::AuthorizationManager::schemaVersion26Final

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationManager::updateRoleDocument(mongo::RoleName const&, mongo::BSONObj const&, mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationManager::logOp(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, bool*)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)

<div></div>

    mongo::AuthorizationManager::rolesCollectionNamespace

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationManager::invalidateUsersFromDB(std::string const&)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationManager::releaseUser(mongo::User*)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - src/mongo/db/modules/subscription/src/sasl/auxprop\_mongodb\_internal.cpp
    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationManager::getRoleDescriptionsForDB(std::string, bool, bool, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> >*)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationManager::getBSONForPrivileges(std::vector<mongo::Privilege, std::allocator<mongo::Privilege> > const&, mongo::mutablebson::Element)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationManager::removePrivilegeDocuments(mongo::BSONObj const&, mongo::BSONObj const&, int*) const

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationManager::writeAuthSchemaVersionIfNeeded()

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationManager::queryAuthzDocument(mongo::NamespaceString const&, mongo::BSONObj const&, mongo::BSONObj const&, boost::function<void (mongo::BSONObj const&)> const&)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationManager::getRoleDescription(mongo::RoleName const&, bool, mongo::BSONObj*)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationManager::acquireUser(mongo::UserName const&, mongo::User**)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - src/mongo/db/modules/subscription/src/sasl/auxprop\_mongodb\_internal.cpp
    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationManager::AuthorizationManager(mongo::AuthzManagerExternalState*)

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/tool.cpp](../tools)
    - src/mongo/db/modules/subscription/src/sasl/sasl\_authentication\_session.cpp
    - [src/mongo/dbtests/dbtests.cpp](../unit\_tests)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::AuthorizationManager::getUserDescription(mongo::UserName const&, mongo::BSONObj*)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationManager::ROLE_SOURCE_FIELD_NAME

- Used By:

    - src/mongo/db/modules/subscription/src/audit/audit\_user\_management.cpp
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

<div></div>

    mongo::AuthorizationManager::removeRoleDocuments(mongo::BSONObj const&, mongo::BSONObj const&, int*) const

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationManager::hasAnyPrivilegeDocuments() const

- Used By:

    - [src/mongo/db/restapi.cpp](../database\_web\_accesss)

<div></div>

    mongo::AuthorizationManager::isAuthEnabled() const

- Used By:

    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/db/repl/oplogreader.cpp](../replication)
    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::AuthorizationManager::invalidateUserCache()

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationManager::schemaVersion26Upgrade

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationManager::~AuthorizationManager()

- Used By:

    - src/mongo/db/modules/subscription/src/sasl/sasl\_authentication\_session.cpp

<div></div>

    mongo::AuthorizationManager::insertRoleDocument(mongo::BSONObj const&, mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationManager::updatePrivilegeDocument(mongo::UserName const&, mongo::BSONObj const&, mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationManager::setAuthEnabled(bool)

- Used By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::AuthorizationManager::invalidateUserByName(mongo::UserName const&)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationManager::upgradeSchemaStep(mongo::BSONObj const&, bool*)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationManager::initialize()

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)

<div></div>

    mongo::AuthorizationManager::insertPrivilegeDocument(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationManager::USER_DB_FIELD_NAME

- Used By:

    - src/mongo/db/modules/subscription/src/audit/audit\_authentication.cpp
    - src/mongo/db/modules/subscription/src/audit/audit\_event.cpp
    - src/mongo/db/modules/subscription/src/audit/audit\_user\_management.cpp
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - [src/mongo/db/commands/connection\_status.cpp](../database\_commands)
    - src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

<div></div>

    mongo::AuthorizationManager::usersCollectionNamespace

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationManager::getAuthorizationVersion()

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationManager::USER_NAME_FIELD_NAME

- Used By:

    - src/mongo/db/modules/subscription/src/audit/audit\_authentication.cpp
    - src/mongo/db/modules/subscription/src/audit/audit\_event.cpp
    - src/mongo/db/modules/subscription/src/audit/audit\_user\_management.cpp
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - [src/mongo/db/commands/connection\_status.cpp](../database\_commands)
    - src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

### src/mongo/db/auth/authorization\_manager\_global.cpp

<div></div>

    mongo::getGlobalAuthorizationManager()

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/oplogreader.cpp](../replication)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)

<div></div>

    mongo::setGlobalAuthorizationManager(mongo::AuthorizationManager*)

- Used By:

    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/dbtests.cpp](../unit\_tests)

### src/mongo/db/auth/authorization\_session.cpp

<div></div>

    mongo::AuthorizationSession::startRequest()

- Used By:

    - [src/mongo/s/request.cpp](../sharding)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::AuthorizationSession::grantInternalAuthorization()

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::AuthorizationSession::isAuthenticatedAsUserWithRole(mongo::RoleName const&)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationSession::lookupUser(mongo::UserName const&)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnResource(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Used By:

    - [src/mongo/db/commands/copydb\_common.cpp](../database\_commands)
    - [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForPrivileges(std::vector<mongo::Privilege, std::allocator<mongo::Privilege> > const&)

- Used By:

    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationSession::getAuthorizationManager()

- Used By:

    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
    - src/mongo/db/modules/subscription/src/sasl/auxprop\_mongodb\_internal.cpp
    - [src/mongo/db/restapi.cpp](../database\_web\_accesss)

<div></div>

    mongo::AuthorizationSession::checkAuthorizedToRevokePrivilege(mongo::Privilege const&)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationSession::setImpersonatedUserNames(std::vector<mongo::UserName, std::allocator<mongo::UserName> > const&)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationSession::AuthorizationSession(mongo::AuthzSessionExternalState*)

- Used By:

    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - src/mongo/db/modules/subscription/src/sasl/sasl\_authentication\_session.cpp
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForPrivilege(mongo::Privilege const&)

- Used By:

    - src/mongo/db/modules/subscription/src/audit/impersonate\_helpers\_d.cpp

<div></div>

    mongo::AuthorizationSession::getAuthenticatedUserNamesToken()

- Used By:

    - [src/mongo/db/matcher/expression\_where.cpp](../query\_system)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/dbeval.cpp](../database\_commands)
    - [src/mongo/db/commands/group.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationSession::getImpersonatedUserNames() const

- Used By:

    - src/mongo/db/modules/subscription/src/audit/audit\_private.cpp

<div></div>

    mongo::AuthorizationSession::isAuthorizedToChangeOwnPasswordAsUser(mongo::UserName const&)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationSession::getAuthenticatedUserNames()

- Used By:

    - [src/mongo/db/commands/connection\_status.cpp](../database\_commands)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../logging\_system)
    - src/mongo/db/modules/subscription/src/audit/audit\_private.cpp
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - src/mongo/db/modules/subscription/src/audit/impersonate\_helpers\_s.cpp

<div></div>

    mongo::AuthorizationSession::logoutDatabase(std::string const&)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationSession::checkAuthForQuery(mongo::NamespaceString const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::AuthorizationSession::checkAuthForInsert(mongo::NamespaceString const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::AuthorizationSession::checkAuthForGetMore(mongo::NamespaceString const&, long long)

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::AuthorizationSession::isAuthorizedToRevokeRole(mongo::RoleName const&)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationSession::isAuthorizedToGrantRole(mongo::RoleName const&)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnResource(mongo::ResourcePattern const&, mongo::ActionType)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)
    - [src/mongo/db/commands/rename\_collection\_common.cpp](../database\_commands)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - src/mongo/db/modules/subscription/src/audit/audit\_command.cpp
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)
    - [src/mongo/s/strategy\_single.cpp](../sharding)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::AuthorizationSession::~AuthorizationSession()

- Used By:

    - [src/mongo/db/client\_basic.cpp](../client\_and\_operation\_tracking)
    - src/mongo/db/modules/subscription/src/sasl/sasl\_authentication\_session.cpp

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnNamespace(mongo::NamespaceString const&, mongo::ActionSet const&)

- Used By:

    - [src/mongo/db/commands/copydb\_common.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationSession::checkAuthForDelete(mongo::NamespaceString const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::AuthorizationSession::checkAuthForUpdate(mongo::NamespaceString const&, mongo::BSONObj const&, mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::AuthorizationSession::isImpersonating() const

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnNamespace(mongo::NamespaceString const&, mongo::ActionType)

- Used By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/db/commands/group.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationSession::checkAuthorizedToGrantPrivilege(mongo::Privilege const&)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationSession::addAndAuthorizeUser(mongo::UserName const&)

- Used By:

    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)

<div></div>

    mongo::AuthorizationSession::clearImpersonatedUserNames()

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationSession::isAuthorizedToChangeOwnCustomDataAsUser(mongo::UserName const&)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

### src/mongo/db/auth/authz\_documents\_update\_guard.cpp

<div></div>

    mongo::AuthzDocumentsUpdateGuard::tryLock(mongo::StringData const&)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthzDocumentsUpdateGuard::~AuthzDocumentsUpdateGuard()

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::AuthzDocumentsUpdateGuard::AuthzDocumentsUpdateGuard(mongo::AuthorizationManager*)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

### src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp

<div></div>

    mongo::AuthzManagerExternalStateMongod::AuthzManagerExternalStateMongod()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp

<div></div>

    mongo::AuthzManagerExternalStateMock::AuthzManagerExternalStateMock()

- Used By:

    - [src/mongo/tools/tool.cpp](../tools)
    - src/mongo/db/modules/subscription/src/sasl/sasl\_authentication\_session.cpp
    - [src/mongo/dbtests/dbtests.cpp](../unit\_tests)

### src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp

<div></div>

    mongo::AuthzManagerExternalStateMongos::AuthzManagerExternalStateMongos()

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/db/auth/authz\_session\_external\_state.cpp

<div></div>

    mongo::AuthzSessionExternalState::AuthzSessionExternalState(mongo::AuthorizationManager*)

- Used By:

    - src/mongo/db/modules/subscription/src/sasl/sasl\_authentication\_session.cpp

<div></div>

    mongo::AuthzSessionExternalState::~AuthzSessionExternalState()

- Used By:

    - src/mongo/db/modules/subscription/src/sasl/sasl\_authentication\_session.cpp

<div></div>

    typeinfo for mongo::AuthzSessionExternalState

- Used By:

    - src/mongo/db/modules/subscription/src/sasl/sasl\_authentication\_session.cpp

### src/mongo/db/auth/authz\_session\_external\_state\_d.cpp

<div></div>

    mongo::AuthzSessionExternalStateMongod::AuthzSessionExternalStateMongod(mongo::AuthorizationManager*)

- Used By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

### src/mongo/db/auth/authz\_session\_external\_state\_s.cpp

<div></div>

    mongo::AuthzSessionExternalStateMongos::AuthzSessionExternalStateMongos(mongo::AuthorizationManager*)

- Used By:

    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

### src/mongo/db/auth/mongo\_authentication\_session.cpp

<div></div>

    mongo::MongoAuthenticationSession::MongoAuthenticationSession(unsigned long long)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)

### src/mongo/db/auth/privilege.cpp

<div></div>

    mongo::Privilege::addPrivilegeToPrivilegeVector(std::vector<mongo::Privilege, std::allocator<mongo::Privilege> >*, mongo::Privilege const&)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Used By:

    - [src/mongo/db/compact.cpp](../database\_commands)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/db/commands/find\_and\_modify\_common.cpp](../database\_commands)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/s/d\_writeback.cpp](../sharding)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)
    - [src/mongo/db/commands/fsync.cpp](../database\_commands)
    - [src/mongo/db/repl/resync.cpp](../replication)
    - [src/mongo/db/geo/haystack.cpp](../geo\_queries)
    - [src/mongo/db/commands/mr\_common.cpp](../database\_commands)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/commands/geonear.cpp](../database\_commands)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/db/stats/top.cpp](../utilities)
    - [src/mongo/db/repl/rs\_initiate.cpp](../replication)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/db/commands/shutdown.cpp](../database\_commands)
    - [src/mongo/db/fts/fts\_command.cpp](../full\_text\_search\_module)
    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/commands/distinct.cpp](../database\_commands)
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

<div></div>

    mongo::Privilege::removeActions(mongo::ActionSet const&)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionType const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/db/commands/mr\_common.cpp](../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../new\_wire\_protocol\_write\_commands)
    - src/mongo/db/modules/subscription/src/audit/impersonate\_helpers\_d.cpp

### src/mongo/db/auth/privilege\_parser.cpp

<div></div>

    mongo::ParsedPrivilege::toBSON() const

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

<div></div>

    mongo::ParsedPrivilege::ParsedPrivilege()

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

<div></div>

    mongo::ParsedPrivilege::toString() const

- Used By:

    - src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

<div></div>

    mongo::ParsedPrivilege::isValid(std::string*) const

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::ParsedPrivilege::~ParsedPrivilege()

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

<div></div>

    mongo::ParsedPrivilege::privilegeToParsedPrivilege(mongo::Privilege const&, mongo::ParsedPrivilege*, std::string*)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

### src/mongo/db/auth/resource\_pattern.cpp

<div></div>

    mongo::ResourcePattern::toString() const

- Used By:

    - [src/mongo/db/commands/mr\_common.cpp](../database\_commands)
    - [src/mongo/db/commands/find\_and\_modify\_common.cpp](../database\_commands)
    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)

### src/mongo/db/auth/role\_graph\_builtin\_roles.cpp

<div></div>

    mongo::RoleGraph::isBuiltinRole(mongo::RoleName const&)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::RoleGraph::generateUniversalPrivileges(std::vector<mongo::Privilege, std::allocator<mongo::Privilege> >*)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/db/dbeval.cpp](../database\_commands)
    - [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)

### src/mongo/db/auth/role\_name.cpp

<div></div>

    mongo::RoleName::RoleName(mongo::StringData const&, mongo::StringData const&)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::operator<<(std::ostream&, mongo::RoleName const&)

- Used By:

    - src/mongo/db/modules/subscription/src/audit/audit\_user\_management.cpp
    - src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

### src/mongo/db/auth/security\_key.cpp

<div></div>

    mongo::isInternalAuthSet()

- Used By:

    - [src/mongo/db/repl/oplogreader.cpp](../replication)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)

<div></div>

    mongo::authenticateInternalUser(mongo::DBClientWithCommands*)

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/db/repl/oplogreader.cpp](../replication)
    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)

<div></div>

    mongo::setInternalUserAuthParams(mongo::BSONObj)

- Used By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)

<div></div>

    mongo::setUpSecurityKey(std::string const&)

- Used By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)

### src/mongo/db/auth/user.cpp

<div></div>

    mongo::User::getRoles() const

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::User::getCredentials() const

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
    - src/mongo/db/modules/subscription/src/sasl/auxprop\_mongodb\_internal.cpp

<div></div>

    mongo::User::getName() const

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)

### src/mongo/db/auth/user\_cache\_invalidator\_job.cpp

<div></div>

    vtable for mongo::UserCacheInvalidator

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/db/auth/user\_document\_parser.cpp

<div></div>

    mongo::V2UserDocumentParser::checkValidUserDocument(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
    - [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)

### src/mongo/db/auth/user\_management\_commands\_parser.cpp

<div></div>

    mongo::auth::parseCreateOrUpdateUserCommands(mongo::BSONObj const&, mongo::StringData const&, std::string const&, mongo::auth::CreateOrUpdateUserArgs*)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::auth::parseAndValidateDropUserCommand(mongo::BSONObj const&, std::string const&, mongo::UserName*, mongo::BSONObj*)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::auth::parseDropRoleCommand(mongo::BSONObj const&, std::string const&, mongo::RoleName*, mongo::BSONObj*)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::auth::parseRoleNamesFromBSONArray(mongo::BSONArray const&, mongo::StringData const&, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> >*)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::auth::parseDropAllRolesFromDatabaseCommand(mongo::BSONObj const&, std::string const&, mongo::BSONObj*)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::auth::parseRolesInfoCommand(mongo::BSONObj const&, mongo::StringData const&, mongo::auth::RolesInfoArgs*)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::auth::parseUsersInfoCommand(mongo::BSONObj const&, mongo::StringData const&, mongo::auth::UsersInfoArgs*)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::auth::parseAuthSchemaUpgradeStepCommand(mongo::BSONObj const&, std::string const&, mongo::BSONObj*)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::auth::parseUserNamesFromBSONArray(mongo::BSONArray const&, mongo::StringData const&, std::vector<mongo::UserName, std::allocator<mongo::UserName> >*)

- Used By:

    - src/mongo/db/modules/subscription/src/audit/impersonate\_helpers\_d.cpp

<div></div>

    mongo::auth::parseAndValidateDropAllUsersFromDatabaseCommand(mongo::BSONObj const&, std::string const&, mongo::BSONObj*)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::auth::parseRolePossessionManipulationCommands(mongo::BSONObj const&, mongo::StringData const&, std::string const&, std::string*, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> >*, mongo::BSONObj*)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::auth::parseAndValidateRolePrivilegeManipulationCommands(mongo::BSONObj const&, mongo::StringData const&, std::string const&, mongo::RoleName*, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> >*, mongo::BSONObj*)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::auth::parseCreateOrUpdateRoleCommands(mongo::BSONObj const&, mongo::StringData const&, std::string const&, mongo::auth::CreateOrUpdateRoleArgs*)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::auth::parseAndValidatePrivilegeArray(mongo::BSONArray const&, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> >*)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

### src/mongo/db/auth/user\_name.cpp

<div></div>

    mongo::UserName::UserName(mongo::StringData const&, mongo::StringData const&)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - src/mongo/db/modules/subscription/src/sasl/auxprop\_mongodb\_internal.cpp
    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
    - src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::operator<<(std::ostream&, mongo::UserName const&)

- Used By:

    - src/mongo/db/modules/subscription/src/audit/audit\_user\_management.cpp
    - src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp
