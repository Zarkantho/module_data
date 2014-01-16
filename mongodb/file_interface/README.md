# file\_interface

# Module Groups

-------------

# Group Description
Abstraction layer for dealing with files. It's basically the read(2), open(2), and write(2)  interface for posix, and something else for Windows. Not used by mmap code, and does not depend  on file allocator library. Use this if you need a file but not a memory mapped file.

# Files
- src/mongo/util/file.cpp   (cppclientdriver)
- src/mongo/util/file.h

# Interface

### src/mongo/util/file.cpp

    mongo::File::write(unsigned long long, char const*, unsigned int)

- Used By:

    - [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
    - [src/mongo/db/durop.cpp](../journaling)
    - [src/mongo/db/dur\_journal.cpp](../journaling)

    mongo::File::File()

- Used By:

    - [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/db/durop.cpp](../journaling)

    mongo::File::open(char const*, bool, bool)

- Used By:

    - [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/db/durop.cpp](../journaling)

    mongo::File::truncate(unsigned long long)

- Used By:

    - [src/mongo/db/dur\_journal.cpp](../journaling)

    mongo::File::~File()

- Used By:

    - [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/db/durop.cpp](../journaling)

    mongo::File::is_open() const

- Used By:

    - [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/db/durop.cpp](../journaling)
    - [src/mongo/db/dur\_journal.cpp](../journaling)

    mongo::File::freeSpace(std::string const&)

- Used By:

    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dur\_journal.cpp](../journaling)

    mongo::File::fsync() const

- Used By:

    - [src/mongo/db/durop.cpp](../journaling)
    - [src/mongo/db/dur\_journal.cpp](../journaling)

    mongo::File::len()

- Used By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/db/dur\_journal.cpp](../journaling)

    mongo::File::read(unsigned long long, char*, unsigned int)

- Used By:

    - [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
