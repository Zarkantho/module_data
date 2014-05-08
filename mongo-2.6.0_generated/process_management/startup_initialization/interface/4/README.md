
# Interface for Command Line Censorship
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/util/cmdline\_utils/censor\_cmdline.cpp

<div></div>

    mongo::cmdline_utils::censorArgsVector(std::vector<std::string, std::allocator<std::string> >*)

- Used By:

    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::cmdline_utils::censorBSONObj(mongo::BSONObj*)

- Used By:

    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::cmdline_utils::censorArgvArray(int, char**)

- Used By:

    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
