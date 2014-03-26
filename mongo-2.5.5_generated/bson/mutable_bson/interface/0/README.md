
# Interface

### src/mongo/bson/mutable/document.cpp

<div></div>

    mongo::mutablebson::Element::setValueSafeNum(mongo::SafeNum)

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Element::isNumeric() const

- Used By:

    - [src/mongo/db/ops/modifier\_inc.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Document::makeElementSafeNum(mongo::StringData const&, mongo::SafeNum)

- Used By:

    - [src/mongo/db/ops/log\_builder.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_bit.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Document::disableInPlaceUpdates()

- Used By:

    - [src/mongo/db/ops/update\_driver.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Document::reset()

- Used By:

    - [src/mongo/db/ops/update.cpp](../../../core\_query\_system)
    - [src/mongo/db/ops/update\_driver.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Element::isIntegral() const

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Element::leftSibling(unsigned long) const

- Used By:

    - [src/mongo/db/ops/update.cpp](../../../core\_query\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Element::compareWithElement(mongo::mutablebson::ConstElement const&, bool) const

- Used By:

    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Document::makeElementDate(mongo::StringData const&, mongo::Date_t)

- Used By:

    - [src/mongo/db/ops/modifier\_current\_date.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Document::makeElementTimestamp(mongo::StringData const&, mongo::OpTime)

- Used By:

    - [src/mongo/db/ops/modifier\_current\_date.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Document::Document()

- Used By:

    - [src/mongo/db/ops/update\_driver.cpp](../../../update\_system)
    - [src/mongo/db/auth/role\_graph\_update.cpp](../../../authorization)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../../../update\_system)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../authorization)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../../../authorization)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../../../authorization)

<div></div>

    mongo::mutablebson::Document::makeElementArray(mongo::StringData const&)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../../../authorization)
    - [src/mongo/db/auth/authorization\_manager.cpp](../../../authorization)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../authorization)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Element::getValueSafeNum() const

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Element::getValue() const

- Used By:

    - [src/mongo/db/ops/modifier\_rename.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Element::remove()

- Used By:

    - [src/mongo/db/ops/modifier\_unset.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_rename.cpp](../../../update\_system)
    - [src/mongo/db/ops/update.cpp](../../../core\_query\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_pop.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Element::rightChild() const

- Used By:

    - [src/mongo/db/ops/modifier\_pop.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Element::leftChild() const

- Used By:

    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_bit.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_rename.cpp](../../../update\_system)
    - [src/mongo/db/ops/update.cpp](../../../core\_query\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_pop.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Document::getInPlaceUpdates(std::vector<mongo::mutablebson::DamageEvent, std::allocator<mongo::mutablebson::DamageEvent> >*, char const**, unsigned long*)

- Used By:

    - [src/mongo/db/ops/update.cpp](../../../core\_query\_system)

<div></div>

    mongo::mutablebson::Element::rightSibling(unsigned long) const

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../authentication)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../../../update\_system)
    - [src/mongo/db/ops/update.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../authorization)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Document::makeElementObject(mongo::StringData const&)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../../../authorization)
    - [src/mongo/db/auth/authorization\_manager.cpp](../../../authorization)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../authorization)
    - [src/mongo/db/ops/log\_builder.cpp](../../../update\_system)
    - [src/mongo/db/ops/path\_support.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Element::writeTo(mongo::BSONObjBuilder*) const

- Used By:

    - [src/mongo/db/commands.cpp](../../../database\_commands)
    - [src/mongo/db/commands/authentication\_commands.cpp](../../../authentication)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../../../authorization)
    - [src/mongo/db/ops/update.cpp](../../../core\_query\_system)
    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/ops/update\_driver.cpp](../../../update\_system)
    - [src/mongo/db/auth/role\_graph\_update.cpp](../../../authorization)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../authorization)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../../../authorization)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Element::findFirstChildNamed(mongo::StringData const&) const

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../authentication)
    - [src/mongo/db/ops/update.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../authorization)
    - [src/mongo/db/ops/modifier\_inc.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_pop.cpp](../../../update\_system)
    - [src/mongo/db/ops/path\_support.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Document::makeElementWithNewFieldName(mongo::StringData const&, mongo::mutablebson::ConstElement)

- Used By:

    - [src/mongo/db/ops/log\_builder.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_pop.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_rename.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Element::getType() const

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_unset.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_rename.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../../../update\_system)
    - [src/mongo/db/ops/path\_support.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../update\_system)
    - [src/mongo/db/ops/update.cpp](../../../core\_query\_system)
    - [src/mongo/db/ops/modifier\_set.cpp](../../../update\_system)
    - [src/mongo/db/ops/log\_builder.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_pop.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Element::setValueTimestamp(mongo::OpTime)

- Used By:

    - [src/mongo/db/ops/modifier\_current\_date.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Element::findElementNamed(mongo::StringData const&) const

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../authentication)
    - [src/mongo/db/ops/modifier\_bit.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_rename.cpp](../../../update\_system)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../authorization)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Document::Document(mongo::BSONObj const&, mongo::mutablebson::Document::InPlaceMode)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../authentication)
    - [src/mongo/db/commands.cpp](../../../database\_commands)
    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/ops/update.cpp](../../../core\_query\_system)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../../../authorization)
    - [src/mongo/dbtests/repltests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../../../unit\_tests)

<div></div>

    mongo::mutablebson::Element::setValueString(mongo::StringData const&)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../authentication)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../authorization)

<div></div>

    mongo::mutablebson::Document::reset(mongo::BSONObj const&, mongo::mutablebson::Document::InPlaceMode)

- Used By:

    - [src/mongo/db/ops/update.cpp](../../../core\_query\_system)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../../../authorization)

