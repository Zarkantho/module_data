
# Interface for Journaling Memory Map Management
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/storage/durable\_mapped\_file.cpp

<div></div>

    mongo::DurableMappedFile::create(std::string const&, unsigned long long&, bool)

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mmaptests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/storage/data\_file.cpp](../../../../storage/data\_files)

<div></div>

    mongo::DurableMappedFile::open(std::string const&, bool)

- Used By:

    - [src/mongo/dbtests/mmaptests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/storage/data\_file.cpp](../../../../storage/data\_files)

<div></div>

    mongo::DurableMappedFile::~DurableMappedFile()

- Used By:

    - [src/mongo/db/storage/extent\_manager.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mmaptests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DurableMappedFile::DurableMappedFile()

- Used By:

    - [src/mongo/db/storage/extent\_manager.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/mmaptests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
