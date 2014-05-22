
# Interface for Repair Database
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/repair\_database.cpp

<div></div>

    mongo::inDBRepair

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::repairDatabase(std::string, bool, bool)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::_deleteDataFiles(std::string const&)

- Used By:

    - [src/mongo/db/durop.cpp](../../../../storage/journaling)
    - [src/mongo/db/pdfile.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::dbSize(std::string const&)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
