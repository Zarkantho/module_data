
# Interface for Query Settings
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/query/query\_settings.cpp

<div></div>

    mongo::QuerySettings::clearAllowedIndices()

- Used By:

    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../../core\_query\_system/query\_system\_commands)

<div></div>

    mongo::AllowedIndexEntry::~AllowedIndexEntry()

- Used By:

    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../../core\_query\_system/query\_system\_commands)

<div></div>

    mongo::AllowedIndices::~AllowedIndices()

- Used By:

    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::QuerySettings::setAllowedIndices(mongo::CanonicalQuery const&, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const&)

- Used By:

    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../../core\_query\_system/query\_system\_commands)

<div></div>

    mongo::QuerySettings::QuerySettings()

- Used By:

    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::QuerySettings::~QuerySettings()

- Used By:

    - [src/mongo/db/catalog/collection.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::QuerySettings::removeAllowedIndices(mongo::CanonicalQuery const&)

- Used By:

    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../../core\_query\_system/query\_system\_commands)

<div></div>

    mongo::QuerySettings::getAllAllowedIndices() const

- Used By:

    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../../core\_query\_system/query\_system\_commands)

<div></div>

    mongo::QuerySettings::getAllowedIndices(mongo::CanonicalQuery const&, mongo::AllowedIndices**) const

- Used By:

    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)
