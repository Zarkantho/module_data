
# Interface for Write Concern Checks
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/write\_concern.cpp

<div></div>

    mongo::WriteConcernResult::appendTo(mongo::BSONObjBuilder*) const

- Used By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::waitForWriteConcern(mongo::WriteConcernOptions const&, mongo::OpTime const&, mongo::WriteConcernResult*)

- Used By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::validateWriteConcern(mongo::WriteConcernOptions const&)

- Used By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
