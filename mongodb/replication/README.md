# replication

# Module Groups

-------------

Replication code? TODO: verify that this is all replication related and document the architecture.   a part of this i would like to have documented is threads+locks, e.g.   heartbeats are sent in a unique thread (i think?) and maybe listened for   in a unique thread too? what threads get started if replication is being   used?

- src/mongo/db/repl/bgsync.cpp   (mongod, tools)
- src/mongo/db/repl/bgsync.h
- src/mongo/db/repl/connections.h
- src/mongo/db/repl/consensus.cpp   (mongod, tools)
- src/mongo/db/repl/health.cpp   (mongod, tools)
- src/mongo/db/repl/health.h
- src/mongo/db/repl/heartbeat.cpp   (mongod, tools)
- src/mongo/db/repl/is\_master.h
- src/mongo/db/repl/manager.cpp   (mongod, tools)
- src/mongo/db/repl/master\_slave.cpp   (mongod, tools)
- src/mongo/db/repl/master\_slave.h
- src/mongo/db/repl/multicmd.h
- src/mongo/db/repl/oplog.cpp   (mongod, tools)
- src/mongo/db/repl/oplog.h
- src/mongo/db/repl/oplogreader.cpp   (mongod, tools)
- src/mongo/db/repl/oplogreader.h
- src/mongo/db/repl/repl\_reads\_ok.cpp   (mongod, tools)
- src/mongo/db/repl/repl\_reads\_ok.h
- src/mongo/db/repl/repl\_start.cpp   (mongod, tools)
- src/mongo/db/repl/repl\_start.h
- src/mongo/db/repl/replication\_server\_status.cpp   (mongod, tools)
- src/mongo/db/repl/replication\_server\_status.h
- src/mongo/db/repl/replset\_commands.cpp   (mongod, tools)
- src/mongo/db/repl/replset\_web\_handler.cpp   (mongod)
- src/mongo/db/repl/resync.cpp   (mongod, tools)
- src/mongo/db/repl/rs.cpp   (mongod, tools)
- src/mongo/db/repl/rs.h
- src/mongo/db/repl/rs\_config.cpp   (mongod, tools)
- src/mongo/db/repl/rs\_config.h
- src/mongo/db/repl/rs\_exception.h
- src/mongo/db/repl/rs\_initialsync.cpp   (mongod, tools)
- src/mongo/db/repl/rs\_initiate.cpp   (mongod, tools)
- src/mongo/db/repl/rs\_member.h
- src/mongo/db/repl/rs\_rollback.cpp   (mongod, tools)
- src/mongo/db/repl/rs\_sync.cpp   (mongod, tools)
- src/mongo/db/repl/rs\_sync.h
- src/mongo/db/repl/sync.cpp   (mongod, tools)
- src/mongo/db/repl/sync.h
- src/mongo/db/repl/sync\_source\_feedback.cpp   (mongod, tools)
- src/mongo/db/repl/sync\_source\_feedback.h

-------------

Helpers to wait for the appropriate write concern

- src/mongo/db/write\_concern.cpp   (mongod, tools)
- src/mongo/db/write\_concern.h

-------------

Actual meat of the waiting for write concern code

- src/mongo/db/repl/write\_concern.cpp   (mongod, tools)
- src/mongo/db/repl/write\_concern.h
