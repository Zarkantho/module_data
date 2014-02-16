
# Interface

### src/third\_party/snappy/snappy.cc

<div></div>

    snappy::MaxCompressedLength(unsigned long)

- Used By:

    - [src/mongo/util/compress.cpp](../utilities)

<div></div>

    snappy::Compress(char const*, unsigned long, std::string*)

- Used By:

    - [src/mongo/util/compress.cpp](../utilities)
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
    - [src/mongo/db/extsort.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)

<div></div>

    snappy::RawCompress(char const*, unsigned long, char*, unsigned long*)

- Used By:

    - [src/mongo/util/compress.cpp](../utilities)

<div></div>

    snappy::GetUncompressedLength(char const*, unsigned long, unsigned long*)

- Used By:

    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
    - [src/mongo/db/extsort.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)

<div></div>

    snappy::Uncompress(char const*, unsigned long, std::string*)

- Used By:

    - [src/mongo/util/compress.cpp](../utilities)

<div></div>

    snappy::RawUncompress(char const*, unsigned long, char*)

- Used By:

    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
    - [src/mongo/db/extsort.cpp](../aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)
