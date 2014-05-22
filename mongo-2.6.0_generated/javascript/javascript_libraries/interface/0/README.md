
# Interface for V8 Bindings
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/scripting/engine.cpp

<div></div>

    mongo::globalScriptEngine

- Used By:

    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/kill\_current\_op.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/dbeval.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/matcher/expression\_where.cpp](../../../../core\_query\_system/query\_preprocessing)
    - [src/mongo/db/commands/group.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ScriptEngine::_checkInterruptCallback

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::ScriptEngine::_connectCallback

- Used By:

    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)

<div></div>

    mongo::Scope::invoke(char const*, mongo::BSONObj const*, mongo::BSONObj const*, int)

- Used By:

    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::ScriptEngine::_getCurrentOpIdCallback

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::Scope::storedFuncMod()

- Used By:

    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::ScriptEngine::getPooledScope(std::string const&, std::string const&)

- Used By:

    - [src/mongo/db/matcher/expression\_where.cpp](../../../../core\_query\_system/query\_preprocessing)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/group.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/dbeval.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::directDBClient

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

### src/mongo/scripting/engine\_v8.cpp

<div></div>

    mongo::ScriptEngine::setup()

- Used By:

    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::ScriptEngine::getInterpreterVersionString()

- Used By:

    - [src/mongo/shell/shell\_utils.cpp](../../../../mongo\_shell/mongo\_shell)
