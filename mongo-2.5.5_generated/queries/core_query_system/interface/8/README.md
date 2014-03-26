
# Interface for TODO: Name this group
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/queryutil.cpp

<div></div>

    mongo::FieldRangeVectorIterator::FieldIntervalMatcher::FieldIntervalMatcher(mongo::FieldInterval const&, mongo::BSONElement const&, bool)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FieldRange::operator|=(mongo::FieldRange const&)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::OrRangeGenerator::popOrClauseSingleKey()

- Used By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/sharding)

<div></div>

    mongo::FieldRangeSet::toString() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FieldRangeVectorIterator::prepDive()

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FieldRangeVector::FieldRangeVector(mongo::FieldRangeSet const&, mongo::BSONObj, int)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FieldRange::operator-=(mongo::FieldRange const&)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FieldInterval::toString() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FieldRangeVector::startKey() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FieldRangeVector::endKey() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FieldRangeVector::startKeyInclusive() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FieldRangeVectorIterator::FieldIntervalMatcher::upperCmp() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FieldRangeSet::subset(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::isSimpleIdQuery(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::FieldRangeVectorIterator::advance(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FieldRangeSetPair::frsForIndex(mongo::NamespaceDetails const*, int) const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FieldRange::isPointIntervalSet() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FieldRangeVectorIterator::FieldIntervalMatcher::lowerCmp() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FieldRangeSet::universalRange() const

- Used By:

    - [src/mongo/db/keypattern.cpp](../../../../queries/indexing)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/chunk.cpp](../../../../sharding/sharding)

<div></div>

    mongo::FieldRange::universal() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/chunk.cpp](../../../../sharding/sharding)

<div></div>

    mongo::FieldRangeVectorIterator::CompoundRangeCounter::CompoundRangeCounter(int, int)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FieldRangeSetPair::operator&=(mongo::FieldRangeSetPair const&)

- Used By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/sharding)

<div></div>

    mongo::FieldRangeSetPair::operator-=(mongo::FieldRangeSet const&)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FieldRangeVector::isSingleInterval() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FieldRange::toString() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FieldRangeSetPair::assertValidIndex(mongo::NamespaceDetails const*, int) const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FieldRangeSetPair::noNonUniversalRanges() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FieldRange::FieldRange(mongo::BSONElement const&, bool, bool)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FieldRange::intersect(mongo::FieldRange const&, bool)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FieldRangeVectorIterator::FieldRangeVectorIterator(mongo::FieldRangeVector const&, int)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FieldRangeSet::operator&=(mongo::FieldRangeSet const&)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FieldRangeSet::FieldRangeSet(char const*, mongo::BSONObj const&, bool, bool)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FieldRangeSet::getSpecial() const

- Used By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/sharding)

<div></div>

    mongo::FieldRangeVector::toString() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FieldRangeSet::numNonUniversalRanges() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::applySkipLimit(long long, mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding)

<div></div>

    mongo::FieldRangeVector::endKeyInclusive() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FieldRangeSet::operator-=(mongo::FieldRangeSet const&)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::FieldRangeSetPair::toString() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::OrRangeGenerator::OrRangeGenerator(char const*, mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/sharding)

<div></div>

    mongo::FieldRangeSet::prefixed(std::string const&) const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
