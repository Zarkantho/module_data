# bson

# Module Groups

-------------

BSON library   is this library standalone? (lots of third party stuff might want to make   use of BSON) - what does it depend on?   why is some of this stuff in db/ ?

- src/mongo/bson/bson-inl.h
- src/mongo/bson/bson\_builder\_base.h
- src/mongo/bson/bson\_db.h
- src/mongo/bson/bson\_field.h
- src/mongo/bson/bson\_field\_test.cpp   ()
- src/mongo/bson/bson\_obj\_test.cpp   ()
- src/mongo/bson/bson\_validate.cpp   (cppclientdriver)
- src/mongo/bson/bson\_validate.h
- src/mongo/bson/bson\_validate\_test.cpp   ()
- src/mongo/bson/bsondemo/bsondemo.cpp   ()
- src/mongo/bson/bsonelement.h
- src/mongo/bson/bsonmisc.h
- src/mongo/bson/bsonobj.h
- src/mongo/bson/bsonobjbuilder.h
- src/mongo/bson/bsonobjbuilder\_test.cpp   ()
- src/mongo/bson/bsonobjiterator.h
- src/mongo/bson/bsontypes.h
- src/mongo/bson/inline\_decls.h
- src/mongo/bson/oid.cpp   (mongod, tools, mongos)
- src/mongo/bson/oid.h
- src/mongo/bson/optime.cpp   (mongod, tools, mongos)
- src/mongo/bson/optime.h
- src/mongo/bson/ordering.h
- src/mongo/bson/util/atomic\_int.h
- src/mongo/bson/util/bson\_extract.cpp   (cppclientdriver)
- src/mongo/bson/util/bson\_extract.h
- src/mongo/bson/util/bson\_extract\_test.cpp   ()
- src/mongo/bson/util/builder.h
- src/mongo/bson/util/builder\_test.cpp   ()
- src/mongo/bson/util/misc.h
- src/mongo/db/jsobj.cpp   (cppclientdriver)
- src/mongo/db/jsobj.h
- src/mongo/db/jsobjmanipulator.h
- src/mongo/db/json.cpp   (mongod, tools, mongos)
- src/mongo/db/json.h

-------------

Mutable BSON is built on top of the BSON library. It has a mutable, consistently sized vector of  the changes that have been made to an object.   is this part of libbson? does this depend on bson/* ?

- src/mongo/bson/mutable/algorithm.h
- src/mongo/bson/mutable/const\_element-inl.h
- src/mongo/bson/mutable/const\_element.h
- src/mongo/bson/mutable/damage\_vector.h
- src/mongo/bson/mutable/document-inl.h
- src/mongo/bson/mutable/document.cpp   (mongod, tools, mongos)
- src/mongo/bson/mutable/document.h
- src/mongo/bson/mutable/element-inl.h
- src/mongo/bson/mutable/element.cpp   (mongod, tools, mongos)
- src/mongo/bson/mutable/element.h
- src/mongo/bson/mutable/mutable\_bson\_algo\_test.cpp   ()
- src/mongo/bson/mutable/mutable\_bson\_test.cpp   ()
- src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp   ()
- src/mongo/bson/mutable/mutable\_bson\_test\_utils.h
