# Data Files
Non journaling related code for dealing with database data files


-------------

## Mmapped File Interface
Portion of the code for interacting with memory mapped files that is not platform specific.

#### Files
- [src/mongo/util/mmap.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/mmap.cpp)   (mongod, tools)
- [src/mongo/util/mmap.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/mmap.h)   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Posix Mmapped File Implementation
Implementation for dealing with memory mapped files in a posix system.

#### Files
- [src/mongo/util/mmap\_posix.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/mmap_posix.cpp)   (mongod, tools)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Windows Mmapped File Implementation
Implementation for dealing with memory mapped files in Windows.

#### Files
- [src/mongo/util/mmap\_win.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/mmap_win.cpp)   ()

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Data File Layout
Class for interacting with a database data file and managing the on disk data file format.

#### Files
- [src/mongo/db/storage/data\_file.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/storage/data_file.cpp)   (mongod, tools)
- [src/mongo/db/storage/data\_file.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/storage/data_file.h)   (mongod, tools, mongos)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)
