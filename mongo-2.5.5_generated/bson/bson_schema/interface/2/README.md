
# Interface for BSON Value Extraction
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/bson/util/bson\_extract.cpp

<div></div>

    mongo::bsonExtractBooleanFieldWithDefault(mongo::BSONObj const&, mongo::StringData const&, bool, bool*)

- Used By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../../../../security/authorization)

<div></div>

    mongo::bsonExtractStringFieldWithDefault(mongo::BSONObj const&, mongo::StringData const&, mongo::StringData const&, std::string*)

- Used By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../../../../security/authorization)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)
    - [src/mongo/client/auth\_helpers.cpp](../../../../utilities/utilities)

<div></div>

    mongo::bsonExtractIntegerField(mongo::BSONObj const&, mongo::StringData const&, long long*)

- Used By:

    - [src/mongo/tools/restore.cpp](../../../../tools/tools)

<div></div>

    mongo::bsonExtractTypedField(mongo::BSONObj const&, mongo::StringData const&, mongo::BSONType, mongo::BSONElement*)

- Used By:

    - [src/mongo/db/auth/role\_graph\_update.cpp](../../../../security/authorization)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../../../../security/authorization)
    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../../../../security/authorization)
    - [src/mongo/db/commands/oplog\_note.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::bsonExtractStringField(mongo::BSONObj const&, mongo::StringData const&, std::string*)

- Used By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../../../../security/authorization)

<div></div>

    mongo::bsonExtractIntegerFieldWithDefault(mongo::BSONObj const&, mongo::StringData const&, long long, long long*)

- Used By:

    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../../../../security/authorization)

<div></div>

    mongo::bsonExtractField(mongo::BSONObj const&, mongo::StringData const&, mongo::BSONElement*)

- Used By:

    - [src/mongo/client/sasl\_client\_authenticate.cpp](../../../../network/cpp\_client\_driver)
