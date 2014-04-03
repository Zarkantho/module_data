
# Interface for Extent Manager
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/storage/extent\_manager.cpp

<div></div>

    mongo::ExtentManager::getExtent(mongo::DiskLoc const&, bool) const

- Used By:

    - [src/mongo/db/commands/storage\_details.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../../queries/database\_commands)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)
    - [src/mongo/db/commands/touch.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ExtentManager::flushFiles(bool)

- Used By:

    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../../replication/replication)

<div></div>

    mongo::ExtentManager::quantizeExtentSize(int)

- Used By:

    - [src/mongo/dbtests/pdfiletests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::ExtentManager::getFile(int, int, bool)

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ExtentManager::getNextExtent(mongo::Extent*) const

- Used By:

    - [src/mongo/db/commands/storage\_details.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/touch.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ExtentManager::fileSize() const

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ExtentManager::getNextRecordInExtent(mongo::DiskLoc const&) const

- Used By:

    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/storage\_details.cpp](../../../../queries/database\_commands)
