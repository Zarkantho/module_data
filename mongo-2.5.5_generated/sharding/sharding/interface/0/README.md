
# Interface

### src/mongo/db/range\_deleter.cpp

<div></div>

    mongo::RangeDeleter::deleteNow(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&, bool, std::string*)

- Used By:

    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)

<div></div>

    mongo::RangeDeleter::startWorkers()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/db/range\_deleter\_service.cpp

<div></div>

    mongo::getDeleter()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)
