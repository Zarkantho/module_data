
# Interface for TODO: Name this group
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/util/safe\_num.cpp

<div></div>

    mongo::SafeNum::isIdentical(mongo::SafeNum const&) const

- Used By:

    - [src/mongo/db/ops/modifier\_inc.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/ops/modifier\_bit.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::SafeNum::orInternal(mongo::SafeNum const&, mongo::SafeNum const&)

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::SafeNum::xorInternal(mongo::SafeNum const&, mongo::SafeNum const&)

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::SafeNum::andInternal(mongo::SafeNum const&, mongo::SafeNum const&)

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::SafeNum::debugString() const

- Used By:

    - [src/mongo/db/ops/log\_builder.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/ops/modifier\_bit.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::SafeNum::mulInternal(mongo::SafeNum const&, mongo::SafeNum const&)

- Used By:

    - [src/mongo/db/ops/modifier\_inc.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::SafeNum::SafeNum(mongo::BSONElement const&)

- Used By:

    - [src/mongo/db/ops/modifier\_inc.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/ops/modifier\_bit.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::SafeNum::addInternal(mongo::SafeNum const&, mongo::SafeNum const&)

- Used By:

    - [src/mongo/db/ops/modifier\_inc.cpp](../../../../core\_query\_system/update\_system)

### src/mongo/util/signal\_handlers.cpp

<div></div>

    mongo::setupSignalHandlers()

- Used By:

    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::startSignalProcessingThread()

- Used By:

    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

### src/mongo/util/stack\_introspect.cpp

<div></div>

    mongo::inConstructorChainSupported()

- Used By:

    - [src/mongo/dbtests/stacktests.cpp](../../../../tests/unit\_tests)

### src/mongo/util/stacktrace.cpp

<div></div>

    mongo::printStackTrace(std::ostream&)

- Used By:

    - [src/mongo/util/log.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)
    - [src/mongo/db/dur\_commitjob.cpp](../../../../storage/journaling)
    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/dur\_preplogbuffer.cpp](../../../../storage/journaling)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/db/tests.cpp](../../../../dead\_code/dead\_code)

### src/mongo/util/startup\_test.cpp

<div></div>

    mongo::StartupTest::~StartupTest()

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/shardkey.cpp](../../../../sharding/routing)
    - [src/mongo/bson/optime.cpp](../../../../bson/bson)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/structure/btree/key.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/util/logfile.cpp](../../../../storage/journaling)
    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/util/mmap\_posix.cpp](../../../../storage/data\_files)
    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/health.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::StartupTest::StartupTest()

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/shardkey.cpp](../../../../sharding/routing)
    - [src/mongo/bson/optime.cpp](../../../../bson/bson)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/structure/btree/key.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/util/logfile.cpp](../../../../storage/journaling)
    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/util/mmap\_posix.cpp](../../../../storage/data\_files)
    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/health.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::StartupTest::runTests()

- Used By:

    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/dbtests/dbtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/s/mongos\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    typeinfo for mongo::StartupTest

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/shardkey.cpp](../../../../sharding/routing)
    - [src/mongo/bson/optime.cpp](../../../../bson/bson)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/structure/btree/key.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/util/logfile.cpp](../../../../storage/journaling)
    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/util/mmap\_posix.cpp](../../../../storage/data\_files)
    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/health.cpp](../../../../replication/replica\_set\_state)

### src/mongo/util/stringutils.cpp

<div></div>

    mongo::versionCmp(mongo::StringData, mongo::StringData)

- Used By:

    - [src/mongo/tools/restore.cpp](../../../../tools/tools)
    - [src/mongo/s/mongo\_version\_range.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::joinStringDelim(std::vector<std::string, std::allocator<std::string> > const&, std::string*, char)

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::LexNumCmp::operator()(mongo::StringData const&, mongo::StringData const&) const

- Used By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::splitStringDelim(std::string const&, std::vector<std::string, std::allocator<std::string> >*, char)

- Used By:

    - [src/mongo/db/auth/action\_set.cpp](../../../../security/authorization)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/server\_parameters.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/s/mongos\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::LexNumCmp::cmp(mongo::StringData const&, mongo::StringData const&) const

- Used By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::LexNumCmp::LexNumCmp(bool)

- Used By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

### src/mongo/util/text.cpp

<div></div>

    mongo::parseLL(char const*)

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    mongo::isValidUTF8(char const*)

- Used By:

    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/bsondump.cpp](../../../../tools/tools)
    - [src/mongo/tools/import.cpp](../../../../tools/tools)

<div></div>

    mongo::StringSplitter::split(std::vector<std::string, std::allocator<std::string> >&)

- Used By:

    - [src/mongo/tools/mongoimport\_options.cpp](../../../../tools/tools)

<div></div>

    mongo::StringSplitter::next()

- Used By:

    - [src/mongo/tools/stat.cpp](../../../../tools/tools)

<div></div>

    mongo::StringSplitter::join(std::vector<std::string, std::allocator<std::string> > const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::StringSplitter::split(std::string const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)

### src/mongo/util/time\_support.cpp

<div></div>

    mongo::Date_t::toString() const

- Used By:

    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)

