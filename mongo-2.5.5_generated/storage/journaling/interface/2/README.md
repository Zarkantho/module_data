
# Interface for TODO: Name this group
This interface information represents symbols thatare defined in this group but used in other modules.  Does not includesymbols defined in this group that are used inside this module.

### src/mongo/util/logfile.cpp

<div></div>

    mongo::LogFile::synchronousAppend(void const*, unsigned long)

- Used By:

    - [src/mongo/db/dbcommands\_admin.cpp](../../../queries/database\_commands)
    - [src/mongo/client/examples/mongoperf.cpp](../../../network/cpp\_client\_driver)

<div></div>

    mongo::LogFile::~LogFile()

- Used By:

    - [src/mongo/db/dbcommands\_admin.cpp](../../../queries/database\_commands)
    - [src/mongo/client/examples/mongoperf.cpp](../../../network/cpp\_client\_driver)

<div></div>

    mongo::LogFile::writeAt(unsigned long long, void const*, unsigned long)

- Used By:

    - [src/mongo/client/examples/mongoperf.cpp](../../../network/cpp\_client\_driver)

<div></div>

    mongo::LogFile::LogFile(std::string const&, bool)

- Used By:

    - [src/mongo/db/dbcommands\_admin.cpp](../../../queries/database\_commands)
    - [src/mongo/client/examples/mongoperf.cpp](../../../network/cpp\_client\_driver)

<div></div>

    mongo::LogFile::readAt(unsigned long long, void*, unsigned long)

- Used By:

    - [src/mongo/client/examples/mongoperf.cpp](../../../network/cpp\_client\_driver)
