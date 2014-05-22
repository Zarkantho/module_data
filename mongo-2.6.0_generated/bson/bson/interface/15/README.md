
# Interface for Miscellaneous BSON Code
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/jsobj.cpp

<div></div>

    mongo::BSIZE

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::LT

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BSONObj::clientReadable() const

- Used By:

    - [src/mongo/db/queryutil.cpp](../../../../core\_query\_system/legacy\_query\_code)
    - [src/mongo/db/query/index\_bounds.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::BSONNULL

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/value.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/index\_legacy.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/pipeline/expression.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/index/hash\_key\_generator.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/dbtests/accumulatortests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)

<div></div>

    mongo::dotted2nested(mongo::BSONObjBuilder&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::staticUndefined

- Used By:

    - [src/mongo/db/queryutil.cpp](../../../../core\_query\_system/legacy\_query\_code)

<div></div>

    mongo::BSONObj::woSortOrder(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Used By:

    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BSONObj::getFieldsDotted(mongo::StringData const&, std::set<mongo::BSONElement, mongo::BSONElementCmpWithoutField, std::allocator<mongo::BSONElement> >&, bool) const

- Used By:

    - [src/mongo/db/index/haystack\_key\_generator.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/commands/distinct.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/index/2d\_key\_generator.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/index/s2\_key\_generator.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::compareDottedFieldNames(std::string const&, std::string const&, mongo::LexNumCmp const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BSONObjBuilder::appendAsNumber(mongo::StringData const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/import.cpp](../../../../tools/tools)

<div></div>

    mongo::nested2dotted(mongo::BSONObjBuilder&, mongo::BSONObj const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BSONObj::isFieldNamePrefixOf(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/query/lite\_parsed\_query.cpp](../../../../core\_query\_system/query\_preprocessing)
    - [src/mongo/s/shard\_key\_pattern.cpp](../../../../sharding/routing)

<div></div>

    mongo::LTE

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BSONObjBuilder::appendMaxForType(mongo::StringData const&, int)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/queryutil.cpp](../../../../core\_query\_system/legacy\_query\_code)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BSONObj::isPrefixOf(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/query/planner\_analysis.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::minKey

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/queryutil.cpp](../../../../core\_query\_system/legacy\_query\_code)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::Ordering const&, bool) const

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/structure/btree/key.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::BSONObj::jsonString(mongo::JsonStringFormat, int) const

- Used By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/index/btree\_interface.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/client/syncclusterconnection.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/db/queryutil.cpp](../../../../core\_query\_system/legacy\_query\_code)
    - [src/mongo/db/query/plan\_ranker.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/restapi.cpp](../../../../network/web\_server)
    - [src/mongo/tools/bsondump.cpp](../../../../tools/tools)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)
    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/export.cpp](../../../../tools/tools)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::BSONObj::_okForStorage(bool, bool) const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/ops/insert.cpp](../../../../core\_query\_system/insert\_operations)
    - [src/mongo/s/shardkey.cpp](../../../../sharding/routing)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    mongo::GTE

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_count.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::typeName(mongo::BSONType)

- Used By:

    - [src/mongo/db/ops/update.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/ops/update\_driver.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/ops/modifier\_pop.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/pipeline/value.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/pipeline/expression.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/ops/modifier\_bit.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/ops/log\_builder.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../../../../security/authorization)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/bson/util/bson\_extract.cpp](../../../../bson/bson\_schema)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/ops/modifier\_current\_date.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/pipeline/document\_source\_out.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_unwind.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::BSONObj::md5() const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replica\_set\_configuration)

<div></div>

    mongo::BSONObj::replaceFieldNames(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::BSONElement::getGtLtOp(int) const

- Used By:

    - [src/mongo/db/queryutil.cpp](../../../../core\_query\_system/legacy\_query\_code)
    - [src/mongo/db/pipeline/document\_source\_match.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/fts/fts\_spec.cpp](../../../../core\_query\_system/full\_text\_search\_module)
    - [src/mongo/db/matcher/expression\_parser.cpp](../../../../core\_query\_system/query\_preprocessing)
    - [src/mongo/db/ops/modifier\_pull.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/geo/geoquery.cpp](../../../../core\_query\_system/geo\_queries)

<div></div>

    mongo::BSONObj::valid() const

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/tools/sniffer.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/jsontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/structure/collection\_compact.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)

<div></div>

    mongo::getGtLtOp(mongo::BSONElement const&)

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../../sharding/routing)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/queryutil.cpp](../../../../core\_query\_system/legacy\_query\_code)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::MAXKEY

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/keypatterntests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/value.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/keypattern.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/collection\_metadata.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::NIN

