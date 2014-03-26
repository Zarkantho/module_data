
# Interface for Config Upgrade
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/s/config\_upgrade.cpp

<div></div>

    mongo::checkAndUpgradeConfigVersion(mongo::ConnectionString const&, bool, mongo::VersionType*, mongo::VersionType*, std::string*)

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::getConfigVersion(mongo::ConnectionString const&, mongo::VersionType*)

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
