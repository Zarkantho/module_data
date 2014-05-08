# Delete Operations
Code that is specific to deletion operations


-------------

## Legacy Delete Function
Standalone function to perform a delete operation.  Nothing more than a thin shim around the core deletion functionality.

#### Files
- src/mongo/db/ops/delete.cpp   (mongod, tools)
- src/mongo/db/ops/delete.h   (mongod, tools)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Delete Request
Parsed representation of a delete request that contains all information needed to execute a delete operation.

#### Files
- src/mongo/db/ops/delete\_request.h   (mongod, tools)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Delete Executor
Class for parsing and executing a delete operation.  This exists to centralize all the delete execution code as well as to separate the processing and actual execution of a delete request so that as much is done outside a write lock as possible.

#### Files
- src/mongo/db/ops/delete\_executor.h   (mongod, tools)
- src/mongo/db/ops/delete\_executor.cpp   (mongod, tools)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)
