# journaling

# Module Groups

-------------

Page aligned buffer builder   what sort of buffer? i don't understand ;(

- src/mongo/util/alignedbuilder.cpp   (mongod, tools)
- src/mongo/util/alignedbuilder.h

## Interface
### src/mongo/util/alignedbuilder.cpp
<pre>mongo::AlignedBuilder::kill()</pre>
#### Used By:
- [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)

<pre>mongo::AlignedBuilder::AlignedBuilder(unsigned int)</pre>
#### Used By:
- [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)

-------------

Journaling module   who calls/owns stuff in here? only used by mongod, correct?

- src/mongo/db/dur.cpp   (mongod, tools)
- src/mongo/db/dur.h
- src/mongo/db/dur\_commitjob.cpp   (mongod, tools)
- src/mongo/db/dur\_commitjob.h
- src/mongo/db/dur\_journal.cpp   (mongod, tools)
- src/mongo/db/dur\_journal.h
- src/mongo/db/dur\_journalformat.h
- src/mongo/db/dur\_journalimpl.h
- src/mongo/db/dur\_preplogbuffer.cpp   (mongod, tools)
- src/mongo/db/dur\_recover.cpp   (mongod, tools)
- src/mongo/db/dur\_recover.h
- src/mongo/db/dur\_stats.h
- src/mongo/db/dur\_writetodatafiles.cpp   (mongod, tools)
- src/mongo/db/durop.cpp   (mongod, tools)
- src/mongo/db/durop.h
- src/mongo/db/storage/durable\_mapped\_file.cpp   (mongod, tools)
- src/mongo/db/storage/durable\_mapped\_file.h

## Interface
### src/mongo/db/dur.cpp
<pre>mongo::dur::Stats::S::_asCSV()</pre>
#### Used By:
- [src/mongo/dbtests/perftests.cpp](../unit\_tests)

<pre>mongo::dur::Stats::S::_asObj()</pre>
#### Used By:
- [src/mongo/dbtests/perftests.cpp](../unit\_tests)

<pre>mongo::dur::commitJob</pre>
#### Used By:
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::dur::stats</pre>
#### Used By:
- [src/mongo/dbtests/perftests.cpp](../unit\_tests)

<pre>mongo::dur::Stats::S::_CSVHeader()</pre>
#### Used By:
- [src/mongo/dbtests/perftests.cpp](../unit\_tests)

<pre>mongo::dur::Stats::S::reset()</pre>
#### Used By:
- [src/mongo/dbtests/perftests.cpp](../unit\_tests)

<pre>mongo::dur::DurableInterface::_impl</pre>
#### Used By:
- [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)
- [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)
- [src/mongo/db/database\_holder.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
- [src/mongo/db/write\_concern.cpp](../replication)
- [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
- [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)
- [src/mongo/db/structure/btree/state.cpp](../storage\_layer\_structure)
- [src/mongo/db/compact.cpp](../database\_commands)
- [src/mongo/db/structure/record\_store.cpp](../storage\_layer\_structure)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/ops/update.cpp](../query\_system)
- [src/mongo/db/storage/extent.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
- [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
- [src/mongo/db/commands/fsync.cpp](../database\_commands)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/d\_concurrency.cpp](../concurrency)
- [src/mongo/db/ops/delete.cpp](../query\_system)
- [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)
- [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
- [src/mongo/db/cap.cpp](../storage\_layer\_structure)
- [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/repl/rs\_sync.cpp](../replication)

<pre>mongo::dur::startup()</pre>
#### Used By:
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/tools/tool.cpp](../tools)
- [src/mongo/dbtests/framework.cpp](../unit\_tests)

<pre>mongo::dur::releasingWriteLock()</pre>
#### Used By:
- [src/mongo/db/d\_concurrency.cpp](../concurrency)
### src/mongo/db/dur\_journal.cpp
<pre>mongo::dur::getJournalDir()</pre>
#### Used By:
- [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)

<pre>mongo::dur::haveJournalFiles(bool)</pre>
#### Used By:
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::dur::journalCleanup(bool)</pre>
#### Used By:
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
### src/mongo/db/storage/durable\_mapped\_file.cpp
<pre>mongo::DurableMappedFile::create(std::string const&, unsigned long long&, bool)</pre>
#### Used By:
- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)
- [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)
- [src/mongo/dbtests/mmaptests.cpp](../unit\_tests)

<pre>mongo::DurableMappedFile::open(std::string const&, bool)</pre>
#### Used By:
- [src/mongo/dbtests/mmaptests.cpp](../unit\_tests)
- [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)
- [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)

<pre>mongo::DurableMappedFile::~DurableMappedFile()</pre>
#### Used By:
- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
- [src/mongo/db/database.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/mmaptests.cpp](../unit\_tests)

<pre>mongo::DurableMappedFile::DurableMappedFile()</pre>
#### Used By:
- [src/mongo/dbtests/mmaptests.cpp](../unit\_tests)
- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
- [src/mongo/db/database.cpp](../storage\_layer\_structure)

-------------

This is not actually used in our logging system. Just utilities to create files that you can  append to. One notable example of a system that uses this is our preallocation of journal files.  In fact, it isn't used in anything not journaling related right now.

- src/mongo/util/logfile.cpp   (mongod, tools)
- src/mongo/util/logfile.h

## Interface
### src/mongo/util/logfile.cpp
<pre>mongo::LogFile::synchronousAppend(void const*, unsigned long)</pre>
#### Used By:
- [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)
- [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)

<pre>mongo::LogFile::~LogFile()</pre>
#### Used By:
- [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)
- [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)

<pre>mongo::LogFile::writeAt(unsigned long long, void const*, unsigned long)</pre>
#### Used By:
- [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)

<pre>mongo::LogFile::LogFile(std::string const&, bool)</pre>
#### Used By:
- [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)
- [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)

<pre>mongo::LogFile::readAt(unsigned long long, void*, unsigned long)</pre>
#### Used By:
- [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)
