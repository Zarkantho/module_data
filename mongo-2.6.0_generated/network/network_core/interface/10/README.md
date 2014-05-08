
# Interface for GetLastError Data
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/lasterror.cpp

<div></div>

    mongo::LastErrorHolder::startRequest(mongo::Message&, mongo::LastError*)

- Used By:

    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::LastErrorHolder::get(bool)

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../../network/write\_commands)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/s/d\_logic.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/get\_last\_error.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::isShell

- Used By:

    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)

<div></div>

    mongo::LastErrorHolder::reset(mongo::LastError*)

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/directclienttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::LastErrorHolder::disableForCommand()

- Used By:

    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/commands/get\_last\_error.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::LastError::appendSelfStatus(mongo::BSONObjBuilder&)

- Used By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::lastError

- Used By:

    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../../network/write\_commands)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/get\_last\_error.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/s/d\_logic.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/directclienttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../../network/write\_commands)
    - [src/mongo/dbtests/updatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/s\_only.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::LastErrorHolder::release()

- Used By:

    - [src/mongo/dbtests/updatetests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::LastError::appendSelf(mongo::BSONObjBuilder&, bool)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/commands/get\_last\_error.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::LastError::noError

- Used By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::LastErrorHolder::initThread()

- Used By:

    - [src/mongo/s/s\_only.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::LastErrorHolder::_get(bool)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::setLastError(int, char const*)

- Used By:

    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../../network/write\_commands)
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../../network/write\_commands)
    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)
