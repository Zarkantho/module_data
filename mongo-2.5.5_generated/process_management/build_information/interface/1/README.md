
# Interface for Server Version Information
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/util/version.cpp

<div></div>

    mongo::versionArray

- Used By:

    - [src/mongo/util/version\_reporting.cpp](../../../../utilities/utilities)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../../security/authorization)

<div></div>

    mongo::versionString

- Used By:

    - [src/mongo/tools/tool\_options.cpp](../../../../tools/tools)
    - [src/mongo/util/version\_reporting.cpp](../../../../utilities/utilities)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/version\_mongos.cpp](../../../../sharding/sharding)
    - [src/mongo/scripting/utils.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/s/balance.cpp](../../../../sharding/sharding)
    - [src/mongo/db/commands/server\_status.cpp](../../../../queries/database\_commands)
    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/s/config\_upgrade.cpp](../../../../sharding/sharding)
    - [src/mongo/shell/shell\_options.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/startup\_warnings.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::toVersionArray(char const*)

- Used By:

    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../../security/authorization)

<div></div>

    mongo::mongodVersion()

- Used By:

    - [src/mongo/db/log\_process\_details.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::isSameMajorVersion(char const*)

- Used By:

    - [src/mongo/s/balance.cpp](../../../../sharding/sharding)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../../security/authorization)
