# Queries

System for handling the processing of various queries, such as full text search, geo queries, aggregation, and normal find queries.  This layer also includes the update, remove, and insert systems

## Modules

### [Client And Operation Tracking](client\_and\_operation\_tracking)
This module contains the code to track and manage the state of clients and database operations.
MongoDB conflates "threads", "operations", and "connections".  This means everything gets wrapped together into a blobs of global thread local state.  Many things that will eventually have control blocks of their own are just thread local state.  For example, all the operation state and connection state is thread local, which means there is currently no good way to have multiple connections or operations handled by a single thread.
See TODO: wiki on Contexts for an introduction to more specific implementation details.

### [Concurrency](concurrency)
TODO: concurrency description

### [Database Commands](database\_commands)
In the base MongoDB wire protocol, each packet has an "opCode" field that specifies what kind of operation it is.  These are things like "OP\_GET\_MORE", "OP\_QUERY", "OP\_INSERT", etc.
However, there is no "OP\_COMMAND" or anything that looks like it.  What are "Commands" then? What happens when you run "db.serverStatus()"?
Well, it turns out that commands are simply queries against the special reserved "$cmd" collection.  What this means is that "db.serverStatus()" calls "db.runCommand({serverStatus:1})" which then calls "db.$cmd.findOne({serverStatus:1})".
See TODO: wiki on Commands for more details.

### [Indexing](indexing)
TODO: indexing description

### [Core Query System](core\_query\_system)
TODO: core query system description

### [Update System](update\_system)
TODO: update\_system description

### [Aggregation Framework](aggregation\_framework)
This is the aggregation framework for MongoDB.  It handles code to perform aggregation on a single instance as well as on a sharded cluster.
The basic operation for sharded aggregation is that the mongos does the coordination of the aggregation and makes decisions on what can be done distributed (mapped) and what must be done centralized (reduced/merged).  It then sends out the necessary aggregation commands to the appropriate places.  The distributed step is handled by the source shards that have the inital data, and the merger step is handled by the primary shard for that database.
There are various optimizations that are done as part of this process.  They are split into two categories:  Local, which rewrites the pipeline for more optimal performance on a single node, and Sharded, which rewrites and spits the pipeline for more optimal performance on the level of the whole cluster.  To see these optimizations in action, you can run "db.foo.aggregate([...], { explain : true }) from the mongo shell.  This will show how the pipeline was rewritten throughout the course of the operation.

### [Full Text Search Module](full\_text\_search\_module)
TODO: full\_text\_search\_module description

### [Geo Queries](geo\_queries)
TODO: geo\_queries description

