# Mutable BSON
Mutable BSON is built on top of the BSON library, and provides an interface for logically a BSON object.  It lazily unpacks a BSON object into a vector of elements as changes are made, and can reserialize into a new BSON object with all the changes.


-------------

## In Place Modification Tracker
What's the damage?  Class to record what has changed for an in place update for the purpose of notifying the journal what has changed.  This is an artifact of how the journaling system works, not a core part of the mutable BSON library.

#### Files
- src/mongo/bson/mutable/damage\_vector.h   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Mutable BSON Document
Representation of a mutable BSON object.  Can be constructed from a BSON object and reserialzed into a BSON object.  When constructed from an existing BSON object, it can lazily unpack the object into the mutable representation lazily as modifications are made to the object.

#### Files
- src/mongo/bson/mutable/document-inl.h   (mongod, tools, mongos)
- src/mongo/bson/mutable/document.cpp   (mongod, tools, mongos)
- src/mongo/bson/mutable/document.h   (mongod, tools, mongos)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Mutable BSON Element
Representation of an element in a mutable BSON object.  These are effectively nodes in a DOM structured heirarchy.  Much like a BSONElement in the core BSON implementation, the memory backing these elements is owned by the parent document.

#### Files
- src/mongo/bson/mutable/const\_element-inl.h   (mongod, tools, mongos)
- src/mongo/bson/mutable/const\_element.h   (mongod, tools, mongos)
- src/mongo/bson/mutable/element-inl.h   (mongod, tools, mongos)
- src/mongo/bson/mutable/element.cpp   (mongod, tools, mongos)
- src/mongo/bson/mutable/element.h   (mongod, tools, mongos)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Mutable BSON Utilities
Useful utilities and algorithms for use with the mutable BSON library

#### Files
- src/mongo/bson/mutable/algorithm.h   (mongod, tools, mongos)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Mutable BSON Tests
Unit tests for the mutable BSON library

#### Files
- src/mongo/bson/mutable/mutable\_bson\_algo\_test.cpp   ()
- src/mongo/bson/mutable/mutable\_bson\_test.cpp   ()
- src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp   ()
- src/mongo/bson/mutable/mutable\_bson\_test\_utils.h   ()

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)
