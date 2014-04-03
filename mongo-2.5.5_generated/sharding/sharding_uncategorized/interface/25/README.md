
# Interface for Shard Version Stubs
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/s/default\_version.cpp

<div></div>

    mongo::versionManager

- Used By:

    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../../../../network/write\_commands)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/client/parallel.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::VersionManager::isVersionableCB(mongo::DBClientBase*)

- Used By:

    - [src/mongo/client/parallel.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::VersionManager::forceRemoteCheckShardVersionCB(std::string const&)

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/client/parallel.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::VersionManager::checkShardVersionCB(mongo::DBClientBase*, std::string const&, bool, int)

- Used By:

    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../../../../network/write\_commands)
    - [src/mongo/client/parallel.cpp](../../../../network/cpp\_client\_driver)
