
# Interface for Background Index Build
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/index\_builder.cpp

<div></div>

    mongo::IndexBuilder::IndexBuilder(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::IndexBuilder::restoreIndexes(std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const&)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/compact.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/test\_commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::IndexBuilder::killMatchingIndexBuilds(mongo::Collection*, mongo::IndexCatalog::IndexKillCriteria const&)

- Used By:

    - [src/mongo/db/commands/rename\_collection.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/compact.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/test\_commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::IndexBuilder::~IndexBuilder()

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::IndexBuilder::build(mongo::Client::Context&) const

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)
