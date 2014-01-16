# javascript\_libraries

# Module Groups

-------------

v8 Javascript library files

- src/mongo/scripting/engine.cpp   (mongod, tools, mongos)
- src/mongo/scripting/engine.h
- src/mongo/scripting/engine\_v8.cpp   (mongod, tools, mongos)
- src/mongo/scripting/engine\_v8.h
- src/mongo/scripting/utils.cpp   (mongod, tools, mongos)
- src/mongo/scripting/v8\_db.cpp   (mongod, tools, mongos)
- src/mongo/scripting/v8\_db.h
- src/mongo/scripting/v8\_deadline\_monitor.h
- src/mongo/scripting/v8\_deadline\_monitor\_test.cpp   ()
- src/mongo/scripting/v8\_profiler.cpp   (mongod, tools, mongos)
- src/mongo/scripting/v8\_profiler.h
- src/mongo/scripting/v8\_utils.cpp   (mongod, tools, mongos)
- src/mongo/scripting/v8\_utils.h

## Interface


### src/mongo/scripting/engine.cpp

<pre>mongo::ScriptEngine::_checkInterruptCallback</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

<pre>mongo::globalScriptEngine</pre>

#### Used By:

- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/db/dbeval.cpp](../database\_commands)
- [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
- [src/mongo/db/matcher/expression\_where.cpp](../query\_system)
- [src/mongo/shell/dbshell.cpp](../mongo\_shell)
- [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/commands/group.cpp](../database\_commands)
- [src/mongo/dbtests/jstests.cpp](../unit\_tests)

<pre>mongo::ScriptEngine::_connectCallback</pre>

#### Used By:

- [src/mongo/shell/dbshell.cpp](../mongo\_shell)

<pre>mongo::Scope::storedFuncMod()</pre>

#### Used By:

- [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/oplog.cpp](../replication)

<pre>mongo::Scope::invoke(char const*, mongo::BSONObj const*, mongo::BSONObj const*, int)</pre>

#### Used By:

- [src/mongo/dbtests/jstests.cpp](../unit\_tests)
- [src/mongo/shell/dbshell.cpp](../mongo\_shell)

<pre>mongo::ScriptEngine::getPooledScope(std::string const&, std::string const&)</pre>

#### Used By:

- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/db/matcher/expression\_where.cpp](../query\_system)
- [src/mongo/db/dbeval.cpp](../database\_commands)
- [src/mongo/db/commands/group.cpp](../database\_commands)

<pre>mongo::ScriptEngine::_getCurrentOpIdCallback</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/scripting/engine\_v8.cpp

<pre>mongo::ScriptEngine::getInterpreterVersionString()</pre>

#### Used By:

- [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)

<pre>mongo::ScriptEngine::setup()</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/dbtests/jstests.cpp](../unit\_tests)
- [src/mongo/shell/dbshell.cpp](../mongo\_shell)

-------------

Benchrunner suite. See  https://blog.serverdensity.com/real-world-mongodb-benchmarks-with-benchrun/.

- src/mongo/scripting/bench.cpp   (mongod, tools, mongos)
- src/mongo/scripting/bench.h
- src/mongo/scripting/bson\_template\_evaluator.cpp   (mongod, tools, mongos)
- src/mongo/scripting/bson\_template\_evaluator.h
- src/mongo/scripting/bson\_template\_evaluator\_test.cpp   ()

## Interface

(not used outside this module)
