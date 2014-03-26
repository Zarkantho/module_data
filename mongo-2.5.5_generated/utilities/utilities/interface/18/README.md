
# Interface for TODO: Name this group
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/util/safe\_num.cpp

<div></div>

    mongo::SafeNum::isIdentical(mongo::SafeNum const&) const

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../../../../queries/update\_system)

<div></div>

    mongo::SafeNum::orInternal(mongo::SafeNum const&, mongo::SafeNum const&)

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../../../../queries/update\_system)

<div></div>

    mongo::SafeNum::xorInternal(mongo::SafeNum const&, mongo::SafeNum const&)

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../../../../queries/update\_system)

<div></div>

    mongo::SafeNum::andInternal(mongo::SafeNum const&, mongo::SafeNum const&)

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../../../../queries/update\_system)

<div></div>

    mongo::SafeNum::debugString() const

- Used By:

    - [src/mongo/db/ops/log\_builder.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/modifier\_bit.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../../../../queries/update\_system)

<div></div>

    mongo::SafeNum::mulInternal(mongo::SafeNum const&, mongo::SafeNum const&)

- Used By:

    - [src/mongo/db/ops/modifier\_inc.cpp](../../../../queries/update\_system)

<div></div>

    mongo::SafeNum::SafeNum(mongo::BSONElement const&)

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../../../../queries/update\_system)

<div></div>

    mongo::SafeNum::addInternal(mongo::SafeNum const&, mongo::SafeNum const&)

- Used By:

    - [src/mongo/db/ops/modifier\_inc.cpp](../../../../queries/update\_system)

### src/mongo/util/signal\_handlers.cpp

<div></div>

    mongo::printStackAndExit(int)

- Used By:

    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

### src/mongo/util/stack\_introspect.cpp

<div></div>

    mongo::inConstructorChainSupported()

- Used By:

    - [src/mongo/dbtests/stacktests.cpp](../../../../tests/unit\_tests)

### src/mongo/util/stacktrace.cpp

<div></div>

    mongo::printStackTrace(std::ostream&)

- Used By:

    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/dur\_commitjob.cpp](../../../../storage/journaling)
    - [src/mongo/db/tests.cpp](../../../../dead\_code/dead\_code)
    - [src/mongo/util/log.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/db/dur\_preplogbuffer.cpp](../../../../storage/journaling)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/sharding)

### src/mongo/util/startup\_test.cpp

<div></div>

    mongo::StartupTest::~StartupTest()

- Used By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)
    - [src/mongo/db/structure/btree/key.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/bson/optime.cpp](../../../../bson/bson)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/shardkey.cpp](../../../../sharding/sharding)
    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/util/mmap\_posix.cpp](../../../../storage/mmap)
    - [src/mongo/db/repl/health.cpp](../../../../replication/replication)
    - [src/mongo/s/chunk.cpp](../../../../sharding/sharding)
    - [src/mongo/s/grid.cpp](../../../../sharding/sharding)
    - [src/mongo/util/logfile.cpp](../../../../storage/journaling)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/sharding)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::StartupTest::StartupTest()

- Used By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)
    - [src/mongo/db/structure/btree/key.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/bson/optime.cpp](../../../../bson/bson)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/shardkey.cpp](../../../../sharding/sharding)
    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/util/mmap\_posix.cpp](../../../../storage/mmap)
    - [src/mongo/db/repl/health.cpp](../../../../replication/replication)
    - [src/mongo/s/chunk.cpp](../../../../sharding/sharding)
    - [src/mongo/s/grid.cpp](../../../../sharding/sharding)
    - [src/mongo/util/logfile.cpp](../../../../storage/journaling)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/sharding)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::StartupTest::runTests()

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/s/mongos\_options.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/dbtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)

<div></div>

    typeinfo for mongo::StartupTest

- Used By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)
    - [src/mongo/db/structure/btree/key.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/bson/optime.cpp](../../../../bson/bson)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/shardkey.cpp](../../../../sharding/sharding)
    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/util/mmap\_posix.cpp](../../../../storage/mmap)
    - [src/mongo/db/repl/health.cpp](../../../../replication/replication)
    - [src/mongo/s/chunk.cpp](../../../../sharding/sharding)
    - [src/mongo/s/grid.cpp](../../../../sharding/sharding)
    - [src/mongo/util/logfile.cpp](../../../../storage/journaling)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/sharding)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../../storage/storage\_layer\_structure)

### src/mongo/util/stringutils.cpp

<div></div>

    mongo::versionCmp(mongo::StringData, mongo::StringData)

- Used By:

    - [src/mongo/s/mongo\_version\_range.cpp](../../../../sharding/sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/sharding)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)

<div></div>

    mongo::joinStringDelim(std::vector<std::string, std::allocator<std::string> > const&, std::string*, char)

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/sharding)

