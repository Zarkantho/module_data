
# Interface

### src/mongo/util/safe\_num.cpp

<div></div>

    mongo::SafeNum::isIdentical(mongo::SafeNum const&) const

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)

<div></div>

    mongo::SafeNum::orInternal(mongo::SafeNum const&, mongo::SafeNum const&)

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)

<div></div>

    mongo::SafeNum::xorInternal(mongo::SafeNum const&, mongo::SafeNum const&)

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)

<div></div>

    mongo::SafeNum::andInternal(mongo::SafeNum const&, mongo::SafeNum const&)

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)

<div></div>

    mongo::SafeNum::debugString() const

- Used By:

    - [src/mongo/db/ops/log\_builder.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)

<div></div>

    mongo::SafeNum::mulInternal(mongo::SafeNum const&, mongo::SafeNum const&)

- Used By:

    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)

<div></div>

    mongo::SafeNum::SafeNum(mongo::BSONElement const&)

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)

<div></div>

    mongo::SafeNum::addInternal(mongo::SafeNum const&, mongo::SafeNum const&)

- Used By:

    - [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)

### src/mongo/util/signal\_handlers.cpp

<div></div>

    mongo::printStackAndExit(int)

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/util/stack\_introspect.cpp

<div></div>

    mongo::inConstructorChainSupported()

- Used By:

    - [src/mongo/dbtests/stacktests.cpp](../unit\_tests)

### src/mongo/util/stacktrace.cpp

<div></div>

    mongo::printStackTrace(std::ostream&)

- Used By:

    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/db/dur\_commitjob.cpp](../journaling)
    - [src/mongo/db/tests.cpp](../dead\_code)
    - [src/mongo/util/log.cpp](../logging\_system)
    - [src/mongo/db/dur\_preplogbuffer.cpp](../journaling)
    - [src/mongo/s/shardconnection.cpp](../sharding)

### src/mongo/util/startup\_test.cpp

<div></div>

    mongo::StartupTest::~StartupTest()

- Used By:

    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/db/structure/btree/key.cpp](../storage\_layer\_structure)
    - [src/mongo/bson/optime.cpp](../bson)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dur\_recover.cpp](../journaling)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/s/shardkey.cpp](../sharding)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/util/mmap\_posix.cpp](../mmap)
    - [src/mongo/db/repl/health.cpp](../replication)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/util/logfile.cpp](../journaling)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../storage\_layer\_structure)

<div></div>

    mongo::StartupTest::StartupTest()

- Used By:

    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/db/structure/btree/key.cpp](../storage\_layer\_structure)
    - [src/mongo/bson/optime.cpp](../bson)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dur\_recover.cpp](../journaling)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/s/shardkey.cpp](../sharding)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/util/mmap\_posix.cpp](../mmap)
    - [src/mongo/db/repl/health.cpp](../replication)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/util/logfile.cpp](../journaling)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../storage\_layer\_structure)

<div></div>

    mongo::StartupTest::runTests()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/dbtests.cpp](../unit\_tests)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)

<div></div>

    typeinfo for mongo::StartupTest

- Used By:

    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/db/structure/btree/key.cpp](../storage\_layer\_structure)
    - [src/mongo/bson/optime.cpp](../bson)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dur\_recover.cpp](../journaling)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../storage\_layer\_structure)
    - [src/mongo/s/shardkey.cpp](../sharding)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/util/mmap\_posix.cpp](../mmap)
    - [src/mongo/db/repl/health.cpp](../replication)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/util/logfile.cpp](../journaling)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../storage\_layer\_structure)

### src/mongo/util/stringutils.cpp

<div></div>

    mongo::versionCmp(mongo::StringData, mongo::StringData)

- Used By:

    - [src/mongo/s/mongo\_version\_range.cpp](../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/tools/restore.cpp](../tools)

<div></div>

    mongo::joinStringDelim(std::vector<std::string, std::allocator<std::string> > const&, std::string*, char)

- Used By:

    - [src/mongo/s/config.cpp](../sharding)

