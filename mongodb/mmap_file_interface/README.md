# mmap\_file\_interface

# Module Groups

-------------

Interface to data file. Depends on journaling module. These are the actual data files on disk  "<dbname>. ". Handles file preallocation.

- src/mongo/db/storage/data\_file.cpp   (mongod, tools)
- src/mongo/db/storage/data\_file.h

## Interface


### src/mongo/db/storage/data\_file.cpp

<pre>mongo::DataFile::openExisting(char const*)</pre>

#### Used By:

- [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)

<pre>mongo::DataFile::open(char const*, int, bool)</pre>

#### Used By:

- [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)

<pre>mongo::DataFile::flush(bool)</pre>

#### Used By:

- [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)

<pre>mongo::DataFile::allocExtentArea(int)</pre>

#### Used By:

- [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)

<pre>mongo::DataFile::maxSize()</pre>

#### Used By:

- [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)
- [src/mongo/db/storage/extent.cpp](../storage\_layer\_structure)
- [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)

<pre>mongo::DataFile::badOfs(int) const</pre>

#### Used By:

- [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
