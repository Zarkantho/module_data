# BSON Schema
Utilities and interfaces for converting BSON objects and BSON types to and from C++ objects and C++ types.


-------------

## BSON Field Schema
Classes that represent a schema for a particular field in BSON.  For a field, having schema just means that the field must have a particular type.  The class itself does type validation at compile time and can be used with a BSONObjBuilder.

#### Files
- src/mongo/bson/bson\_field.h   (mongod, tools, mongos)
- src/mongo/bson/bson\_field\_test.cpp   ()

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## BSON Field Parser
Given a field schema description and a BSON object, attempts to parse the field out of the BSON object with the expected type.  It is an error if the field is in the BSON object with the wrong type.

#### Files
- src/mongo/db/field\_parser-inl.h   (mongod, tools, mongos)
- src/mongo/db/field\_parser.cpp   (mongod, tools, mongos)
- src/mongo/db/field\_parser.h   (mongod, tools, mongos)
- src/mongo/db/field\_parser\_test.cpp   ()

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## BSON Value Extraction
Helpers to extract specific typed values out of BSON objects.  This provides the same functionality as the field schema with a slightly different interface.

#### Files
- src/mongo/bson/util/bson\_extract.cpp   (mongod, tools, mongos)
- src/mongo/bson/util/bson\_extract.h   (mongod, tools, mongos)
- src/mongo/bson/util/bson\_extract\_test.cpp   ()

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## BSON Serializable Interface
Interface for a C++ class that is serializable to BSON and deserializable from BSON.  Each C++ object that implements this interface effectively will enforce a "schema" on the BSON objects it is meant to parse and represent.

#### Files
- src/mongo/s/bson\_serializable.h   (mongod, tools, mongos)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)
