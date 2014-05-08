
# Interface for Mongod Aggregation Commands
This dependency information represents symbols that are used in this group but defined in other modules.  Does not include symbols used in this group that are defined inside this module.

### src/mongo/db/commands/pipeline\_command.cpp

<div></div>

    mongo::Client::ReadContext::ReadContext(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::MaxBytesToReturnToClientAtOnce

- Provided By:

    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)

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

    mongo::invariantFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    vtable for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../../../../utilities/utilities)

<div></div>

    vtable for mongo::Command

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::IntrusiveCounterUnsigned::addRef() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::IntrusiveCounterUnsigned::release() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../../../../utilities/utilities)

<div></div>

    typeinfo for mongo::Command

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::InterruptStatusMongod::status

- Provided By:

    - [src/mongo/db/interrupt\_status\_mongod.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ClientCursorPin::ClientCursorPin(mongo::Collection const*, long long)

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::Command::Command(mongo::StringData, bool, mongo::StringData)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::Command::checkAuthForCommand(mongo::ClientBasic*, std::string const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::CurOp::getRemainingMaxTimeMicros() const

- Provided By:

    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::Command::stopIndexBuilds(mongo::Database*, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../../bson/bson)

<div></div>

    mongo::ClientCursorPin::c() const

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    typeinfo for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Command::parseNs(std::string const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ClientCursor::ClientCursor(mongo::Collection const*, mongo::Runner*, int, mongo::BSONObj)

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::ClientCursorPin::~ClientCursorPin()

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::Command::redactForLogging(mongo::mutablebson::Document*)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::ClientCursorPin::deleteUnderlying()

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