<div></div>

    mongo::mutablebson::Document::makeElement(mongo::BSONElement const&)

- Used By:

    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../../../update\_system)
    - [src/mongo/db/ops/update\_driver.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Document::makeElementBool(mongo::StringData const&, bool)

- Used By:

    - [src/mongo/db/ops/log\_builder.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Document::makeElementWithNewFieldName(mongo::StringData const&, mongo::BSONElement const&)

- Used By:

    - [src/mongo/db/ops/modifier\_compare.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_rename.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_set.cpp](../../../update\_system)
    - [src/mongo/db/ops/log\_builder.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Element::compareWithBSONElement(mongo::BSONElement const&, bool) const

- Used By:

    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_compare.cpp](../../../update\_system)
    - [src/mongo/db/ops/update.cpp](../../../core\_query\_system)
    - [src/mongo/db/ops/modifier\_set.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Element::setValueDate(mongo::Date_t)

- Used By:

    - [src/mongo/db/ops/modifier\_current\_date.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Element::hasChildren() const

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../../../authorization)
    - [src/mongo/db/ops/modifier\_pull.cpp](../../../update\_system)
    - [src/mongo/db/ops/update.cpp](../../../core\_query\_system)
    - [src/mongo/db/ops/log\_builder.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_pop.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../../../update\_system)
    - [src/mongo/db/ops/path\_support.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Document::makeElementNewOID(mongo::StringData const&)

- Used By:

    - [src/mongo/db/ops/update.cpp](../../../core\_query\_system)

<div></div>

    mongo::mutablebson::Element::setValueObject(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/ops/modifier\_set.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Element::findNthChild(unsigned long) const

- Used By:

    - [src/mongo/db/ops/path\_support.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Element::parent() const

- Used By:

    - [src/mongo/db/ops/update.cpp](../../../core\_query\_system)
    - [src/mongo/db/ops/modifier\_rename.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_unset.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Element::setValueBSONElement(mongo::BSONElement const&)

- Used By:

    - [src/mongo/db/ops/modifier\_set.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_compare.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Element::setValueNull()

- Used By:

    - [src/mongo/db/ops/modifier\_unset.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Document::~Document()

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../authentication)
    - [src/mongo/db/auth/role\_graph\_update.cpp](../../../authorization)
    - [src/mongo/db/ops/update\_driver.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../../../update\_system)
    - [src/mongo/db/commands.cpp](../../../database\_commands)
    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/ops/update.cpp](../../../core\_query\_system)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../authorization)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../../../authorization)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../../../authorization)
    - [src/mongo/dbtests/repltests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../../../unit\_tests)

<div></div>

    mongo::mutablebson::Element::addSiblingRight(mongo::mutablebson::Element)

- Used By:

    - [src/mongo/db/ops/modifier\_push.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Element::getFieldName() const

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_rename.cpp](../../../update\_system)
    - [src/mongo/db/ops/update.cpp](../../../core\_query\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../../../update\_system)
    - [src/mongo/db/ops/log\_builder.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_pop.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Element::countChildren() const

- Used By:

    - [src/mongo/db/ops/path\_support.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../update\_system)

### src/mongo/bson/mutable/element.cpp

<div></div>

    mongo::mutablebson::Element::pushBack(mongo::mutablebson::Element)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../../../authorization)
    - [src/mongo/db/auth/authorization\_manager.cpp](../../../authorization)
    - [src/mongo/db/commands/user\_management\_commands.cpp](../../../authorization)
    - [src/mongo/db/ops/log\_builder.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_pull.cpp](../../../update\_system)
    - [src/mongo/db/ops/path\_support.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Element::appendElement(mongo::BSONElement const&)

- Used By:

    - [src/mongo/db/ops/update.cpp](../../../core\_query\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../../../update\_system)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../../../authorization)

<div></div>

    mongo::mutablebson::Element::appendBool(mongo::StringData const&, bool)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../../../authorization)

<div></div>

    mongo::mutablebson::Element::appendString(mongo::StringData const&, mongo::StringData const&)

- Used By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../../../authorization)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../../../authorization)

<div></div>

    mongo::mutablebson::Element::appendObject(mongo::StringData const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/auth/authorization\_manager.cpp](../../../authorization)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../../../authorization)

<div></div>

    mongo::mutablebson::Element::pushFront(mongo::mutablebson::Element)

- Used By:

    - [src/mongo/db/ops/update.cpp](../../../core\_query\_system)
    - [src/mongo/db/ops/update\_driver.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Element::appendNull(mongo::StringData const&)

- Used By:

    - [src/mongo/db/ops/path\_support.cpp](../../../update\_system)

<div></div>

    mongo::mutablebson::Element::toString() const

- Used By:

    - [src/mongo/db/ops/modifier\_bit.cpp](../../../update\_system)
    - [src/mongo/db/ops/path\_support.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_rename.cpp](../../../update\_system)
    - [src/mongo/db/ops/update.cpp](../../../core\_query\_system)
    - [src/mongo/db/ops/modifier\_inc.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_pull\_all.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_object\_replace.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_pop.cpp](../../../update\_system)
    - [src/mongo/db/ops/modifier\_push.cpp](../../../update\_system)

### src/mongo/bson/mutable/mutable\_bson\_test\_utils.cpp

<div></div>

    mongo::mutablebson::checkEqualNoOrdering(mongo::mutablebson::Document const&, mongo::mutablebson::Document const&)

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../../../unit\_tests)

<div></div>

    mongo::mutablebson::operator<<(std::ostream&, mongo::mutablebson::UnorderedWrapper_Obj const&)

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../../../unit\_tests)
