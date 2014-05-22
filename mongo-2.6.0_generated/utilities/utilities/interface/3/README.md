
# Interface for Operation Tracker
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/background.cpp

<div></div>

    mongo::BackgroundOperation::assertNoBgOpInProgForDb(mongo::StringData const&)

- Used By:

    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repair\_database.cpp](../../../../storage/repair\_database)
    - [src/mongo/db/pdfile.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::BackgroundOperation::BackgroundOperation(mongo::StringData const&)

- Used By:

    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::BackgroundOperation::assertNoBgOpInProgForNs(mongo::StringData const&)

- Used By:

    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/compact.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::BackgroundOperation::dump(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&)

- Used By:

    - [src/mongo/db/restapi.cpp](../../../../network/web\_server)

<div></div>

    mongo::BackgroundOperation::inProgForDb(mongo::StringData const&)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/database\_holder.cpp](../../../../storage/storage\_layer\_structure)