<div></div>

    mongo::LexNumCmp::operator()(mongo::StringData const&, mongo::StringData const&) const

- Used By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::splitStringDelim(std::string const&, std::vector<std::string, std::allocator<std::string> >*, char)

- Used By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::LexNumCmp::cmp(mongo::StringData const&, mongo::StringData const&) const

- Used By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::LexNumCmp::LexNumCmp(bool)

- Used By:

    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

### src/mongo/util/text.cpp

<div></div>

    mongo::parseLL(char const*)

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

<div></div>

    mongo::isValidUTF8(char const*)

- Used By:

    - [src/mongo/tools/bsondump.cpp](../tools)
    - [src/mongo/tools/import.cpp](../tools)
    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)

<div></div>

    mongo::StringSplitter::split(std::vector<std::string, std::allocator<std::string> >&)

- Used By:

    - [src/mongo/tools/mongoimport\_options.cpp](../tools)

<div></div>

    mongo::StringSplitter::next()

- Used By:

    - [src/mongo/tools/stat.cpp](../tools)

<div></div>

    mongo::StringSplitter::join(std::vector<std::string, std::allocator<std::string> > const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)

<div></div>

    mongo::StringSplitter::split(std::string const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)

### src/mongo/util/time\_support.cpp

<div></div>

    mongo::Date_t::toString() const

- Used By:

    - [src/mongo/s/distlock.cpp](../sharding)

<div></div>

    mongo::jsTime()

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/db/ops/modifier\_current\_date.cpp](../update\_system)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/client/gridfs.cpp](../cpp\_client\_driver)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::sleepmillis(long long)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/range\_deleter.cpp](../sharding)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/db/write\_concern.cpp](../replication)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/db/repl/resync.cpp](../replication)
    - [src/mongo/scripting/utils.cpp](../javascript\_libraries)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)
    - [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../unit\_tests)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/util/net/message\_server\_port.cpp](../network)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/util/fail\_point.cpp](../fail\_points)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/util/mmap.cpp](../mmap)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::Date_t::toTimeT() const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)

<div></div>

    mongo::Backoff::getNextSleepMillis(int, unsigned long long, unsigned long long) const

- Used By:

    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)

<div></div>

    mongo::time_t_to_Struct(long, tm*, bool)

- Used By:

    - [src/mongo/tools/stat\_util.cpp](../tools)

<div></div>

    mongo::currentDate()

- Used By:

    - [src/mongo/s/grid.cpp](../sharding)

<div></div>

    mongo::dateToISOStringLocal(mongo::Date_t)

- Used By:

    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/logger/message\_event\_utf8\_encoder.cpp](../logging\_system)

<div></div>

    mongo::dateFromISOString(mongo::StringData const&)

- Used By:

    - [src/mongo/db/json.cpp](../bson)

<div></div>

    mongo::sleepmicros(long long)

- Used By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)

<div></div>

    mongo::toPointInTime(std::string const&, boost::posix_time::ptime*)

- Used By:

    - [src/mongo/s/type\_settings.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)

<div></div>

    mongo::getJSTimeVirtualThreadSkew()

- Used By:

    - [src/mongo/s/distlock.cpp](../sharding)

<div></div>

    mongo::dateToISOStringUTC(mongo::Date_t)

- Used By:

    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
    - [src/mongo/tools/export.cpp](../tools)

<div></div>

    mongo::Backoff::nextSleepMillis()

- Used By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)

<div></div>

    mongo::time_t_to_String_short(long)

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/value.cpp](../aggregation\_framework)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/repl/health.cpp](../replication)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/tools/oplog.cpp](../tools)

<div></div>

    mongo::curTimeMicros64()

