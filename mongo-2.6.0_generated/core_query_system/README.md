# Core Query System

Query execution framework.  Handles query parsing, optimization, and execution.
TODO: High level description of the phases of query execution.

## Modules

### [Query System Commands](query\_system\_commands)
Database commands specifically for interacting with the query system.

### [Query System Parameters](query\_system\_parameters)
User facing or hard coded tunables or configuration for the query system.

### [Legacy Query Code](legacy\_query\_code)
Old query code that is gradually being phased out.

### [Query System Entry Points](query\_system\_entry\_points)
Entry points into the query system from outside the query system.  Note that there may be other things in the query system that are used elsewhere, but this is where query operations start.  For example, another query system entry point that may not be here is the update code, which also directly interacts with the query system itself.

### [Query Preprocessing](query\_preprocessing)
Classes that do processing of queries that is independent of the database state, and does not involve coming up with a plan for executing the query.  This parses the information contained in the query into a structured form that is easier to manage as well as does some normalization of the query (for example, flattening a deep tree of AND operations).

### [Query Planner](query\_planner)
This is the place where we try to make decisions that optimize query execution.  We do both static and dynamic optimization.
The static optimization involves using information we have independendently of the actual execution, such as whether a query can use an index, or whether a query can be satisfied entirely by the index keys.
The dynamic optimization involves using information about the actual execution of the query to determine what solution to use, which is done by executing multiple possible solutions and caching the best one.

### [Query Execution](query\_execution)
This handles the actual execution of a query.  This is what interacts with the indexes and the storage layer to actually fetch the stream of results.

### [Insert Operations](insert\_operations)
Code that is specific to insert operations

### [Delete Operations](delete\_operations)
Code that is specific to deletion operations

### [Update System](update\_system)
System for handling update operations against the database.  See http://docs.mongodb.org/manual/core/write-operations-introduction/ update for details about the suppported update operations.

### [Aggregation Framework](aggregation\_framework)
This is the aggregation framework for MongoDB.  It handles code to perform aggregation on a single instance as well as on a sharded cluster.
The basic operation for sharded aggregation is that the mongos does the coordination of the aggregation and makes decisions on what can be done distributed (mapped) and what must be done centralized (reduced/merged).  It then sends out the necessary aggregation commands to the appropriate places.  The distributed step is handled by the source shards that have the inital data, and the merger step is handled by the primary shard for that database.
There are various optimizations that are done as part of this process.  They are split into two categories:  Local, which rewrites the pipeline for more optimal performance on a single node, and Sharded, which rewrites and spits the pipeline for more optimal performance on the level of the whole cluster.  To see these optimizations in action, you can run "db.foo.aggregate([...], { explain : true }) from the mongo shell.  This will show how the pipeline was rewritten throughout the course of the operation.

### [Full Text Search Module](full\_text\_search\_module)
TODO: full\_text\_search\_module description

### [Geo Queries](geo\_queries)
TODO: geo\_queries description

