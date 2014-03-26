
# Interface for Auth Utils
This interface information represents symbols thatare defined in this group but used in other modules.  Does not includesymbols defined in this group that are used inside this module.

### src/mongo/client/auth\_helpers.cpp

<div></div>

    mongo::auth::createPasswordDigest(mongo::StringData const&, mongo::StringData const&)

- Used By:

    - [src/mongo/client/dbclient.cpp](../../../network/cpp\_client\_driver)
    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../../../security/authorization)

<div></div>

    mongo::auth::getRemoteStoredAuthorizationVersion(mongo::DBClientBase*, int*)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../security/authorization)
    - [src/mongo/tools/dump.cpp](../../../tools/tools)
    - [src/mongo/tools/restore.cpp](../../../tools/tools)

<div></div>

    mongo::auth::schemaVersionServerParameter

- Used By:

    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../../../security/authorization)

<div></div>

    mongo::auth::getUpdateToUpgradeUser(mongo::StringData const&, mongo::BSONObj const&, mongo::BSONObj*, mongo::BSONObj*)

- Used By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../../../security/authorization)
