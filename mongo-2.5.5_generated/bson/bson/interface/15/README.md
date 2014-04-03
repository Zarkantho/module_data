
# Interface for Miscellaneous BSON Code
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/jsobj.cpp

<div></div>

    mongo::BSONObjBuilder::appendMaxForType(mongo::StringData const&, int)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BSONObj::_okForStorage(bool, bool) const

- Used By:

    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../../../../queries/update\_system)
    - [src/mongo/s/shardkey.cpp](../../../../sharding/routing)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BSONObj::clientReadable() const

- Used By:

    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/query/index\_bounds.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::MINKEY

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BSONObj::couldBeArray() const

- Used By:

    - [src/mongo/db/exec/projection\_exec.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::nested2dotted(mongo::BSONObjBuilder&, mongo::BSONObj const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::typeName(mongo::BSONType)

- Used By:

    - [src/mongo/db/ttl.cpp](../../../../queries/indexing)
    - [src/mongo/db/pipeline/value.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/ops/modifier\_bit.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/update\_driver.cpp](../../../../queries/update\_system)
    - [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/ops/modifier\_current\_date.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/update.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/pipeline/document\_source\_unwind.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_out.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/ops/modifier\_inc.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/log\_builder.cpp](../../../../queries/update\_system)
    - [src/mongo/db/pipeline/expression.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../../../../queries/update\_system)
    - [src/mongo/bson/util/bson\_extract.cpp](../../../../bson/bson\_schema)
    - [src/mongo/db/ops/modifier\_pop.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../../queries/update\_system)

<div></div>

    mongo::BSONObj::md5() const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replica\_set\_configuration)

<div></div>

    mongo::BSONNULL

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/documenttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::GT

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BSONObj::replaceFieldNames(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::BSONElement::getGtLtOp(int) const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_match.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/geo/geoquery.cpp](../../../../queries/geo\_queries)
    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/matcher/expression\_parser.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../../../../queries/update\_system)
    - [src/mongo/db/fts/fts\_spec.cpp](../../../../queries/full\_text\_search\_module)

<div></div>

    mongo::minKey

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::BSONObjIteratorSorted::BSONObjIteratorSorted(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BSIZE

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::LTE

- Used By:

    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::dotted2nested(mongo::BSONObjBuilder&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::staticUndefined

- Used By:

    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::BSONObj::isFieldNamePrefixOf(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/s/shard\_key\_pattern.cpp](../../../../sharding/routing)
    - [src/mongo/db/query/lite\_parsed\_query.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::LT

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)

<div></div>

    mongo::BSONObj::valid() const

- Used By:

    - [src/mongo/db/structure/collection\_compact.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/tools/sniffer.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)

<div></div>

    mongo::GTE

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::getGtLtOp(mongo::BSONElement const&)

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../../sharding/routing)
    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::BSONArrayIteratorSorted::BSONArrayIteratorSorted(mongo::BSONArray const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::BSONObj::extractFields(mongo::BSONObj const&, bool) const

- Used By:

    - [src/mongo/dbtests/updatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../../queries/update\_system)
    - [src/mongo/db/keypattern.cpp](../../../../queries/indexing)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/commands/group.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::Ordering const&, bool) const

- Used By:

    - [src/mongo/db/structure/btree/key.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)

<div></div>

    mongo::BSONElement::Array() const

- Used By:

    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/db/commands/index\_stats.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/geo/geoparser.cpp](../../../../queries/geo\_queries)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../../../../queries/update\_system)
    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replica\_set\_configuration)

<div></div>

    mongo::BSONObj::woSortOrder(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)

<div></div>

    mongo::MAXKEY

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::NIN

- Used By:

    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)

