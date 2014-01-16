# authentication

# Module Groups

-------------

Authapalooza! TODO: actually separate this logically.

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

## Interface


### src/mongo/db/auth/action\_set.cpp

<pre>mongo::ActionSet::addAction(mongo::ActionType const&)</pre>

#### Used By:

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

<pre>mongo::ActionSet::removeAllActions()</pre>

#### Used By:

- [src/mongo/db/commands/copydb\_common.cpp](../database\_commands)
- [src/mongo/db/commands/rename\_collection\_common.cpp](../database\_commands)

### src/mongo/db/auth/auth\_index\_d.cpp

<pre>mongo::authindex::createSystemIndexes(mongo::NamespaceString const&)</pre>

#### Used By:

- [src/mongo/db/database.cpp](../storage\_layer\_structure)

### src/mongo/db/auth/authorization\_manager.cpp

<pre>mongo::AuthorizationManager::updateAuthzDocuments(mongo::NamespaceString const&, mongo::BSONObj const&, mongo::BSONObj const&, bool, bool, mongo::BSONObj const&, int*) const</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::internalSecurity</pre>

#### Used By:

- [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationManager::ROLE_NAME_FIELD_NAME</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/audit/audit\_user\_management.cpp
- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
- src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

<pre>mongo::AuthorizationManager::schemaVersion26Final</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationManager::updateRoleDocument(mongo::RoleName const&, mongo::BSONObj const&, mongo::BSONObj const&) const</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationManager::logOp(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, bool*)</pre>

#### Used By:

- [src/mongo/db/repl/oplog.cpp](../replication)

<pre>mongo::AuthorizationManager::rolesCollectionNamespace</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationManager::invalidateUsersFromDB(std::string const&)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationManager::releaseUser(mongo::User*)</pre>

#### Used By:

- [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
- src/mongo/db/modules/subscription/src/sasl/auxprop\_mongodb\_internal.cpp
- [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationManager::getRoleDescriptionsForDB(std::string, bool, bool, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> >*)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationManager::getBSONForPrivileges(std::vector<mongo::Privilege, std::allocator<mongo::Privilege> > const&, mongo::mutablebson::Element)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationManager::removePrivilegeDocuments(mongo::BSONObj const&, mongo::BSONObj const&, int*) const</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationManager::writeAuthSchemaVersionIfNeeded()</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationManager::queryAuthzDocument(mongo::NamespaceString const&, mongo::BSONObj const&, mongo::BSONObj const&, boost::function<void (mongo::BSONObj const&)> const&)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationManager::getRoleDescription(mongo::RoleName const&, bool, mongo::BSONObj*)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationManager::acquireUser(mongo::UserName const&, mongo::User**)</pre>

#### Used By:

- [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
- src/mongo/db/modules/subscription/src/sasl/auxprop\_mongodb\_internal.cpp
- [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationManager::AuthorizationManager(mongo::AuthzManagerExternalState*)</pre>

#### Used By:

- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/tools/tool.cpp](../tools)
- src/mongo/db/modules/subscription/src/sasl/sasl\_authentication\_session.cpp
- [src/mongo/dbtests/dbtests.cpp](../unit\_tests)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

<pre>mongo::AuthorizationManager::getUserDescription(mongo::UserName const&, mongo::BSONObj*)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationManager::ROLE_SOURCE_FIELD_NAME</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/audit/audit\_user\_management.cpp
- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
- src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

<pre>mongo::AuthorizationManager::removeRoleDocuments(mongo::BSONObj const&, mongo::BSONObj const&, int*) const</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationManager::hasAnyPrivilegeDocuments() const</pre>

#### Used By:

- [src/mongo/db/restapi.cpp](../database\_web\_accesss)

<pre>mongo::AuthorizationManager::isAuthEnabled() const</pre>

#### Used By:

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

<pre>mongo::AuthorizationManager::invalidateUserCache()</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationManager::schemaVersion26Upgrade</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationManager::~AuthorizationManager()</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/sasl/sasl\_authentication\_session.cpp

<pre>mongo::AuthorizationManager::insertRoleDocument(mongo::BSONObj const&, mongo::BSONObj const&) const</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationManager::updatePrivilegeDocument(mongo::UserName const&, mongo::BSONObj const&, mongo::BSONObj const&) const</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationManager::setAuthEnabled(bool)</pre>

#### Used By:

- [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<pre>mongo::AuthorizationManager::invalidateUserByName(mongo::UserName const&)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationManager::upgradeSchemaStep(mongo::BSONObj const&, bool*)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationManager::initialize()</pre>

#### Used By:

- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/repl/rs\_initialsync.cpp](../replication)

<pre>mongo::AuthorizationManager::insertPrivilegeDocument(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&) const</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationManager::USER_DB_FIELD_NAME</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/audit/audit\_authentication.cpp
- src/mongo/db/modules/subscription/src/audit/audit\_event.cpp
- src/mongo/db/modules/subscription/src/audit/audit\_user\_management.cpp
- [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
- [src/mongo/db/commands/connection\_status.cpp](../database\_commands)
- src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

<pre>mongo::AuthorizationManager::usersCollectionNamespace</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationManager::getAuthorizationVersion()</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationManager::USER_NAME_FIELD_NAME</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/audit/audit\_authentication.cpp
- src/mongo/db/modules/subscription/src/audit/audit\_event.cpp
- src/mongo/db/modules/subscription/src/audit/audit\_user\_management.cpp
- [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
- [src/mongo/db/commands/connection\_status.cpp](../database\_commands)
- src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

### src/mongo/db/auth/authorization\_manager\_global.cpp

<pre>mongo::getGlobalAuthorizationManager()</pre>

#### Used By:

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

<pre>mongo::setGlobalAuthorizationManager(mongo::AuthorizationManager*)</pre>

#### Used By:

- [src/mongo/tools/tool.cpp](../tools)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/dbtests/dbtests.cpp](../unit\_tests)

### src/mongo/db/auth/authorization\_session.cpp

<pre>mongo::AuthorizationSession::startRequest()</pre>

#### Used By:

- [src/mongo/s/request.cpp](../sharding)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::AuthorizationSession::grantInternalAuthorization()</pre>

#### Used By:

- [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
- [src/mongo/db/ttl.cpp](../indexing)
- [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
- [src/mongo/db/repl/write\_concern.cpp](../replication)
- [src/mongo/s/writeback\_listener.cpp](../sharding)
- [src/mongo/db/index\_rebuilder.cpp](../indexing)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
- [src/mongo/s/d\_migrate.cpp](../sharding)

<pre>mongo::AuthorizationSession::isAuthenticatedAsUserWithRole(mongo::RoleName const&)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationSession::lookupUser(mongo::UserName const&)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationSession::isAuthorizedForActionsOnResource(mongo::ResourcePattern const&, mongo::ActionSet const&)</pre>

#### Used By:

- [src/mongo/db/commands/copydb\_common.cpp](../database\_commands)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/db/commands/rename\_collection\_common.cpp](../database\_commands)

<pre>mongo::AuthorizationSession::isAuthorizedForPrivileges(std::vector<mongo::Privilege, std::allocator<mongo::Privilege> > const&)</pre>

#### Used By:

- [src/mongo/db/commands.cpp](../database\_commands)
- [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/commands/server\_status.cpp](../database\_commands)

<pre>mongo::AuthorizationSession::getAuthorizationManager()</pre>

#### Used By:

- [src/mongo/db/commands.cpp](../database\_commands)
- [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
- src/mongo/db/modules/subscription/src/sasl/auxprop\_mongodb\_internal.cpp
- [src/mongo/db/restapi.cpp](../database\_web\_accesss)

<pre>mongo::AuthorizationSession::checkAuthorizedToRevokePrivilege(mongo::Privilege const&)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationSession::setImpersonatedUserNames(std::vector<mongo::UserName, std::allocator<mongo::UserName> > const&)</pre>

#### Used By:

- [src/mongo/db/dbcommands.cpp](../database\_commands)

<pre>mongo::AuthorizationSession::AuthorizationSession(mongo::AuthzSessionExternalState*)</pre>

#### Used By:

- [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
- src/mongo/db/modules/subscription/src/sasl/sasl\_authentication\_session.cpp
- [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<pre>mongo::AuthorizationSession::isAuthorizedForPrivilege(mongo::Privilege const&)</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/audit/impersonate\_helpers\_d.cpp

<pre>mongo::AuthorizationSession::getAuthenticatedUserNamesToken()</pre>

#### Used By:

- [src/mongo/db/matcher/expression\_where.cpp](../query\_system)
- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/db/dbeval.cpp](../database\_commands)
- [src/mongo/db/commands/group.cpp](../database\_commands)

<pre>mongo::AuthorizationSession::getImpersonatedUserNames() const</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/audit/audit\_private.cpp

<pre>mongo::AuthorizationSession::isAuthorizedToChangeOwnPasswordAsUser(mongo::UserName const&)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationSession::getAuthenticatedUserNames()</pre>

#### Used By:

- [src/mongo/db/commands/connection\_status.cpp](../database\_commands)
- [src/mongo/db/server\_extra\_log\_context.cpp](../logging\_system)
- src/mongo/db/modules/subscription/src/audit/audit\_private.cpp
- [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
- src/mongo/db/modules/subscription/src/audit/impersonate\_helpers\_s.cpp

<pre>mongo::AuthorizationSession::logoutDatabase(std::string const&)</pre>

#### Used By:

- [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationSession::checkAuthForQuery(mongo::NamespaceString const&, mongo::BSONObj const&)</pre>

#### Used By:

- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::AuthorizationSession::checkAuthForInsert(mongo::NamespaceString const&, mongo::BSONObj const&)</pre>

#### Used By:

- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::AuthorizationSession::checkAuthForGetMore(mongo::NamespaceString const&, long long)</pre>

#### Used By:

- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::AuthorizationSession::isAuthorizedToRevokeRole(mongo::RoleName const&)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationSession::isAuthorizedToGrantRole(mongo::RoleName const&)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationSession::isAuthorizedForActionsOnResource(mongo::ResourcePattern const&, mongo::ActionType)</pre>

#### Used By:

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

<pre>mongo::AuthorizationSession::~AuthorizationSession()</pre>

#### Used By:

- [src/mongo/db/client\_basic.cpp](../client\_and\_operation\_tracking)
- src/mongo/db/modules/subscription/src/sasl/sasl\_authentication\_session.cpp

<pre>mongo::AuthorizationSession::isAuthorizedForActionsOnNamespace(mongo::NamespaceString const&, mongo::ActionSet const&)</pre>

#### Used By:

- [src/mongo/db/commands/copydb\_common.cpp](../database\_commands)

<pre>mongo::AuthorizationSession::checkAuthForDelete(mongo::NamespaceString const&, mongo::BSONObj const&)</pre>

#### Used By:

- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::AuthorizationSession::checkAuthForUpdate(mongo::NamespaceString const&, mongo::BSONObj const&, mongo::BSONObj const&, bool)</pre>

#### Used By:

- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::AuthorizationSession::isImpersonating() const</pre>

#### Used By:

- [src/mongo/db/dbcommands.cpp](../database\_commands)

<pre>mongo::AuthorizationSession::isAuthorizedForActionsOnNamespace(mongo::NamespaceString const&, mongo::ActionType)</pre>

#### Used By:

- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/s/cursors.cpp](../sharding)
- [src/mongo/db/commands/group.cpp](../database\_commands)

<pre>mongo::AuthorizationSession::checkAuthorizedToGrantPrivilege(mongo::Privilege const&)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthorizationSession::addAndAuthorizeUser(mongo::UserName const&)</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
- [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)

<pre>mongo::AuthorizationSession::clearImpersonatedUserNames()</pre>

#### Used By:

- [src/mongo/db/dbcommands.cpp](../database\_commands)

<pre>mongo::AuthorizationSession::isAuthorizedToChangeOwnCustomDataAsUser(mongo::UserName const&)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

### src/mongo/db/auth/authz\_documents\_update\_guard.cpp

<pre>mongo::AuthzDocumentsUpdateGuard::tryLock(mongo::StringData const&)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthzDocumentsUpdateGuard::~AuthzDocumentsUpdateGuard()</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::AuthzDocumentsUpdateGuard::AuthzDocumentsUpdateGuard(mongo::AuthorizationManager*)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

### src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp

<pre>mongo::AuthzManagerExternalStateMongod::AuthzManagerExternalStateMongod()</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp

<pre>mongo::AuthzManagerExternalStateMock::AuthzManagerExternalStateMock()</pre>

#### Used By:

- [src/mongo/tools/tool.cpp](../tools)
- src/mongo/db/modules/subscription/src/sasl/sasl\_authentication\_session.cpp
- [src/mongo/dbtests/dbtests.cpp](../unit\_tests)

### src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp

<pre>mongo::AuthzManagerExternalStateMongos::AuthzManagerExternalStateMongos()</pre>

#### Used By:

- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/db/auth/authz\_session\_external\_state.cpp

<pre>mongo::AuthzSessionExternalState::AuthzSessionExternalState(mongo::AuthorizationManager*)</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/sasl/sasl\_authentication\_session.cpp

<pre>mongo::AuthzSessionExternalState::~AuthzSessionExternalState()</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/sasl/sasl\_authentication\_session.cpp

<pre>typeinfo for mongo::AuthzSessionExternalState</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/sasl/sasl\_authentication\_session.cpp

### src/mongo/db/auth/authz\_session\_external\_state\_d.cpp

<pre>mongo::AuthzSessionExternalStateMongod::AuthzSessionExternalStateMongod(mongo::AuthorizationManager*)</pre>

#### Used By:

- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

### src/mongo/db/auth/authz\_session\_external\_state\_s.cpp

<pre>mongo::AuthzSessionExternalStateMongos::AuthzSessionExternalStateMongos(mongo::AuthorizationManager*)</pre>

#### Used By:

- [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
- [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

### src/mongo/db/auth/mongo\_authentication\_session.cpp

<pre>mongo::MongoAuthenticationSession::MongoAuthenticationSession(unsigned long long)</pre>

#### Used By:

- [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)

### src/mongo/db/auth/privilege.cpp

<pre>mongo::Privilege::addPrivilegeToPrivilegeVector(std::vector<mongo::Privilege, std::allocator<mongo::Privilege> >*, mongo::Privilege const&)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)</pre>

#### Used By:

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

<pre>mongo::Privilege::removeActions(mongo::ActionSet const&)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionType const&)</pre>

#### Used By:

- [src/mongo/s/commands\_public.cpp](../database\_commands)
- [src/mongo/db/commands/mr\_common.cpp](../database\_commands)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)
- [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../new\_wire\_protocol\_write\_commands)
- src/mongo/db/modules/subscription/src/audit/impersonate\_helpers\_d.cpp

### src/mongo/db/auth/privilege\_parser.cpp

<pre>mongo::ParsedPrivilege::toBSON() const</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
- src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

<pre>mongo::ParsedPrivilege::ParsedPrivilege()</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
- src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

<pre>mongo::ParsedPrivilege::toString() const</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

<pre>mongo::ParsedPrivilege::isValid(std::string*) const</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::ParsedPrivilege::~ParsedPrivilege()</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
- src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

<pre>mongo::ParsedPrivilege::privilegeToParsedPrivilege(mongo::Privilege const&, mongo::ParsedPrivilege*, std::string*)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
- src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

### src/mongo/db/auth/resource\_pattern.cpp

<pre>mongo::ResourcePattern::toString() const</pre>

#### Used By:

- [src/mongo/db/commands/mr\_common.cpp](../database\_commands)
- [src/mongo/db/commands/find\_and\_modify\_common.cpp](../database\_commands)
- [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)

### src/mongo/db/auth/role\_graph\_builtin\_roles.cpp

<pre>mongo::RoleGraph::isBuiltinRole(mongo::RoleName const&)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::RoleGraph::generateUniversalPrivileges(std::vector<mongo::Privilege, std::allocator<mongo::Privilege> >*)</pre>

#### Used By:

- [src/mongo/s/commands\_public.cpp](../database\_commands)
- [src/mongo/db/dbeval.cpp](../database\_commands)
- [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)

### src/mongo/db/auth/role\_name.cpp

<pre>mongo::RoleName::RoleName(mongo::StringData const&, mongo::StringData const&)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::operator<<(std::ostream&, mongo::RoleName const&)</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/audit/audit\_user\_management.cpp
- src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

### src/mongo/db/auth/security\_key.cpp

<pre>mongo::isInternalAuthSet()</pre>

#### Used By:

- [src/mongo/db/repl/oplogreader.cpp](../replication)
- [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
- [src/mongo/db/commands/isself.cpp](../database\_commands)

<pre>mongo::authenticateInternalUser(mongo::DBClientWithCommands*)</pre>

#### Used By:

- [src/mongo/db/repl/heartbeat.cpp](../replication)
- [src/mongo/db/repl/consensus.cpp](../replication)
- [src/mongo/db/commands/isself.cpp](../database\_commands)
- [src/mongo/s/shard.cpp](../sharding)
- [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
- [src/mongo/db/repl/oplogreader.cpp](../replication)
- [src/mongo/db/repl/manager.cpp](../replication)
- [src/mongo/db/repl/rs\_config.cpp](../replication)

<pre>mongo::setInternalUserAuthParams(mongo::BSONObj)</pre>

#### Used By:

- [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)

<pre>mongo::setUpSecurityKey(std::string const&)</pre>

#### Used By:

- [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)

### src/mongo/db/auth/user.cpp

<pre>mongo::User::getRoles() const</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::User::getCredentials() const</pre>

#### Used By:

- [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
- [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
- src/mongo/db/modules/subscription/src/sasl/auxprop\_mongodb\_internal.cpp

<pre>mongo::User::getName() const</pre>

#### Used By:

- [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)

### src/mongo/db/auth/user\_cache\_invalidator\_job.cpp

<pre>vtable for mongo::UserCacheInvalidator</pre>

#### Used By:

- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/db/auth/user\_document\_parser.cpp

<pre>mongo::V2UserDocumentParser::checkValidUserDocument(mongo::BSONObj const&) const</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
- [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)

### src/mongo/db/auth/user\_management\_commands\_parser.cpp

<pre>mongo::auth::parseCreateOrUpdateUserCommands(mongo::BSONObj const&, mongo::StringData const&, std::string const&, mongo::auth::CreateOrUpdateUserArgs*)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::auth::parseAndValidateDropUserCommand(mongo::BSONObj const&, std::string const&, mongo::UserName*, mongo::BSONObj*)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::auth::parseDropRoleCommand(mongo::BSONObj const&, std::string const&, mongo::RoleName*, mongo::BSONObj*)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::auth::parseRoleNamesFromBSONArray(mongo::BSONArray const&, mongo::StringData const&, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> >*)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::auth::parseDropAllRolesFromDatabaseCommand(mongo::BSONObj const&, std::string const&, mongo::BSONObj*)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::auth::parseRolesInfoCommand(mongo::BSONObj const&, mongo::StringData const&, mongo::auth::RolesInfoArgs*)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::auth::parseUsersInfoCommand(mongo::BSONObj const&, mongo::StringData const&, mongo::auth::UsersInfoArgs*)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::auth::parseAuthSchemaUpgradeStepCommand(mongo::BSONObj const&, std::string const&, mongo::BSONObj*)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::auth::parseUserNamesFromBSONArray(mongo::BSONArray const&, mongo::StringData const&, std::vector<mongo::UserName, std::allocator<mongo::UserName> >*)</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/audit/impersonate\_helpers\_d.cpp

<pre>mongo::auth::parseAndValidateDropAllUsersFromDatabaseCommand(mongo::BSONObj const&, std::string const&, mongo::BSONObj*)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::auth::parseRolePossessionManipulationCommands(mongo::BSONObj const&, mongo::StringData const&, std::string const&, std::string*, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> >*, mongo::BSONObj*)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::auth::parseAndValidateRolePrivilegeManipulationCommands(mongo::BSONObj const&, mongo::StringData const&, std::string const&, mongo::RoleName*, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> >*, mongo::BSONObj*)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::auth::parseCreateOrUpdateRoleCommands(mongo::BSONObj const&, mongo::StringData const&, std::string const&, mongo::auth::CreateOrUpdateRoleArgs*)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::auth::parseAndValidatePrivilegeArray(mongo::BSONArray const&, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> >*)</pre>

#### Used By:

- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

### src/mongo/db/auth/user\_name.cpp

<pre>mongo::UserName::UserName(mongo::StringData const&, mongo::StringData const&)</pre>

#### Used By:

- [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
- src/mongo/db/modules/subscription/src/sasl/auxprop\_mongodb\_internal.cpp
- [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<pre>mongo::operator<<(std::ostream&, mongo::UserName const&)</pre>

#### Used By:

- src/mongo/db/modules/subscription/src/audit/audit\_user\_management.cpp
- src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp
