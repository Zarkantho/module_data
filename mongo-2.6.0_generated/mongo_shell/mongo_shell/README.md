# Mongo Shell
The mongo shell is a the v8 javascript interpreter with bindings into the C++ driver.  This is used to run javascript tests against the server


-------------

## Javascript Helper Generated Bindings
C++ files that are automatically generated from the Javascript source files. This means that certain Javascript files work in the shell because they are actually compiled in, which means that sometimes the server needs to be recompiled to see changes in Javascript files

#### Files
- build/darwin/dbg\_off/opt\_off/ssl/mongo/shell/mongo-server.cpp   ()
- build/darwin/dbg\_off/opt\_off/ssl/mongo/shell/mongo.cpp   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Shell Bulk API
Helpers for using write command bulk operations from the shell.  If write commands are not supported, it emulates the bulk operation by executing the commands one at a time using old style write operations and returns the whole result batch to the user.

#### Files
- src/mongo/shell/bulk\_api.js   (mongod, tools, mongos)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Shell Upgrade Checker
Helper to check whether the mongod version that this shell is connected to has invalid databases somehow, likely because we now disallow some bad data that we once allowed.  See http://dochub.mongodb.org/core/upgrade\_checker\_help

#### Files
- src/mongo/shell/upgrade\_check.js   (mongod, tools, mongos)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Javascript Helpers
Javascript files that get wrapped in strings and put in cpp files. See the "env.JSHeader" calls  in src/mongo/SConscript and shell/createCPPfromJavaScriptFiles.js

#### Files
- src/mongo/shell/assert.js   (mongod, tools, mongos)
- src/mongo/shell/collection.js   (mongod, tools, mongos)
- src/mongo/shell/db.js   (mongod, tools, mongos)
- src/mongo/shell/mongo.js   (mongod, tools, mongos)
- src/mongo/shell/mr.js   (mongod, tools, mongos)
- src/mongo/shell/query.js   (mongod, tools, mongos)
- src/mongo/shell/replsetbridge.js   ()
- src/mongo/shell/replsettest.js   ()
- src/mongo/shell/servers.js   ()
- src/mongo/shell/servers\_misc.js   ()
- src/mongo/shell/shardingtest.js   ()
- src/mongo/shell/types.js   (mongod, tools, mongos)
- src/mongo/shell/utils.js   (mongod, tools, mongos)
- src/mongo/shell/utils\_sh.js   (mongod, tools, mongos)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Shell Core
Files only built into the mongo shell

#### Files
- src/mongo/shell/dbshell.cpp   ()
- src/mongo/shell/linenoise.cpp   ()
- src/mongo/shell/linenoise.h   ()
- src/mongo/shell/linenoise\_utf8.cpp   ()
- src/mongo/shell/linenoise\_utf8.h   ()
- src/mongo/shell/mk\_wcwidth.cpp   ()
- src/mongo/shell/mk\_wcwidth.h   ()
- src/mongo/shell/shell\_utils.cpp   ()
- src/mongo/shell/shell\_utils.h   ()
- src/mongo/shell/shell\_utils\_extended.cpp   ()
- src/mongo/shell/shell\_utils\_extended.h   ()
- src/mongo/shell/shell\_utils\_launcher.cpp   ()
- src/mongo/shell/shell\_utils\_launcher.h   ()

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## Shell Command Line Options
Shell command line options

#### Files
- src/mongo/shell/shell\_options.cpp   ()
- src/mongo/shell/shell\_options.h   ()
- src/mongo/shell/shell\_options\_init.cpp   ()

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)
