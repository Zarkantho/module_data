
# Interface for Authorization Manager
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/auth/authorization\_manager.cpp

<div></div>

    mongo::AuthorizationManager::setSupportOldStylePrivilegeDocuments(bool)

- Used By:

    - [src/mongo/db/auth/auth\_server\_parameters.cpp](../../../../security/legacy\_code)

<div></div>

    mongo::internalSecurity

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../../security/authentication)
    - [src/mongo/db/auth/security\_key.cpp](../../../../security/authentication)

<div></div>

    mongo::AuthorizationManager::schemaVersion26Final

- Used By:

    - [src/mongo/tools/restore.cpp](../../../../tools/tools)

<div></div>

    mongo::AuthorizationManager::logOp(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, bool*)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::AuthorizationManager::releaseUser(mongo::User*)

- Used By:

    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/db/commands/authentication\_commands.cpp](../../../../security/authentication)

<div></div>

    mongo::AuthorizationManager::schemaVersionFieldName

- Used By:

    - [src/mongo/tools/restore.cpp](../../../../tools/tools)

<div></div>

    mongo::AuthorizationManager::versionDocumentQuery

- Used By:

    - [src/mongo/tools/restore.cpp](../../../../tools/tools)

<div></div>

    mongo::AuthorizationManager::acquireUser(mongo::UserName const&, mongo::User**)

- Used By:

    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/db/commands/authentication\_commands.cpp](../../../../security/authentication)

<div></div>

    mongo::AuthorizationManager::AuthorizationManager(mongo::AuthzManagerExternalState*)

- Used By:

    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/dbtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)

<div></div>

    mongo::AuthorizationManager::hasAnyPrivilegeDocuments() const

- Used By:

    - [src/mongo/db/restapi.cpp](../../../../network/web\_server)

<div></div>

    mongo::AuthorizationManager::isAuthEnabled() const

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/commands/isself.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/db/repl/oplogreader.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/manager.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::AuthorizationManager::setAuthEnabled(bool)

- Used By:

    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::AuthorizationManager::schemaVersion24

- Used By:

    - [src/mongo/tools/restore.cpp](../../../../tools/tools)

<div></div>

    mongo::AuthorizationManager::defaultTempRolesCollectionNamespace

- Used By:

    - [src/mongo/tools/mongorestore\_options.cpp](../../../../tools/tools)

<div></div>

    mongo::AuthorizationManager::defaultTempUsersCollectionNamespace

- Used By:

    - [src/mongo/tools/mongorestore\_options.cpp](../../../../tools/tools)

<div></div>

    mongo::AuthorizationManager::initialize()

- Used By:

    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::AuthorizationManager::versionCollectionNamespace

- Used By:

    - [src/mongo/tools/restore.cpp](../../../../tools/tools)

<div></div>

    mongo::AuthorizationManager::USER_DB_FIELD_NAME

- Used By:

    - [src/mongo/db/introspect.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/connection\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::AuthorizationManager::USER_NAME_FIELD_NAME

- Used By:

    - [src/mongo/db/introspect.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/connection\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)

### src/mongo/db/auth/authorization\_manager\_global.cpp

<div></div>

    mongo::clearGlobalAuthorizationManager()

- Used By:

    - [src/mongo/tools/restore.cpp](../../../../tools/tools)

<div></div>

    mongo::getGlobalAuthorizationManager()

- Used By:

    - [src/mongo/db/commands/isself.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/manager.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/commands/authentication\_commands.cpp](../../../../security/authentication)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/db/repl/oplogreader.cpp](../../../../replication/data\_sync)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/client\_info.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::setGlobalAuthorizationManager(mongo::AuthorizationManager*)

- Used By:

    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/dbtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)
