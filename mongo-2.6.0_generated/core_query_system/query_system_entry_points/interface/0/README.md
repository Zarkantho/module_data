
# Interface for Find and getMore Entry Point
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/query/new\_find.cpp

<div></div>

    mongo::MaxBytesToReturnToClientAtOnce

- Used By:

    - [src/mongo/db/commands/pipeline\_command.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::newGetMore(char const*, int, long long, mongo::CurOp&, int, bool&, bool*)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::newRunQuery(mongo::Message&, mongo::QueryMessage&, mongo::CurOp&, mongo::Message&)

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
