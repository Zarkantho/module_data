# Write Concern
Code where we ask the user how "concerned" they are about their writes, and make sure that we only reply if their concerns have been addressed.


-------------

## Write Concern Checks
Main entry point to write concern checking.  Contains code to wait for the appropriate write concern to be satisfied.

#### Files
- src/mongo/db/write\_concern.cpp   (mongod, tools)
- src/mongo/db/write\_concern.h   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Write Concern Replication Checks
Implementation of replication specific write concern checks. Contains code for making sure an operation has been replicated to a certain number of nodes, but does not contain code for dealing with disk related write concern values.

#### Files
- src/mongo/db/repl/write\_concern.cpp   (mongod, tools)
- src/mongo/db/repl/write\_concern.h   (mongod, tools, mongos)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Write Concern Object Parser
Helper to parse write concern options out of a BSONObj representing a "write concern object"

#### Files
- src/mongo/db/write\_concern\_options.cpp   (mongod, tools, mongos)
- src/mongo/db/write\_concern\_options.h   (mongod, tools, mongos)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)
