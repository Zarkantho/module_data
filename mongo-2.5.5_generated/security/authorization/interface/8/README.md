
# Interface for Authorization Manager
This interface information represents symbols thatare defined in this group but used in other modules.  Does not includesymbols defined in this group that are used inside this module.

### src/mongo/db/auth/authorization\_manager.cpp

<div></div>

    mongo::AuthorizationManager::setSupportOldStylePrivilegeDocuments(bool)

- Used By:

    - [src/mongo/db/auth/auth\_server\_parameters.cpp](../../../security/legacy\_code)

<div></div>

    mongo::internalSecurity

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../security/authentication)
    - [src/mongo/db/auth/security\_key.cpp](../../../security/authentication)

<div></div>

    mongo::AuthorizationManager::schemaVersion26Final

- Used By:

    - [src/mongo/tools/restore.cpp](../../../tools/tools)

<div></div>

    mongo::AuthorizationManager::logOp(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, bool*)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../replication/replication)

<div></div>

    mongo::AuthorizationManager::releaseUser(mongo::User*)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../security/authentication)
    - [src/mongo/db/dbwebserver.cpp](../../../network/web\_server)

<div></div>

    mongo::AuthorizationManager::schemaVersionFieldName

- Used By:

    - [src/mongo/tools/restore.cpp](../../../tools/tools)

<div></div>

    mongo::AuthorizationManager::acquireUser(mongo::UserName const&, mongo::User**)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../security/authentication)
    - [src/mongo/db/dbwebserver.cpp](../../../network/web\_server)

<div></div>

    mongo::AuthorizationManager::AuthorizationManager(mongo::AuthzManagerExternalState*)

- Used By:

    - [src/mongo/s/server.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/tools/tool.cpp](../../../tools/tools)
    - [src/mongo/dbtests/dbtests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::AuthorizationManager::hasAnyPrivilegeDocuments() const

- Used By:

    - [src/mongo/db/restapi.cpp](../../../network/web\_server)

<div></div>

    mongo::AuthorizationManager::isAuthEnabled() const

- Used By:

    - [src/mongo/db/commands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/repl/heartbeat.cpp](../../../replication/replication)
    - [src/mongo/db/repl/consensus.cpp](../../../replication/replication)
    - [src/mongo/db/commands/isself.cpp](../../../queries/database\_commands)
    - [src/mongo/s/shard.cpp](../../../sharding/sharding)
    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication/replication)
    - [src/mongo/db/repl/oplogreader.cpp](../../../replication/replication)
    - [src/mongo/db/repl/manager.cpp](../../../replication/replication)
    - [src/mongo/db/repl/rs\_config.cpp](../../../replication/replication)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding/sharding)

<div></div>

    mongo::AuthorizationManager::setAuthEnabled(bool)

- Used By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../process\_management/startup\_initialization)
    - [src/mongo/db/mongod\_options.cpp](../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::AuthorizationManager::schemaVersion24

- Used By:

    - [src/mongo/tools/restore.cpp](../../../tools/tools)

<div></div>

    mongo::AuthorizationManager::initialize()

- Used By:

    - [src/mongo/s/server.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication/replication)
    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../replication/replication)

<div></div>

    mongo::AuthorizationManager::USER_DB_FIELD_NAME

- Used By:

    - [src/mongo/db/introspect.cpp](../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/connection\_status.cpp](../../../queries/database\_commands)

<div></div>

    mongo::AuthorizationManager::USER_NAME_FIELD_NAME

- Used By:

    - [src/mongo/db/introspect.cpp](../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/connection\_status.cpp](../../../queries/database\_commands)

### src/mongo/db/auth/authorization\_manager\_global.cpp

<div></div>

    mongo::getGlobalAuthorizationManager()

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../security/authentication)
    - [src/mongo/db/repl/heartbeat.cpp](../../../replication/replication)
    - [src/mongo/db/repl/consensus.cpp](../../../replication/replication)
    - [src/mongo/db/mongod\_options.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication/replication)
    - [src/mongo/s/server.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication/replication)
    - [src/mongo/s/s\_only.cpp](../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../replication/replication)
    - [src/mongo/db/repl/manager.cpp](../../../replication/replication)
    - [src/mongo/db/commands/isself.cpp](../../../queries/database\_commands)
    - [src/mongo/db/client.cpp](../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/repl/oplog.cpp](../../../replication/replication)
    - [src/mongo/db/repl/rs\_config.cpp](../../../replication/replication)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding/sharding)
    - [src/mongo/s/client\_info.cpp](../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../process\_management/startup\_initialization)
    - [src/mongo/s/shard.cpp](../../../sharding/sharding)
    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/oplogreader.cpp](../../../replication/replication)

<div></div>

    mongo::setGlobalAuthorizationManager(mongo::AuthorizationManager*)

- Used By:

    - [src/mongo/tools/tool.cpp](../../../tools/tools)
    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/s/server.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/dbtests.cpp](../../../tests/unit\_tests)
