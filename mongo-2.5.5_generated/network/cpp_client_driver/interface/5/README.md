
# Interface

### src/mongo/db/lasterror.cpp

<div></div>

    mongo::LastErrorHolder::startRequest(mongo::Message&, mongo::LastError*)

- Used By:

    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/s/server.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::LastErrorHolder::get(bool)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../indexing)
    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/tools/tool.cpp](../../../tools)
    - [src/mongo/s/chunk.cpp](../../../sharding)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_create.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/commands/get\_last\_error.cpp](../../../database\_commands)
    - [src/mongo/s/d\_logic.cpp](../../../sharding)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/shardconnection.cpp](../../../sharding)

<div></div>

    mongo::isShell

- Used By:

    - [src/mongo/shell/dbshell.cpp](../../../mongo\_shell)

<div></div>

    mongo::LastErrorHolder::reset(mongo::LastError*)

- Used By:

    - [src/mongo/dbtests/directclienttests.cpp](../../../unit\_tests)
    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../../../unit\_tests)
    - [src/mongo/util/net/message\_server\_port.cpp](../../../network)
    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)
    - [src/mongo/s/s\_only.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::LastErrorHolder::disableForCommand()

- Used By:

    - [src/mongo/s/d\_state.cpp](../../../sharding)
    - [src/mongo/db/commands/get\_last\_error.cpp](../../../database\_commands)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../replication)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../replication)

<div></div>

    mongo::LastError::appendSelfStatus(mongo::BSONObjBuilder&)

- Used By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../../../database\_commands)

<div></div>

    mongo::lastError

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../replication)
    - [src/mongo/db/catalog/index\_create.cpp](../../../storage\_layer\_structure)
    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)
    - [src/mongo/s/server.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/s/d\_state.cpp](../../../sharding)
    - [src/mongo/db/commands/get\_last\_error.cpp](../../../database\_commands)
    - [src/mongo/s/shardconnection.cpp](../../../sharding)
    - [src/mongo/dbtests/directclienttests.cpp](../../../unit\_tests)
    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/util/net/message\_server\_port.cpp](../../../network)
    - [src/mongo/s/d\_logic.cpp](../../../sharding)
    - [src/mongo/s/s\_only.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../indexing)
    - [src/mongo/db/repl/replset\_commands.cpp](../../../replication)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../../../unit\_tests)
    - [src/mongo/s/chunk.cpp](../../../sharding)
    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/tools/tool.cpp](../../../tools)

<div></div>

    mongo::LastErrorHolder::release()

- Used By:

    - [src/mongo/dbtests/updatetests.cpp](../../../unit\_tests)

<div></div>

    mongo::LastError::appendSelf(mongo::BSONObjBuilder&, bool)

- Used By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../../../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)

<div></div>

    mongo::LastError::noError

- Used By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../../../database\_commands)

<div></div>

    mongo::LastErrorHolder::initThread()

- Used By:

    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../../../client\_and\_operation\_tracking)

<div></div>

    mongo::LastErrorHolder::_get(bool)

- Used By:

    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::setLastError(int, char const*)

- Used By:

    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../new\_wire\_protocol\_write\_commands)
    - [src/mongo/util/assert\_util.cpp](../../../utilities)
