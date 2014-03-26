# BSON

# Module Groups

-------------

# JSON to BSON parser
Parser that can convert a JSON string into a binary BSON object. This has extra features that are not in a standard JSON parser to make sure we can represent specific BSON types that are not in strict JSON.  See http://docs.mongodb.org/manual/reference/mongodb-extended-json/ for more details. The JSON parser should be able to parse anything on that page.

## Files
- src/mongo/db/json.cpp   (mongod, tools, mongos)
- src/mongo/db/json.h   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

# Uncategorized BSON code
TODO: organize this into real sections

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

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)
