
# Interface for Namespace Index
This interface information represents symbols thatare defined in this group but used in other modules.  Does not includesymbols defined in this group that are used inside this module.

### src/mongo/db/structure/catalog/namespace\_index.cpp

<div></div>

    mongo::NamespaceIndex::getNamespaces(std::list<std::string, std::allocator<std::string> >&, bool) const

- Used By:

    - [src/mongo/db/commands/dbhash.cpp](../../../queries/database\_commands)
    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/tools/admin.cpp](../../../tools/tools)
    - [src/mongo/db/dbcommands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/index\_rebuilder.cpp](../../../queries/indexing)
    - [src/mongo/tools/dump.cpp](../../../tools/tools)

<div></div>

    mongo::NamespaceIndex::details(mongo::StringData const&)

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/exec/oplogstart.cpp](../../../queries/core\_query\_system)
    - [src/mongo/dbtests/namespacetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/pdfiletests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/test\_commands.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/replsettests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/touch.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/clienttests.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::NamespaceIndex::_init()

- Used By:

    - [src/mongo/db/db.cpp](../../../process\_management/mongos\_and\_mongod\_mains)
