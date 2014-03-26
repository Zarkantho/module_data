
# Interface

### src/mongo/db/matcher/expression.cpp

<div></div>

    mongo::MatchExpression::toString() const

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../storage\_layer\_structure)

<div></div>

    vtable for mongo::MatchExpression

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::MatchExpression::MatchExpression(mongo::MatchExpression::MatchType)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::MatchExpression::matchesBSON(mongo::BSONObj const&, mongo::MatchDetails*) const

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../storage\_layer\_structure)

### src/mongo/db/matcher/expression\_leaf.cpp

<div></div>

    mongo::ComparisonMatchExpression::init(mongo::StringData const&, mongo::BSONElement const&)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::ComparisonMatchExpression::debugString(mongo::StringBuilderImpl<mongo::TrivialAllocator>&, int) const

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../storage\_layer\_structure)

<div></div>

    vtable for mongo::LeafMatchExpression

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::ComparisonMatchExpression::matchesSingleElement(mongo::BSONElement const&) const

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::LeafMatchExpression::matches(mongo::MatchableDocument const*, mongo::MatchDetails*) const

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::ComparisonMatchExpression::equivalent(mongo::MatchExpression const*) const

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../storage\_layer\_structure)

<div></div>

    typeinfo for mongo::ComparisonMatchExpression

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../storage\_layer\_structure)

### src/mongo/db/matcher/expression\_parser.cpp

<div></div>

    mongo::MatchExpressionParser::_parse(mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../../../authorization)
    - [src/mongo/db/ops/modifier\_pull.cpp](../../../update\_system)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../unit\_tests)
