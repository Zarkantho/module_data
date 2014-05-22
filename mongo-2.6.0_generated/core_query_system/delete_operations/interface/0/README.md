
# Interface for Legacy Delete Function
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/ops/delete.cpp

<div></div>

    mongo::deleteObjects(mongo::StringData const&, mongo::BSONObj, bool, bool, bool)

- Used By:

    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
