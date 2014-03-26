
# Interface for TODO: Name this group
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/lasterror.cpp

<div></div>

    mongo::LastErrorHolder::startRequest(mongo::Message&, mongo::LastError*)

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::LastErrorHolder::get(bool)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/s/chunk.cpp](../../../../sharding/sharding)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/get\_last\_error.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/d\_logic.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../../network/write\_commands)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/sharding)

<div></div>

    mongo::isShell

- Used By:

    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)

<div></div>

    mongo::LastErrorHolder::reset(mongo::LastError*)

- Used By:

    - [src/mongo/dbtests/directclienttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/util/net/message\_server\_port.cpp](../../../../network/network\_core)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/s\_only.cpp](../../../../queries/client\_and\_operation\_tracking)

<div></div>

    mongo::LastErrorHolder::disableForCommand()

- Used By:

    - [src/mongo/s/d\_state.cpp](../../../../sharding/sharding)
    - [src/mongo/db/commands/get\_last\_error.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replication)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication)

<div></div>

    mongo::LastError::appendSelfStatus(mongo::BSONObjBuilder&)

- Used By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::lastError

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replication)
    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/sharding)
    - [src/mongo/db/commands/get\_last\_error.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/sharding)
    - [src/mongo/dbtests/directclienttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/util/net/message\_server\_port.cpp](../../../../network/network\_core)
    - [src/mongo/s/d\_logic.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/s/s\_only.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/chunk.cpp](../../../../sharding/sharding)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../../network/write\_commands)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)

<div></div>

    mongo::LastErrorHolder::release()

- Used By:

    - [src/mongo/dbtests/updatetests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::LastError::appendSelf(mongo::BSONObjBuilder&, bool)

- Used By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding)

<div></div>

    mongo::LastError::noError

- Used By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::LastErrorHolder::initThread()

- Used By:

    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../../../../queries/client\_and\_operation\_tracking)

<div></div>

    mongo::LastErrorHolder::_get(bool)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::setLastError(int, char const*)

- Used By:

    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../../network/write\_commands)
    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)
