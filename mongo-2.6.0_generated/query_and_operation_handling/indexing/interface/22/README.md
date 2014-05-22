
# Interface for Index Key Pregeneration
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/catalog/index\_pregen.cpp

<div></div>

    mongo::GeneratorHolder::getInstance()

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/pdfile.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::GeneratorHolder::prepare(mongo::StringData const&, mongo::BSONObj const&, mongo::PregeneratedKeys*)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::GeneratorHolder::droppedDatabase(std::string const&)

- Used By:

    - [src/mongo/db/pdfile.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::GeneratorHolder::reset(mongo::Collection const*)

- Used By:

    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::PregeneratedKeys::get(mongo::IndexCatalogEntry*) const

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::GeneratorHolder::dropped(std::string const&)

- Used By:

    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
