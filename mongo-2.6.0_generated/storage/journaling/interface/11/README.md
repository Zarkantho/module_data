
# Interface for Append Only File
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/util/logfile.cpp

<div></div>

    mongo::LogFile::LogFile(std::string const&, bool)

- Used By:

    - [src/mongo/client/examples/mongoperf.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/dbcommands\_admin.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::LogFile::readAt(unsigned long long, void*, unsigned long)

- Used By:

    - [src/mongo/client/examples/mongoperf.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::LogFile::synchronousAppend(void const*, unsigned long)

- Used By:

    - [src/mongo/client/examples/mongoperf.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/dbcommands\_admin.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::LogFile::~LogFile()

- Used By:

    - [src/mongo/client/examples/mongoperf.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/dbcommands\_admin.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::LogFile::writeAt(unsigned long long, void const*, unsigned long)

- Used By:

    - [src/mongo/client/examples/mongoperf.cpp](../../../../network/cpp\_client\_driver)
