
# Dependencies

### src/mongo/db/commands/write\_commands/write\_commands.cpp

<div></div>

    mongo::BatchedCommandRequest::parseBSON(mongo::BSONObj const&, std::string*)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::BatchedCommandRequest::BatchedCommandRequest(mongo::BatchedCommandRequest::BatchType)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::BatchedCommandRequest::isValid(std::string*) const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::Command::appendCommandStatus(mongo::BSONObjBuilder&, mongo::Status const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    mongo::LastErrorHolder::get(bool)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../../../cpp\_client\_driver)

<div></div>

    vtable for mongo::Command

- Provided By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../../../startup\_initialization)

<div></div>

    mongo::userAllowedWriteNS(mongo::NamespaceString const&)

- Provided By:

    - [src/mongo/db/ops/insert.cpp](../../../core\_query\_system)

<div></div>

    mongo::BatchedCommandResponse::BatchedCommandResponse()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    typeinfo for mongo::Command

- Provided By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    mongo::BatchedCommandResponse::toBSON() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::Command::help(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&) const

- Provided By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::Command::Command(mongo::StringData, bool, mongo::StringData)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    mongo::BatchedCommandResponse::getOk() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    mongo::lastError

- Provided By:

    - [src/mongo/db/lasterror.cpp](../../../cpp\_client\_driver)

<div></div>

    mongo::globalOpCounters

- Provided By:

    - [src/mongo/db/stats/counters.cpp](../../../utilities)

<div></div>

    vtable for mongo::BatchedCommandRequest

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::BatchedCommandResponse::~BatchedCommandResponse()

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../../../write\_command\_schema)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../utilities)

<div></div>

    mongo::BatchedCommandRequest::getNS() const

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::Command::parseNs(std::string const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    mongo::getLastErrorDefault

- Provided By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../../../database\_commands)

<div></div>

    mongo::BatchedCommandRequest::setNS(mongo::StringData const&)

- Provided By:

    - [src/mongo/s/write\_ops/batched\_command\_request.cpp](../../../write\_command\_schema)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../../../startup\_initialization)

<div></div>

    mongo::Command::redactForLogging(mongo::mutablebson::Document*)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    mongo::Command::stopIndexBuilds(std::string const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    mongo::setLastError(int, char const*)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../../../cpp\_client\_driver)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../base\_utilites)
