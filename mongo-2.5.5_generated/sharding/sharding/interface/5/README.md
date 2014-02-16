
# Interface

### src/mongo/db/field\_parser.cpp

<div></div>

    mongo::FieldParser::extractID(mongo::BSONObj, mongo::BSONField<mongo::BSONObj> const&, mongo::BSONObj*, std::string*)

- Used By:

    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../../../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<int> const&, int*, std::string*)

- Used By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::OpTime> const&, mongo::OpTime*, std::string*)

- Used By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../../../database\_commands)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::FieldParser::extract(mongo::BSONElement, mongo::BSONField<std::string> const&, std::string*, std::string*)

- Used By:

    - [src/mongo/db/auth/privilege\_parser.cpp](../../../authentication)
    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<std::string> const&, std::string*, std::string*)

- Used By:

    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../../../database\_commands)
    - [src/mongo/db/auth/privilege\_parser.cpp](../../../authentication)
    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/query/type\_explain.cpp](../../../core\_query\_system)
    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../database\_commands)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../../../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::BSONObj> const&, mongo::BSONObj*, std::string*)

- Used By:

    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/query/type\_explain.cpp](../../../core\_query\_system)
    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../database\_commands)

<div></div>

    mongo::FieldParser::extractNumber(mongo::BSONObj, mongo::BSONField<int> const&, int*, std::string*)

- Used By:

    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../../../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<bool> const&, bool*, std::string*)

- Used By:

    - [src/mongo/db/query/type\_explain.cpp](../../../core\_query\_system)
    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/auth/privilege\_parser.cpp](../../../authentication)
    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../database\_commands)

<div></div>

    mongo::FieldParser::extract(mongo::BSONElement, mongo::BSONField<bool> const&, bool*, std::string*)

- Used By:

    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<long long> const&, long long*, std::string*)

- Used By:

    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/query/type\_explain.cpp](../../../core\_query\_system)

<div></div>

    mongo::FieldParser::extract(mongo::BSONElement, mongo::BSONField<mongo::BSONObj> const&, mongo::BSONObj*, std::string*)

- Used By:

    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../../../database\_commands)

<div></div>

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::OID> const&, mongo::OID*, std::string*)

- Used By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../../../database\_commands)
    - [src/mongo/db/commands/get\_last\_error.cpp](../../../database\_commands)
