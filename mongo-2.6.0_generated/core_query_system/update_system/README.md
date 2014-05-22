# Update System
System for handling update operations against the database.  See http://docs.mongodb.org/manual/core/write-operations-introduction/ update for details about the suppported update operations.


-------------

## Modifier Interface
Interface that the various update modifiers implement.  Note that this includes update operators as well as document replacement.

#### Files
- [src/mongo/db/ops/modifier\_interface.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_interface.h)   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Update Modifiers
Transformations that can be applied to a document during an update

#### Files
- [src/mongo/db/ops/modifier\_add\_to\_set.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_add_to_set.cpp)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_add\_to\_set.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_add_to_set.h)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_add\_to\_set\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_add_to_set_test.cpp)   ()
- [src/mongo/db/ops/modifier\_bit.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_bit.cpp)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_bit.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_bit.h)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_bit\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_bit_test.cpp)   ()
- [src/mongo/db/ops/modifier\_compare.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_compare.cpp)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_compare.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_compare.h)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_compare\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_compare_test.cpp)   ()
- [src/mongo/db/ops/modifier\_current\_date.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_current_date.cpp)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_current\_date.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_current_date.h)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_current\_date\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_current_date_test.cpp)   ()
- [src/mongo/db/ops/modifier\_inc.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_inc.cpp)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_inc.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_inc.h)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_inc\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_inc_test.cpp)   ()
- [src/mongo/db/ops/modifier\_object\_replace.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_object_replace.cpp)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_object\_replace.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_object_replace.h)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_object\_replace\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_object_replace_test.cpp)   ()
- [src/mongo/db/ops/modifier\_pop.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_pop.cpp)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_pop.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_pop.h)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_pop\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_pop_test.cpp)   ()
- [src/mongo/db/ops/modifier\_pull.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_pull.cpp)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_pull.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_pull.h)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_pull\_all.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_pull_all.cpp)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_pull\_all.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_pull_all.h)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_pull\_all\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_pull_all_test.cpp)   ()
- [src/mongo/db/ops/modifier\_pull\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_pull_test.cpp)   ()
- [src/mongo/db/ops/modifier\_push.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_push.cpp)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_push.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_push.h)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_push\_sorter.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_push_sorter.h)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_push\_sorter\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_push_sorter_test.cpp)   ()
- [src/mongo/db/ops/modifier\_push\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_push_test.cpp)   ()
- [src/mongo/db/ops/modifier\_rename.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_rename.cpp)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_rename.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_rename.h)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_rename\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_rename_test.cpp)   ()
- [src/mongo/db/ops/modifier\_set.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_set.cpp)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_set.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_set.h)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_set\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_set_test.cpp)   ()
- [src/mongo/db/ops/modifier\_unset.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_unset.cpp)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_unset.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_unset.h)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_unset\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_unset_test.cpp)   ()

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Modifier Table
Table of all update operations that can be performed on a document, not including document replacement.  Has utilities for converting from the "$" string representation to the internal modifier classes.

#### Files
- [src/mongo/db/ops/modifier\_table.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_table.cpp)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_table.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_table.h)   (mongod, tools, mongos)
- [src/mongo/db/ops/modifier\_table\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/modifier_table_test.cpp)   ()

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Update Driver
Main entry to the portion of the update module responsible for updating individual documents based on the update expression.

#### Files
- [src/mongo/db/ops/update\_driver.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/update_driver.cpp)   (mongod, tools, mongos)
- [src/mongo/db/ops/update\_driver.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/update_driver.h)   (mongod, tools, mongos)
- [src/mongo/db/ops/update\_driver\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/update_driver_test.cpp)   ()

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Update Execution
Code that actually handles the execution of update operations.  Main entry point to the full update system.

#### Files
- [src/mongo/db/ops/update.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/update.cpp)   (mongod, tools)
- [src/mongo/db/ops/update.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/update.h)   (mongod, tools)

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## Update Oplog Entry Builder
Utility for creating properly constructed oplog entries.  This is important because update operations must be converted to an equivalent combination of idempotent operations for replication, since secondaries might apply the same oplog entry more than once.

#### Files
- [src/mongo/db/ops/log\_builder.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/log_builder.cpp)   (mongod, tools, mongos)
- [src/mongo/db/ops/log\_builder.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/log_builder.h)   (mongod, tools, mongos)
- [src/mongo/db/ops/log\_builder\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/log_builder_test.cpp)   ()

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

## Update Lifecycle
Interface to keep tabs on the state of the database that might be relevent to the operation throughout the lifetime of an update.

#### Files
- [src/mongo/db/ops/update\_lifecycle.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/update_lifecycle.h)   (mongod, tools)
- [src/mongo/db/ops/update\_lifecycle\_impl.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/update_lifecycle_impl.cpp)   (mongod, tools)
- [src/mongo/db/ops/update\_lifecycle\_impl.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/update_lifecycle_impl.h)   (mongod, tools)

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)

-------------

## Dotted Field Utilities
Utilites for managing dotted field names such as "a.b.c"

TODO: Split this up and put all shared query utilities in the same module

#### Files
- [src/mongo/db/ops/path\_support.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/path_support.cpp)   (mongod, tools, mongos)
- [src/mongo/db/ops/path\_support.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/path_support.h)   (mongod, tools, mongos)
- [src/mongo/db/ops/path\_support\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/path_support_test.cpp)   ()
- [src/mongo/db/field\_ref.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/field_ref.cpp)   (mongod, tools, mongos)
- [src/mongo/db/field\_ref.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/field_ref.h)   (mongod, tools, mongos)
- [src/mongo/db/field\_ref\_set.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/field_ref_set.cpp)   (mongod, tools, mongos)
- [src/mongo/db/field\_ref\_set.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/field_ref_set.h)   (mongod, tools, mongos)
- [src/mongo/db/field\_ref\_set\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/field_ref_set_test.cpp)   ()
- [src/mongo/db/field\_ref\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/field_ref_test.cpp)   ()
- [src/mongo/db/ops/field\_checker.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/field_checker.cpp)   (mongod, tools, mongos)
- [src/mongo/db/ops/field\_checker.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/field_checker.h)   (mongod, tools, mongos)
- [src/mongo/db/ops/field\_checker\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/field_checker_test.cpp)   ()

#### [Interface](interface/7)

#### [Dependencies](dependencies/7)

-------------

## Update Request
Parsed representation of an update request that contains all information needed to execute an update operation.

#### Files
- [src/mongo/db/ops/update\_request.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/update_request.h)   (mongod, tools)

#### [Interface](interface/8)

#### [Dependencies](dependencies/8)

-------------

## Update Executor
Class for parsing and executing an update operation.  This exists to centralize all the update execution code as well as to separate the processing and actual execution of an update request so that as much is done outside a write lock as possible.

#### Files
- [src/mongo/db/ops/update\_executor.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/update_executor.h)   (mongod, tools)
- [src/mongo/db/ops/update\_executor.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/update_executor.cpp)   (mongod, tools)

#### [Interface](interface/9)

#### [Dependencies](dependencies/9)

-------------

## Update Result
Container for all information about the results of an update operation

#### Files
- [src/mongo/db/ops/update\_result.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/ops/update_result.h)   (mongod, tools)

#### [Interface](interface/10)

#### [Dependencies](dependencies/10)
