
# Interface

### src/mongo/client/auth\_helpers.cpp

<div></div>

    mongo::auth::createPasswordDigest(mongo::StringData const&, mongo::StringData const&)

- Used By:

    - [src/mongo/client/dbclient.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../../../authorization)

<div></div>

    mongo::auth::getRemoteStoredAuthorizationVersion(mongo::DBClientBase*, int*)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../authorization)
    - [src/mongo/tools/dump.cpp](../../../tools)
    - [src/mongo/tools/restore.cpp](../../../tools)

<div></div>

    mongo::auth::schemaVersionServerParameter

- Used By:

    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../../../authorization)

<div></div>

    mongo::auth::getUpdateToUpgradeUser(mongo::StringData const&, mongo::BSONObj const&, mongo::BSONObj*, mongo::BSONObj*)

- Used By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../../../authorization)