<div></div>

    mongo::LexNumCmp::operator()(mongo::StringData const&, mongo::StringData const&) const

- Used By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::splitStringDelim(std::string const&, std::vector<std::string, std::allocator<std::string> >*, char)

- Used By:

    - [src/mongo/db/server\_parameters.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/s/config.cpp](../../../../sharding/sharding)
    - [src/mongo/s/mongos\_options.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/auth/action\_set.cpp](../../../../security/authorization)

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

    - [src/mongo/tools/bsondump.cpp](../../../../tools/tools)
    - [src/mongo/tools/import.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)

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

    - [src/mongo/s/distlock.cpp](../../../../sharding/sharding)

<div></div>

    mongo::jsTime()

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/config.cpp](../../../../sharding/sharding)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replication)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding)
    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replication)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/s/balance.cpp](../../../../sharding/sharding)
    - [src/mongo/db/ops/modifier\_current\_date.cpp](../../../../queries/update\_system)
    - [src/mongo/db/commands/server\_status.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/introspect.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/distlock.cpp](../../../../sharding/sharding)
    - [src/mongo/client/gridfs.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/sharding)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::sleepmillis(long long)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../../security/authentication)
    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/replication)
    - [src/mongo/db/range\_deleter.cpp](../../../../sharding/sharding)
    - [src/mongo/db/repl/consensus.cpp](../../../../replication/replication)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)
    - [src/mongo/db/commands/test\_commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/write\_concern.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/s/chunk.cpp](../../../../sharding/sharding)
    - [src/mongo/s/version\_manager.cpp](../../../../sharding/sharding)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/scripting/bench.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/repl/resync.cpp](../../../../replication/replication)
    - [src/mongo/scripting/utils.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding)
    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/replication)
    - [src/mongo/db/dbcommands\_admin.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/util/net/message\_server\_port.cpp](../../../../network/network\_core)
    - [src/mongo/s/distlock.cpp](../../../../sharding/sharding)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/sharding)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/util/fail\_point.cpp](../../../../tests/fail\_points)
    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/util/mmap.cpp](../../../../storage/mmap)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Date_t::toTimeT() const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/storage\_details.cpp](../../../../queries/database\_commands)

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

    - [src/mongo/s/grid.cpp](../../../../sharding/sharding)

<div></div>

    mongo::dateToISOStringLocal(mongo::Date_t)

- Used By:

    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)
    - [src/mongo/logger/message\_event\_utf8\_encoder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::dateFromISOString(mongo::StringData const&)

- Used By:

    - [src/mongo/db/json.cpp](../../../../bson/bson)

<div></div>

    mongo::sleepmicros(long long)

- Used By:

    - [src/mongo/db/clientcursor.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbhelpers.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/client/examples/mongoperf.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::toPointInTime(std::string const&, boost::posix_time::ptime*)

- Used By:

    - [src/mongo/s/type\_settings.cpp](../../../../sharding/sharding)
    - [src/mongo/s/grid.cpp](../../../../sharding/sharding)

<div></div>

    mongo::getJSTimeVirtualThreadSkew()

- Used By:

    - [src/mongo/s/distlock.cpp](../../../../sharding/sharding)

<div></div>

    mongo::dateToISOStringUTC(mongo::Date_t)

- Used By:

    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/tools/export.cpp](../../../../tools/tools)

<div></div>

    mongo::Backoff::nextSleepMillis()

- Used By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../../sharding/sharding)

<div></div>

    mongo::time_t_to_String_short(long)

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/documenttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/value.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/s/balance.cpp](../../../../sharding/sharding)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/replication)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/health.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/replication)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replication)
    - [src/mongo/tools/oplog.cpp](../../../../tools/tools)

<div></div>

    mongo::curTimeMicros64()