<div></div>

    mongo::jsTime()

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/server\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/ops/modifier\_current\_date.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/dbtests/documenttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/introspect.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/client/gridfs.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::sleepmillis(long long)

- Used By:

    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/test\_commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/commands/authentication\_commands.cpp](../../../../security/authentication)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)
    - [src/mongo/util/fail\_point.cpp](../../../../tests/fail\_points)
    - [src/mongo/db/dbcommands\_admin.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/scripting/bench.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/scripting/utils.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/repl/resync.cpp](../../../../replication/data\_sync)
    - [src/mongo/util/net/message\_server\_port.cpp](../../../../network/network\_core)
    - [src/mongo/db/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/db/range\_deleter.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/util/mmap.cpp](../../../../storage/data\_files)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../../replication/data\_sync)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/version\_manager.cpp](../../../../sharding/metadata\_versioning)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::Date_t::toTimeT() const

- Used By:

    - [src/mongo/db/commands/storage\_details.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Backoff::getNextSleepMillis(int, unsigned long long, unsigned long long) const

- Used By:

    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::time_t_to_Struct(long, tm*, bool)

- Used By:

    - [src/mongo/tools/stat\_util.cpp](../../../../tools/tools)

<div></div>

    mongo::currentDate()

- Used By:

    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::dateToISOStringLocal(mongo::Date_t)

- Used By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)
    - [src/mongo/logger/message\_event\_utf8\_encoder.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::dateFromISOString(mongo::StringData const&)

- Used By:

    - [src/mongo/db/json.cpp](../../../../bson/bson)

<div></div>

    mongo::sleepmicros(long long)

- Used By:

    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/client/examples/mongoperf.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::toPointInTime(std::string const&, boost::posix_time::ptime*)

- Used By:

    - [src/mongo/s/type\_settings.cpp](../../../../sharding/config\_server\_schema)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::getJSTimeVirtualThreadSkew()

- Used By:

    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)

<div></div>

    mongo::dateToISOStringUTC(mongo::Date_t)

- Used By:

    - [src/mongo/tools/export.cpp](../../../../tools/tools)
    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::Backoff::nextSleepMillis()

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../../sharding/routing)
    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::time_t_to_String_short(long)

- Used By:

    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/db/pipeline/value.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/data\_sync)
    - [src/mongo/tools/oplog.cpp](../../../../tools/tools)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/repl/health.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/dbtests/documenttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::curTimeMicros64()

- Used By:

    - [src/mongo/s/d\_writeback.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/s/request.cpp](../../../../network/network\_core)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/dbhash.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/dbeval.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)
    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/distinct.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)
    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../../../../core\_query\_system/full\_text\_search\_module)
    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/util/file\_allocator.cpp](../../../../storage/file\_allocation)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/dbcommands\_admin.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/exec/oplogstart.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/scripting/bench.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/storage/extent\_manager.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/matchertests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/client/examples/mongoperf.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/clientlistplugin.cpp](../../../../network/web\_server)
    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)
    - [src/mongo/db/commands/touch.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/dur\_writetodatafiles.cpp](../../../../storage/journaling)
    - [src/mongo/db/restapi.cpp](../../../../network/web\_server)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/repl/resync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/dur\_preplogbuffer.cpp](../../../../storage/journaling)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/commands/geonear.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mmaptests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/util/net/sock.cpp](../../../../network/network\_core)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../../../../core\_query\_system/full\_text\_search\_module)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/structure/collection\_compact.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::terseCurrentTime(bool)

- Used By:

    - [src/mongo/util/log.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/tools/top.cpp](../../../../tools/tools)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::sleepsecs(int)

- Used By:

    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/client/examples/mongoperf.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/writeback\_listener.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/s/config\_server\_checker\_service.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/util/file\_allocator.cpp](../../../../storage/file\_allocation)
    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/tools/top.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/framework.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/repl/sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/util/net/listen.cpp](../../../../network/network\_core)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../../../../security/authorization)
    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/tools/stat.cpp](../../../../tools/tools)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::jsTimeVirtualThreadSkew(long long)

- Used By:

    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)

<div></div>

    mongo::dateToCtimeString(mongo::Date_t)

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::curTimeMicros()

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::curTimeMillis64()

- Used By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)
    - [src/mongo/db/commands/server\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)

### src/mongo/util/timer.cpp

<div></div>

    mongo::Timer::_countsPerSecond

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/dbhash.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/dbeval.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/distinct.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)
    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../../../../core\_query\_system/full\_text\_search\_module)
    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/util/file\_allocator.cpp](../../../../storage/file\_allocation)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/dbcommands\_admin.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/exec/oplogstart.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/scripting/bench.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/storage/extent\_manager.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/matchertests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/client/examples/mongoperf.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/commands/touch.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/dur\_writetodatafiles.cpp](../../../../storage/journaling)
    - [src/mongo/db/restapi.cpp](../../../../network/web\_server)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/repl/resync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/dur\_preplogbuffer.cpp](../../../../storage/journaling)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)
    - [src/mongo/s/request.cpp](../../../../network/network\_core)
    - [src/mongo/db/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mmaptests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../../../../core\_query\_system/full\_text\_search\_module)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/structure/collection\_compact.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)