- Used By:

    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)
    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/unittest/unittest.cpp](../unit\_tests)
    - [src/mongo/db/exec/oplogstart.cpp](../core\_query\_system)
    - [src/mongo/db/write\_concern.cpp](../replication)
    - [src/mongo/dbtests/mock/mock\_dbclient\_connection.cpp](../unit\_tests)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/db/query/new\_find.cpp](../core\_query\_system)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/db/commands/geonear.cpp](../database\_commands)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/s/d\_writeback.cpp](../sharding)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)
    - [src/mongo/dbtests/mmaptests.cpp](../unit\_tests)
    - [src/mongo/db/structure/collection\_compact.cpp](../storage\_layer\_structure)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/db/repl/resync.cpp](../replication)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)
    - [src/mongo/dbtests/matchertests.cpp](../unit\_tests)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)
    - [src/mongo/db/dur\_preplogbuffer.cpp](../journaling)
    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)
    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/dur\_writetodatafiles.cpp](../journaling)
    - [src/mongo/db/clientlistplugin.cpp](../web\_server)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/s/request.cpp](../sharding)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/dbeval.cpp](../database\_commands)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/db/d\_concurrency.cpp](../concurrency)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/restapi.cpp](../web\_server)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/commands/distinct.cpp](../database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::terseCurrentTime(bool)

- Used By:

    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
    - [src/mongo/tools/top.cpp](../tools)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::sleepsecs(int)

- Used By:

    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)
    - [src/mongo/util/net/listen.cpp](../network)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../authentication)
    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/tools/top.cpp](../tools)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/db/repl/sync.cpp](../replication)
    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/s/config\_server\_checker\_service.cpp](../sharding)

<div></div>

    mongo::jsTimeVirtualThreadSkew(long long)

- Used By:

    - [src/mongo/s/distlock.cpp](../sharding)

<div></div>

    mongo::dateToCtimeString(mongo::Date_t)

- Used By:

    - [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::curTimeMicros()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::curTimeMillis64()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/repl/replset\_commands.cpp](../replication)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/d\_concurrency.cpp](../concurrency)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

### src/mongo/util/timer.cpp

<div></div>

    mongo::Timer::_countsPerSecond

- Used By:

    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/unittest/unittest.cpp](../unit\_tests)
    - [src/mongo/db/exec/oplogstart.cpp](../core\_query\_system)
    - [src/mongo/db/write\_concern.cpp](../replication)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
    - [src/mongo/dbtests/mmaptests.cpp](../unit\_tests)
    - [src/mongo/db/structure/collection\_compact.cpp](../storage\_layer\_structure)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/db/repl/resync.cpp](../replication)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)
    - [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)
    - [src/mongo/db/restapi.cpp](../web\_server)
    - [src/mongo/db/dur\_preplogbuffer.cpp](../journaling)
    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)
    - [src/mongo/db/commands.cpp](../database\_commands)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/dur\_writetodatafiles.cpp](../journaling)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/s/request.cpp](../sharding)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/dbeval.cpp](../database\_commands)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/db/d\_concurrency.cpp](../concurrency)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/dbtests/matchertests.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/commands/distinct.cpp](../database\_commands)

### src/mongo/util/touch\_pages.cpp

<div></div>

    mongo::touch_pages(char const*, unsigned long)

- Used By:

    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../database\_commands)
    - [src/mongo/db/structure/collection\_compact.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)

### src/mongo/util/util.cpp

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Used By:

    - [src/mongo/util/net/listen.cpp](../network)
    - [src/mongo/db/index/btree\_index\_cursor.cpp](../indexing)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/util/net/sock.cpp](../network)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)
    - [src/mongo/db/repl/manager.cpp](../replication)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)
    - [src/mongo/db/commands/fsync.cpp](../database\_commands)
    - [src/mongo/db/range\_deleter\_mock\_env.cpp](../sharding)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/dbtests.cpp](../unit\_tests)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../database\_commands)
    - [src/mongo/client/syncclusterconnection.cpp](../cpp\_client\_driver)
    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)
    - [src/mongo/db/range\_deleter.cpp](../sharding)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
    - [src/mongo/db/dur\_commitjob.cpp](../journaling)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/util/net/ssl\_manager.cpp](../network)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - [src/mongo/db/repl/health.cpp](../replication)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/s/commands\_admin.cpp](../sharding)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/dbtests/counttests.cpp](../unit\_tests)
    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/repl/consensus.cpp](../replication)
    - [src/mongo/util/concurrency/synchronization.cpp](../concurrency)
    - [src/mongo/db/repl/heartbeat.cpp](../replication)
    - [src/mongo/s/version\_manager.cpp](../sharding)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/s/d\_writeback.cpp](../sharding)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/util/fail\_point\_service.cpp](../fail\_points)
    - [src/mongo/s/d\_state.cpp](../sharding)
    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../storage\_layer\_structure)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/exec/fetch.cpp](../core\_query\_system)
    - [src/mongo/db/d\_concurrency.cpp](../concurrency)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/s/config\_server\_checker\_service.cpp](../sharding)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/tools/bridge.cpp](../tools)
    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/bson/optime.cpp](../bson)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dur\_recover.cpp](../journaling)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/util/concurrency/spin\_lock.cpp](../concurrency)
    - [src/mongo/db/commands/isself.cpp](../database\_commands)
    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
    - [src/mongo/s/distlock.cpp](../sharding)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)
    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/dbtests/mock/mock\_conn\_registry.cpp](../unit\_tests)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)

