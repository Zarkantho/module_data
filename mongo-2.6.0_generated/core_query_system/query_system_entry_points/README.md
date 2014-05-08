# Query System Entry Points
Entry points into the query system from outside the query system.  Note that there may be other things in the query system that are used elsewhere, but this is where query operations start.  For example, another query system entry point that may not be here is the update code, which also directly interacts with the query system itself.


-------------

## Find and getMore Entry Point
Top level entry point for find and getMore operations.  Essentially a bunch of glue that connects all the different pieces of the query system together.

#### Files
- src/mongo/db/query/new\_find.cpp   (mongod, tools)
- src/mongo/db/query/new\_find.h   (mongod, tools)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Count Command
Entry point to run the count command.  Defers actual work to the core query system.

#### Files
- src/mongo/db/ops/count.cpp   (mongod, tools)
- src/mongo/db/ops/count.h   (mongod, tools)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)
