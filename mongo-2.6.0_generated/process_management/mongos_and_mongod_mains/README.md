# Mongos And Mongod Mains
Main functions for the mongos and mongod binaries


-------------

## Mongod Main
Main for mongod.  Contains mongod startup and shutdown code as well as the network message handler for mongod

#### Files
- src/mongo/db/db.cpp   (mongod)
- src/mongo/db/db.h   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Mongos Main
Main for mongos.  Contains mongos startup and shutdown code as well as the network message handler for mongos

#### Files
- src/mongo/s/server.cpp   (mongos)
- src/mongo/s/server.h   (mongod, tools, mongos)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)
