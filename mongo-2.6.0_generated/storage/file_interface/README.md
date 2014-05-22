# File Interface
TODO: file\_interface description


-------------

## TODO: Name this group
Abstraction layer for dealing with files. It's basically the read(2), open(2), and write(2)  interface for posix, and something else for Windows. Not used by mmap code, and does not depend  on file allocator library. Use this if you need a file but not a memory mapped file.

#### Files
- [src/mongo/util/file.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/file.cpp)   (mongod, tools, mongos)
- [src/mongo/util/file.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/file.h)   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)
