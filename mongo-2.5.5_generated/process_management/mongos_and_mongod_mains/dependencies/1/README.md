
# Interface for TODO: Name this group
This dependency information represents symbols that are used in this group but defined in other modules.  Does not include symbols used in this group that are defined inside this module.

### src/mongo/db/mongod\_options.cpp

<div></div>

    mongo::addGeneralServerOptions(mongo::optionenvironment::OptionSection*)

- Provided By:

    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    mongo::_diaglog

- Provided By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::DiagLog::setLevel(int)

- Provided By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::optionenvironment::OptionDescription::hidden()

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::startupWarningsLog

- Provided By:

    - [src/mongo/util/log.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::optionenvironment::OptionDescription::setDefault(mongo::optionenvironment::Value)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::optionenvironment::startupOptions

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    vtable for mongo::MsgAssertionException

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

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::optionenvironment::Environment::operator[](std::string const&) const

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::replSettings

- Provided By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::optionenvironment::Value::get(std::string*) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::optionenvironment::OptionDescription::positional(int, int)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::logger::LogstreamBuilder::operator<<(mongo::logger::Tee*)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::optionenvironment::Environment::count(std::string const&) const

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::Record::MemoryTrackingEnabled

- Provided By:

    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::enableIPv6(bool)

- Provided By:

    - [src/mongo/util/net/sock.cpp](../../../../network/network\_core)

<div></div>

    mongo::mongodVersion()

- Provided By:

    - [src/mongo/util/version.cpp](../../../../process\_management/build\_information)

<div></div>

    mongo::optionenvironment::OptionSection::addOptionChaining(std::string const&, std::string const&, mongo::optionenvironment::OptionType, std::string const&)

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::optionenvironment::OptionSection::helpString() const

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::optionenvironment::Value::get(unsigned int*) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::addSSLServerOptions(mongo::optionenvironment::OptionSection*)

- Provided By:

    - [src/mongo/util/net/ssl\_options.cpp](../../../../network/ssl)

<div></div>

    mongo::optionenvironment::Value::get(double*) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::optionenvironment::Value::get(long*) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::optionenvironment::OptionDescription::format(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::storeServerOptions(mongo::optionenvironment::Environment const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    typeinfo for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::optionenvironment::OptionSection::addSection(mongo::optionenvironment::OptionSection const&)

- Provided By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::printGitVersion()

- Provided By:

    - [src/mongo/util/version\_reporting.cpp](../../../../utilities/utilities)

<div></div>

    mongo::optionenvironment::OptionDescription::setSources(mongo::optionenvironment::OptionSources)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::optionenvironment::Value::get(bool*) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::printOpenSSLVersion()

- Provided By:

    - [src/mongo/util/version\_reporting.cpp](../../../../utilities/utilities)

<div></div>

    mongo::optionenvironment::OptionDescription::incompatibleWith(std::string const&)

- Provided By:

    - [src/mongo/util/options\_parser/option\_description.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::getGlobalAuthorizationManager()

- Provided By:

    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../../../../security/authorization)

<div></div>

    mongo::AuthorizationManager::setAuthEnabled(bool)

- Provided By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../../../../security/authorization)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::optionenvironment::Value::get(int*) const

- Provided By:

    - [src/mongo/util/options\_parser/value.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

### src/mongo/db/mongod\_options\_init.cpp

<div></div>

    mongo::optionenvironment::startupOptionsParsed

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::optionenvironment::Environment::validate()

- Provided By:

    - [src/mongo/util/options\_parser/environment.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::optionenvironment::startupOptions

- Provided By:

    - [src/mongo/util/options\_parser/startup\_options.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../../../../process\_management/startup\_initialization)
