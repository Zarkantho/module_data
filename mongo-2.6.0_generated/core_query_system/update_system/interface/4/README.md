
# Interface for Update Execution
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/ops/update.cpp

<div></div>

    mongo::update(mongo::UpdateRequest const&, mongo::OpDebug*)

- Used By:

    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::applyUpdateOperators(mongo::BSONObj const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../../../../storage/storage\_layer\_structure)
