# Replication

TODO: High level description of Replication

## Modules

### [Master Slave](master\_slave)
Legacy Master/Slave implementation

### [Consensus](consensus)
Module for handling consensus between nodes of a replica set to ensure that one and only one node is the primary node.

### [Data Sync](data\_sync)
This module contains the code that replica sets use to keep the data synced between nodes.  Note that there are multiple phases.  The first stage is the initial sync, where all the data must be copied over, and the second is the stage where the node syncing the data reads the oplog and applies all operations to its local copy of the data.

### [Replica Set Configuration](replica\_set\_configuration)
Persistent confiruation of a replica set.

### [Replica Set State](replica\_set\_state)
Non persistent runtime state of a replica set.

### [Networking](networking)
Replication specific networking layer.  Reimplements some of the functionality in the network stack in a more specialized way.

### [Replication Initialization](replication\_initialization)
Code to initialize the replication subsystem

### [Replication Commands](replication\_commands)
Commands specifically related to replication

### [Replication Error Handling](replication\_error\_handling)
Replication code specific error handling mechanisms

### [Replication Web Interface](replication\_web\_interface)
Web interface to a replica set

### [Write Concern](write\_concern)
Code where we ask the user how "concerned" they are about their writes, and make sure that we only reply if their concerns have been addressed.

