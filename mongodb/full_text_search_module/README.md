# full\_text\_search\_module

# Module Groups

-------------

# Group Description


# Files
- src/mongo/db/fts/fts\_command.cpp   (mongod, tools, mongos)
- src/mongo/db/fts/fts\_command.h
- src/mongo/db/fts/fts\_command\_mongod.cpp   (mongod, tools)
- src/mongo/db/fts/fts\_command\_mongos.cpp   (mongos)
- src/mongo/db/fts/fts\_enabled.cpp   (mongod, tools, mongos)
- src/mongo/db/fts/fts\_index\_format.cpp   (mongod, tools, mongos)
- src/mongo/db/fts/fts\_index\_format.h
- src/mongo/db/fts/fts\_index\_format\_test.cpp   ()
- src/mongo/db/fts/fts\_language.cpp   (mongod, tools, mongos)
- src/mongo/db/fts/fts\_language.h
- src/mongo/db/fts/fts\_language\_test.cpp   ()
- src/mongo/db/fts/fts\_matcher.cpp   (mongod, tools, mongos)
- src/mongo/db/fts/fts\_matcher.h
- src/mongo/db/fts/fts\_matcher\_test.cpp   ()
- src/mongo/db/fts/fts\_query.cpp   (mongod, tools, mongos)
- src/mongo/db/fts/fts\_query.h
- src/mongo/db/fts/fts\_query\_test.cpp   ()
- src/mongo/db/fts/fts\_spec.cpp   (mongod, tools, mongos)
- src/mongo/db/fts/fts\_spec.h
- src/mongo/db/fts/fts\_spec\_test.cpp   ()
- src/mongo/db/fts/fts\_util.cpp   (mongod, tools, mongos)
- src/mongo/db/fts/fts\_util.h
- src/mongo/db/fts/fts\_util\_test.cpp   ()
- src/mongo/db/fts/generate\_stop\_words.py
- src/mongo/db/fts/stemmer.cpp   (mongod, tools, mongos)
- src/mongo/db/fts/stemmer.h
- src/mongo/db/fts/stemmer\_test.cpp   ()
- src/mongo/db/fts/stop\_words.cpp   (mongod, tools, mongos)
- src/mongo/db/fts/stop\_words.h
- src/mongo/db/fts/stop\_words\_danish.txt
- src/mongo/db/fts/stop\_words\_dutch.txt
- src/mongo/db/fts/stop\_words\_english.txt
- src/mongo/db/fts/stop\_words\_finnish.txt
- src/mongo/db/fts/stop\_words\_french.txt
- src/mongo/db/fts/stop\_words\_german.txt
- src/mongo/db/fts/stop\_words\_hungarian.txt
- src/mongo/db/fts/stop\_words\_italian.txt
- src/mongo/db/fts/stop\_words\_norwegian.txt
- src/mongo/db/fts/stop\_words\_portuguese.txt
- src/mongo/db/fts/stop\_words\_romanian.txt
- src/mongo/db/fts/stop\_words\_russian.txt
- src/mongo/db/fts/stop\_words\_spanish.txt
- src/mongo/db/fts/stop\_words\_swedish.txt
- src/mongo/db/fts/stop\_words\_test.cpp   ()
- src/mongo/db/fts/stop\_words\_turkish.txt
- src/mongo/db/fts/tokenizer.cpp   (mongod, tools, mongos)
- src/mongo/db/fts/tokenizer.h
- src/mongo/db/fts/tokenizer\_test.cpp   ()

# Interface

### src/mongo/db/fts/fts\_command\_mongod.cpp

- <pre>mongo::fts::FTSCommand::_run(std::string const&, mongo::BSONObj&, int, std::string const&, std::string const&, std::string, int, mongo::BSONObj&, mongo::BSONObj&, std::string&, mongo::BSONObjBuilder&)</pre>
Used By:
    - [src/mongo/db/fts/fts\_command.cpp](../full\_text\_search\_module)

- <pre>vtable for mongo::fts::FTSCommand</pre>
Used By:
    - [src/mongo/db/fts/fts\_command.cpp](../full\_text\_search\_module)

### src/mongo/db/fts/fts\_command\_mongos.cpp

- <pre>mongo::fts::FTSCommand::_run(std::string const&, mongo::BSONObj&, int, std::string const&, std::string const&, std::string, int, mongo::BSONObj&, mongo::BSONObj&, std::string&, mongo::BSONObjBuilder&)</pre>
Used By:
    - [src/mongo/db/fts/fts\_command.cpp](../full\_text\_search\_module)

- <pre>vtable for mongo::fts::FTSCommand</pre>
Used By:
    - [src/mongo/db/fts/fts\_command.cpp](../full\_text\_search\_module)

