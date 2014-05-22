
# Interface for Index Catalog
This dependency information represents symbols that are used in this group but defined in other modules.  Does not include symbols used in this group that are defined inside this module.

### src/mongo/db/catalog/index\_catalog.cpp

<div></div>

    mongo::IndexNames::findPluginName(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/index\_names.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::IndexNames::existedBefore24(std::string const&)

- Provided By:

    - [src/mongo/db/index\_names.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::FieldRef::FieldRef()

- Provided By:

    - [src/mongo/db/field\_ref.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::PregeneratedKeys::get(mongo::IndexCatalogEntry*) const

- Provided By:

    - [src/mongo/db/catalog/index\_pregen.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::TwoDAccessMethod::TwoDAccessMethod(mongo::IndexCatalogEntry*)

- Provided By:

    - [src/mongo/db/index/2d\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::LeafMatchExpression::matches(mongo::MatchableDocument const*, mongo::MatchDetails*) const

- Provided By:

    - [src/mongo/db/matcher/expression\_leaf.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::theReplSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::invariantFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    vtable for mongo::ComparisonMatchExpression

- Provided By:

    - [src/mongo/db/matcher/expression\_leaf.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::getcurns

- Provided By:

    - [src/mongo/util/log.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::ComparisonMatchExpression::equivalent(mongo::MatchExpression const*) const

- Provided By:

    - [src/mongo/db/matcher/expression\_leaf.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    typeinfo for mongo::DBException

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

    mongo::Lock::assertWriteLocked(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::HaystackAccessMethod::HaystackAccessMethod(mongo::IndexCatalogEntry*)

- Provided By:

    - [src/mongo/db/index/haystack\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::wasserted(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::IndexNames::GEO_2DSPHERE

- Provided By:

    - [src/mongo/db/index\_names.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::ComparisonMatchExpression::init(mongo::StringData const&, mongo::BSONElement const&)

- Provided By:

    - [src/mongo/db/matcher/expression\_leaf.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::WorkingSet::WorkingSet()

- Provided By:

    - [src/mongo/db/exec/working\_set.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    typeinfo for mongo::ComparisonMatchExpression

- Provided By:

    - [src/mongo/db/matcher/expression\_leaf.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::IndexLegacy::postBuildHook(mongo::Collection*, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/index\_legacy.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::HashAccessMethod::HashAccessMethod(mongo::IndexCatalogEntry*)

- Provided By:

    - [src/mongo/db/index/hash\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::validateKeyPattern(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/catalog/index\_key\_validate.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    vtable for mongo::MatchExpression

- Provided By:

    - [src/mongo/db/matcher/expression.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    vtable for mongo::LeafMatchExpression

- Provided By:

    - [src/mongo/db/matcher/expression\_leaf.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::IndexNames::HASHED

- Provided By:

    - [src/mongo/db/index\_names.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::ComparisonMatchExpression::debugString(mongo::StringBuilderImpl<mongo::TrivialAllocator>&, int) const

- Provided By:

    - [src/mongo/db/matcher/expression\_leaf.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::Lock::somethingWriteLocked()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)

<div></div>

    mongo::MatchExpression::toString() const

- Provided By:

    - [src/mongo/db/matcher/expression.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::EOFRunner::EOFRunner(mongo::CanonicalQuery*, std::string const&)

- Provided By:

    - [src/mongo/db/query/eof\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::IndexNames::TEXT

- Provided By:

    - [src/mongo/db/index\_names.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::ComparisonMatchExpression::matchesSingleElement(mongo::BSONElement const&) const

- Provided By:

    - [src/mongo/db/matcher/expression\_leaf.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::KillCurrentOp::kill(mongo::AtomicUInt)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::IndexNames::isKnownName(std::string const&)

- Provided By:

    - [src/mongo/db/index\_names.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::audit::logDropIndex(mongo::ClientBasic*, mongo::StringData const&, mongo::StringData const&)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../../security/auditing)

<div></div>

    mongo::CollectionScan::CollectionScan(mongo::CollectionScanParams const&, mongo::WorkingSet*, mongo::MatchExpression const*)

- Provided By:

    - [src/mongo/db/exec/collection\_scan.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::S2AccessMethod::S2AccessMethod(mongo::IndexCatalogEntry*)

- Provided By:

    - [src/mongo/db/index/s2\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::GeneratorHolder::getInstance()

- Provided By:

    - [src/mongo/db/catalog/index\_pregen.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    boost::this_thread::disable_interruption::~disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    mongo::MatchExpression::matchesBSON(mongo::BSONObj const&, mongo::MatchDetails*) const

- Provided By:

    - [src/mongo/db/matcher/expression.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::BtreeAccessMethod::BtreeAccessMethod(mongo::IndexCatalogEntry*)

- Provided By:

    - [src/mongo/db/index/btree\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::IndexLegacy::adjustIndexSpecObject(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/index\_legacy.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::Client::allowedToThrowPageFaultException() const

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::IndexDescriptor::areIndexOptionsEquivalent(mongo::IndexDescriptor const*) const

- Provided By:

    - [src/mongo/db/index/index\_descriptor.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::IndexNames::GEO_HAYSTACK

- Provided By:

    - [src/mongo/db/index\_names.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::FTSAccessMethod::FTSAccessMethod(mongo::IndexCatalogEntry*)

- Provided By:

    - [src/mongo/db/index/fts\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    boost::this_thread::interruption_point()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    mongo::ErrorCodes::fromInt(int)

- Provided By:

    - [build/darwin/dbg\_off/opt\_off/ssl/mongo/base/error\_codes.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::Client::Context::Context(std::string const&, mongo::Database*)

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::IndexNames::GEO_2D

- Provided By:

    - [src/mongo/db/index\_names.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::BackgroundOperation::assertNoBgOpInProgForNs(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/background.cpp](../../../../utilities/utilities)

<div></div>

    boost::this_thread::disable_interruption::disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

<div></div>

    mongo::InternalRunner::InternalRunner(mongo::Collection const*, mongo::PlanStage*, mongo::WorkingSet*)

- Provided By:

    - [src/mongo/db/query/internal\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::GeneratorHolder::reset(mongo::Collection const*)

- Provided By:

    - [src/mongo/db/catalog/index\_pregen.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::deleteObjects(mongo::StringData const&, mongo::BSONObj, bool, bool, bool)

- Provided By:

    - [src/mongo/db/ops/delete.cpp](../../../../core\_query\_system/delete\_operations)

<div></div>

    boost::detail::get_current_thread_data()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../../../../third\_party/boost\_thread)

<div></div>

    mongo::MatchExpression::MatchExpression(mongo::MatchExpression::MatchType)

- Provided By:

    - [src/mongo/db/matcher/expression.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::BSONObj::isPrefixOf(mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../../../../bson/bson)

### src/mongo/db/catalog/index\_catalog\_entry.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../../../../process\_management/logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

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

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)
