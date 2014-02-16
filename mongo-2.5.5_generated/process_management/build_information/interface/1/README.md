
# Interface

### src/mongo/util/version.cpp

<div></div>

    mongo::versionArray

- Used By:

    - [src/mongo/util/version\_reporting.cpp](../../../utilities)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../database\_commands)

<div></div>

    mongo::versionString

- Used By:

    - [src/mongo/tools/tool\_options.cpp](../../../tools)
    - [src/mongo/util/version\_reporting.cpp](../../../utilities)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../unit\_tests)
    - [src/mongo/s/version\_mongos.cpp](../../../sharding)
    - [src/mongo/scripting/utils.cpp](../../../javascript\_libraries)
    - [src/mongo/s/balance.cpp](../../../sharding)
    - [src/mongo/db/commands/server\_status.cpp](../../../database\_commands)
    - [src/mongo/shell/dbshell.cpp](../../../mongo\_shell)
    - [src/mongo/s/config\_upgrade.cpp](../../../sharding)
    - [src/mongo/shell/shell\_options.cpp](../../../mongo\_shell)
    - [src/mongo/db/startup\_warnings.cpp](../../../startup\_initialization)
    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)

<div></div>

    mongo::toVersionArray(char const*)

- Used By:

    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../database\_commands)

<div></div>

    mongo::mongodVersion()

- Used By:

    - [src/mongo/db/log\_process\_details.cpp](../../../logging\_system)
    - [src/mongo/db/dbwebserver.cpp](../../../web\_server)
    - [src/mongo/db/mongod\_options.cpp](../../../mongos\_and\_mongod\_mains)

<div></div>

    mongo::isSameMajorVersion(char const*)

- Used By:

    - [src/mongo/s/balance.cpp](../../../sharding)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../database\_commands)
