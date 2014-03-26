
# Interface for Database Holder
This interface information represents symbols thatare defined in this group but used in other modules.  Does not includesymbols defined in this group that are used inside this module.

### src/mongo/db/catalog/database\_holder.cpp

<div></div>

    mongo::DatabaseHolder::closeAll(std::string const&, mongo::BSONObjBuilder&, bool)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../queries/database\_commands)

<div></div>

    mongo::DatabaseHolder::getOrCreate(std::string const&, std::string const&, bool&)

- Used By:

    - [src/mongo/db/client.cpp](../../../queries/client\_and\_operation\_tracking)
