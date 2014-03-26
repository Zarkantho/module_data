
# Interface for TODO: Name this group
This interface information represents symbols thatare defined in this group but used in other modules.  Does not includesymbols defined in this group that are used inside this module.

### src/mongo/db/storage/data\_file.cpp

<div></div>

    mongo::DataFile::openExisting(char const*)

- Used By:

    - [src/mongo/db/storage/extent\_manager.cpp](../../../storage/storage\_layer\_structure)

<div></div>

    mongo::DataFile::open(char const*, int, bool)

- Used By:

    - [src/mongo/db/storage/extent\_manager.cpp](../../../storage/storage\_layer\_structure)

<div></div>

    mongo::DataFile::flush(bool)

- Used By:

    - [src/mongo/db/storage/extent\_manager.cpp](../../../storage/storage\_layer\_structure)

<div></div>

    mongo::DataFile::allocExtentArea(int)

- Used By:

    - [src/mongo/db/storage/extent\_manager.cpp](../../../storage/storage\_layer\_structure)

<div></div>

    mongo::DataFile::maxSize()

- Used By:

    - [src/mongo/dbtests/pdfiletests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/storage/extent.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/storage/extent\_manager.cpp](../../../storage/storage\_layer\_structure)

<div></div>

    mongo::DataFile::badOfs(int) const

- Used By:

    - [src/mongo/db/storage/extent\_manager.cpp](../../../storage/storage\_layer\_structure)