- Used By:

    - [src/mongo/util/file\_allocator.cpp](../../../../storage/file\_allocation)
    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replication)
    - [src/mongo/db/commands/dbhash.cpp](../../../../queries/database\_commands)
    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/exec/oplogstart.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/write\_concern.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/db/query/new\_find.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/geonear.cpp](../../../../queries/database\_commands)
    - [src/mongo/util/net/sock.cpp](../../../../network/network\_core)
    - [src/mongo/scripting/bench.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/s/d\_writeback.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/db/commands/touch.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/mmaptests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/structure/collection\_compact.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/db/repl/resync.cpp](../../../../replication/replication)
    - [src/mongo/db/clientcursor.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/sharding)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/dbtests/matchertests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../../sharding/sharding)
    - [src/mongo/db/storage/extent\_manager.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/client/examples/mongoperf.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/dur\_preplogbuffer.cpp](../../../../storage/journaling)
    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding)
    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/curop.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/dur\_writetodatafiles.cpp](../../../../storage/journaling)
    - [src/mongo/db/clientlistplugin.cpp](../../../../network/web\_server)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/request.cpp](../../../../network/network\_core)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/s/distlock.cpp](../../../../sharding/sharding)
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../../../../queries/full\_text\_search\_module)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/sharding)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/sharding)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dbcommands\_admin.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/replication)
    - [src/mongo/db/dbeval.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding)
    - [src/mongo/db/d\_concurrency.cpp](../../../../queries/concurrency)
    - [src/mongo/s/chunk.cpp](../../../../sharding/sharding)
    - [src/mongo/db/restapi.cpp](../../../../network/web\_server)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../../../../queries/full\_text\_search\_module)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/distinct.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::terseCurrentTime(bool)

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/sharding)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/tools/top.cpp](../../../../tools/tools)
    - [src/mongo/db/dbhelpers.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/sharding)
    - [src/mongo/util/log.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::sleepsecs(int)

- Used By:

    - [src/mongo/util/file\_allocator.cpp](../../../../storage/file\_allocation)
    - [src/mongo/util/net/listen.cpp](../../../../network/network\_core)
    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replication)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../../../../security/authorization)
    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/replication)
    - [src/mongo/tools/top.cpp](../../../../tools/tools)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../../replication/replication)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../../sharding/sharding)
    - [src/mongo/s/config.cpp](../../../../sharding/sharding)
    - [src/mongo/s/writeback\_listener.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/db/clientcursor.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/s/balance.cpp](../../../../sharding/sharding)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replication)
    - [src/mongo/db/ttl.cpp](../../../../queries/indexing)
    - [src/mongo/dbtests/framework.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/distlock.cpp](../../../../sharding/sharding)
    - [src/mongo/db/repl/sync.cpp](../../../../replication/replication)
    - [src/mongo/client/examples/mongoperf.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/sharding)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/tools/stat.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/config\_server\_checker\_service.cpp](../../../../sharding/sharding)

<div></div>

    mongo::jsTimeVirtualThreadSkew(long long)

- Used By:

    - [src/mongo/s/distlock.cpp](../../../../sharding/sharding)

<div></div>

    mongo::dateToCtimeString(mongo::Date_t)

- Used By:

    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::curTimeMicros()

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::curTimeMillis64()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/ttl.cpp](../../../../queries/indexing)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/d\_concurrency.cpp](../../../../queries/concurrency)
    - [src/mongo/db/commands/server\_status.cpp](../../../../queries/database\_commands)
    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

### src/mongo/util/timer.cpp

<div></div>

    mongo::Timer::_countsPerSecond

- Used By:

    - [src/mongo/util/file\_allocator.cpp](../../../../storage/file\_allocation)
    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replication)
    - [src/mongo/db/commands/dbhash.cpp](../../../../queries/database\_commands)
    - [src/mongo/unittest/unittest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/exec/oplogstart.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/write\_concern.cpp](../../../../replication/replication)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/scripting/bench.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../../sharding/sharding)
    - [src/mongo/dbtests/mmaptests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/structure/collection\_compact.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/db/repl/resync.cpp](../../../../replication/replication)
    - [src/mongo/db/clientcursor.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/sharding)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/commands/touch.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/storage/extent\_manager.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/client/examples/mongoperf.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/restapi.cpp](../../../../network/web\_server)
    - [src/mongo/db/dur\_preplogbuffer.cpp](../../../../storage/journaling)
    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding)
    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/dur\_writetodatafiles.cpp](../../../../storage/journaling)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/request.cpp](../../../../network/network\_core)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/s/distlock.cpp](../../../../sharding/sharding)
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../../../../queries/full\_text\_search\_module)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/sharding)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/sharding)
    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dbcommands\_admin.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/replication)
    - [src/mongo/db/dbeval.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding)
    - [src/mongo/db/d\_concurrency.cpp](../../../../queries/concurrency)
    - [src/mongo/s/chunk.cpp](../../../../sharding/sharding)
    - [src/mongo/dbtests/matchertests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../../../../queries/full\_text\_search\_module)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/distinct.cpp](../../../../queries/database\_commands)

### src/mongo/util/touch\_pages.cpp

<div></div>

    mongo::touch_pages(char const*, unsigned long)

- Used By:

    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/structure/collection\_compact.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/touch.cpp](../../../../queries/database\_commands)

