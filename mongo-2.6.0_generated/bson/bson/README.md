# BSON
This is the core class for managing BSON objects.  Mutable BSON and other in memory BSON management methods in the server are all built on this library


-------------

## JSON to BSON parser
Parser that can convert a JSON string into a binary BSON object. This has extra features that are not in a standard JSON parser to make sure we can represent specific BSON types that are not in strict JSON.  See http://docs.mongodb.org/manual/reference/mongodb-extended-json/ for more details. The JSON parser should be able to parse anything on that page.

#### Files
- [src/mongo/db/json.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/json.cpp)   (mongod, tools, mongos)
- [src/mongo/db/json.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/json.h)   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## BSON Validator
Helper to check if a BSON object is valid

#### Files
- [src/mongo/bson/bson\_validate.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/bson/bson_validate.cpp)   (mongod, tools, mongos)
- [src/mongo/bson/bson\_validate.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/bson/bson_validate.h)   (mongod, tools, mongos)
- [src/mongo/bson/bson\_validate\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/bson/bson_validate_test.cpp)   ()

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## BSON Builder
Class to build a BSON object.  Note that the low level BSON object construction is append only since BSON is a packed binary format.

#### Files
- [src/mongo/bson/bson\_builder\_base.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/bson/bson_builder_base.h)   (mongod, tools, mongos)
- [src/mongo/bson/bsonobjbuilder.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/bson/bsonobjbuilder.h)   (mongod, tools, mongos)
- [src/mongo/bson/bsonobjbuilder\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/bson/bsonobjbuilder_test.cpp)   ()

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Raw Builder
Class that provides an append interface to an automatically growing buffer.  Used by the BSON Builder internally.

#### Files
- [src/mongo/bson/util/builder.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/bson/util/builder.h)   (mongod, tools, mongos)
- [src/mongo/bson/util/builder\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/bson/util/builder_test.cpp)   ()

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## BSON Iterator
Class to iterate a BSON object.

#### Files
- [src/mongo/bson/bsonobjiterator.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/bson/bsonobjiterator.h)   (mongod, tools, mongos)

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## BSON Object
Class wrapper for a BSON object that can optionally handle the memory management of the raw buffer containing the BSON object

#### Files
- [src/mongo/bson/bsonobj.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/bson/bsonobj.h)   (mongod, tools, mongos)
- [src/mongo/bson/bson\_obj\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/bson/bson_obj_test.cpp)   ()

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

## BSON Element
Representation of a single element in a BSON object.  Note that a BSONElement does not own any memory.  Instead, it represents a pointer into some parent BSONObj.  This means that a BSONElement should never outlive its parent BSONObj.

#### Files
- [src/mongo/bson/bsonelement.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/bson/bsonelement.h)   (mongod, tools, mongos)

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)

-------------

## BSON Library Header
Top level header to include to pull in the entire BSON library.

#### Files
- [src/mongo/db/jsobj.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/jsobj.h)   (mongod, tools, mongos)

#### [Interface](interface/7)

#### [Dependencies](dependencies/7)

-------------

## Legacy Key Pattern
Legacy compact representation for a key pattern or a sort specification, such as { a : 1, b : -1 }.

#### Files
- [src/mongo/bson/ordering.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/bson/ordering.h)   (mongod, tools, mongos)

#### [Interface](interface/8)

#### [Dependencies](dependencies/8)

-------------

## BSON ObjectId
C++ representation of the BSON ObjectId type.

#### Files
- [src/mongo/bson/oid.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/bson/oid.cpp)   (mongod, tools, mongos)
- [src/mongo/bson/oid.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/bson/oid.h)   (mongod, tools, mongos)

#### [Interface](interface/9)

#### [Dependencies](dependencies/9)

-------------

## BSON Timestamp
C++ representation of the BSON Timestamp type.

Note that the relationship between this class, the BSON Timestamp, the BSON Date and the Date\_t class, which is supposed to be the C++ equivalent of a BSON date, is rather convoluted and incestuous, so be aware that things you change here may affect how dates are handled, and vice versa.

#### Files
- [src/mongo/bson/optime.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/bson/optime.cpp)   (mongod, tools, mongos)
- [src/mongo/bson/optime.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/bson/optime.h)   (mongod, tools, mongos)

#### [Interface](interface/10)

#### [Dependencies](dependencies/10)

-------------

## BSON Types
List of all the native BSON types used in the BSON code.

#### Files
- [src/mongo/bson/bsontypes.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/bson/bsontypes.h)   (mongod, tools, mongos)

#### [Interface](interface/11)

#### [Dependencies](dependencies/11)

-------------

## BSON Element Manipulator
Wrapper around a BSONElement that allows for modification of BSON types that can be altered in place, such as number values.

#### Files
- [src/mongo/db/jsobjmanipulator.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/jsobjmanipulator.h)   (mongod, tools)

#### [Interface](interface/12)

#### [Dependencies](dependencies/12)

-------------

## Atomic Integer
Class representing an integer that supports atomic read modify write operations.  Also used outside the BSON library.

#### Files
- [src/mongo/bson/util/atomic\_int.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/bson/util/atomic_int.h)   (mongod, tools, mongos)

#### [Interface](interface/13)

#### [Dependencies](dependencies/13)

-------------

## Miscellaneous BSON Code
BSON code that is not organized in any specific way.  Most of this code is either implementing random parts of the various BSON related classes and should go with those sections, is a general utility that should not be with the BSON code, or is legacy code that should be removed.

#### Files
- [src/mongo/bson/bson-inl.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/bson/bson-inl.h)   (mongod, tools, mongos)
- [src/mongo/bson/bson\_db.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/bson/bson_db.h)   (mongod, tools, mongos)
- [src/mongo/bson/bsonmisc.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/bson/bsonmisc.h)   (mongod, tools, mongos)
- [src/mongo/bson/inline\_decls.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/bson/inline_decls.h)   (mongod, tools, mongos)
- [src/mongo/bson/util/misc.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/bson/util/misc.h)   (mongod, tools, mongos)
- [src/mongo/db/jsobj.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/jsobj.cpp)   (mongod, tools, mongos)

#### [Interface](interface/14)

#### [Dependencies](dependencies/14)
