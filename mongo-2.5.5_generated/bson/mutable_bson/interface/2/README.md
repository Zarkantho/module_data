
# Interface for Mutable BSON Element
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/bson/mutable/element.cpp

<div></div>

    mongo::mutablebson::Element::pushBack(mongo::mutablebson::Element)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../../../../security/authorization)
    - [src/mongo/db/auth/authorization\_manager.cpp](../../../../security/authorization)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../../security/authorization)
    - [src/mongo/db/ops/log\_builder.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/path\_support.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../../queries/update\_system)

<div></div>

    mongo::mutablebson::Element::appendElement(mongo::BSONElement const&)

- Used By:

    - [src/mongo/db/ops/update.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../../../../queries/update\_system)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../../../../security/authorization)

<div></div>

    mongo::mutablebson::Element::appendBool(mongo::StringData const&, bool)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../../../../security/authorization)

<div></div>

    mongo::mutablebson::Element::appendString(mongo::StringData const&, mongo::StringData const&)

- Used By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../../../../security/authorization)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../../../../security/authorization)

<div></div>

    mongo::mutablebson::Element::appendObject(mongo::StringData const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../../../../security/authorization)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../../../../security/authorization)

<div></div>

    mongo::mutablebson::Element::pushFront(mongo::mutablebson::Element)

- Used By:

    - [src/mongo/db/ops/update.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/ops/update\_driver.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../../queries/update\_system)

<div></div>

    mongo::mutablebson::Element::appendNull(mongo::StringData const&)

- Used By:

    - [src/mongo/db/ops/path\_support.cpp](../../../../queries/update\_system)

<div></div>

    mongo::mutablebson::Element::toString() const

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/path\_support.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/modifier\_rename.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/update.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/modifier\_pop.cpp](../../../../queries/update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../../queries/update\_system)
