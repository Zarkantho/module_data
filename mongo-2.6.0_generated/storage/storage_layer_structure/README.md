# Storage Layer Structure
Structure of the storage layer.  Some of these files are for the persistent on disk representation, whereas some are for the in memory representation. TODO: Come up with better sections.  Split up btree info, persistent structure, and in memory structure into separate modules


-------------

## Namespace String
Helper to manage strings that look like "<db>.<collection>"

#### Files
- src/mongo/db/namespace\_string-inl.h   (mongod, tools, mongos)
- src/mongo/db/namespace\_string.h   (mongod, tools, mongos)
- src/mongo/db/namespace\_string\_test.cpp   ()

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Namespace Holder
Class to hold namespace strings that look like "<db>.<collection>" in a fixed width form

#### Files
- src/mongo/db/structure/catalog/namespace.cpp   (mongod, tools, mongos)
- src/mongo/db/structure/catalog/namespace.h   (mongod, tools, mongos)
- src/mongo/db/structure/catalog/namespace-inl.h   (mongod, tools, mongos)
- src/mongo/db/structure/catalog/namespace\_test.cpp   ()

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Index Catalog
Classes to manage and iterate indexes.  There should only be one index catalog per collection.  Contains some subset of the metadata about an index as well as an index descriptor containing the rest of the data

#### Files
- src/mongo/db/catalog/index\_catalog.cpp   (mongod, tools)
- src/mongo/db/catalog/index\_catalog.h   (mongod, tools, mongos)
- src/mongo/db/catalog/index\_catalog\_entry.cpp   (mongod, tools)
- src/mongo/db/catalog/index\_catalog\_entry.h   (mongod, tools, mongos)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Database Holder
Top level class to keep track of databases.  Essentially a map of path + dbname to a Database object with extra logic to optionally create the database if it does not exist.

#### Files
- src/mongo/db/catalog/database\_holder.cpp   (mongod, tools)
- src/mongo/db/catalog/database\_holder.h   (mongod, tools, mongos)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Database Class
Class to manage a single database.  This currently contains the code to manage data files and collections and provides mechanisms to access other database information, such as indexes.

#### Files
- src/mongo/db/catalog/database.cpp   (mongod, tools)
- src/mongo/db/catalog/database.h   (mongod, tools, mongos)

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## Namespace Details
Class to manage the disk format of an entry for a single collection in the ".ns" files

#### Files
- src/mongo/db/structure/catalog/namespace\_details-inl.h   (mongod, tools, mongos)
- src/mongo/db/structure/catalog/namespace\_details.cpp   (mongod, tools)
- src/mongo/db/structure/catalog/namespace\_details.h   (mongod, tools, mongos)

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

## Namespace Index
Manages the disk format for the ".ns" files, including adding the metadata for a new namespace or removing metadata for a deleted namespace.  Provides a way to access the Namespace Details for a single namespace

#### Files
- src/mongo/db/structure/catalog/namespace\_index.cpp   (mongod, tools)
- src/mongo/db/structure/catalog/namespace\_index.h   (mongod, tools, mongos)

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)

-------------

## Collection Class
Class to manage a single collection, including collection data and collection metadata.

#### Files
- src/mongo/db/catalog/collection.cpp   (mongod, tools)
- src/mongo/db/catalog/collection.h   (mongod, tools, mongos)

#### [Interface](interface/7)

#### [Dependencies](dependencies/7)

-------------

## Collection Info Cache
Contains methods to update and access non persistent collection state, such as the current query plan cache

#### Files
- src/mongo/db/catalog/collection\_info\_cache.cpp   (mongod, tools)
- src/mongo/db/catalog/collection\_info\_cache.h   (mongod, tools, mongos)

#### [Interface](interface/8)

#### [Dependencies](dependencies/8)

-------------

## Collection Cursor Cache
Keeps track of cursors and query runners for timeout and invalidation purposes.  The pattern is that the relevant objects must be registered here so that this code can essentially call back to do the invalidation when necessary

#### Files
- src/mongo/db/catalog/collection\_cursor\_cache.cpp   (mongod, tools)
- src/mongo/db/catalog/collection\_cursor\_cache.h   (mongod, tools, mongos)

#### [Interface](interface/9)

#### [Dependencies](dependencies/9)

-------------

## Foreground Index Creation
Free function to create an index in the foreground.  TODO: Find all the ways an index can be created and put them in the same section

#### Files
- src/mongo/db/catalog/index\_create.cpp   (mongod, tools)
- src/mongo/db/catalog/index\_create.h   (mongod, tools)

#### [Interface](interface/10)

#### [Dependencies](dependencies/10)

-------------

## Storage Options
Command line options for the storage system.  This should only be in binaries that have a storaage layer.

#### Files
- src/mongo/db/storage\_options.cpp   (mongod, tools)
- src/mongo/db/storage\_options.h   (mongod, tools, mongos)

#### [Interface](interface/11)

#### [Dependencies](dependencies/11)

-------------

## Capped Collection Management
Contains code to do low level storage management of a capped collection, such as allocation of new records

#### Files
- src/mongo/db/structure/catalog/cap.cpp   (mongod, tools)

#### [Interface](interface/12)

#### [Dependencies](dependencies/12)

-------------

## Persistent Hash Table
Fixed size hash table that is appropriate for managing memory that is persisted to disk

#### Files
- src/mongo/db/structure/catalog/hashtab.h   (mongod, tools, mongos)

