
# Interface for Update Driver
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/ops/update\_driver.cpp

<div></div>

    mongo::UpdateDriver::makeOplogEntryQuery(mongo::BSONObj const&, bool) const

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../../../../security/authorization)

<div></div>

    mongo::UpdateDriver::update(mongo::StringData const&, mongo::mutablebson::Document*, mongo::BSONObj*, mongo::FieldRefSet*)

- Used By:

    - [src/mongo/db/auth/role\_graph\_update.cpp](../../../../security/authorization)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../../../../security/authorization)

<div></div>

    mongo::UpdateDriver::UpdateDriver(mongo::UpdateDriver::Options const&)

- Used By:

    - [src/mongo/db/auth/role\_graph\_update.cpp](../../../../security/authorization)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../../../../security/authorization)

<div></div>

    mongo::UpdateDriver::populateDocumentWithQueryFields(mongo::BSONObj const&, mongo::mutablebson::Document&) const

- Used By:

    - [src/mongo/db/auth/role\_graph\_update.cpp](../../../../security/authorization)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../../../../security/authorization)

<div></div>

    mongo::UpdateDriver::parse(mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/db/auth/role\_graph\_update.cpp](../../../../security/authorization)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../../../../security/authorization)

<div></div>

    mongo::UpdateDriver::~UpdateDriver()

- Used By:

    - [src/mongo/db/auth/role\_graph\_update.cpp](../../../../security/authorization)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../../../../security/authorization)
