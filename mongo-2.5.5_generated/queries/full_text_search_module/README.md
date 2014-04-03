# Full Text Search Module
TODO: full\_text\_search\_module description


-------------

## TODO: Name this group
Uncategorized Full Text Search Code

#### Files
- src/mongo/db/fts/fts\_command.cpp   (mongod, tools, mongos)
- src/mongo/db/fts/fts\_command.h   (mongod, tools, mongos)
- src/mongo/db/fts/fts\_command\_mongod.cpp   (mongod, tools)
- src/mongo/db/fts/fts\_command\_mongos.cpp   (mongos)
- src/mongo/db/fts/fts\_element\_iterator.cpp   (mongod, tools, mongos)
- src/mongo/db/fts/fts\_element\_iterator.h   (mongod, tools, mongos)
- src/mongo/db/fts/fts\_element\_iterator\_test.cpp   ()
- src/mongo/db/fts/fts\_enabled.cpp   (mongod, tools, mongos)
- src/mongo/db/fts/fts\_index\_format.cpp   (mongod, tools, mongos)
- src/mongo/db/fts/fts\_index\_format.h   (mongod, tools, mongos)
- src/mongo/db/fts/fts\_index\_format\_test.cpp   ()
- src/mongo/db/fts/fts\_language.cpp   (mongod, tools, mongos)
- src/mongo/db/fts/fts\_language.h   (mongod, tools, mongos)
- src/mongo/db/fts/fts\_language\_test.cpp   ()
- src/mongo/db/fts/fts\_matcher.cpp   (mongod, tools, mongos)
- src/mongo/db/fts/fts\_matcher.h   (mongod, tools, mongos)
- src/mongo/db/fts/fts\_matcher\_test.cpp   ()
- src/mongo/db/fts/fts\_query.cpp   (mongod, tools, mongos)
- src/mongo/db/fts/fts\_query.h   (mongod, tools, mongos)
- src/mongo/db/fts/fts\_query\_test.cpp   ()
- src/mongo/db/fts/fts\_spec.cpp   (mongod, tools, mongos)
- src/mongo/db/fts/fts\_spec.h   (mongod, tools, mongos)
- src/mongo/db/fts/fts\_spec\_legacy.cpp   (mongod, tools, mongos)
- src/mongo/db/fts/fts\_spec\_test.cpp   ()
- src/mongo/db/fts/fts\_util.cpp   (mongod, tools, mongos)
- src/mongo/db/fts/fts\_util.h   (mongod, tools, mongos)
- src/mongo/db/fts/fts\_util\_test.cpp   ()
- src/mongo/db/fts/stemmer.cpp   (mongod, tools, mongos)
- src/mongo/db/fts/stemmer.h   (mongod, tools, mongos)
- src/mongo/db/fts/stemmer\_test.cpp   ()
- src/mongo/db/fts/tokenizer.cpp   (mongod, tools, mongos)
- src/mongo/db/fts/tokenizer.h   (mongod, tools, mongos)
- src/mongo/db/fts/tokenizer\_test.cpp   ()

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Full Text Search Stop Words
Stop words are words that get filtered out prior to text searches.  These are words like "and" and "the" in English.  The stop words list text files get processed by the python script into auto generated C++ files.

#### Files
- src/mongo/db/fts/generate\_stop\_words.py   (mongod, tools, mongos)
- build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/fts/stop\_words\_list.cpp   (mongod, tools, mongos)
- build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/fts/stop\_words\_list.h   (mongod, tools, mongos)
- src/mongo/db/fts/stop\_words\_danish.txt   (mongod, tools, mongos)
- src/mongo/db/fts/stop\_words\_dutch.txt   (mongod, tools, mongos)
- src/mongo/db/fts/stop\_words\_english.txt   (mongod, tools, mongos)
- src/mongo/db/fts/stop\_words\_finnish.txt   (mongod, tools, mongos)
- src/mongo/db/fts/stop\_words\_french.txt   (mongod, tools, mongos)
- src/mongo/db/fts/stop\_words\_german.txt   (mongod, tools, mongos)
- src/mongo/db/fts/stop\_words\_hungarian.txt   (mongod, tools, mongos)
- src/mongo/db/fts/stop\_words\_italian.txt   (mongod, tools, mongos)
- src/mongo/db/fts/stop\_words\_norwegian.txt   (mongod, tools, mongos)
- src/mongo/db/fts/stop\_words\_portuguese.txt   (mongod, tools, mongos)
- src/mongo/db/fts/stop\_words\_romanian.txt   (mongod, tools, mongos)
- src/mongo/db/fts/stop\_words\_russian.txt   (mongod, tools, mongos)
- src/mongo/db/fts/stop\_words\_spanish.txt   (mongod, tools, mongos)
- src/mongo/db/fts/stop\_words\_swedish.txt   (mongod, tools, mongos)
- src/mongo/db/fts/stop\_words\_turkish.txt   (mongod, tools, mongos)
- src/mongo/db/fts/stop\_words.cpp   (mongod, tools, mongos)
- src/mongo/db/fts/stop\_words.h   (mongod, tools, mongos)
- src/mongo/db/fts/stop\_words\_test.cpp   ()

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)