- <pre>mongo::fts::FTSCommand::_run(std::string const&, mongo::BSONObj&, int, std::string const&, std::string const&, std::string, int, mongo::BSONObj&, mongo::BSONObj&, std::string&, mongo::BSONObjBuilder&)</pre>
Used By:
    - [src/mongo/db/fts/fts\_command.cpp](../full\_text\_search\_module)

- <pre>vtable for mongo::fts::FTSCommand</pre>
Used By:
    - [src/mongo/db/fts/fts\_command.cpp](../full\_text\_search\_module)

### src/mongo/db/fts/fts\_index\_format.cpp

- <pre>mongo::fts::FTSIndexFormat::getKeys(mongo::fts::FTSSpec const&, mongo::BSONObj const&, std::set<mongo::BSONObj, mongo::BSONObjCmp, std::allocator<mongo::BSONObj> >*)</pre>
Used By:
    - [src/mongo/db/index/fts\_access\_method.cpp](../indexing)

- <pre>mongo::fts::FTSIndexFormat::getIndexKey(double, std::string const&, mongo::BSONObj const&)</pre>
Used By:
    - [src/mongo/db/exec/text.cpp](../query\_system)

### src/mongo/db/fts/fts\_language.cpp

- <pre>mongo::fts::FTSLanguage::makeFTSLanguage(std::string const&)</pre>
Used By:
    - [src/mongo/db/matcher/expression\_parser\_text.cpp](../query\_system)

- <pre>mongo::fts::FTSLanguage::FTSLanguage(mongo::fts::FTSLanguage const&)</pre>
Used By:
    - [src/mongo/db/exec/text.cpp](../query\_system)
    - [src/mongo/db/query/stage\_builder.cpp](../query\_system)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)

- <pre>mongo::fts::FTSLanguage::str() const</pre>
Used By:
    - [src/mongo/db/query/stage\_builder.cpp](../query\_system)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)

- <pre>mongo::fts::FTSLanguage::operator=(mongo::fts::FTSLanguage const&)</pre>
Used By:
    - [src/mongo/db/query/stage\_builder.cpp](../query\_system)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)

- <pre>mongo::fts::FTSLanguage::~FTSLanguage()</pre>
Used By:
    - [src/mongo/db/index/fts\_access\_method.cpp](../indexing)
    - [src/mongo/db/exec/text.cpp](../query\_system)
    - [src/mongo/db/query/stage\_builder.cpp](../query\_system)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
    - [src/mongo/db/matcher/expression\_parser\_text.cpp](../query\_system)

- <pre>mongo::fts::FTSLanguage::FTSLanguage()</pre>
Used By:
    - [src/mongo/db/query/stage\_builder.cpp](../query\_system)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)

### src/mongo/db/fts/fts\_matcher.cpp

- <pre>mongo::fts::FTSMatcher::FTSMatcher(mongo::fts::FTSQuery const&, mongo::fts::FTSSpec const&)</pre>
Used By:
    - [src/mongo/db/exec/text.cpp](../query\_system)

- <pre>mongo::fts::FTSMatcher::phrasesMatch(mongo::BSONObj const&) const</pre>
Used By:
    - [src/mongo/db/exec/text.cpp](../query\_system)

- <pre>mongo::fts::FTSMatcher::hasNegativeTerm(mongo::BSONObj const&) const</pre>
Used By:
    - [src/mongo/db/exec/text.cpp](../query\_system)

### src/mongo/db/fts/fts\_query.cpp

- <pre>mongo::fts::FTSQuery::parse(std::string const&, std::string const&)</pre>
Used By:
    - [src/mongo/db/query/stage\_builder.cpp](../query\_system)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)

### src/mongo/db/fts/fts\_spec.cpp

- <pre>mongo::fts::FTSSpec::fixSpec(mongo::BSONObj const&)</pre>
Used By:
    - [src/mongo/db/index\_legacy.cpp](../indexing)

- <pre>mongo::fts::FTSSpec::FTSSpec(mongo::BSONObj const&)</pre>
Used By:
    - [src/mongo/db/index/fts\_access\_method.cpp](../indexing)

- <pre>mongo::fts::MAX_WEIGHT</pre>
Used By:
    - [src/mongo/db/exec/text.cpp](../query\_system)

- <pre>mongo::fts::FTSSpec::getIndexPrefix(mongo::BSONObj const&, mongo::BSONObj*) const</pre>
Used By:
    - [src/mongo/db/query/stage\_builder.cpp](../query\_system)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)

### src/mongo/db/fts/stemmer.cpp

- <pre>mongo::fts::Stemmer::~Stemmer()</pre>
Used By:
    - [src/mongo/db/exec/text.cpp](../query\_system)
