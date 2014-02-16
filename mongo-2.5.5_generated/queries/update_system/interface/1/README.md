
# Interface

### src/mongo/db/ops/update\_driver.cpp

<div></div>

    mongo::UpdateDriver::populateDocumentWithQueryFields(mongo::CanonicalQuery const*, mongo::mutablebson::Document&) const

- Used By:

    - [src/mongo/db/ops/update.cpp](../core\_query\_system)

<div></div>

    mongo::UpdateDriver::modsAffectIndices() const

- Used By:

    - [src/mongo/db/ops/update.cpp](../core\_query\_system)

<div></div>

    mongo::UpdateDriver::refreshIndexKeys(mongo::IndexPathSet const*)

- Used By:

    - [src/mongo/db/ops/update.cpp](../core\_query\_system)

<div></div>

    mongo::UpdateDriver::~UpdateDriver()

- Used By:

    - [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
    - [src/mongo/db/ops/update.cpp](../core\_query\_system)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::UpdateDriver::modOptions() const

- Used By:

    - [src/mongo/db/ops/update.cpp](../core\_query\_system)

<div></div>

    mongo::UpdateDriver::makeOplogEntryQuery(mongo::BSONObj const&, bool) const

- Used By:

    - [src/mongo/db/ops/update.cpp](../core\_query\_system)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)

<div></div>

    mongo::UpdateDriver::setLogOp(bool)

- Used By:

    - [src/mongo/db/ops/update.cpp](../core\_query\_system)

<div></div>

    mongo::UpdateDriver::isDocReplacement() const

- Used By:

    - [src/mongo/db/ops/update.cpp](../core\_query\_system)

<div></div>

    mongo::UpdateDriver::UpdateDriver(mongo::UpdateDriver::Options const&)

- Used By:

    - [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
    - [src/mongo/db/ops/update.cpp](../core\_query\_system)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::UpdateDriver::parse(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
    - [src/mongo/db/ops/update.cpp](../core\_query\_system)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::UpdateDriver::setContext(mongo::ModifierInterface::ExecInfo::UpdateContext)

- Used By:

    - [src/mongo/db/ops/update.cpp](../core\_query\_system)

<div></div>

    mongo::UpdateDriver::populateDocumentWithQueryFields(mongo::BSONObj const&, mongo::mutablebson::Document&) const

- Used By:

    - [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)

<div></div>

    mongo::UpdateDriver::update(mongo::StringData const&, mongo::mutablebson::Document*, mongo::BSONObj*, mongo::FieldRefSet*)

- Used By:

    - [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
    - [src/mongo/db/ops/update.cpp](../core\_query\_system)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)
