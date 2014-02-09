# build\_information

# Module Groups

-------------

# Group Description
Source files that get automatically generated in each compile.  Contains functions to get things like compile flags and the Javascript interpreter version

# Files
- build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/buildinfo.cpp   (mongod, tools, mongos)
- build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/buildinfo.cpp   (mongod, tools, mongos)

# Interface

### build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/buildinfo.cpp

<div></div>

    mongo::gitVersion()

- Used By:

    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/util/version\_reporting.cpp](../utilities)
    - [src/mongo/s/version\_mongos.cpp](../sharding)
    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)

<div></div>

    mongo::allocator()

- Used By:

    - [src/mongo/util/version\_reporting.cpp](../utilities)

<div></div>

    mongo::compiledJSEngine()

- Used By:

    - [src/mongo/util/version\_reporting.cpp](../utilities)

<div></div>

    mongo::loaderFlags()

- Used By:

    - [src/mongo/util/version\_reporting.cpp](../utilities)

<div></div>

    mongo::sysInfo()

- Used By:

    - [src/mongo/util/version\_reporting.cpp](../utilities)
    - [src/mongo/s/version\_mongos.cpp](../sharding)
    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)

<div></div>

    mongo::compilerFlags()

- Used By:

    - [src/mongo/util/version\_reporting.cpp](../utilities)

# Dependencies
(no dependencies outside this module)

-------------

# Group Description
Contains the string for the current server version that gets bumped when we release, as well as code to parse it

# Files
- src/mongo/util/version.cpp   (mongod, tools, mongos)
- src/mongo/util/version.h   (mongod, tools, mongos)

# Interface

### src/mongo/util/version.cpp

<div></div>

    mongo::versionArray

- Used By:

    - [src/mongo/util/version\_reporting.cpp](../utilities)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../database\_commands)

<div></div>

    mongo::versionString

- Used By:

    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/util/version\_reporting.cpp](../utilities)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/s/version\_mongos.cpp](../sharding)
    - [src/mongo/scripting/utils.cpp](../javascript\_libraries)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/s/config\_upgrade.cpp](../sharding)
    - [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
    - [src/mongo/db/startup\_warnings.cpp](../startup\_initialization)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)

<div></div>

    mongo::toVersionArray(char const*)

- Used By:

    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../database\_commands)

<div></div>

    mongo::mongodVersion()

- Used By:

    - [src/mongo/db/log\_process\_details.cpp](../logging\_system)
    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::isSameMajorVersion(char const*)

- Used By:

    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../database\_commands)

# Dependencies

### src/mongo/util/version.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<int>(mongo::StringData const&, int, int*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)
