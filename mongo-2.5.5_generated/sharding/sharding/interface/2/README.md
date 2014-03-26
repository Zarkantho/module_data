
# Interface for Range Deleter
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/range\_deleter.cpp

<div></div>

    mongo::RangeDeleter::deleteNow(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&, bool, std::string*)

- Used By:

    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::RangeDeleter::startWorkers()

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

### src/mongo/db/range\_deleter\_service.cpp

<div></div>

    mongo::getDeleter()

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../../queries/database\_commands)
