
# Interface for Delete Executor
This dependency information represents symbols that are used in this group but defined in other modules.  Does not include symbols used in this group that are defined inside this module.

### src/mongo/db/ops/delete\_executor.cpp

<div></div>

    mongo::replAllDead

- Provided By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::theReplSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    mongo::getcurns

- Provided By:

    - [src/mongo/util/log.cpp](../../../../process\_management/logging\_system)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../../../../storage/journaling)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogstreamBuilder const&)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::getRunner(mongo::Collection*, mongo::CanonicalQuery*, mongo::Runner**, unsigned long)

- Provided By:

    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::replSettings

- Provided By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::logOp(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, bool*, bool, mongo::BSONObj const*)

- Provided By:

    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::getRunner(mongo::Collection*, std::string const&, mongo::BSONObj const&, mongo::Runner**, mongo::CanonicalQuery**, unsigned long)

- Provided By:

    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Status::operator==(mongo::ErrorCodes::Error) const

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::replSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::ScopedRunnerRegistration::~ScopedRunnerRegistration()

- Provided By:

    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::LiteParsedQuery::isQueryIsolated(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/query/lite\_parsed\_query.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::ScopedRunnerRegistration::ScopedRunnerRegistration(mongo::Runner*)

- Provided By:

    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::Collection::isCapped() const

- Provided By:

    - [src/mongo/db/catalog/collection.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::Collection::deleteDocument(mongo::DiskLoc const&, bool, bool, mongo::BSONObj*)

- Provided By:

    - [src/mongo/db/catalog/collection.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::legalClientSystemNS(mongo::StringData const&, bool)

- Provided By:

    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::CanonicalQuery::isSimpleIdQuery(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/query/canonical\_query.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::CanonicalQuery::canonicalize(std::string const&, mongo::BSONObj const&, mongo::CanonicalQuery**)

- Provided By:

    - [src/mongo/db/query/canonical\_query.cpp](../../../../core\_query\_system/query\_preprocessing)
