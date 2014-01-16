# file\_interface

# Module Groups

-------------

Abstraction layer for dealing with files. It's basically the read(2), open(2), and write(2)  interface for posix, and something else for Windows. Not used by mmap code, and does not depend  on file allocator library. Use this if you need a file but not a memory mapped file.

- src/mongo/util/file.cpp   (cppclientdriver)
- src/mongo/util/file.h

## Interface
### src/mongo/util/file.cpp
<pre>mongo::File::write(unsigned long long, char const*, unsigned int)</pre>
#### Used By:
- [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
- [src/mongo/db/durop.cpp](../journaling)
- [src/mongo/db/dur\_journal.cpp](../journaling)

<pre>mongo::File::File()</pre>
#### Used By:
- [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
- [src/mongo/scripting/engine.cpp](../javascript\_libraries)
- [src/mongo/db/dur\_journal.cpp](../journaling)
- [src/mongo/shell/dbshell.cpp](../mongo\_shell)
- [src/mongo/db/durop.cpp](../journaling)

<pre>mongo::File::open(char const*, bool, bool)</pre>
#### Used By:
- [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
- [src/mongo/scripting/engine.cpp](../javascript\_libraries)
- [src/mongo/db/dur\_journal.cpp](../journaling)
- [src/mongo/shell/dbshell.cpp](../mongo\_shell)
- [src/mongo/db/durop.cpp](../journaling)

<pre>mongo::File::truncate(unsigned long long)</pre>
#### Used By:
- [src/mongo/db/dur\_journal.cpp](../journaling)

<pre>mongo::File::~File()</pre>
#### Used By:
- [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
- [src/mongo/scripting/engine.cpp](../javascript\_libraries)
- [src/mongo/db/dur\_journal.cpp](../journaling)
- [src/mongo/shell/dbshell.cpp](../mongo\_shell)
- [src/mongo/db/durop.cpp](../journaling)

<pre>mongo::File::is_open() const</pre>
#### Used By:
- [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
- [src/mongo/scripting/engine.cpp](../javascript\_libraries)
- [src/mongo/db/durop.cpp](../journaling)
- [src/mongo/db/dur\_journal.cpp](../journaling)

<pre>mongo::File::freeSpace(std::string const&)</pre>
#### Used By:
- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/db/dur\_journal.cpp](../journaling)

<pre>mongo::File::fsync() const</pre>
#### Used By:
- [src/mongo/db/durop.cpp](../journaling)
- [src/mongo/db/dur\_journal.cpp](../journaling)

<pre>mongo::File::len()</pre>
#### Used By:
- [src/mongo/scripting/engine.cpp](../javascript\_libraries)
- [src/mongo/db/dur\_journal.cpp](../journaling)

<pre>mongo::File::read(unsigned long long, char*, unsigned int)</pre>
#### Used By:
- [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
- [src/mongo/scripting/engine.cpp](../javascript\_libraries)
- [src/mongo/db/dur\_journal.cpp](../journaling)
