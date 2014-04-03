
# Interface for TODO: Name this group
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/index/2d\_access\_method.cpp

<div></div>

    mongo::TwoDAccessMethod::TwoDAccessMethod(mongo::IndexCatalogEntry*)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::TwoDAccessMethod::getKeys(mongo::BSONObj const&, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> >&) const

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)

### src/mongo/db/index/btree\_access\_method.cpp

<div></div>

    mongo::BtreeAccessMethod::BtreeAccessMethod(mongo::IndexCatalogEntry*)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

### src/mongo/db/index/btree\_based\_access\_method.cpp

<div></div>

    mongo::BtreeBasedAccessMethod::getComparison(int, mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/extsorttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)

### src/mongo/db/index/btree\_index\_cursor.cpp

<div></div>

    mongo::BtreeIndexCursor::seek(std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&)

- Used By:

    - [src/mongo/db/exec/index\_scan.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/distinct\_scan.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::BtreeIndexCursor::seek(mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/db/exec/count.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::BtreeIndexCursor::pointsAt(mongo::BtreeIndexCursor const&)

- Used By:

    - [src/mongo/db/exec/count.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::BtreeIndexCursor::skip(mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&)

- Used By:

    - [src/mongo/db/exec/index\_scan.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/distinct\_scan.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::BtreeIndexCursor::aboutToDeleteBucket(mongo::DiskLoc const&)

- Used By:

    - [src/mongo/db/structure/btree/btree.cpp](../../../../storage/storage\_layer\_structure)

### src/mongo/db/index/btree\_key\_generator.cpp

<div></div>

    mongo::BtreeKeyGeneratorV1::BtreeKeyGeneratorV1(std::vector<char const*, std::allocator<char const*> >, std::vector<mongo::BSONElement, std::allocator<mongo::BSONElement> >, bool)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/exec/sort.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::BtreeKeyGenerator::getKeys(mongo::BSONObj const&, std::set<mongo::BSONObj, mongo::BSONObjCmp, std::allocator<mongo::BSONObj> >*) const

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/exec/sort.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)

### src/mongo/db/index/fts\_access\_method.cpp

<div></div>

    typeinfo for mongo::FTSAccessMethod

- Used By:

    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::FTSAccessMethod::FTSAccessMethod(mongo::IndexCatalogEntry*)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

### src/mongo/db/index/hash\_access\_method.cpp

<div></div>

    mongo::HashAccessMethod::HashAccessMethod(mongo::IndexCatalogEntry*)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::HashAccessMethod::makeSingleKey(mongo::BSONElement const&, int, int)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::HashAccessMethod::getKeysImpl(mongo::BSONObj const&, std::string const&, int, int, bool, std::set<mongo::BSONObj, mongo::BSONObjCmp, std::allocator<mongo::BSONObj> >*)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)

### src/mongo/db/index/haystack\_access\_method.cpp

<div></div>

    mongo::HaystackAccessMethod::HaystackAccessMethod(mongo::IndexCatalogEntry*)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::HaystackAccessMethod::searchCommand(mongo::BSONObj const&, double, mongo::BSONObj const&, mongo::BSONObjBuilder*, unsigned int)

- Used By:

    - [src/mongo/db/geo/haystack.cpp](../../../../queries/geo\_queries)

### src/mongo/db/index/s2\_access\_method.cpp

<div></div>

    mongo::S2AccessMethod::S2AccessMethod(mongo::IndexCatalogEntry*)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

### src/mongo/db/index\_builder.cpp

<div></div>

    mongo::IndexBuilder::IndexBuilder(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::IndexBuilder::restoreIndexes(std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const&)

- Used By:

    - [src/mongo/db/commands/compact.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/test\_commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::IndexBuilder::~IndexBuilder()

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::IndexBuilder::killMatchingIndexBuilds(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/commands/compact.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/test\_commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::IndexBuilder::build(mongo::Client::Context&) const

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)

### src/mongo/db/index\_legacy.cpp

<div></div>

    mongo::IndexLegacy::adjustIndexSpecObject(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::IndexLegacy::postBuildHook(mongo::Collection*, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::IndexLegacy::getMissingField(mongo::Collection*, mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)

### src/mongo/db/index\_names.cpp

<div></div>

    mongo::IndexNames::findPluginName(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::IndexNames::GEO_HAYSTACK

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/geo/haystack.cpp](../../../../queries/geo\_queries)

<div></div>

    mongo::IndexNames::GEO_2D

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/commands/geonear.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::IndexNames::GEO_2DSPHERE

- Used By:

    - [src/mongo/db/commands/geonear.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::IndexNames::TEXT

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::IndexNames::HASHED

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

### src/mongo/db/index\_rebuilder.cpp

<div></div>

    mongo::indexRebuilder

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

### src/mongo/db/index\_set.cpp

<div></div>

    mongo::IndexPathSet::clear()

- Used By:

    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::IndexPathSet::addPath(mongo::StringData const&)

- Used By:

    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::IndexPathSet::mightBeIndexed(mongo::StringData const&) const

- Used By:

    - [src/mongo/db/ops/update\_driver.cpp](../../../../queries/update\_system)
