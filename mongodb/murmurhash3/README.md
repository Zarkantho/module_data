# murmurhash3

# Module Groups

-------------

# Group Description
Third Party - Non cryptographic hashing library

# Files
- src/third\_party/murmurhash3/MurmurHash3.cpp   (mongod, tools, mongos)
- src/third\_party/murmurhash3/MurmurHash3.h

# Interface

### src/third\_party/murmurhash3/MurmurHash3.cpp

<div></div>

    MurmurHash3_x86_32(void const*, int, unsigned int, void*)

- Used By:

    - [src/mongo/base/string\_data.cpp](../base\_utilites)
    - [src/mongo/db/pipeline/document.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/value.cpp](../aggregation\_framework)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/base/string\_data.cpp](../base\_utilites)

# Dependencies
(no dependencies outside this module)
