# Networking
Replication specific networking layer.  Reimplements some of the functionality in the network stack in a more specialized way.


-------------

## One Per Host Connection Pool
Class to manage remote connections.  Contains only one connection per remote host, protected by a mutex.  Note that this also means only one thread can be contacting a given host at a time using this class.

#### Files
- [src/mongo/db/repl/connections.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/repl/connections.h)   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)
