# mmap

# Module Groups

-------------

mmap library (only depends on file allocation library)

- src/mongo/util/mmap.cpp   (mongod, tools)
- src/mongo/util/mmap.h
- src/mongo/util/mmap\_posix.cpp   (mongod, tools)

## Interface


### src/mongo/util/mmap.cpp

<pre>mongo::printMemInfo(char const*)</pre>

#### Used By:

- [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)

<pre>mongo::LockMongoFilesShared::mmmutex</pre>

#### Used By:

- [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)
- [src/mongo/dbtests/mmaptests.cpp](../unit\_tests)
- [src/mongo/db/dur\_recover.cpp](../journaling)
- [src/mongo/tools/sniffer.cpp](../tools)
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/dur.cpp](../journaling)
- [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)
- [src/mongo/db/commands/touch.cpp](../database\_commands)
- [src/mongo/s/d\_migrate.cpp](../sharding)

<pre>mongo::MongoFile::getAllFiles()</pre>

#### Used By:

- [src/mongo/db/dur.cpp](../journaling)

<pre>mongo::MongoFile::totalMappedLength()</pre>

#### Used By:

- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

<pre>mongo::LockMongoFilesShared::era</pre>

#### Used By:

- [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)
- [src/mongo/db/dur\_recover.cpp](../journaling)
- [src/mongo/tools/sniffer.cpp](../tools)
- [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)

<pre>mongo::MongoFile::flushAll(bool)</pre>

#### Used By:

- [src/mongo/db/dur.cpp](../journaling)
- [src/mongo/db/repl/oplog.cpp](../replication)
- [src/mongo/db/dur\_recover.cpp](../journaling)
- [src/mongo/db/write\_concern.cpp](../replication)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/commands/fsync.cpp](../database\_commands)

<pre>mongo::MongoFile::notifyPostFlush</pre>

#### Used By:

- [src/mongo/db/dur\_journal.cpp](../journaling)

<pre>mongo::MemoryMappedFile::mapWithOptions(char const*, int)</pre>

#### Used By:

- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
- [src/mongo/db/dur\_recover.cpp](../journaling)

<pre>mongo::MongoFile::notifyPreFlush</pre>

#### Used By:

- [src/mongo/db/dur\_journal.cpp](../journaling)

<pre>mongo::MongoFile::closeAllFiles(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&)</pre>

#### Used By:

- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::MongoFileFinder::findByPath(std::string const&) const</pre>

#### Used By:

- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/dbtests/mmaptests.cpp](../unit\_tests)
- [src/mongo/db/dur\_recover.cpp](../journaling)

<pre>mongo::MemoryMappedFile::map(char const*)</pre>

#### Used By:

- [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)

### src/mongo/util/mmap\_posix.cpp

<pre>mongo::MemoryMappedFile::prepareFlush()</pre>

#### Used By:

- [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)

<pre>mongo::MemoryMappedFile::close()</pre>

#### Used By:

- [src/mongo/tools/sniffer.cpp](../tools)
- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
- [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)
- [src/mongo/db/dur\_recover.cpp](../journaling)

<pre>mongo::MemoryMappedFile::createPrivateMap()</pre>

#### Used By:

- [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)

<pre>vtable for mongo::MemoryMappedFile</pre>

#### Used By:

- [src/mongo/tools/sniffer.cpp](../tools)
- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
- [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)
- [src/mongo/db/dur\_recover.cpp](../journaling)

<pre>typeinfo for mongo::MemoryMappedFile</pre>

#### Used By:

- [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)

<pre>mongo::MemoryMappedFile::flush(bool)</pre>

#### Used By:

- [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)
- [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)

<pre>mongo::MemoryMappedFile::remapPrivateView(void*)</pre>

#### Used By:

- [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)

<pre>mongo::MemoryMappedFile::map(char const*, unsigned long long&, int)</pre>

#### Used By:

- [src/mongo/tools/sniffer.cpp](../tools)
- [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)

<pre>mongo::g_minOSPageSizeBytes</pre>

#### Used By:

- [src/mongo/util/touch\_pages.cpp](../utilities)
- [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
- [src/mongo/util/logfile.cpp](../journaling)

<pre>mongo::MemoryMappedFile::MemoryMappedFile()</pre>

#### Used By:

- [src/mongo/tools/sniffer.cpp](../tools)
- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
- [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)
- [src/mongo/db/dur\_recover.cpp](../journaling)
