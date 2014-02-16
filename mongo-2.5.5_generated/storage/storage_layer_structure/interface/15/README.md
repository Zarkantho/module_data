
# Interface

### src/mongo/db/structure/catalog/namespace\_index.cpp

<div></div>

    mongo::NamespaceIndex::getNamespaces(std::list<std::string, std::allocator<std::string> >&, bool) const

- Used By:

    - [src/mongo/db/commands/dbhash.cpp](../../../database\_commands)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/admin.cpp](../../../tools)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/index\_rebuilder.cpp](../../../indexing)
    - [src/mongo/tools/dump.cpp](../../../tools)

<div></div>

    mongo::NamespaceIndex::details(mongo::StringData const&)

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../../../database\_commands)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../unit\_tests)
    - [src/mongo/db/exec/oplogstart.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/namespacetests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../database\_commands)
    - [src/mongo/dbtests/pdfiletests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/test\_commands.cpp](../../../database\_commands)
    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/touch.cpp](../../../database\_commands)
    - [src/mongo/dbtests/clienttests.cpp](../../../unit\_tests)

<div></div>

    mongo::NamespaceIndex::_init()

- Used By:

    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
