
# Interface for General Mongod Commands
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/dbcommands.cpp

<div></div>

    mongo::Command::execCommand(mongo::Command*, mongo::Client&, int, char const*, mongo::BSONObj&, mongo::BSONObjBuilder&, bool)

- Used By:

    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)

<div></div>

    mongo::_runCommands(char const*, mongo::BSONObj&, mongo::_BufBuilder<mongo::TrivialAllocator>&, mongo::BSONObjBuilder&, bool, int)

- Used By:

    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)
