# Query And Operation Handling

Different operations that are supported in MongoDB, along with operation management code.

## Modules

### [Client And Operation Tracking](client\_and\_operation\_tracking)
This module contains the code to track and manage the state of clients and database operations.
MongoDB conflates "threads", "operations", and "connections".  This means everything gets wrapped together into a blobs of global thread local state.  Many things that will eventually have control blocks of their own are just thread local state.  For example, all the operation state and connection state is thread local, which means there is currently no good way to have multiple connections or operations handled by a single thread.
See TODO: wiki on Contexts for an introduction to more specific implementation details.

### [Concurrency](concurrency)
Concurrency management for operations on mongod as well as synchronization primitives.

### [Database Commands](database\_commands)
In the base MongoDB wire protocol, each packet has an "opCode" field that specifies what kind of operation it is.  These are things like "OP\_GET\_MORE", "OP\_QUERY", "OP\_INSERT", etc.
However, there is no "OP\_COMMAND" or anything that looks like it.  What are "Commands" then? What happens when you run "db.serverStatus()"?
Well, it turns out that commands are simply queries against the special reserved "$cmd" collection.  What this means is that "db.serverStatus()" calls "db.runCommand({serverStatus:1})" which then calls "db.$cmd.findOne({serverStatus:1})".
See TODO: wiki on Commands for more details.

### [Indexing](indexing)
TODO: indexing description

