# BSON
This is the core class for managing BSON objects.  Mutable BSON and other in memory BSON management methods in the server are all built on this library


-------------

## JSON to BSON parser
Parser that can convert a JSON string into a binary BSON object. This has extra features that are not in a standard JSON parser to make sure we can represent specific BSON types that are not in strict JSON.  See http://docs.mongodb.org/manual/reference/mongodb-extended-json/ for more details. The JSON parser should be able to parse anything on that page.

#### Files
- src/mongo/db/json.cpp   (mongod, tools, mongos)
- src/mongo/db/json.h   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## BSON Validator
Helper to check if a BSON object is valid

#### Files
- src/mongo/bson/bson\_validate.cpp   (mongod, tools, mongos)
- src/mongo/bson/bson\_validate.h   (mongod, tools, mongos)
- src/mongo/bson/bson\_validate\_test.cpp   ()

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Old BSON Example
Old example of how to use BSON that should be updated with the current recommended methods.

#### Files
- src/mongo/bson/bsondemo/bsondemo.cpp   ()

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## BSON Builder
Class to build a BSON object.  Note that the low level BSON object construction is append only since BSON is a packed binary format.

#### Files
- src/mongo/bson/bson\_builder\_base.h   (mongod, tools, mongos)
- src/mongo/bson/bsonobjbuilder.h   (mongod, tools, mongos)
- src/mongo/bson/bsonobjbuilder\_test.cpp   ()

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Raw Builder
Class that provides an append interface to an automatically growing buffer.  Used by the BSON Builder internally.

#### Files
- src/mongo/bson/util/builder.h   (mongod, tools, mongos)
- src/mongo/bson/util/builder\_test.cpp   ()

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## BSON Iterator
Class to iterate a BSON object.

#### Files
- src/mongo/bson/bsonobjiterator.h   (mongod, tools, mongos)

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

## BSON Object
Class wrapper for a BSON object that can optionally handle the memory management of the raw buffer containing the BSON object

#### Files
- src/mongo/bson/bsonobj.h   (mongod, tools, mongos)
- src/mongo/bson/bson\_obj\_test.cpp   ()

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)

-------------

## BSON Element
Representation of a single element in a BSON object.  Note that a BSONElement does not own any memory.  Instead, it represents a pointer into some parent BSONObj.  This means that a BSONElement should never outlive its parent BSONObj.

#### Files
- src/mongo/bson/bsonelement.h   (mongod, tools, mongos)

#### [Interface](interface/7)

#### [Dependencies](dependencies/7)

-------------

## BSON Library Header
Top level header to include to pull in the entire BSON library.

#### Files
- src/mongo/db/jsobj.h   (mongod, tools, mongos)

#### [Interface](interface/8)

#### [Dependencies](dependencies/8)

-------------

## Legacy Key Pattern
Legacy compact representation for a key pattern or a sort specification, such as { a : 1, b : -1 }.

#### Files
- src/mongo/bson/ordering.h   (mongod, tools, mongos)

#### [Interface](interface/9)

#### [Dependencies](dependencies/9)

-------------

## BSON ObjectId
C++ representation of the BSON ObjectId type.

#### Files
- src/mongo/bson/oid.cpp   (mongod, tools, mongos)
- src/mongo/bson/oid.h   (mongod, tools, mongos)

#### [Interface](interface/10)

#### [Dependencies](dependencies/10)

-------------

## BSON Timestamp
C++ representation of the BSON Timestamp type.
Note that the relationship between this class, the BSON Timestamp, the BSON Date and the Date\_t class, which is supposed to be the C++ equivalent of a BSON date, is rather convoluted and incestuous, so be aware that things you change here may affect how dates are handled, and vice versa.

#### Files
- src/mongo/bson/optime.cpp   (mongod, tools, mongos)
- src/mongo/bson/optime.h   (mongod, tools, mongos)

#### [Interface](interface/11)

#### [Dependencies](dependencies/11)

-------------

## BSON Types
List of all the native BSON types used in the BSON code.

#### Files
- src/mongo/bson/bsontypes.h   (mongod, tools, mongos)

#### [Interface](interface/12)

#### [Dependencies](dependencies/12)

-------------

## BSON Element Manipulator
Wrapper around a BSONElement that allows for modification of BSON types that can be altered in place, such as number values.

#### Files
- src/mongo/db/jsobjmanipulator.h   (mongod, tools, mongos)

#### [Interface](interface/13)

#### [Dependencies](dependencies/13)

-------------

## Atomic Integer
Class representing an integer that supports atomic read modify write operations.  Also used outside the BSON library.

#### Files
- src/mongo/bson/util/atomic\_int.h   (mongod, tools, mongos)

#### [Interface](interface/14)

#### [Dependencies](dependencies/14)

-------------

## Miscellaneous BSON Code
BSON code that is not organized in any specific way.  Most of this code is either implementing random parts of the various BSON related classes and should go with those sections, is a general utility that should not be with the BSON code, or is legacy code that should be removed.

#### Files
- src/mongo/bson/bson-inl.h   (mongod, tools, mongos)
- src/mongo/bson/bson\_db.h   (mongod, tools, mongos)
- src/mongo/bson/bsonmisc.h   (mongod, tools, mongos)
- src/mongo/bson/inline\_decls.h   (mongod, tools, mongos)
- src/mongo/bson/util/misc.h   (mongod, tools, mongos)
- src/mongo/db/jsobj.cpp   (mongod, tools, mongos)

#### [Interface](interface/15)

#### [Dependencies](dependencies/15)