### src/mongo/util/touch\_pages.cpp

<div></div>

    mongo::touch_pages(char const*, unsigned long)

- Used By:

    - [src/mongo/db/commands/touch.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/structure/collection\_compact.cpp](../../../../storage/storage\_layer\_structure)

### src/mongo/util/util.cpp

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Used By:

    - [src/mongo/s/d\_writeback.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/exec/collection\_scan.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/writeback\_listener.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../../storage/journaling)
    - [src/mongo/util/file\_allocator.cpp](../../../../storage/file\_allocation)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/scripting/engine.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/catalog/index\_pregen.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/dbtests/counttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/util/net/listen.cpp](../../../../network/network\_core)
    - [src/mongo/db/commands/dbhash.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/version\_manager.cpp](../../../../sharding/metadata\_versioning)
    - [src/mongo/dbtests/framework.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/kill\_current\_op.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)
    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/tools/stat.cpp](../../../../tools/tools)
    - [src/mongo/db/dur\_commitjob.cpp](../../../../storage/journaling)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)
    - [src/mongo/util/fail\_point\_service.cpp](../../../../tests/fail\_points)
    - [src/mongo/db/pdfile.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/util/net/sock.cpp](../../../../network/network\_core)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../../security/authorization)
    - [src/mongo/client/syncclusterconnection.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/client/examples/mongoperf.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/repl/manager.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/util/concurrency/synchronization.cpp](../../../../query\_and\_operation\_handling/concurrency)
    - [src/mongo/db/range\_deleter\_mock\_env.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/util/concurrency/spin\_lock.cpp](../../../../query\_and\_operation\_handling/concurrency)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/db/repl/health.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/commands/fsync.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/shell/shell\_utils.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/index/btree\_index\_cursor.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/commands/authentication\_commands.cpp](../../../../security/authentication)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/util/net/ssl\_manager.cpp](../../../../network/ssl)
    - [src/mongo/bson/optime.cpp](../../../../bson/bson)
    - [src/mongo/db/range\_deleter.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/dbtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/isself.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/mock/mock\_conn\_registry.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/exec/fetch.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/s/config\_server\_checker\_service.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)

<div></div>

    mongo::operator<<(std::ostream&, mongo::ThreadSafeString const&)

- Used By:

    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::hexdump(char const*, unsigned int)

- Used By:

    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)

### src/mongo/util/version\_reporting.cpp

<div></div>

    mongo::printSysInfo()

- Used By:

    - [src/mongo/dbtests/framework.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/log\_process\_details.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::openSSLVersion(std::string const&, std::string const&)

- Used By:

    - [src/mongo/s/version\_mongos.cpp](../../../../process\_management/build\_information)
    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::appendBuildInfo(mongo::BSONObjBuilder&)

- Used By:

    - [src/mongo/shell/shell\_utils.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::printAllocator()

- Used By:

    - [src/mongo/db/log\_process\_details.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::printGitVersion()

- Used By:

    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/dbtests/framework.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/log\_process\_details.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::printOpenSSLVersion()

- Used By:

    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/dbtests/framework.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/log\_process\_details.cpp](../../../../process\_management/logging\_system)

### src/mongo/util/base64.cpp

<div></div>

    mongo::base64::chars

- Used By:

    - [src/mongo/db/json.cpp](../../../../bson/bson)

<div></div>

    mongo::base64::encode(std::string const&)

- Used By:

    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::base64::encode(char const*, int)

- Used By:

    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    mongo::base64::decode(std::string const&)

- Used By:

    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/client/sasl\_client\_authenticate.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/json.cpp](../../../../bson/bson)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    mongo::base64::encode(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&, char const*, int)

- Used By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

### src/mongo/util/compress.cpp

<div></div>

    mongo::maxCompressedLength(unsigned long)

- Used By:

    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)

<div></div>

    mongo::compress(char const*, unsigned long, std::string*)

- Used By:

    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::uncompress(char const*, unsigned long, std::string*)

- Used By:

    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::rawCompress(char const*, unsigned long, char*, unsigned long*)

- Used By:

    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)

### src/mongo/util/concurrency/thread\_pool.cpp

<div></div>

    mongo::threadpool::ThreadPool::ThreadPool(int)

- Used By:

    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::threadpool::ThreadPool::~ThreadPool()

- Used By:

    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::threadpool::ThreadPool::schedule(boost::function<void ()>)

- Used By:

    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::threadpool::ThreadPool::join()

- Used By:

    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)

### src/mongo/util/exception\_filter\_win32.cpp

<div></div>

    mongo::setWindowsUnhandledExceptionFilter()

- Used By:

    - [src/mongo/dbtests/dbtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/unittest/unittest\_main.cpp](../../../../tests/unit\_tests)
