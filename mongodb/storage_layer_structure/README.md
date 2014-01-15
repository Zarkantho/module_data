# storage\_layer\_structure

# Module Groups

-------------

Helper to manage strings that look like "<db>.<collection>"

- src/mongo/db/namespace\_string-inl.h
- src/mongo/db/namespace\_string.h
- src/mongo/db/namespace\_string\_test.cpp   ()

-------------

Files containing the structural metadata about the databases/data files/collections/indexes.  TODO: Add more details here about the relationships between these files.

- src/mongo/db/namespace\_details-inl.h
- src/mongo/db/namespace\_details.cpp   (mongod, tools)
- src/mongo/db/namespace\_details.h
- src/mongo/db/database.cpp   (mongod, tools)
- src/mongo/db/database.h
- src/mongo/db/database\_holder.cpp   (mongod, tools)
- src/mongo/db/database\_holder.h
- src/mongo/db/storage/index\_details.cpp   (mongod, tools)
- src/mongo/db/storage/index\_details.h
- src/mongo/db/storage\_options.cpp   (mongod, tools)
- src/mongo/db/storage\_options.h
- src/mongo/db/structure/btree/btree.cpp   (mongod, tools)
- src/mongo/db/structure/btree/btree.h
- src/mongo/db/structure/btree/btree\_stats.cpp   (mongod, tools)
- src/mongo/db/structure/btree/btree\_stats.h
- src/mongo/db/structure/btree/btreebuilder.cpp   (mongod, tools)
- src/mongo/db/structure/btree/btreebuilder.h
- src/mongo/db/structure/btree/key.cpp   (mongod, tools)
- src/mongo/db/structure/btree/key.h
- src/mongo/db/structure/btree/state-inl.h
- src/mongo/db/structure/btree/state.cpp   (mongod, tools)
- src/mongo/db/structure/btree/state.h
- src/mongo/db/structure/collection.cpp   (mongod, tools)
- src/mongo/db/structure/collection.h
- src/mongo/db/structure/collection\_info\_cache.cpp   (mongod, tools)
- src/mongo/db/structure/collection\_info\_cache.h
- src/mongo/db/structure/collection\_iterator.cpp   (mongod, tools)
- src/mongo/db/structure/collection\_iterator.h
- src/mongo/db/structure/record\_store.cpp   (mongod, tools)
- src/mongo/db/structure/record\_store.h
- src/mongo/db/cap.cpp   (mongod, tools)
- src/mongo/db/catalog/index\_catalog.cpp   (mongod, tools)
- src/mongo/db/catalog/index\_catalog.h
- src/mongo/db/catalog/index\_create.cpp   (mongod, tools)
- src/mongo/db/catalog/index\_create.h
- src/mongo/db/catalog/ondisk/namespace-inl.h
- src/mongo/db/catalog/ondisk/namespace.cpp   (mongod, tools, mongos)
- src/mongo/db/catalog/ondisk/namespace.h
- src/mongo/db/catalog/ondisk/namespace\_index.cpp   (mongod, tools)
- src/mongo/db/catalog/ondisk/namespace\_index.h
- src/mongo/db/catalog/ondisk/namespace\_test.cpp   ()

-------------

A DiskLoc is simply a file number and offset into the file for a db. You can think of this as an  "address" into our database's storage space.

- src/mongo/db/diskloc.h
- src/mongo/db/diskloc\_test.cpp   ()

-------------

A record is simply a "node" in a linked list. It contains "prev" and "next" offsets, as well as  the offset of the extent in the current file.

- src/mongo/db/storage/record.cpp   (mongod, tools)
- src/mongo/db/storage/record.h

-------------

An extent is a bucket of records. Extents themselves are in a kind of linked list, except instead  of offsets into a single datafile, their "prev" and "next" members are DiskLocs.

- src/mongo/db/storage/extent.cpp   (mongod, tools)
- src/mongo/db/storage/extent.h

-------------

Sits above an extent and has helper functions to manage them as a whole. This is the new way to  iterate extents.

- src/mongo/db/storage/extent\_manager.cpp   (mongod, tools)
- src/mongo/db/storage/extent\_manager.h

-------------

Utilities to clone entire collections and databases

- src/mongo/db/cloner.cpp   (mongod, tools)
- src/mongo/db/cloner.h

-------------

One of the very hairy, very old parts of the server. Contains code for the DBDirectClient, which  is an implementation of the "DBClientBase" class in the client driver. The DBDirectClient has the  same interface as the client driver, except that instead of connecting over the network it is just  doing operations on the local server behind the scenes.   This also has code for the "BSONElementManipulator which is what allows us to do in place  updates in the old code. It appears now that it is only used in updating the "expireAfterSeconds"  field for a document in a TTL index.   Also have random things like "getDatabaseNames" which just iteratest the db directory getting all  the names of the files there. Also has the version of "inShutdown" and "dbexit" for mongod.   clarify relationship between instance.cpp and the various ops/* (insert/update etc)

- src/mongo/db/instance.cpp   (mongod, tools)
- src/mongo/db/instance.h

-------------

This is another really hairy, really old legacy file. At this point it's easier to just write out  all the functions in the interface than describe what it does. I believe "pdfile" is short for  "persistent data file". It contains a bunch of old legacy things to manipulate data files and  data file metadata.   Here are all the functions in pdfile.cpp that are currently used in the project.   mongo::inDBRepair  mongo::allocateSpaceForANewRecord(char const*, mongo::NamespaceDetails*, int, bool)  mongo::dbSize(char const*)  mongo::dropDatabase(std::string const&)  mongo::dbHolderUnchecked()  mongo::addRecordToRecListInExtent(mongo::Record*, mongo::DiskLoc)  mongo::userCreateNS(char const*, mongo::BSONObj, std::string&, bool, bool*)  mongo::\_deleteDataFiles(char const*)  mongo::dropAllDatabasesExceptLocal()  mongo::isValidNS(mongo::StringData const&)  mongo::repairDatabase(std::string, std::string&, bool, bool)

- src/mongo/db/pdfile.cpp   (mongod, tools)
- src/mongo/db/pdfile.h
- src/mongo/db/pdfile\_private.h
- src/mongo/db/pdfile\_version.h
