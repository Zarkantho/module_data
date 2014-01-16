# snappy

# Module Groups

-------------

# Group Description
Third Party - Snappy compression library

# Files
- src/third\_party/shim\_snappy.cpp   (mongod, tools, mongos)
- src/third\_party/snappy/config.h
- src/third\_party/snappy/snappy-internal.h
- src/third\_party/snappy/snappy-sinksource.cc   (mongod, tools, mongos)
- src/third\_party/snappy/snappy-sinksource.h
- src/third\_party/snappy/snappy-stubs-internal.h
- src/third\_party/snappy/snappy-stubs-public.h
- src/third\_party/snappy/snappy.cc   (mongod, tools, mongos)
- src/third\_party/snappy/snappy.h

# Interface

### src/third\_party/snappy/snappy.cc

    snappy::MaxCompressedLength(unsigned long)

- Used By:

    - [src/mongo/util/compress.cpp](../utilities)

    snappy::Compress(char const*, unsigned long, std::string*)

- Used By:

    - [src/mongo/util/compress.cpp](../utilities)
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
    - [src/mongo/db/extsort.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)

    snappy::RawCompress(char const*, unsigned long, char*, unsigned long*)

- Used By:

    - [src/mongo/util/compress.cpp](../utilities)

    snappy::GetUncompressedLength(char const*, unsigned long, unsigned long*)

- Used By:

    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
    - [src/mongo/db/extsort.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)

    snappy::Uncompress(char const*, unsigned long, std::string*)

- Used By:

    - [src/mongo/util/compress.cpp](../utilities)

    snappy::RawUncompress(char const*, unsigned long, char*)

- Used By:

    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
    - [src/mongo/db/extsort.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)
