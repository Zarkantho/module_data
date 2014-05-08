# Build Stubs
Stubs not related to sharding but needed to make mongos link


-------------

## Storage Layer Stubs
Some code that is shared between mongos and mongod references symbols in the storage layer, which should not be built into mongos.  You should not care about this file unless you are trying to fix our build dependencies.

#### Files
- src/mongo/s/mongos\_persistence\_stubs.cpp   (mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)
