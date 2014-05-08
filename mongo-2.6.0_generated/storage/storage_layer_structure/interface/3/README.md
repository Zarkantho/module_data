
# Interface for Database Holder
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/catalog/database\_holder.cpp

<div></div>

    mongo::DatabaseHolder::closeAll(std::string const&, mongo::BSONObjBuilder&, bool)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::DatabaseHolder::getOrCreate(std::string const&, std::string const&, bool&)

- Used By:

    - [src/mongo/db/repair\_database.cpp](../../../../storage/repair\_database)
    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
