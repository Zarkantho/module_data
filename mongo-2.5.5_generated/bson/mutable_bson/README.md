# Mutable BSON
Mutable BSON is built on top of the BSON library, and provides an interface for logically a BSON object.  It lazily unpacks a BSON object into a vector of elements as changes are made, and can reserialize into a new BSON object with all the changes.


-------------

## Uncategorized Mutable BSON code
TODO: organize this into real sections

#### Files
- src/mongo/bson/mutable/algorithm.h   (mongod, tools, mongos)
- src/mongo/bson/mutable/const\_element-inl.h   (mongod, tools, mongos)
- src/mongo/bson/mutable/const\_element.h   (mongod, tools, mongos)
- src/mongo/bson/mutable/damage\_vector.h   (mongod, tools, mongos)
- src/mongo/bson/mutable/document-inl.h   (mongod, tools, mongos)
- src/mongo/bson/mutable/document.cpp   (mongod, tools, mongos)
- src/mongo/bson/mutable/document.h   (mongod, tools, mongos)
- src/mongo/bson/mutable/element-inl.h   (mongod, tools, mongos)
- src/mongo/bson/mutable/element.cpp   (mongod, tools, mongos)
- src/mongo/bson/mutable/element.h   (mongod, tools, mongos)
- src/mongo/bson/mutable/mutable\_bson\_algo\_test.cpp   ()
- src/mongo/bson/mutable/mutable\_bson\_test.cpp   ()
- src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp   ()
- src/mongo/bson/mutable/mutable\_bson\_test\_utils.h   ()

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)
