
# Interface

### src/mongo/s/config\_upgrade.cpp

<div></div>

    mongo::checkAndUpgradeConfigVersion(mongo::ConnectionString const&, bool, mongo::VersionType*, mongo::VersionType*, std::string*)

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/s/server.cpp](../../../mongos\_and\_mongod\_mains)

<div></div>

    mongo::getConfigVersion(mongo::ConnectionString const&, mongo::VersionType*)

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
