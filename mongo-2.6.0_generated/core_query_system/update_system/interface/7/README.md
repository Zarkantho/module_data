
# Interface for Dotted Field Utilities
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/field\_ref.cpp

<div></div>

    mongo::FieldRef::FieldRef()

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/matcher/expression\_parser\_geo.cpp](../../../../core\_query\_system/query\_preprocessing)
    - [src/mongo/db/matcher/expression\_parser.cpp](../../../../core\_query\_system/query\_preprocessing)
    - [src/mongo/db/matcher/expression\_array.cpp](../../../../core\_query\_system/query\_preprocessing)
    - [src/mongo/db/matcher/expression\_text.cpp](../../../../core\_query\_system/query\_preprocessing)
    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/matcher/expression\_parser\_text.cpp](../../../../core\_query\_system/query\_preprocessing)
    - [src/mongo/db/matcher/expression\_geo.cpp](../../../../core\_query\_system/query\_preprocessing)
    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)
    - [src/mongo/s/collection\_metadata.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/db/matcher/expression\_leaf.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::FieldRef::parse(mongo::StringData const&)

- Used By:

    - [src/mongo/s/collection\_metadata.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)

<div></div>

    mongo::FieldRef::FieldRef(mongo::StringData const&)

- Used By:

    - [src/mongo/db/fts/fts\_spec.cpp](../../../../core\_query\_system/full\_text\_search\_module)
    - [src/mongo/db/catalog/index\_key\_validate.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::FieldRef::getPart(unsigned long) const

- Used By:

    - [src/mongo/db/matcher/path\_internal.cpp](../../../../core\_query\_system/query\_preprocessing)
    - [src/mongo/db/fts/fts\_spec.cpp](../../../../core\_query\_system/full\_text\_search\_module)
    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)
    - [src/mongo/db/catalog/index\_key\_validate.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::FieldRef::dottedField(unsigned long) const

- Used By:

    - [src/mongo/db/exec/collection\_scan.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/fetch.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/or.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/and\_sorted.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/index\_scan.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/matcher/path.cpp](../../../../core\_query\_system/query\_preprocessing)
    - [src/mongo/db/exec/keep\_mutations.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/and\_hash.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::FieldRef::equalsDottedField(mongo::StringData const&) const

- Used By:

    - [src/mongo/db/exec/fetch.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/and\_hash.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/collection\_scan.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/index\_scan.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/text.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/and\_sorted.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/or.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/keep\_mutations.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/2dcommon.cpp](../../../../core\_query\_system/query\_execution)
