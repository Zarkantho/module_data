# update\_system

# Module Groups

-------------

# Group Description
libupdate.a (only used by libupdate\_driver.a). This is the new code for handling update  operations:   is this stuff only called from update.cpp?

## Files
- src/mongo/db/ops/modifier\_add\_to\_set.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_add\_to\_set.h   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_add\_to\_set\_test.cpp   ()
- src/mongo/db/ops/modifier\_bit.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_bit.h   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_bit\_test.cpp   ()
- src/mongo/db/ops/modifier\_compare.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_compare.h   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_compare\_test.cpp   ()
- src/mongo/db/ops/modifier\_current\_date.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_current\_date.h   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_current\_date\_test.cpp   ()
- src/mongo/db/ops/modifier\_inc.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_inc.h   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_inc\_test.cpp   ()
- src/mongo/db/ops/modifier\_interface.h   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_object\_replace.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_object\_replace.h   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_object\_replace\_test.cpp   ()
- src/mongo/db/ops/modifier\_pop.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_pop.h   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_pop\_test.cpp   ()
- src/mongo/db/ops/modifier\_pull.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_pull.h   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_pull\_all.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_pull\_all.h   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_pull\_all\_test.cpp   ()
- src/mongo/db/ops/modifier\_pull\_test.cpp   ()
- src/mongo/db/ops/modifier\_push.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_push.h   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_push\_sorter.h   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_push\_sorter\_test.cpp   ()
- src/mongo/db/ops/modifier\_push\_test.cpp   ()
- src/mongo/db/ops/modifier\_rename.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_rename.h   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_rename\_test.cpp   ()
- src/mongo/db/ops/modifier\_set.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_set.h   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_set\_test.cpp   ()
- src/mongo/db/ops/modifier\_unset.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_unset.h   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_unset\_test.cpp   ()

## [Interface](interface/0)

## [Dependencies](dependencies/0)

-------------

# Group Description
libupdate\_driver.a. This is the external interface to the new update system:

## Files
- src/mongo/db/ops/modifier\_table.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_table.h   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_table\_test.cpp   ()
- src/mongo/db/ops/update\_driver.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/update\_driver.h   (mongod, tools, mongos)
- src/mongo/db/ops/update\_driver\_test.cpp   ()

## [Interface](interface/1)

## [Dependencies](dependencies/1)

-------------

# Group Description
Utilities for the new update system (libupdate\_common.a)

## Files
- src/mongo/db/ops/path\_support.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/path\_support.h   (mongod, tools, mongos)
- src/mongo/db/ops/path\_support\_test.cpp   ()
- src/mongo/db/ops/log\_builder.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/log\_builder.h   (mongod, tools, mongos)
- src/mongo/db/ops/log\_builder\_test.cpp   ()
- src/mongo/db/ops/field\_checker.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/field\_checker.h   (mongod, tools, mongos)
- src/mongo/db/ops/field\_checker\_test.cpp   ()

## [Interface](interface/2)

## [Dependencies](dependencies/2)

-------------

# Group Description
Other things used by the update system. TODO: figure out what these are for.

## Files
- src/mongo/db/ops/update\_lifecycle.h   (mongod, tools)
- src/mongo/db/ops/update\_lifecycle\_impl.cpp   (mongod, tools)
- src/mongo/db/ops/update\_lifecycle\_impl.h   (mongod, tools)
- src/mongo/db/ops/update\_request.h   (mongod, tools)
- src/mongo/db/ops/update\_result.h   (mongod, tools)

## [Interface](interface/3)

## [Dependencies](dependencies/3)

-------------

# Group Description
Utilites for managing dotted field names such as "a.b.c". For example, has things like  "isPrefixOf".   is there any relationship between this and bson/ or bson/mutable ?

## Files
- src/mongo/db/field\_ref.cpp   (mongod, tools, mongos)
- src/mongo/db/field\_ref.h   (mongod, tools, mongos)
- src/mongo/db/field\_ref\_set.cpp   (mongod, tools, mongos)
- src/mongo/db/field\_ref\_set.h   (mongod, tools, mongos)
- src/mongo/db/field\_ref\_set\_test.cpp   ()
- src/mongo/db/field\_ref\_test.cpp   ()

## [Interface](interface/4)

## [Dependencies](dependencies/4)