<div></div>

    mongo::operator<<(std::ostream&, mongo::ThreadSafeString const&)

- Used By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::hexdump(char const*, unsigned int)

- Used By:

    - [src/mongo/db/dur\_recover.cpp](../journaling)

### src/mongo/util/version\_reporting.cpp

<div></div>

    mongo::printSysInfo()

- Used By:

    - [src/mongo/db/log\_process\_details.cpp](../logging\_system)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)

<div></div>

    mongo::openSSLVersion(std::string const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/db/dbwebserver.cpp](../web\_server)
    - [src/mongo/s/version\_mongos.cpp](../sharding)

<div></div>

    mongo::appendBuildInfo(mongo::BSONObjBuilder&)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)

<div></div>

    mongo::printAllocator()

- Used By:

    - [src/mongo/db/log\_process\_details.cpp](../logging\_system)

<div></div>

    mongo::printGitVersion()

- Used By:

    - [src/mongo/db/log\_process\_details.cpp](../logging\_system)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::printOpenSSLVersion()

- Used By:

    - [src/mongo/db/log\_process\_details.cpp](../logging\_system)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/util/base64.cpp

<div></div>

    mongo::base64::chars

- Used By:

    - [src/mongo/db/json.cpp](../bson)

<div></div>

    mongo::base64::encode(std::string const&)

- Used By:

    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)

<div></div>

    mongo::base64::encode(char const*, int)

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)

<div></div>

    mongo::base64::decode(std::string const&)

- Used By:

    - [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)
    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
    - [src/mongo/db/json.cpp](../bson)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)
    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)

<div></div>

    mongo::base64::encode(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&, char const*, int)

- Used By:

    - [src/mongo/db/jsobj.cpp](../bson)
    - [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)

### src/mongo/util/compress.cpp

<div></div>

    mongo::maxCompressedLength(unsigned long)

- Used By:

    - [src/mongo/db/dur\_journal.cpp](../journaling)

<div></div>

    mongo::compress(char const*, unsigned long, std::string*)

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)

<div></div>

    mongo::uncompress(char const*, unsigned long, std::string*)

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)
    - [src/mongo/db/dur\_recover.cpp](../journaling)

<div></div>

    mongo::rawCompress(char const*, unsigned long, char*, unsigned long*)

- Used By:

    - [src/mongo/db/dur\_journal.cpp](../journaling)

### src/mongo/util/concurrency/thread\_pool.cpp

<div></div>

    mongo::threadpool::ThreadPool::ThreadPool(int)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::threadpool::ThreadPool::~ThreadPool()

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::threadpool::ThreadPool::schedule(boost::function<void ()>)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)

<div></div>

    mongo::threadpool::ThreadPool::join()

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)

### src/mongo/util/exception\_filter\_win32.cpp

<div></div>

    mongo::setWindowsUnhandledExceptionFilter()

- Used By:

    - [src/mongo/unittest/unittest\_main.cpp](../unit\_tests)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/dbtests.cpp](../unit\_tests)
