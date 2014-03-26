
# Interface for BSON Field Parser
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/field\_parser.cpp

<div></div>

    mongo::FieldParser::extractID(mongo::BSONObj, mongo::BSONField<mongo::BSONObj> const&, mongo::BSONObj*, std::string*)

- Used By:

    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<int> const&, int*, std::string*)

- Used By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::OpTime> const&, mongo::OpTime*, std::string*)

- Used By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::FieldParser::extract(mongo::BSONElement, mongo::BSONField<std::string> const&, std::string*, std::string*)

- Used By:

    - [src/mongo/db/auth/privilege\_parser.cpp](../../../../security/authorization)
    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<std::string> const&, std::string*, std::string*)

- Used By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../../../../network/write\_commands)
    - [src/mongo/db/auth/privilege\_parser.cpp](../../../../security/authorization)
    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/db/query/type\_explain.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::BSONObj> const&, mongo::BSONObj*, std::string*)

- Used By:

    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/db/query/type\_explain.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::FieldParser::extractNumber(mongo::BSONObj, mongo::BSONField<int> const&, int*, std::string*)

- Used By:

    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../../../../network/write\_commands)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<bool> const&, bool*, std::string*)

- Used By:

    - [src/mongo/db/query/type\_explain.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/db/auth/privilege\_parser.cpp](../../../../security/authorization)
    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::FieldParser::extract(mongo::BSONElement, mongo::BSONField<bool> const&, bool*, std::string*)

- Used By:

    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<long long> const&, long long*, std::string*)

- Used By:

    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/db/query/type\_explain.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::FieldParser::extract(mongo::BSONElement, mongo::BSONField<mongo::BSONObj> const&, mongo::BSONObj*, std::string*)

- Used By:

    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../../network/write\_command\_schema)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::OID> const&, mongo::OID*, std::string*)

- Used By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../../network/write\_command\_schema)
    - [src/mongo/db/commands/get\_last\_error.cpp](../../../../queries/database\_commands)
