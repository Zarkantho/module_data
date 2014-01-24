# murmurhash3

# Module Groups

-------------

# Group Description
Third Party - Non cryptographic hashing library

# Files
- src/third\_party/murmurhash3/MurmurHash3.cpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/murmurhash3/MurmurHash3.h   (mongod, cppclientdriver, tools, mongos)

# Interface

### src/third\_party/murmurhash3/MurmurHash3.cpp

<div></div>

    MurmurHash3_x86_32(void const*, int, unsigned int, void*)

- Used By:

    - [src/mongo/db/pipeline/document.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/value.cpp](../aggregation\_framework)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)

<div></div>

    MurmurHash3_x64_128(void const*, int, unsigned int, void*)

- Used By:

    - [src/mongo/base/string\_data.cpp](../base\_utilites)
    - [src/mongo/base/string\_data.cpp](../base\_utilites)

# Dependencies
(no dependencies outside this module)
