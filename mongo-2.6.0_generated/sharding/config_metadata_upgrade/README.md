# Config Metadata Upgrade
Code to handle the versioning and upgrading of metadata on the config servers


-------------

## Config Upgrade
Code to upgrade config server metadata

#### Files
- [src/mongo/s/config\_upgrade.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/config_upgrade.cpp)   (mongos)
- [src/mongo/s/config\_upgrade.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/config_upgrade.h)   (mongos)
- [src/mongo/s/config\_upgrade\_helpers.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/config_upgrade_helpers.cpp)   (mongos)
- [src/mongo/s/config\_upgrade\_helpers.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/config_upgrade_helpers.h)   (mongos)
- [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/config_upgrade_v0_to_v5.cpp)   (mongos)
- [src/mongo/s/config\_upgrade\_v4\_to\_v5.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/config_upgrade_v4_to_v5.cpp)   (mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Version Validity Checker
Helpers to check whether a version is within a range of versions. It is used by the config metadata upgrade system to determine if the version being upgraded to is in an invalid range.

#### Files
- [src/mongo/s/mongo\_version\_range.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/mongo_version_range.cpp)   (mongod, tools, mongos)
- [src/mongo/s/mongo\_version\_range.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/mongo_version_range.h)   (mongod, tools, mongos)
- [src/mongo/s/mongo\_version\_range\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/mongo_version_range_test.cpp)   ()

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Cluster Management Utilities
Helpers for accessing the current state of a cluster.  Has helpers to get config metadata as well as helpers to check the versions of all nodes in the cluster.  Used by the config metadata upgrade system as well as the auth schema upgrade system.

#### Files
- [src/mongo/s/cluster\_client\_internal.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/cluster_client_internal.cpp)   (mongos)
- [src/mongo/s/cluster\_client\_internal.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/cluster_client_internal.h)   (mongos)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)
