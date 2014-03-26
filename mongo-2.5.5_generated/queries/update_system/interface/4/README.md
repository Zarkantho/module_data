
# Interface for TODO: Name this group
This interface information represents symbols thatare defined in this group but used in other modules.  Does not includesymbols defined in this group that are used inside this module.

### src/mongo/db/field\_ref.cpp

<div></div>

    mongo::FieldRef::FieldRef()

- Used By:

    - [src/mongo/db/matcher/expression\_geo.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/matcher/path.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/matcher/expression\_parser\_text.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/matcher/expression\_text.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/matcher/expression\_parser.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/matcher/expression\_parser\_geo.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/matcher/expression\_leaf.cpp](../../../queries/core\_query\_system)
    - [src/mongo/s/collection\_metadata.cpp](../../../sharding/sharding)
    - [src/mongo/db/matcher/expression\_array.cpp](../../../queries/core\_query\_system)

<div></div>

    mongo::FieldRef::parse(mongo::StringData const&)

- Used By:

    - [src/mongo/s/collection\_metadata.cpp](../../../sharding/sharding)
    - [src/mongo/db/matcher/path.cpp](../../../queries/core\_query\_system)

<div></div>

    mongo::FieldRef::FieldRef(mongo::StringData const&)

- Used By:

    - [src/mongo/db/fts/fts\_spec.cpp](../../../queries/full\_text\_search\_module)
    - [src/mongo/db/ops/update.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../storage/storage\_layer\_structure)

<div></div>

    mongo::FieldRef::getPart(unsigned long) const

- Used By:

    - [src/mongo/db/matcher/path\_internal.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/fts/fts\_spec.cpp](../../../queries/full\_text\_search\_module)
    - [src/mongo/db/ops/update.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/matcher/path.cpp](../../../queries/core\_query\_system)

<div></div>

    mongo::FieldRef::dottedField(unsigned long) const

- Used By:

    - [src/mongo/db/matcher/path.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/exec/keep\_mutations.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/exec/and\_sorted.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/exec/index\_scan.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/exec/or.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/exec/and\_hash.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/ops/update.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/exec/collection\_scan.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/exec/fetch.cpp](../../../queries/core\_query\_system)

<div></div>

    mongo::FieldRef::equalsDottedField(mongo::StringData const&) const

- Used By:

    - [src/mongo/db/exec/and\_hash.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/exec/fetch.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/exec/keep\_mutations.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/exec/and\_sorted.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/exec/index\_scan.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/exec/text.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/exec/2dcommon.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/exec/collection\_scan.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/exec/or.cpp](../../../queries/core\_query\_system)

### src/mongo/db/field\_ref\_set.cpp

<div></div>

    mongo::FieldRefSet::findConflicts(mongo::FieldRef const*, mongo::FieldRefSet*) const

- Used By:

    - [src/mongo/db/ops/update.cpp](../../../queries/core\_query\_system)

<div></div>

    mongo::FieldRefSet::toString() const

- Used By:

    - [src/mongo/db/ops/update.cpp](../../../queries/core\_query\_system)

<div></div>

    mongo::FieldRefSet::fillFrom(std::vector<mongo::FieldRef*, std::allocator<mongo::FieldRef*> > const&)

- Used By:

    - [src/mongo/db/ops/update.cpp](../../../queries/core\_query\_system)

<div></div>

    mongo::FieldRefSet::FieldRefSet()

- Used By:

    - [src/mongo/db/ops/update.cpp](../../../queries/core\_query\_system)

<div></div>

    mongo::FieldRefSet::keepShortest(mongo::FieldRef const*)

- Used By:

    - [src/mongo/db/ops/update.cpp](../../../queries/core\_query\_system)
