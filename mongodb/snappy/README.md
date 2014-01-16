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

- <pre>snappy::MaxCompressedLength(unsigned long)</pre>
Used By:
    - [src/mongo/util/compress.cpp](../utilities)

- <pre>snappy::Compress(char const*, unsigned long, std::string*)</pre>
Used By:
    - [src/mongo/util/compress.cpp](../utilities)
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
    - [src/mongo/db/extsort.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)

- <pre>snappy::RawCompress(char const*, unsigned long, char*, unsigned long*)</pre>
Used By:
    - [src/mongo/util/compress.cpp](../utilities)

- <pre>snappy::GetUncompressedLength(char const*, unsigned long, unsigned long*)</pre>
Used By:
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
    - [src/mongo/db/extsort.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)

- <pre>snappy::Uncompress(char const*, unsigned long, std::string*)</pre>
Used By:
    - [src/mongo/util/compress.cpp](../utilities)

- <pre>snappy::RawUncompress(char const*, unsigned long, char*)</pre>
Used By:
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
    - [src/mongo/db/extsort.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)