### src/mongo/util/util.cpp

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Used By:

    - [src/mongo/util/net/listen.cpp](../../../../network/network\_core)
    - [src/mongo/db/index/btree\_index\_cursor.cpp](../../../../queries/indexing)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replication)
    - [src/mongo/util/net/sock.cpp](../../../../network/network\_core)
    - [src/mongo/s/balance.cpp](../../../../sharding/sharding)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/repl/manager.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/framework.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/fsync.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/range\_deleter\_mock\_env.cpp](../../../../sharding/sharding)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/dbtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../../security/authorization)
    - [src/mongo/client/syncclusterconnection.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/util/file\_allocator.cpp](../../../../storage/file\_allocation)
    - [src/mongo/db/range\_deleter.cpp](../../../../sharding/sharding)
    - [src/mongo/db/commands/dbhash.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../../../../storage/journaling)
    - [src/mongo/db/dur\_commitjob.cpp](../../../../storage/journaling)
    - [src/mongo/tools/stat.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/util/net/ssl\_manager.cpp](../../../../network/ssl)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/writeback\_listener.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/db/repl/health.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding)
    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replication)
    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/pdfile.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/counttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/kill\_current\_op.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/consensus.cpp](../../../../replication/replication)
    - [src/mongo/util/concurrency/synchronization.cpp](../../../../queries/concurrency)
    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replication)
    - [src/mongo/s/version\_manager.cpp](../../../../sharding/sharding)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_writeback.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/s/config.cpp](../../../../sharding/sharding)
    - [src/mongo/util/fail\_point\_service.cpp](../../../../tests/fail\_points)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/sharding)
    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/sharding)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/shell/shell\_utils.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/sharding)
    - [src/mongo/db/exec/fetch.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/d\_concurrency.cpp](../../../../queries/concurrency)
    - [src/mongo/s/chunk.cpp](../../../../sharding/sharding)
    - [src/mongo/s/config\_server\_checker\_service.cpp](../../../../sharding/sharding)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/replication)
    - [src/mongo/db/commands/authentication\_commands.cpp](../../../../security/authentication)
    - [src/mongo/tools/bridge.cpp](../../../../tools/tools)
    - [src/mongo/scripting/engine.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/bson/optime.cpp](../../../../bson/bson)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/util/concurrency/spin\_lock.cpp](../../../../queries/concurrency)
    - [src/mongo/db/commands/isself.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/curop.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/distlock.cpp](../../../../sharding/sharding)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/sharding)
    - [src/mongo/client/examples/mongoperf.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/s/shard.cpp](../../../../sharding/sharding)
    - [src/mongo/s/cursors.cpp](../../../../sharding/sharding)
    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/s/grid.cpp](../../../../sharding/sharding)
    - [src/mongo/dbtests/mock/mock\_conn\_registry.cpp](../../../../tests/unit\_tests)
    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)

<div></div>

    mongo::operator<<(std::ostream&, mongo::ThreadSafeString const&)

- Used By:

    - [src/mongo/db/curop.cpp](../../../../queries/client\_and\_operation\_tracking)

<div></div>

    mongo::hexdump(char const*, unsigned int)

- Used By:

    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)

### src/mongo/util/version\_reporting.cpp

<div></div>

    mongo::printSysInfo()

- Used By:

    - [src/mongo/db/log\_process\_details.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/dbtests/framework.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::openSSLVersion(std::string const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/s/version\_mongos.cpp](../../../../sharding/sharding)

<div></div>

    mongo::appendBuildInfo(mongo::BSONObjBuilder&)

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../../queries/database\_commands)
    - [src/mongo/shell/shell\_utils.cpp](../../../../mongo\_shell/mongo\_shell)

<div></div>

    mongo::printAllocator()

- Used By:

    - [src/mongo/db/log\_process\_details.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::printGitVersion()

- Used By:

    - [src/mongo/db/log\_process\_details.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/dbtests/framework.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::printOpenSSLVersion()

- Used By:

    - [src/mongo/db/log\_process\_details.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/dbtests/framework.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

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

    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::base64::decode(std::string const&)

- Used By:

    - [src/mongo/client/sasl\_client\_authenticate.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/json.cpp](../../../../bson/bson)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)

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

    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::uncompress(char const*, unsigned long, std::string*)

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/basictests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)

<div></div>

    mongo::rawCompress(char const*, unsigned long, char*, unsigned long*)

- Used By:

    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)

### src/mongo/util/concurrency/thread\_pool.cpp

<div></div>

    mongo::threadpool::ThreadPool::ThreadPool(int)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replication)

<div></div>

    mongo::threadpool::ThreadPool::~ThreadPool()

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replication)

<div></div>

    mongo::threadpool::ThreadPool::schedule(boost::function<void ()>)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/replication)

<div></div>

    mongo::threadpool::ThreadPool::join()

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/replication)

### src/mongo/util/exception\_filter\_win32.cpp

<div></div>

    mongo::setWindowsUnhandledExceptionFilter()

- Used By:

    - [src/mongo/unittest/unittest\_main.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/dbtests.cpp](../../../../tests/unit\_tests)
