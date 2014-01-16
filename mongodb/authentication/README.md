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

# Dependencies

### src/mongo/db/auth/action\_set.cpp

<div></div>

    mongo::ActionType::operator==(mongo::ActionType const&) const

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::splitStringDelim(std::string const&, std::vector<std::string, std::allocator<std::string> >*, char)

- Provided By:

    - [src/mongo/util/stringutils.cpp](../utilities)

<div></div>

    mongo::ActionType::parseActionFromString(std::string const&, mongo::ActionType*)

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::actionToString(mongo::ActionType const&)

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::toString() const

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::anyAction

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::operator!=(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/db/auth/action\_set\_test.cpp

<div></div>

    mongo::ActionType::find

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::operator<<(std::ostream&, mongo::Status const&)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::ActionType::update

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::ActionType::insert

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::operator<<(std::ostream&, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::ActionType::anyAction

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Status::operator==(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::ActionType::remove

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

### src/mongo/db/auth/auth\_index\_d.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::Helpers::ensureIndex(char const*, mongo::BSONObj, bool, char const*)

- Provided By:

    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/db/auth/auth\_server\_parameters.cpp

<div></div>

    typeinfo for mongo::ServerParameter

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::ServerParameter::~ServerParameter()

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::ServerParameter::ServerParameter(mongo::ServerParameterSet*, std::string const&, bool, bool)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::ServerParameterSet::getGlobal()

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

<div></div>

    mongo::ExportedServerParameter<bool>::setFromString(std::string const&)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

### src/mongo/db/auth/authorization\_manager.cpp

<div></div>

    mongo::ActionType::update

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::mutablebson::Element::pushBack(mongo::mutablebson::Element)

- Provided By:

    - [src/mongo/bson/mutable/element.cpp](../bson)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::ActionType::insert

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Status::operator!=(mongo::ErrorCodes::Error) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::bsonExtractStringFieldWithDefault(mongo::BSONObj const&, mongo::StringData const&, mongo::StringData const&, std::string*)

- Provided By:

    - [src/mongo/bson/util/bson\_extract.cpp](../bson)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::mutablebson::Document::makeElementObject(mongo::StringData const&)

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::mutablebson::Element::appendString(mongo::StringData const&, mongo::StringData const&)

- Provided By:

    - [src/mongo/bson/mutable/element.cpp](../bson)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::operator==(mongo::ErrorCodes::Error) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::ActionType::remove

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::mutablebson::Element::appendObject(mongo::StringData const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/bson/mutable/element.cpp](../bson)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::ActionType::createIndex

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::ActionType::find

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::ActionType::dropIndex

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    boost::this_thread::interruption_point()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::mutablebson::Document::makeElementArray(mongo::StringData const&)

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::operator<<(std::ostream&, mongo::StringData const&)

- Provided By:

    - [src/mongo/base/string\_data.cpp](../base\_utilites)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    boost::detail::get_current_thread_data()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

### src/mongo/db/auth/authorization\_manager\_global.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::ServerParameter::~ServerParameter()

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::ServerParameter::ServerParameter(mongo::ServerParameterSet*, std::string const&, bool, bool)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    typeinfo for mongo::ServerParameter

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ServerParameterSet::getGlobal()

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

### src/mongo/db/auth/authorization\_manager\_test.cpp

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::mutablebson::Document::reset()

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::ActionType::insert

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::mutablebson::Document::~Document()

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::mutablebson::Element::writeTo(mongo::BSONObjBuilder*) const

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::BSONElement::Array() const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::operator!=(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::operator<<(std::ostream&, mongo::Status const&)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::Status::operator==(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::ActionType::find

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::mutablebson::Document::Document()

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

### src/mongo/db/auth/authorization\_session.cpp

<div></div>

    mongo::ActionType::update

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ActionType::insert

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::revokeRole

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Status::operator!=(mongo::ErrorCodes::Error) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::ActionType::changeOwnCustomData

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ActionType::remove

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::ActionType::createIndex

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::ActionType::find

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::ActionType::changeOwnPassword

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::grantRole

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/db/auth/authorization\_session\_test.cpp

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::ActionType::insert

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::operator<<(std::ostream&, mongo::ErrorCodes::Error)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::operator==(mongo::ErrorCodes::Error) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::operator<<(std::ostream&, mongo::Status const&)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::ActionType::collMod

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Status::operator==(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::ActionType::find

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::ActionType::dbStats

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::ActionType::shutdown

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

### src/mongo/db/auth/authz\_documents\_update\_guard.cpp

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/db/auth/authz\_manager\_external\_state.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp

<div></div>

    mongo::Client::ReadContext::ReadContext(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::DBClientBase::update(std::string const&, mongo::Query, mongo::BSONObj, bool, bool)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBClientWithCommands

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Lock::GlobalRead::GlobalRead(int)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::DBClientBase::ConnectionIdSequence

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBDirectClient

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::DBException::convertExceptionCode(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::DBClientWithCommands::dropIndexes(std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    vtable for mongo::DBClientBase

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::operator==(mongo::ErrorCodes::Error) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::DBClientWithCommands::runCommand(std::string const&, mongo::BSONObj const&, mongo::BSONObj&, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Lock::GlobalRead::~GlobalRead()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::DBClientBase::remove(std::string const&, mongo::Query, bool)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::DBClientBase::query(boost::function<void (mongo::BSONObj const&)>, std::string const&, mongo::Query, mongo::BSONObj const*, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientBase::insert(std::string const&, mongo::BSONObj, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Helpers::findOne(mongo::StringData const&, mongo::BSONObj const&, mongo::BSONObj&, bool)

- Provided By:

    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::DBClientWithCommands::ensureIndex(std::string const&, mongo::BSONObj, bool, std::string const&, bool, bool, int, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientWithCommands::getLastErrorString(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::getDatabaseNames(std::vector<std::string, std::allocator<std::string> >&, std::string const&)

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::operator<<(std::ostream&, mongo::StringData const&)

- Provided By:

    - [src/mongo/base/string\_data.cpp](../base\_utilites)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp

<div></div>

    mongo::mutablebson::Element::pushBack(mongo::mutablebson::Element)

- Provided By:

    - [src/mongo/bson/mutable/element.cpp](../bson)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::mutablebson::Element::hasChildren() const

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::mutablebson::Element::appendBool(mongo::StringData const&, bool)

- Provided By:

    - [src/mongo/bson/mutable/element.cpp](../bson)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::mutablebson::Document::~Document()

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::bsonExtractTypedField(mongo::BSONObj const&, mongo::StringData const&, mongo::BSONType, mongo::BSONElement*)

- Provided By:

    - [src/mongo/bson/util/bson\_extract.cpp](../bson)

<div></div>

    mongo::mutablebson::Document::makeElementObject(mongo::StringData const&)

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::mutablebson::Element::appendString(mongo::StringData const&, mongo::StringData const&)

- Provided By:

    - [src/mongo/bson/mutable/element.cpp](../bson)

<div></div>

    mongo::mutablebson::Element::writeTo(mongo::BSONObjBuilder*) const

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::operator==(mongo::ErrorCodes::Error) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::mutablebson::Element::appendObject(mongo::StringData const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/bson/mutable/element.cpp](../bson)

<div></div>

    mongo::mutablebson::Document::Document(mongo::BSONObj const&, mongo::mutablebson::Document::InPlaceMode)

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::fassertFailedWithStatus(int, mongo::Status const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::mutablebson::Document::makeElementArray(mongo::StringData const&)

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::mutablebson::Document::Document()

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::mutablebson::Element::appendElement(mongo::BSONElement const&)

- Provided By:

    - [src/mongo/bson/mutable/element.cpp](../bson)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBException::convertExceptionCode(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::mutablebson::Document::~Document()

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::mutablebson::Element::writeTo(mongo::BSONObjBuilder*) const

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::UpdateDriver::makeOplogEntryQuery(mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::operator==(mongo::ErrorCodes::Error) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::UpdateDriver::update(mongo::StringData const&, mongo::mutablebson::Document*, mongo::BSONObj*, mongo::FieldRefSet*)

- Provided By:

    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)

<div></div>

    mongo::MatchExpressionParser::_parse(mongo::BSONObj const&, bool)

- Provided By:

    - [src/mongo/db/matcher/expression\_parser.cpp](../query\_system)

<div></div>

    mongo::mutablebson::Document::reset(mongo::BSONObj const&, mongo::mutablebson::Document::InPlaceMode)

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::UpdateDriver::UpdateDriver(mongo::UpdateDriver::Options const&)

- Provided By:

    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::UpdateDriver::parse(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)

<div></div>

    mongo::UpdateDriver::populateDocumentWithQueryFields(mongo::BSONObj const&, mongo::mutablebson::Document&) const

- Provided By:

    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Document::Document()

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::UpdateDriver::~UpdateDriver()

- Provided By:

    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)

<div></div>

    mongo::OID::init()

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp

<div></div>

    mongo::Grid::getDBConfig(mongo::StringData const&, bool, std::string const&)

- Provided By:

    - [src/mongo/s/grid.cpp](../sharding)

<div></div>

    mongo::DBConnectionPool::get(std::string const&, double)

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    vtable for mongo::ScopedDbConnection

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DatabaseType::~DatabaseType()

- Provided By:

    - [src/mongo/s/type\_database.cpp](../sharding)

<div></div>

    mongo::DatabaseType::DatabaseType()

- Provided By:

    - [src/mongo/s/type\_database.cpp](../sharding)

<div></div>

    mongo::DatabaseType::parseBSON(mongo::BSONObj const&, std::string*)

- Provided By:

    - [src/mongo/s/type\_database.cpp](../sharding)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::DatabaseType::ConfigNS

- Provided By:

    - [src/mongo/s/type\_database.cpp](../sharding)

<div></div>

    mongo::ScopedDbConnection::_setSocketTimeout()

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBException::convertExceptionCode(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::DBConfig::getShard(std::string const&)

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::DatabaseType::isValid(std::string*) const

- Provided By:

    - [src/mongo/s/type\_database.cpp](../sharding)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::grid

- Provided By:

    - [src/mongo/s/grid.cpp](../sharding)

<div></div>

    mongo::BSONElement::Array() const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::configServer

- Provided By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::ScopedDistributedLock::acquire(long long, std::string*)

- Provided By:

    - [src/mongo/client/distlock.cpp](../sharding)

<div></div>

    mongo::ScopedDistributedLock::ScopedDistributedLock(mongo::ConnectionString const&, std::string const&)

- Provided By:

    - [src/mongo/client/distlock.cpp](../sharding)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::ConnectionString::_finishInit()

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ConnectionString::_fillServers(std::string)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientWithCommands::getLastErrorString(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::pool

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::AScopedConnection::_numConnections

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Query::readPref(mongo::ReadPreference, mongo::BSONArray const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

### src/mongo/db/auth/authz\_session\_external\_state\_d.cpp

<div></div>

    mongo::Lock::isLocked()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

### src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::ExportedServerParameter<bool>::setFromString(std::string const&)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::ServerParameter::~ServerParameter()

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::ServerParameterSet::getGlobal()

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::ServerParameter::ServerParameter(mongo::ServerParameterSet*, std::string const&, bool, bool)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::ServerParameter

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::ClientBasic::getCurrent()

- Provided By:

    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)

### src/mongo/db/auth/privilege\_parser.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<std::string> const&, std::string*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<bool> const&, bool*, std::string*)

- Provided By:

    - [src/mongo/db/field\_parser.cpp](../sharding)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/db/auth/privilege\_parser\_test.cpp

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ActionType::insert

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::ActionType::find

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

### src/mongo/db/auth/role\_graph.cpp

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::operator==(mongo::ErrorCodes::Error) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::fassertFailedWithStatus(int, mongo::Status const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/db/auth/role\_graph\_builtin\_roles.cpp

<div></div>

    mongo::ActionType::collStats

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::cleanupOrphaned

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::getShardVersion

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::addShard

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::applicationMessage

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::dropDatabase

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::touch

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::update

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ActionType::insert

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::reIndex

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::logRotate

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::viewRole

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::removeShard

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::indexStats

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::getParameter

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::connPoolSync

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

<div></div>

    mongo::ActionType::invalidateUserCache

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::resync

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::dropRole

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::top

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::repairDatabase

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::splitChunk

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::getLog

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::getCmdLineOpts

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::killCursors

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::cpuProfiler

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::validate

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::createRole

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::inprog

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::listDatabases

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::unlock

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::authSchemaUpgrade

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::remove

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ActionType::renameCollectionSameDB

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::listShards

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::createCollection

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::hostInfo

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::dropCollection

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::createIndex

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::killop

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::storageDetails

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::replSetConfigure

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::netstat

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::fsync

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::moveChunk

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::changeCustomData

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::enableProfiler

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::shardingState

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::connPoolStats

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::serverStatus

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::viewUser

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::changePassword

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::splitVector

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::setParameter

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::dbHash

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::collMod

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::createUser

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::convertToCapped

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::cursorInfo

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::getShardMap

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::clean

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::revokeRole

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::dropUser

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::find

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::dropIndex

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::diagLogging

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::flushRouterConfig

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::replSetStateChange

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::dbStats

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::emptycapped

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::grantRole

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::writeBacksQueued

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::replSetGetStatus

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::ActionType::enableSharding

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::shutdown

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::closeAllDatabases

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::ActionType::compact

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

### src/mongo/db/auth/role\_graph\_test.cpp

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::ActionType::update

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::ActionType::insert

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::ActionType::remove

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Status::operator!=(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::operator<<(std::ostream&, mongo::Status const&)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::Status::operator==(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::ActionType::find

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::ActionType::shutdown

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

### src/mongo/db/auth/role\_graph\_update.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::UpdateDriver::parse(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Document::~Document()

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::bsonExtractTypedField(mongo::BSONObj const&, mongo::StringData const&, mongo::BSONType, mongo::BSONElement*)

- Provided By:

    - [src/mongo/bson/util/bson\_extract.cpp](../bson)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::UpdateDriver::populateDocumentWithQueryFields(mongo::BSONObj const&, mongo::mutablebson::Document&) const

- Provided By:

    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)

<div></div>

    mongo::mutablebson::Element::writeTo(mongo::BSONObjBuilder*) const

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::mutablebson::Document::Document()

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../bson)

<div></div>

    mongo::UpdateDriver::~UpdateDriver()

- Provided By:

    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)

<div></div>

    mongo::UpdateDriver::UpdateDriver(mongo::UpdateDriver::Options const&)

- Provided By:

    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::operator==(mongo::ErrorCodes::Error) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::UpdateDriver::update(mongo::StringData const&, mongo::mutablebson::Document*, mongo::BSONObj*, mongo::FieldRefSet*)

- Provided By:

    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/db/auth/security\_key.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::DBClientWithCommands::createPasswordDigest(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::saslCommandUserFieldName

- Provided By:

    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)

<div></div>

    mongo::saslCommandPasswordFieldName

- Provided By:

    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::saslCommandUserDBFieldName

- Provided By:

    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    mongo::saslCommandMechanismFieldName

- Provided By:

    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)

<div></div>

    mongo::saslCommandDigestPasswordFieldName

- Provided By:

    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientWithCommands::auth(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/db/auth/user\_cache\_invalidator\_job.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::inShutdown()

- Provided By:

    - [src/mongo/unittest/crutch.cpp](../unit\_tests)
    - [src/mongo/client/clientAndShell.cpp](../cpp\_client\_driver)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/client/scoped\_db\_conn\_test.cpp](../cpp\_client\_driver)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::ExportedServerParameter<int>::setFromString(std::string const&)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::BackgroundJob::~BackgroundJob()

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::sleepsecs(int)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Client::initThread(char const*, mongo::AbstractMessagingPort*)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    typeinfo for mongo::BackgroundJob

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::ServerParameter::~ServerParameter()

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::ServerParameterSet::getGlobal()

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::ServerParameter::ServerParameter(mongo::ServerParameterSet*, std::string const&, bool, bool)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    typeinfo for mongo::ServerParameter

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

### src/mongo/db/auth/user\_document\_parser.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/db/auth/user\_document\_parser\_test.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::operator<<(std::ostream&, mongo::Status const&)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::Status::operator==(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::operator!=(mongo::Status const&) const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/db/auth/user\_management\_commands\_parser.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::auth::createPasswordDigest(mongo::StringData const&, mongo::StringData const&)

- Provided By:

    - [src/mongo/client/auth\_helpers.cpp](../utilities)

<div></div>

    mongo::bsonExtractTypedField(mongo::BSONObj const&, mongo::StringData const&, mongo::BSONType, mongo::BSONElement*)

- Provided By:

    - [src/mongo/bson/util/bson\_extract.cpp](../bson)

<div></div>

    mongo::bsonExtractBooleanFieldWithDefault(mongo::BSONObj const&, mongo::StringData const&, bool, bool*)

- Provided By:

    - [src/mongo/bson/util/bson\_extract.cpp](../bson)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::bsonExtractStringField(mongo::BSONObj const&, mongo::StringData const&, std::string*)

- Provided By:

    - [src/mongo/bson/util/bson\_extract.cpp](../bson)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

### src/mongo/db/auth/user\_set\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)
