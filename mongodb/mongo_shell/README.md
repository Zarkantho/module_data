# mongo\_shell

# Module Groups

-------------

Javascript files that get wrapped in strings and put in cpp files. See the "env.JSHeader" calls  in src/mongo/SConscript and shell/createCPPfromJavaScriptFiles.js

- src/mongo/shell/assert.js
- src/mongo/shell/collection.js
- src/mongo/shell/db.js
- src/mongo/shell/mongo.js
- src/mongo/shell/mr.js
- src/mongo/shell/query.js
- src/mongo/shell/replsetbridge.js
- src/mongo/shell/replsettest.js
- src/mongo/shell/servers.js
- src/mongo/shell/servers\_misc.js
- src/mongo/shell/shardingtest.js
- src/mongo/shell/types.js
- src/mongo/shell/utils.js
- src/mongo/shell/utils\_sh.js
- src/mongo/shell/writes.js

## Interface

(not used outside this module)

-------------

Files only built into the mongo shell

- src/mongo/shell/dbshell.cpp   ()
- src/mongo/shell/linenoise.cpp   ()
- src/mongo/shell/linenoise.h
- src/mongo/shell/linenoise\_utf8.cpp   ()
- src/mongo/shell/linenoise\_utf8.h
- src/mongo/shell/mk\_wcwidth.cpp   ()
- src/mongo/shell/mk\_wcwidth.h
- src/mongo/shell/shell\_utils.cpp   ()
- src/mongo/shell/shell\_utils.h
- src/mongo/shell/shell\_utils\_extended.cpp   ()
- src/mongo/shell/shell\_utils\_extended.h
- src/mongo/shell/shell\_utils\_launcher.cpp   ()
- src/mongo/shell/shell\_utils\_launcher.h

## Interface

(not used outside this module)

-------------

Shell command line options

- src/mongo/shell/shell\_options.cpp   ()
- src/mongo/shell/shell\_options.h
- src/mongo/shell/shell\_options\_init.cpp   ()
- src/mongo/shell/shell\_options\_test.cpp   ()

## Interface

(not used outside this module)
