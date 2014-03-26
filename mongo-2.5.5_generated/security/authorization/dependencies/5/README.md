
# Dependencies

### src/mongo/db/auth/user\_management\_commands\_parser.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../base\_utilites)

<div></div>

    mongo::auth::createPasswordDigest(mongo::StringData const&, mongo::StringData const&)

- Provided By:

    - [src/mongo/client/auth\_helpers.cpp](../../../utilities)

<div></div>

    mongo::bsonExtractTypedField(mongo::BSONObj const&, mongo::StringData const&, mongo::BSONType, mongo::BSONElement*)

- Provided By:

    - [src/mongo/bson/util/bson\_extract.cpp](../../../bson)

<div></div>

    mongo::bsonExtractBooleanFieldWithDefault(mongo::BSONObj const&, mongo::StringData const&, bool, bool*)

- Provided By:

    - [src/mongo/bson/util/bson\_extract.cpp](../../../bson)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::bsonExtractIntegerFieldWithDefault(mongo::BSONObj const&, mongo::StringData const&, long long, long long*)

- Provided By:

    - [src/mongo/bson/util/bson\_extract.cpp](../../../bson)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::bsonExtractStringField(mongo::BSONObj const&, mongo::StringData const&, std::string*)

- Provided By:

    - [src/mongo/bson/util/bson\_extract.cpp](../../../bson)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../base\_utilites)

### src/mongo/db/commands/user\_management\_commands.cpp

<div></div>

    mongo::audit::logRevokeRolesFromRole(mongo::ClientBasic*, mongo::RoleName const&, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> > const&)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../auditing)

<div></div>

    mongo::mutablebson::Element::pushBack(mongo::mutablebson::Element)

- Provided By:

    - [src/mongo/bson/mutable/element.cpp](../../../mutable\_bson)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::audit::logDropAllRolesFromDatabase(mongo::ClientBasic*, mongo::StringData const&)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../auditing)

<div></div>

    mongo::audit::logCreateUser(mongo::ClientBasic*, mongo::UserName const&, bool, mongo::BSONObj const*, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> > const&)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../auditing)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::audit::logDropUser(mongo::ClientBasic*, mongo::UserName const&)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../auditing)

<div></div>

    vtable for mongo::Command

- Provided By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    mongo::audit::logRevokePrivilegesFromRole(mongo::ClientBasic*, mongo::RoleName const&, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> > const&)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../auditing)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

<div></div>

    mongo::mutablebson::Element::rightSibling(unsigned long) const

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../../../mutable\_bson)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../../../base\_utilites)

<div></div>

    mongo::mutablebson::Element::setValueString(mongo::StringData const&)

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../../../mutable\_bson)

<div></div>

    mongo::mutablebson::Document::~Document()

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../../../mutable\_bson)

<div></div>

    mongo::audit::logRevokeRolesFromUser(mongo::ClientBasic*, mongo::UserName const&, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> > const&)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../auditing)

<div></div>

    mongo::mutablebson::Document::makeElementObject(mongo::StringData const&)

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../../../mutable\_bson)

<div></div>

    typeinfo for mongo::Command

- Provided By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    mongo::mutablebson::Element::writeTo(mongo::BSONObjBuilder*) const

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../../../mutable\_bson)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson)

<div></div>

    mongo::audit::logDropRole(mongo::ClientBasic*, mongo::RoleName const&)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../auditing)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../utilities)

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

    mongo::audit::logCreateRole(mongo::ClientBasic*, mongo::RoleName const&, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> > const&, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> > const&)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../auditing)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../base\_utilites)

<div></div>

    mongo::audit::logDropAllUsersFromDatabase(mongo::ClientBasic*, mongo::StringData const&)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../auditing)

<div></div>

    mongo::Status::operator==(mongo::ErrorCodes::Error) const

- Provided By:

    - [src/mongo/base/status.cpp](../../../base\_utilites)

<div></div>

    mongo::mutablebson::Element::findElementNamed(mongo::StringData const&) const

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../../../mutable\_bson)

<div></div>

    mongo::audit::logGrantRolesToUser(mongo::ClientBasic*, mongo::UserName const&, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> > const&)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../auditing)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../base\_utilites)

<div></div>

    mongo::audit::logUpdateRole(mongo::ClientBasic*, mongo::RoleName const&, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> > const*, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> > const*)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../auditing)

<div></div>

    mongo::getSSLManager()

- Provided By:

    - [src/mongo/util/net/ssl\_manager.cpp](../../../ssl)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::audit::logUpdateUser(mongo::ClientBasic*, mongo::UserName const&, bool, mongo::BSONObj const*, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> > const*)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../auditing)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../../../bson)

<div></div>

    mongo::audit::logGrantRolesToRole(mongo::ClientBasic*, mongo::RoleName const&, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> > const&)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../auditing)

<div></div>

    mongo::mutablebson::Document::makeElementArray(mongo::StringData const&)

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../../../mutable\_bson)

<div></div>

    mongo::audit::logGrantPrivilegesToRole(mongo::ClientBasic*, mongo::RoleName const&, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> > const&)

- Provided By:

    - [src/mongo/db/audit.cpp](../../../auditing)

<div></div>

    mongo::mutablebson::Document::Document()

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../../../mutable\_bson)

<div></div>

    mongo::Command::parseNs(std::string const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    mongo::ClientBasic::getCurrent()

- Provided By:

    - [src/mongo/s/client\_info.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/client/clientAndShell.cpp](../../../cpp\_client\_driver)

<div></div>

    mongo::mutablebson::Element::findFirstChildNamed(mongo::StringData const&) const

- Provided By:

    - [src/mongo/bson/mutable/document.cpp](../../../mutable\_bson)

<div></div>

    mongo::Command::appendCommandStatus(mongo::BSONObjBuilder&, mongo::Status const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    mongo::Command::redactForLogging(mongo::mutablebson::Document*)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)

<div></div>

    mongo::Command::stopIndexBuilds(std::string const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)
