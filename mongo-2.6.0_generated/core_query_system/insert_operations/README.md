# Insert Operations
Code that is specific to insert operations


-------------

## Insert Utilities
Utilities that are used for insert operations.  Includes the code that automatically fills in zero timestamps and adds the "\_id" field if it was not present.  Since inserts can happen on two different code paths, there is code that uses this in the legacy insert request handling as well as the insert write command request handling.

#### Files
- [src/mongo/db/ops/insert.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/insert.cpp)   (mongod, tools)
- [src/mongo/db/ops/insert.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/insert.h)   (mongod, tools)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)
