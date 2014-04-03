
# Interface for Range Comparison
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/s/range\_arithmetic.cpp

<div></div>

    mongo::rangeContains(mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/collection\_metadata.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::rangeToString(mongo::BSONObj const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/collection\_metadata.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::getRangeMapOverlap(std::map<mongo::BSONObj, mongo::BSONObj, mongo::BSONObjCmp, std::allocator<std::pair<mongo::BSONObj const, mongo::BSONObj> > > const&, mongo::BSONObj const&, mongo::BSONObj const&, std::vector<std::pair<mongo::BSONObj, mongo::BSONObj>, std::allocator<std::pair<mongo::BSONObj, mongo::BSONObj> > >*)

- Used By:

    - [src/mongo/s/collection\_metadata.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::rangeMapContains(std::map<mongo::BSONObj, mongo::BSONObj, mongo::BSONObjCmp, std::allocator<std::pair<mongo::BSONObj const, mongo::BSONObj> > > const&, mongo::BSONObj const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/collection\_metadata.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::rangeMapOverlaps(std::map<mongo::BSONObj, mongo::BSONObj, mongo::BSONObjCmp, std::allocator<std::pair<mongo::BSONObj const, mongo::BSONObj> > > const&, mongo::BSONObj const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/collection\_metadata.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::overlapToString(std::vector<std::pair<mongo::BSONObj, mongo::BSONObj>, std::allocator<std::pair<mongo::BSONObj, mongo::BSONObj> > >)

- Used By:

    - [src/mongo/s/collection\_metadata.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)