- Used By:

    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::BSONObj::getFieldsDotted(mongo::StringData const&, std::multiset<mongo::BSONElement, mongo::BSONElementCmpWithoutField, std::allocator<mongo::BSONElement> >&, bool) const

- Used By:

    - [src/mongo/db/index/2d\_key\_generator.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::BSONUndefined

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/value.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    mongo::BSONArrayIteratorSorted::BSONArrayIteratorSorted(mongo::BSONArray const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BSONObjBuilder::appendMinForType(mongo::StringData const&, int)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/queryutil.cpp](../../../../core\_query\_system/legacy\_query\_code)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::BSONObj::getFieldDottedOrArray(char const*&) const

- Used By:

    - [src/mongo/db/fts/fts\_spec\_legacy.cpp](../../../../core\_query\_system/full\_text\_search\_module)
    - [src/mongo/db/index/btree\_key\_generator.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/index/hash\_key\_generator.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::MINKEY

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/keypatterntests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/value.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/keypattern.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/collection\_metadata.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::BSONObj::couldBeArray() const

- Used By:

    - [src/mongo/db/exec/projection\_exec.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::GT

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BSONObjIteratorSorted::BSONObjIteratorSorted(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BSONElement::jsonString(mongo::JsonStringFormat, bool, int) const

- Used By:

    - [src/mongo/tools/export.cpp](../../../../tools/tools)

<div></div>

    mongo::BSONObj::extractFields(mongo::BSONObj const&, bool) const

- Used By:

    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/keypattern.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/commands/group.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/updatetests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BSONObj::getFieldNames(std::set<std::string, std::less<std::string>, std::allocator<std::string> >&) const

- Used By:

    - [src/mongo/s/shardkey.cpp](../../../../sharding/routing)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)

<div></div>

    mongo::BSONElement::Array() const

- Used By:

    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/index\_stats.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/db/geo/geoparser.cpp](../../../../core\_query\_system/geo\_queries)
    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../../core\_query\_system/query\_system\_commands)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)

<div></div>

    mongo::fieldsMatch(mongo::BSONObj const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Used By:

    - [src/mongo/db/query/query\_solution.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/index/haystack\_key\_generator.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/catalog/collection.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/query/subplan\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/query\_planner.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/exec/and\_sorted.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/queryutil.cpp](../../../../core\_query\_system/legacy\_query\_code)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/s/collection\_metadata.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/type\_tags.cpp](../../../../sharding/config\_server\_schema)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/jsontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)
    - [src/mongo/bson/mutable/document.cpp](../../../../bson/mutable\_bson)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/query/plan\_enumerator.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/dbtests/pdfiletests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/query/interval.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/commands/group.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/expressiontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/structure/btree/key.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/repl/health.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/db/index/2d\_key\_generator.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/index/hash\_key\_generator.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/dbtests/accumulatortests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/matcher/expression\_leaf.cpp](../../../../core\_query\_system/query\_preprocessing)
    - [src/mongo/db/index/index\_descriptor.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/query/planner\_analysis.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/db/exec/2dcommon.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/commands/distinct.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/query/index\_bounds.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/keypattern.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/dbtests/documenttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/keypatterntests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/exec/sort.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/matcher/expression\_where.cpp](../../../../core\_query\_system/query\_preprocessing)
    - [src/mongo/db/exec/index\_scan.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/s/range\_arithmetic.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/query/planner\_access.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../../sharding/routing)
    - [src/mongo/db/index/s2\_key\_generator.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/client/dbclient\_rs.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/exec/merge\_sort.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)
    - [src/mongo/db/exec/count.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/fts/fts\_index\_format.cpp](../../../../core\_query\_system/full\_text\_search\_module)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/balancer\_policy.cpp](../../../../sharding/balancer)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)
    - [src/mongo/db/query/query\_planner\_test\_lib.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp](../../../../bson/mutable\_bson)
    - [src/mongo/dbtests/mock/mock\_replica\_set.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/extsorttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/shardkey.cpp](../../../../sharding/routing)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/index/btree\_key\_generator.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/dbtests/updatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/exec/and\_hash.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::NE

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/files.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::staticNull

- Used By:

    - [src/mongo/db/queryutil.cpp](../../../../core\_query\_system/legacy\_query\_code)

<div></div>

    mongo::DATENOW

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/client/gridfs.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::maxKey

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/queryutil.cpp](../../../../core\_query\_system/legacy\_query\_code)
