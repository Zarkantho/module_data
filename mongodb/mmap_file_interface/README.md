# mmap\_file\_interface

# Module Groups

-------------

# Group Description
Interface to data file. Depends on journaling module. These are the actual data files on disk  "<dbname>. ". Handles file preallocation.

# Files
- src/mongo/db/storage/data\_file.cpp   (mongod, tools)
- src/mongo/db/storage/data\_file.h

# Interface

### src/mongo/db/storage/data\_file.cpp

<div></div>

    mongo::DataFile::openExisting(char const*)

- Used By:

    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)

<div></div>

    mongo::DataFile::open(char const*, int, bool)

- Used By:

    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)

<div></div>

    mongo::DataFile::flush(bool)

- Used By:

    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)

<div></div>

    mongo::DataFile::allocExtentArea(int)

- Used By:

    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)

<div></div>

    mongo::DataFile::maxSize()

- Used By:

    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)
    - [src/mongo/db/storage/extent.cpp](../storage\_layer\_structure)
    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)

<div></div>

    mongo::DataFile::badOfs(int) const

- Used By:

    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
