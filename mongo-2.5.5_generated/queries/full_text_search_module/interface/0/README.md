
# Interface

### src/mongo/db/fts/fts\_index\_format.cpp

<div></div>

    mongo::fts::FTSIndexFormat::getKeys(mongo::fts::FTSSpec const&, mongo::BSONObj const&, std::set<mongo::BSONObj, mongo::BSONObjCmp, std::allocator<mongo::BSONObj> >*)

- Used By:

    - [src/mongo/db/index/fts\_access\_method.cpp](../indexing)

<div></div>

    mongo::fts::FTSIndexFormat::getIndexKey(double, std::string const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/exec/text.cpp](../core\_query\_system)

### src/mongo/db/fts/fts\_language.cpp

<div></div>

    mongo::fts::FTSLanguage::make(mongo::StringData const&, mongo::fts::TextIndexVersion)

- Used By:

    - [src/mongo/db/matcher/expression\_parser\_text.cpp](../core\_query\_system)

<div></div>

    mongo::fts::FTSLanguage::str() const

- Used By:

    - [src/mongo/db/query/stage\_builder.cpp](../core\_query\_system)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../core\_query\_system)

### src/mongo/db/fts/fts\_matcher.cpp

<div></div>

    mongo::fts::FTSMatcher::phrasesMatch(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/exec/text.cpp](../core\_query\_system)

<div></div>

    mongo::fts::FTSMatcher::FTSMatcher(mongo::fts::FTSQuery const&, mongo::fts::FTSSpec const&)

- Used By:

    - [src/mongo/db/exec/text.cpp](../core\_query\_system)

<div></div>

    mongo::fts::FTSMatcher::hasNegativeTerm(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/exec/text.cpp](../core\_query\_system)

### src/mongo/db/fts/fts\_query.cpp

<div></div>

    mongo::fts::FTSQuery::parse(std::string const&, mongo::StringData const&)

- Used By:

    - [src/mongo/db/query/stage\_builder.cpp](../core\_query\_system)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../core\_query\_system)

### src/mongo/db/fts/fts\_spec.cpp

<div></div>

    mongo::fts::FTSSpec::fixSpec(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/index\_legacy.cpp](../indexing)

<div></div>

    mongo::fts::FTSSpec::FTSSpec(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/index/fts\_access\_method.cpp](../indexing)

<div></div>

    mongo::fts::MAX_WEIGHT

- Used By:

    - [src/mongo/db/exec/text.cpp](../core\_query\_system)

<div></div>

    mongo::fts::FTSSpec::getIndexPrefix(mongo::BSONObj const&, mongo::BSONObj*) const

- Used By:

    - [src/mongo/db/query/stage\_builder.cpp](../core\_query\_system)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../core\_query\_system)

### src/mongo/db/fts/stemmer.cpp

<div></div>

    mongo::fts::Stemmer::~Stemmer()

- Used By:

    - [src/mongo/db/exec/text.cpp](../core\_query\_system)
