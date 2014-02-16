
# Interface

### src/mongo/scripting/engine.cpp

<div></div>

    mongo::ScriptEngine::_checkInterruptCallback

- Used By:

    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)

<div></div>

    mongo::globalScriptEngine

- Used By:

    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/db/dbeval.cpp](../../../database\_commands)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../database\_commands)
    - [src/mongo/db/matcher/expression\_where.cpp](../../../core\_query\_system)
    - [src/mongo/shell/dbshell.cpp](../../../mongo\_shell)
    - [src/mongo/db/kill\_current\_op.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/group.cpp](../../../database\_commands)
    - [src/mongo/dbtests/jstests.cpp](../../../unit\_tests)

<div></div>

    mongo::ScriptEngine::_connectCallback

- Used By:

    - [src/mongo/shell/dbshell.cpp](../../../mongo\_shell)

<div></div>

    mongo::Scope::storedFuncMod()

- Used By:

    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/repl/oplog.cpp](../../../replication)

<div></div>

    mongo::Scope::invoke(char const*, mongo::BSONObj const*, mongo::BSONObj const*, int)

- Used By:

    - [src/mongo/dbtests/jstests.cpp](../../../unit\_tests)
    - [src/mongo/shell/dbshell.cpp](../../../mongo\_shell)

<div></div>

    mongo::ScriptEngine::getPooledScope(std::string const&, std::string const&)

- Used By:

    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/db/matcher/expression\_where.cpp](../../../core\_query\_system)
    - [src/mongo/db/dbeval.cpp](../../../database\_commands)
    - [src/mongo/db/commands/group.cpp](../../../database\_commands)

<div></div>

    mongo::ScriptEngine::_getCurrentOpIdCallback

- Used By:

    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)

### src/mongo/scripting/engine\_v8.cpp

<div></div>

    mongo::ScriptEngine::getInterpreterVersionString()

- Used By:

    - [src/mongo/shell/shell\_utils.cpp](../../../mongo\_shell)

<div></div>

    mongo::ScriptEngine::setup()

- Used By:

    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/jstests.cpp](../../../unit\_tests)
    - [src/mongo/shell/dbshell.cpp](../../../mongo\_shell)
