
# Interface for Query Index Management
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/query/index\_bounds.cpp

<div></div>

    mongo::OrderedIntervalList::isValidFor(int) const

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::IndexBoundsChecker::getStartKey(std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> >*, std::vector<bool, std::allocator<bool> >*)

- Used By:

    - [src/mongo/db/exec/index\_scan.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/distinct\_scan.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::IndexBoundsChecker::checkKey(mongo::BSONObj const&, int*, bool*, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> >*, std::vector<bool, std::allocator<bool> >*)

- Used By:

    - [src/mongo/db/exec/index\_scan.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/distinct\_scan.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::IndexBounds::toBSON() const

- Used By:

    - [src/mongo/db/exec/index\_scan.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::IndexBounds::isValidFor(mongo::BSONObj const&, int)

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::IndexBoundsChecker::IndexBoundsChecker(mongo::IndexBounds const*, mongo::BSONObj const&, int)

- Used By:

    - [src/mongo/db/exec/index\_scan.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/distinct\_scan.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/sort.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::IndexBoundsChecker::isValidKey(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/exec/sort.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::OrderedIntervalList::toString() const

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::IndexBounds::toString() const

- Used By:

    - [src/mongo/db/exec/index\_scan.cpp](../../../../core\_query\_system/query\_execution)

### src/mongo/db/query/index\_bounds\_builder.cpp

<div></div>

    mongo::IndexBoundsBuilder::makePointInterval(std::string const&)

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::IndexBoundsBuilder::makeRangeInterval(std::string const&, std::string const&, bool, bool)

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::IndexBoundsBuilder::reverseInterval(mongo::Interval*)

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::IndexBoundsBuilder::allValues()

- Used By:

    - [src/mongo/db/exec/2dcommon.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../../tests/unit\_tests)

### src/mongo/db/query/index\_tag.cpp

<div></div>

    mongo::sortUsingTags(mongo::MatchExpression*)

- Used By:

    - [src/mongo/db/query/subplan\_runner.cpp](../../../../core\_query\_system/query\_execution)
