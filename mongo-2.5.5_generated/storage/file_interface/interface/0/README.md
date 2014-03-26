
# Interface for TODO: Name this group
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/util/file.cpp

<div></div>

    mongo::File::write(unsigned long long, char const*, unsigned int)

- Used By:

    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/durop.cpp](../../../../storage/journaling)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)

<div></div>

    mongo::File::File()

- Used By:

    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/scripting/engine.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/durop.cpp](../../../../storage/journaling)
    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)

<div></div>

    mongo::File::open(char const*, bool, bool)

- Used By:

    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/scripting/engine.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/durop.cpp](../../../../storage/journaling)
    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)

<div></div>

    mongo::File::truncate(unsigned long long)

- Used By:

    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)

<div></div>

    mongo::File::~File()

- Used By:

    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/scripting/engine.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/durop.cpp](../../../../storage/journaling)
    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)

<div></div>

    mongo::File::is_open() const

- Used By:

    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/scripting/engine.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/durop.cpp](../../../../storage/journaling)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)

<div></div>

    mongo::File::freeSpace(std::string const&)

- Used By:

    - [src/mongo/db/pdfile.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)

<div></div>

    mongo::File::fsync() const

- Used By:

    - [src/mongo/db/durop.cpp](../../../../storage/journaling)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)

<div></div>

    mongo::File::len()

- Used By:

    - [src/mongo/scripting/engine.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)

<div></div>

    mongo::File::read(unsigned long long, char*, unsigned int)

- Used By:

    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/scripting/engine.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
