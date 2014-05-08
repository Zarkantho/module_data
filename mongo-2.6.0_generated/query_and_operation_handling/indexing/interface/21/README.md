
# Interface for Index Path Set
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/index\_set.cpp

<div></div>

    mongo::IndexPathSet::clear()

- Used By:

    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::IndexPathSet::addPath(mongo::StringData const&)

- Used By:

    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::IndexPathSet::mightBeIndexed(mongo::StringData const&) const

- Used By:

    - [src/mongo/db/ops/update\_driver.cpp](../../../../core\_query\_system/update\_system)
