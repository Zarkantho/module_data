# Mongos Commands
General commands available on mongos, run using db.$cmd.findOne(...)


-------------

## Mongos Admin Commands
Mongos commands that can only be run against the admin database.

#### Files
- src/mongo/s/commands\_admin.cpp   (mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Mongos Public Commands
Assorted mongos commands that do not need to be run against the admin database.  Many commands just pass through to the shards or config servers.

#### Files
- src/mongo/s/commands\_public.cpp   (mongos)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)
