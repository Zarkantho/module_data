# bson

# Module Groups

-------------

# Group Description
BSON library   is this library standalone? (lots of third party stuff might want to make   use of BSON) - what does it depend on?   why is some of this stuff in db/ ?

## Files
- src/mongo/bson/bson-inl.h   (mongod, tools, mongos)
- src/mongo/bson/bson\_builder\_base.h   (mongod, tools, mongos)
- src/mongo/bson/bson\_db.h   (mongod, tools, mongos)
- src/mongo/bson/bson\_field.h   (mongod, tools, mongos)
- src/mongo/bson/bson\_field\_test.cpp   ()
- src/mongo/bson/bson\_obj\_test.cpp   ()
- src/mongo/bson/bson\_validate.cpp   (mongod, tools, mongos)
- src/mongo/bson/bson\_validate.h   (mongod, tools, mongos)
- src/mongo/bson/bson\_validate\_test.cpp   ()
- src/mongo/bson/bsondemo/bsondemo.cpp   ()
- src/mongo/bson/bsonelement.h   (mongod, tools, mongos)
- src/mongo/bson/bsonmisc.h   (mongod, tools, mongos)
- src/mongo/bson/bsonobj.h   (mongod, tools, mongos)
- src/mongo/bson/bsonobjbuilder.h   (mongod, tools, mongos)
- src/mongo/bson/bsonobjbuilder\_test.cpp   ()
- src/mongo/bson/bsonobjiterator.h   (mongod, tools, mongos)
- src/mongo/bson/bsontypes.h   (mongod, tools, mongos)
- src/mongo/bson/inline\_decls.h   (mongod, tools, mongos)
- src/mongo/bson/oid.cpp   (mongod, tools, mongos)
- src/mongo/bson/oid.h   (mongod, tools, mongos)
- src/mongo/bson/optime.cpp   (mongod, tools, mongos)
- src/mongo/bson/optime.h   (mongod, tools, mongos)
- src/mongo/bson/ordering.h   (mongod, tools, mongos)
- src/mongo/bson/util/atomic\_int.h   (mongod, tools, mongos)
- src/mongo/bson/util/bson\_extract.cpp   (mongod, tools, mongos)
- src/mongo/bson/util/bson\_extract.h   (mongod, tools, mongos)
- src/mongo/bson/util/bson\_extract\_test.cpp   ()
- src/mongo/bson/util/builder.h   (mongod, tools, mongos)
- src/mongo/bson/util/builder\_test.cpp   ()
- src/mongo/bson/util/misc.h   (mongod, tools, mongos)
- src/mongo/db/jsobj.cpp   (mongod, tools, mongos)
- src/mongo/db/jsobj.h   (mongod, tools, mongos)
- src/mongo/db/jsobjmanipulator.h   (mongod, tools, mongos)
- src/mongo/db/json.cpp   (mongod, tools, mongos)
- src/mongo/db/json.h   (mongod, tools, mongos)

## [Interface](interface/0)

## [Dependencies](dependencies/0)

-------------

# Group Description
Mutable BSON is built on top of the BSON library. It has a mutable, consistently sized vector of  the changes that have been made to an object.   is this part of libbson? does this depend on bson/* ?

## Files
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

## [Interface](interface/1)

## [Dependencies](dependencies/1)
