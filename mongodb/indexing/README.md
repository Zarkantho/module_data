# indexing

# Module Groups

-------------

Indexes and index management code. TODO: go into more details about this. The code is new.  The two parts of the interface that are nice entry points are the "index\_access\_method.h"  (interface for manipulating and accessing the index itself), and "index\_cursor.h" (interface for  getting data from an index) files.   can you say a bit more about the structure in here, wrt. a hypothetical   member of the 'open source community' who wants to add a new type of   index to mongodb?

- src/mongo/db/index/2d\_access\_method.cpp   (mongod, tools)
- src/mongo/db/index/2d\_access\_method.h
- src/mongo/db/index/2d\_common.h
- src/mongo/db/index/btree\_access\_method.cpp   (mongod, tools)
- src/mongo/db/index/btree\_access\_method.h
- src/mongo/db/index/btree\_access\_method\_internal.h
- src/mongo/db/index/btree\_based\_builder.cpp   (mongod, tools)
- src/mongo/db/index/btree\_based\_builder.h
- src/mongo/db/index/btree\_index\_cursor.cpp   (mongod, tools)
- src/mongo/db/index/btree\_index\_cursor.h
- src/mongo/db/index/btree\_interface.cpp   (mongod, tools)
- src/mongo/db/index/btree\_interface.h
- src/mongo/db/index/btree\_key\_generator.cpp   (mongod, tools, mongos)
- src/mongo/db/index/btree\_key\_generator.h
- src/mongo/db/index/expression\_index.h
- src/mongo/db/index/fts\_access\_method.cpp   (mongod, tools)
- src/mongo/db/index/fts\_access\_method.h
- src/mongo/db/index/hash\_access\_method.cpp   (mongod, tools)
- src/mongo/db/index/hash\_access\_method.h
- src/mongo/db/index/haystack\_access\_method.cpp   (mongod, tools)
- src/mongo/db/index/haystack\_access\_method.h
- src/mongo/db/index/haystack\_access\_method\_internal.h
- src/mongo/db/index/index\_access\_method.h
- src/mongo/db/index/index\_cursor.h
- src/mongo/db/index/index\_descriptor.h
- src/mongo/db/index/s2\_access\_method.cpp   (mongod, tools)
- src/mongo/db/index/s2\_access\_method.h
- src/mongo/db/index\_builder.cpp   (mongod, tools)
- src/mongo/db/index\_builder.h
- src/mongo/db/index\_legacy.cpp   (mongod, tools)
- src/mongo/db/index\_legacy.h
- src/mongo/db/index\_names.cpp   (mongod, tools, mongos)
- src/mongo/db/index\_names.h
- src/mongo/db/index\_rebuilder.cpp   (mongod, tools)
- src/mongo/db/index\_rebuilder.h
- src/mongo/db/index\_set.cpp   (mongod, tools, mongos)
- src/mongo/db/index\_set.h
- src/mongo/db/index\_set\_test.cpp   ()

## Interface
### src/mongo/db/index/2d\_access\_method.cpp
<pre>mongo::TwoDAccessMethod::TwoDAccessMethod(mongo::BtreeInMemoryState*)</pre>
#### Used By:
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<pre>mongo::TwoDAccessMethod::getKeys(mongo::BSONObj const&, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> >&) const</pre>
#### Used By:
- [src/mongo/db/exec/2dcommon.cpp](../query\_system)
### src/mongo/db/index/btree\_access\_method.cpp
<pre>typeinfo for mongo::BtreeBasedAccessMethod</pre>
#### Used By:
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<pre>mongo::BtreeAccessMethod::BtreeAccessMethod(mongo::BtreeInMemoryState*)</pre>
#### Used By:
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
### src/mongo/db/index/btree\_based\_builder.cpp
<pre>mongo::BtreeBasedBuilder::fastBuildIndex(mongo::Collection*, mongo::BtreeInMemoryState*, bool)</pre>
#### Used By:
- [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)

<pre>mongo::BtreeBasedBuilder::doDropDups(mongo::Collection*, std::set<mongo::DiskLoc, std::less<mongo::DiskLoc>, std::allocator<mongo::DiskLoc> > const&, bool)</pre>
#### Used By:
- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

