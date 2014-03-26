
# Interface for TODO: Name this group
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/client/gridfs.cpp

<div></div>

    mongo::GridFS::findFile(std::string const&) const

- Used By:

    - [src/mongo/tools/files.cpp](../../../../tools/tools)

<div></div>

    mongo::GridFS::getChunkSize() const

- Used By:

    - [src/mongo/dbtests/gridfstest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::GridFS::setChunkSize(unsigned int)

- Used By:

    - [src/mongo/dbtests/gridfstest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::GridFS::storeFile(std::string const&, std::string const&, std::string const&)

- Used By:

    - [src/mongo/tools/files.cpp](../../../../tools/tools)

<div></div>

    mongo::GridFS::list(mongo::BSONObj) const

- Used By:

    - [src/mongo/tools/files.cpp](../../../../tools/tools)

<div></div>

    mongo::GridFile::write(std::string const&) const

- Used By:

    - [src/mongo/tools/files.cpp](../../../../tools/tools)

<div></div>

    mongo::GridFS::~GridFS()

- Used By:

    - [src/mongo/dbtests/gridfstest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/files.cpp](../../../../tools/tools)

<div></div>

    mongo::GridFS::GridFS(mongo::DBClientBase&, std::string const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/gridfstest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/files.cpp](../../../../tools/tools)

<div></div>

    mongo::GridFS::removeFile(std::string const&)

- Used By:

    - [src/mongo/tools/files.cpp](../../../../tools/tools)
