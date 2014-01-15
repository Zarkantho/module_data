# file\_interface

# Module Groups

-------------

Abstraction layer for dealing with files. It's basically the read(2), open(2), and write(2)  interface for posix, and something else for Windows. Not used by mmap code, and does not depend  on file allocator library. Use this if you need a file but not a memory mapped file.

- src/mongo/util/file.cpp   (cppclientdriver)
- src/mongo/util/file.h