<pre>mongo::BtreeBasedBuilder::getComparison(int, mongo::BSONObj const&)</pre>
#### Used By:
- [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

<pre>mongo::BtreeBasedBuilder::addKeysToPhaseOne(mongo::Collection*, mongo::IndexDescriptor const*, mongo::BSONObj const&, mongo::SortPhaseOne*, mongo::ProgressMeter*, bool)</pre>
#### Used By:
- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

<pre>mongo::BtreeBasedBuilder::makeEmptyIndex(mongo::BtreeInMemoryState*)</pre>
#### Used By:
- [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
### src/mongo/db/index/btree\_index\_cursor.cpp
<pre>mongo::BtreeIndexCursor::seek(std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&)</pre>
#### Used By:
- [src/mongo/db/exec/index\_scan.cpp](../query\_system)

<pre>mongo::BtreeIndexCursor::skip(mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&)</pre>
#### Used By:
- [src/mongo/db/exec/index\_scan.cpp](../query\_system)

<pre>mongo::BtreeIndexCursor::aboutToDeleteBucket(mongo::DiskLoc const&)</pre>
#### Used By:
- [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
### src/mongo/db/index/btree\_key\_generator.cpp
<pre>mongo::BtreeKeyGeneratorV1::BtreeKeyGeneratorV1(std::vector<char const*, std::allocator<char const*> >, std::vector<mongo::BSONElement, std::allocator<mongo::BSONElement> >, bool)</pre>
#### Used By:
- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
- [src/mongo/db/exec/sort.cpp](../query\_system)
- [src/mongo/db/queryutil.cpp](../query\_system)

<pre>mongo::BtreeKeyGenerator::getKeys(mongo::BSONObj const&, std::set<mongo::BSONObj, mongo::BSONObjCmp, std::allocator<mongo::BSONObj> >*) const</pre>
#### Used By:
- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
- [src/mongo/db/exec/sort.cpp](../query\_system)
- [src/mongo/db/queryutil.cpp](../query\_system)
### src/mongo/db/index/fts\_access\_method.cpp
<pre>mongo::FTSAccessMethod::FTSAccessMethod(mongo::BtreeInMemoryState*)</pre>
#### Used By:
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<pre>typeinfo for mongo::FTSAccessMethod</pre>
#### Used By:
- [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
### src/mongo/db/index/hash\_access\_method.cpp
<pre>mongo::HashAccessMethod::makeSingleKey(mongo::BSONElement const&, int, int)</pre>
#### Used By:
- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)

<pre>mongo::HashAccessMethod::HashAccessMethod(mongo::BtreeInMemoryState*)</pre>
#### Used By:
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<pre>mongo::HashAccessMethod::getKeysImpl(mongo::BSONObj const&, std::string const&, int, int, bool, std::set<mongo::BSONObj, mongo::BSONObjCmp, std::allocator<mongo::BSONObj> >*)</pre>
#### Used By:
- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
### src/mongo/db/index/haystack\_access\_method.cpp
<pre>mongo::HaystackAccessMethod::HaystackAccessMethod(mongo::BtreeInMemoryState*)</pre>
#### Used By:
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<pre>mongo::HaystackAccessMethod::searchCommand(mongo::BSONObj const&, double, mongo::BSONObj const&, mongo::BSONObjBuilder*, unsigned int)</pre>
#### Used By:
- [src/mongo/db/geo/haystack.cpp](../geo\_queries)
### src/mongo/db/index/s2\_access\_method.cpp
<pre>mongo::S2AccessMethod::S2AccessMethod(mongo::BtreeInMemoryState*)</pre>
#### Used By:
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
### src/mongo/db/index\_builder.cpp
<pre>mongo::IndexBuilder::IndexBuilder(mongo::BSONObj const&)</pre>
#### Used By:
- [src/mongo/db/repl/oplog.cpp](../replication)

<pre>mongo::IndexBuilder::restoreIndexes(std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const&)</pre>
#### Used By:
- [src/mongo/db/compact.cpp](../database\_commands)
- [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
- [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
- [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)

<pre>mongo::IndexBuilder::~IndexBuilder()</pre>
#### Used By:
- [src/mongo/db/repl/oplog.cpp](../replication)

<pre>mongo::IndexBuilder::killMatchingIndexBuilds(mongo::BSONObj const&)</pre>
#### Used By:
- [src/mongo/db/compact.cpp](../database\_commands)
- [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
- [src/mongo/db/commands/test\_commands.cpp](../database\_commands)

<pre>mongo::IndexBuilder::build(mongo::Client::Context&) const</pre>
#### Used By:
- [src/mongo/db/repl/oplog.cpp](../replication)
### src/mongo/db/index\_legacy.cpp
<pre>mongo::IndexLegacy::adjustIndexSpecObject(mongo::BSONObj const&)</pre>
#### Used By:
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<pre>mongo::IndexLegacy::postBuildHook(mongo::Collection*, mongo::BSONObj const&)</pre>
#### Used By:
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<pre>mongo::IndexLegacy::getMissingField(mongo::Collection*, mongo::BSONObj const&)</pre>
#### Used By:
- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
- [src/mongo/s/d\_split.cpp](../sharding)
### src/mongo/db/index\_names.cpp
<pre>mongo::IndexNames::findPluginName(mongo::BSONObj const&)</pre>
#### Used By:
- [src/mongo/s/commands\_admin.cpp](../database\_commands)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/exec/text.cpp](../query\_system)
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
- [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
- [src/mongo/db/query/stage\_builder.cpp](../query\_system)
- [src/mongo/db/commands/geonear.cpp](../database\_commands)
- [src/mongo/db/geo/haystack.cpp](../geo\_queries)

<pre>mongo::IndexNames::GEO_HAYSTACK</pre>
#### Used By:
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
- [src/mongo/db/geo/haystack.cpp](../geo\_queries)

<pre>mongo::IndexNames::GEO_2D</pre>
#### Used By:
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/exec/index\_scan.cpp](../query\_system)
- [src/mongo/db/queryutil.cpp](../query\_system)
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
- [src/mongo/db/commands/geonear.cpp](../database\_commands)

<pre>mongo::IndexNames::GEO_2DSPHERE</pre>
#### Used By:
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
- [src/mongo/db/commands/geonear.cpp](../database\_commands)
- [src/mongo/db/exec/index\_scan.cpp](../query\_system)
- [src/mongo/db/queryutil.cpp](../query\_system)

<pre>mongo::IndexNames::TEXT</pre>
#### Used By:
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<pre>mongo::IndexNames::HASHED</pre>
#### Used By:
- [src/mongo/s/commands\_admin.cpp](../database\_commands)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
### src/mongo/db/index\_rebuilder.cpp
<pre>mongo::indexRebuilder</pre>
#### Used By:
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
### src/mongo/db/index\_set.cpp
<pre>mongo::IndexPathSet::clear()</pre>
#### Used By:
- [src/mongo/db/structure/collection\_info\_cache.cpp](../storage\_layer\_structure)
- [src/mongo/db/ops/update\_driver.cpp](../update\_system)

<pre>mongo::IndexPathSet::addPath(mongo::StringData const&)</pre>
#### Used By:
- [src/mongo/db/structure/collection\_info\_cache.cpp](../storage\_layer\_structure)

<pre>mongo::IndexPathSet::mightBeIndexed(mongo::StringData const&) const</pre>
#### Used By:
- [src/mongo/db/ops/update\_driver.cpp](../update\_system)

-------------

Class representing an index spec, such as { "a" : 1, "b" : -1 }

- src/mongo/db/keypattern.cpp   (mongod, tools, mongos)
- src/mongo/db/keypattern.h

## Interface
### src/mongo/db/keypattern.cpp
<pre>mongo::KeyPattern::isIdKeyPattern(mongo::BSONObj const&)</pre>
#### Used By:
- [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
- [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<pre>mongo::KeyPattern::KeyPattern(mongo::BSONObj const&)</pre>
#### Used By:
- [src/mongo/s/commands\_admin.cpp](../database\_commands)
- [src/mongo/s/shardkey.cpp](../sharding)
- [src/mongo/dbtests/keypatterntests.cpp](../unit\_tests)
- [src/mongo/db/query/idhack\_runner.cpp](../query\_system)
- [src/mongo/db/exec/shard\_filter.cpp](../query\_system)
- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
- [src/mongo/s/d\_split.cpp](../sharding)
- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/s/d\_migrate.cpp](../sharding)

<pre>mongo::KeyPattern::keyBounds(mongo::FieldRangeSet const&) const</pre>
#### Used By:
- [src/mongo/s/chunk.cpp](../sharding)

<pre>mongo::KeyPattern::extendRangeBound(mongo::BSONObj const&, bool) const</pre>
#### Used By:
- [src/mongo/s/balance.cpp](../sharding)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
- [src/mongo/s/d\_split.cpp](../sharding)
- [src/mongo/dbtests/keypatterntests.cpp](../unit\_tests)
- [src/mongo/s/d\_migrate.cpp](../sharding)

<pre>mongo::KeyPattern::isSpecial() const</pre>
#### Used By:
- [src/mongo/s/shardkey.cpp](../sharding)
- [src/mongo/s/chunk.cpp](../sharding)

<pre>mongo::KeyPattern::extractSingleKey(mongo::BSONObj const&) const</pre>
#### Used By:
- [src/mongo/s/shardkey.cpp](../sharding)
- [src/mongo/db/query/idhack\_runner.cpp](../query\_system)
- [src/mongo/s/chunk.cpp](../sharding)
- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/db/exec/shard\_filter.cpp](../query\_system)
- [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/s/d\_migrate.cpp](../sharding)

-------------

Background job that periodically checks a ttl index.

- src/mongo/db/ttl.cpp   (mongod, tools)
- src/mongo/db/ttl.h

## Interface
### src/mongo/db/ttl.cpp
<pre>mongo::startTTLBackgroundJob()</pre>
#### Used By:
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