<div></div>

    mongo::fieldsMatch(mongo::BSONObj const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::BSONObj::getFieldsDotted(mongo::StringData const&, std::set<mongo::BSONElement, mongo::BSONElementCmpWithoutField, std::allocator<mongo::BSONElement> >&, bool) const

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/commands/distinct.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/index/2d\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/db/index/s2\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../../../../queries/indexing)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/query/query\_solution.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/balancer\_policy.cpp](../../../../sharding/balancer)
    - [src/mongo/db/query/plan\_enumerator.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/count.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/query/get\_runner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/extsorttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/client/dbclient\_rs.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/keypattern.cpp](../../../../queries/indexing)
    - [src/mongo/db/commands/group.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/exec/and\_sorted.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/exec/index\_scan.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../../sharding/routing)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/s/range\_arithmetic.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/query/interval.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/expressiontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/accumulatortests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/db/fts/fts\_index\_format.cpp](../../../../queries/full\_text\_search\_module)
    - [src/mongo/db/matcher/expression\_leaf.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/matcher/expression\_where.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/sort.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/query/index\_bounds.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/keypatterntests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/structure/catalog/index\_details.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/health.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../../queries/update\_system)
    - [src/mongo/db/index/2d\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/db/index/s2\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/query/planner\_analysis.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/s/shardkey.cpp](../../../../sharding/routing)
    - [src/mongo/dbtests/updatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/distinct.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/query/query\_planner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/mock/mock\_replica\_set.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/structure/btree/key.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp](../../../../bson/mutable\_bson)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/catalog/collection.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/type\_tags.cpp](../../../../sharding/config\_server\_schema)
    - [src/mongo/db/query/planner\_access.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/collection\_metadata.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/db/query/query\_planner\_test\_lib.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/index/btree\_key\_generator.cpp](../../../../queries/indexing)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/bson/mutable/document.cpp](../../../../bson/mutable\_bson)
    - [src/mongo/db/exec/and\_hash.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/index/hash\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/type\_chunk.cpp](../../../../sharding/config\_server\_schema)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/exec/merge\_sort.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::BSONObj::isPrefixOf(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::BSONObj::getFieldsDotted(mongo::StringData const&, std::multiset<mongo::BSONElement, mongo::BSONElementCmpWithoutField, std::allocator<mongo::BSONElement> >&, bool) const

- Used By:

    - [src/mongo/db/index/2d\_access\_method.cpp](../../../../queries/indexing)

<div></div>

    mongo::BSONObj::jsonString(mongo::JsonStringFormat, int) const

- Used By:

    - [src/mongo/dbtests/perf/perftest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)
    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/jsontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)
    - [src/mongo/tools/bsondump.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/export.cpp](../../../../tools/tools)
    - [src/mongo/db/restapi.cpp](../../../../network/web\_server)
    - [src/mongo/db/index/btree\_interface.cpp](../../../../queries/indexing)
    - [src/mongo/client/syncclusterconnection.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::BSONUndefined

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::compareDottedFieldNames(std::string const&, std::string const&, mongo::LexNumCmp const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::NE

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/files.cpp](../../../../tools/tools)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::BSONObjBuilder::appendAsNumber(mongo::StringData const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/import.cpp](../../../../tools/tools)

<div></div>

    mongo::BSONObj::getFieldDottedOrArray(char const*&) const

- Used By:

    - [src/mongo/db/index/btree\_key\_generator.cpp](../../../../queries/indexing)
    - [src/mongo/db/index/hash\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/db/fts/fts\_spec\_legacy.cpp](../../../../queries/full\_text\_search\_module)

<div></div>

    mongo::staticNull

- Used By:

    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::BSONElement::jsonString(mongo::JsonStringFormat, bool, int) const

- Used By:

    - [src/mongo/tools/export.cpp](../../../../tools/tools)

<div></div>

    mongo::BSONObjBuilder::appendMinForType(mongo::StringData const&, int)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/query/index\_bounds\_builder.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::maxKey

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/queryutil.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::BSONObj::getFieldNames(std::set<std::string, std::less<std::string>, std::allocator<std::string> >&) const

- Used By:

    - [src/mongo/s/shardkey.cpp](../../../../sharding/routing)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)