#### [Interface](interface/13)

#### [Dependencies](dependencies/13)

-------------

## Index Details
On disk format of index metadata

#### Files
- src/mongo/db/structure/catalog/index\_details.cpp   (mongod, tools)
- src/mongo/db/structure/catalog/index\_details.h   (mongod, tools, mongos)

#### [Interface](interface/14)

#### [Dependencies](dependencies/14)

-------------

## Collection Compact
Contains the code that actually does the work of compacting a collection.  TODO: put this near the actual compact command

#### Files
- src/mongo/db/structure/collection\_compact.cpp   (mongod, tools)

#### [Interface](interface/15)

#### [Dependencies](dependencies/15)

-------------

## Collection Iterator
Contains code that essentially does a table scan of a collection. Has iterators for both capped and non capped collections.

#### Files
- src/mongo/db/structure/collection\_iterator.cpp   (mongod, tools)
- src/mongo/db/structure/collection\_iterator.h   (mongod, tools, mongos)

#### [Interface](interface/16)

#### [Dependencies](dependencies/16)

-------------

## DiskLoc Class
A DiskLoc is simply a file number and offset into the file for a db. You can think of this as an  "address" into our database storage space.

#### Files
- src/mongo/db/diskloc.h   (mongod, tools, mongos)
- src/mongo/db/diskloc\_test.cpp   ()

#### [Interface](interface/17)

#### [Dependencies](dependencies/17)

-------------

## DiskLoc Invalidation Type
Type of a DiskLoc invalidation.

#### Files
- src/mongo/db/invalidation\_type.h   (mongod, tools, mongos)

#### [Interface](interface/18)

#### [Dependencies](dependencies/18)

-------------

## Record Class
A record is simply a "node" in a linked list. It contains "prev" and "next" offsets, as well as  the offset of the extent in the current file.

#### Files
- src/mongo/db/storage/record.cpp   (mongod, tools)
- src/mongo/db/storage/record.h   (mongod, tools, mongos)

#### [Interface](interface/19)

#### [Dependencies](dependencies/19)

-------------

## Record Store
Manages Records.  Contains code to delete and insert records, as well as helpers to construct a Record object from a DiscLoc.  Also handles allocating new extents if the current extent does not have room for another record.

#### Files
- src/mongo/db/structure/record\_store.cpp   (mongod, tools)
- src/mongo/db/structure/record\_store.h   (mongod, tools, mongos)

#### [Interface](interface/20)

#### [Dependencies](dependencies/20)

-------------

## Extent Class
An extent is a bucket of records. Extents themselves are in a kind of linked list, except instead  of offsets into a single datafile, their "prev" and "next" members are DiskLocs.

#### Files
- src/mongo/db/storage/extent.cpp   (mongod, tools)
- src/mongo/db/storage/extent.h   (mongod, tools, mongos)

#### [Interface](interface/21)

#### [Dependencies](dependencies/21)

-------------

## Extent Manager
Sits above an extent and has helper functions to manage them as a whole. This is the new way to  iterate extents.

#### Files
- src/mongo/db/storage/extent\_manager.cpp   (mongod, tools)
- src/mongo/db/storage/extent\_manager.h   (mongod, tools, mongos)

#### [Interface](interface/22)

#### [Dependencies](dependencies/22)

-------------

## Cloner And Copy Commands
Contains various commands to copy entire collections and databases, as well as the Cloner class, which contains the actual implementation of the copy logic and can be used directly in other code.

#### Files
- src/mongo/db/cloner.cpp   (mongod, tools)
- src/mongo/db/cloner.h   (mongod, tools)

#### [Interface](interface/23)

#### [Dependencies](dependencies/23)

-------------

## Legacy Instance File
One of the very hairy, very old parts of the server.  Contains code for the DBDirectClient, which is an implementation of the "DBClientBase" class in the client driver. The DBDirectClient has the same interface as the client driver, except that instead of connecting over the network it is just doing operations on the local server behind the scenes.

This also has code for the "BSONElementManipulator which is what allows us to do in place updates in the old code. It appears now that it is only used in updating the "expireAfterSeconds" field for a document in a TTL index.

Also have random things like "getDatabaseNames" which just iteratest the db directory getting all the names of the files there. Also has the version of "inShutdown" and "dbexit" for mongod.

Unfortunately, it also has the code to handle decoding incoming network requests on mongod.

#### Files
- src/mongo/db/instance.cpp   (mongod, tools)
- src/mongo/db/instance.h   (mongod, tools, mongos)

#### [Interface](interface/24)

#### [Dependencies](dependencies/24)

-------------

## Legacy Pdfile File
This is another really hairy, really old legacy file.

A long time ago, in a galaxy far far away, when MongoDB was 10gen and providing a platform as a service, the persistence layer was called "p".  I have heard that the way to start the database in those days was to just type "p" on the command line.  While I cannot confirm this, it is an amusing story and fits with our past naming convention. That also explains why this is "pdfile" for "P Data File".  It contains various old functions for interacting directly with the storage layer that should soon die a horrible death.

#### Files
- src/mongo/db/pdfile.cpp   (mongod, tools)
- src/mongo/db/pdfile.h   (mongod, tools, mongos)
- src/mongo/db/pdfile\_private.h   (mongod, tools)
- src/mongo/db/pdfile\_version.h   (mongod, tools, mongos)

#### [Interface](interface/25)

#### [Dependencies](dependencies/25)
