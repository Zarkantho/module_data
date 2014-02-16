
# Interface

### src/mongo/util/logfile.cpp

<div></div>

    mongo::LogFile::synchronousAppend(void const*, unsigned long)

- Used By:

    - [src/mongo/db/dbcommands\_admin.cpp](../../../database\_commands)
    - [src/mongo/client/examples/mongoperf.cpp](../../../cpp\_client\_driver)

<div></div>

    mongo::LogFile::~LogFile()

- Used By:

    - [src/mongo/db/dbcommands\_admin.cpp](../../../database\_commands)
    - [src/mongo/client/examples/mongoperf.cpp](../../../cpp\_client\_driver)

<div></div>

    mongo::LogFile::writeAt(unsigned long long, void const*, unsigned long)

- Used By:

    - [src/mongo/client/examples/mongoperf.cpp](../../../cpp\_client\_driver)

<div></div>

    mongo::LogFile::LogFile(std::string const&, bool)

- Used By:

    - [src/mongo/db/dbcommands\_admin.cpp](../../../database\_commands)
    - [src/mongo/client/examples/mongoperf.cpp](../../../cpp\_client\_driver)

<div></div>

    mongo::LogFile::readAt(unsigned long long, void*, unsigned long)

- Used By:

    - [src/mongo/client/examples/mongoperf.cpp](../../../cpp\_client\_driver)
