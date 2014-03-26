
# Interface

### src/mongo/db/auth/authorization\_manager.cpp

<div></div>

    mongo::AuthorizationManager::setSupportOldStylePrivilegeDocuments(bool)

- Used By:

    - [src/mongo/db/auth/auth\_server\_parameters.cpp](../../../legacy\_code)

<div></div>

    mongo::internalSecurity

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../authentication)
    - [src/mongo/db/auth/security\_key.cpp](../../../authentication)

<div></div>

    mongo::AuthorizationManager::schemaVersion26Final

- Used By:

    - [src/mongo/tools/restore.cpp](../../../tools)

<div></div>

    mongo::AuthorizationManager::logOp(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, bool*)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../replication)

<div></div>

    mongo::AuthorizationManager::releaseUser(mongo::User*)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../authentication)
    - [src/mongo/db/dbwebserver.cpp](../../../web\_server)

<div></div>

    mongo::AuthorizationManager::schemaVersionFieldName

- Used By:

    - [src/mongo/tools/restore.cpp](../../../tools)

<div></div>

    mongo::AuthorizationManager::acquireUser(mongo::UserName const&, mongo::User**)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../authentication)
    - [src/mongo/db/dbwebserver.cpp](../../../web\_server)

<div></div>

    mongo::AuthorizationManager::AuthorizationManager(mongo::AuthzManagerExternalState*)

- Used By:

    - [src/mongo/s/server.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/tool.cpp](../../../tools)
    - [src/mongo/dbtests/dbtests.cpp](../../../unit\_tests)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)

<div></div>

    mongo::AuthorizationManager::hasAnyPrivilegeDocuments() const

- Used By:

    - [src/mongo/db/restapi.cpp](../../../web\_server)

<div></div>

    mongo::AuthorizationManager::isAuthEnabled() const

- Used By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)
    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)
    - [src/mongo/db/repl/consensus.cpp](../../../replication)
    - [src/mongo/db/commands/isself.cpp](../../../database\_commands)
    - [src/mongo/s/shard.cpp](../../../sharding)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication)
    - [src/mongo/db/repl/oplogreader.cpp](../../../replication)
    - [src/mongo/db/repl/manager.cpp](../../../replication)
    - [src/mongo/db/repl/rs\_config.cpp](../../../replication)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)

<div></div>

    mongo::AuthorizationManager::setAuthEnabled(bool)

- Used By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../startup\_initialization)
    - [src/mongo/db/mongod\_options.cpp](../../../mongos\_and\_mongod\_mains)

<div></div>

    mongo::AuthorizationManager::schemaVersion24

- Used By:

    - [src/mongo/tools/restore.cpp](../../../tools)

<div></div>

    mongo::AuthorizationManager::initialize()

- Used By:

    - [src/mongo/s/server.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../replication)

<div></div>

    mongo::AuthorizationManager::USER_DB_FIELD_NAME

- Used By:

    - [src/mongo/db/introspect.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/connection\_status.cpp](../../../database\_commands)

<div></div>

    mongo::AuthorizationManager::USER_NAME_FIELD_NAME

- Used By:

    - [src/mongo/db/introspect.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/connection\_status.cpp](../../../database\_commands)

### src/mongo/db/auth/authorization\_manager\_global.cpp

<div></div>

    mongo::getGlobalAuthorizationManager()

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../authentication)
    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)
    - [src/mongo/db/repl/consensus.cpp](../../../replication)
    - [src/mongo/db/mongod\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication)
    - [src/mongo/s/server.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication)
    - [src/mongo/s/s\_only.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../replication)
    - [src/mongo/db/repl/manager.cpp](../../../replication)
    - [src/mongo/db/commands/isself.cpp](../../../database\_commands)
    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/oplog.cpp](../../../replication)
    - [src/mongo/db/repl/rs\_config.cpp](../../../replication)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/s/client\_info.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../startup\_initialization)
    - [src/mongo/s/shard.cpp](../../../sharding)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/oplogreader.cpp](../../../replication)

<div></div>

    mongo::setGlobalAuthorizationManager(mongo::AuthorizationManager*)

- Used By:

    - [src/mongo/tools/tool.cpp](../../../tools)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/s/server.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/dbtests.cpp](../../../unit\_tests)
