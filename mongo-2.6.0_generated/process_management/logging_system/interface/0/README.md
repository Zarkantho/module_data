
# Interface for Log System Interface
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/util/log.cpp

<div></div>

    mongo::rotateLogs()

- Used By:

    - [src/mongo/util/signal\_handlers.cpp](../../../../utilities/utilities)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::tlogLevel

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/index\_stats.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)
    - [src/mongo/dbtests/framework.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/validate.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/storage\_details.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::getcurns

- Used By:

    - [src/mongo/db/ops/delete\_executor.cpp](../../../../core\_query\_system/delete\_operations)
    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/client/dbclientcursor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/util/mmap\_posix.cpp](../../../../storage/data\_files)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/pipeline/document\_source\_out.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/structure/btree/btreebuilder.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/util/mmap.cpp](../../../../storage/data\_files)
    - [src/mongo/db/extsort.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/dbtests/counttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/util/net/message\_port.cpp](../../../../network/network\_core)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::startupWarningsLog

- Used By:

    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/db/startup\_warnings.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/db/fts/fts\_command.cpp](../../../../core\_query\_system/full\_text\_search\_module)

<div></div>

    mongo::LogIndentLevel::~LogIndentLevel()

- Used By:

    - [src/mongo/tools/dump.cpp](../../../../tools/tools)

<div></div>

    mongo::warnings

- Used By:

    - [src/mongo/util/net/listen.cpp](../../../../network/network\_core)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::LogIndentLevel::LogIndentLevel()

- Used By:

    - [src/mongo/tools/dump.cpp](../../../../tools/tools)

<div></div>

    mongo::logContext(char const*)

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)

<div></div>

    mongo::errnoWithDescription(int)

- Used By:

    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)
    - [src/mongo/util/net/listen.cpp](../../../../network/network\_core)
    - [src/mongo/util/logfile.cpp](../../../../storage/journaling)
    - [src/mongo/util/mmap\_posix.cpp](../../../../storage/data\_files)
    - [src/mongo/db/commands/isself.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/util/password.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/db/startup\_warnings.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/util/processinfo\_darwin.cpp](../../../../utilities/utilities)
    - [src/mongo/util/file.cpp](../../../../storage/file\_interface)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/util/net/ssl\_manager.cpp](../../../../network/ssl)
    - [src/mongo/util/stacktrace.cpp](../../../../utilities/utilities)
    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/dbtests/jsontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/util/net/sock.cpp](../../../../network/network\_core)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/db/dbcommands\_admin.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/util/file\_allocator.cpp](../../../../storage/file\_allocation)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../../process\_management/startup\_initialization)
