
# Interface for Namespace Index
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/structure/catalog/namespace\_index.cpp

<div></div>

    mongo::NamespaceIndex::getNamespaces(std::list<std::string, std::allocator<std::string> >&, bool) const

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/index\_rebuilder.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)
    - [src/mongo/db/commands/dbhash.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::NamespaceIndex::details(mongo::StringData const&)

- Used By:

    - [src/mongo/db/commands/rename\_collection.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/index\_stats.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/exec/oplogstart.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/pdfiletests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/test\_commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/clienttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/touch.cpp](../../../../query\_and\_operation\_handling/database\_commands)
