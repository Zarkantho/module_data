# Indexing
TODO: indexing description


-------------

## Index Interface
Top level interface for all indexes.

#### Files
- src/mongo/db/index/index\_access\_method.h   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Btree Backed Index Interface
Top level interface for indexes that are backed by a btree.

#### Files
- src/mongo/db/index/btree\_based\_access\_method.h   (mongod, tools, mongos)
- src/mongo/db/index/btree\_based\_access\_method.cpp   (mongod, tools)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Index Key Generation Interface
Interface for a class that is responsible for generating the index keys for a given document.

#### Files
- src/mongo/db/index/key\_generator.cpp   (mongod, tools, mongos)
- src/mongo/db/index/key\_generator.h   (mongod, tools, mongos)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Index Cursor Interface
Top level interface for iterating elements in an index.

#### Files
- src/mongo/db/index/index\_cursor.h   (mongod, tools, mongos)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Btree Index Cursor
Cursor to iterate the elements in a btree based index.

#### Files
- src/mongo/db/index/btree\_index\_cursor.cpp   (mongod, tools)
- src/mongo/db/index/btree\_index\_cursor.h   (mongod, tools, mongos)

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## Btree Interface
Interface to interact with the underlying btree datastructure. Abstracts away the difference between our different index formats.

#### Files
- src/mongo/db/index/btree\_interface.cpp   (mongod, tools)
- src/mongo/db/index/btree\_interface.h   (mongod, tools, mongos)

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

## Btree Datastructure
Files containing the btree datastructure implementation.  Currently this is the only index datastructure we use.  While this is intended to be a low level datastructure, it currently has a few fingers into replication and other parts of the server, including calling isMaster

#### Files
- src/mongo/db/structure/btree/btree.cpp   (mongod, tools)
- src/mongo/db/structure/btree/btree.h   (mongod, tools, mongos)
- src/mongo/db/structure/btree/btree\_stats.cpp   (mongod, tools)
- src/mongo/db/structure/btree/btree\_stats.h   (mongod, tools)
- src/mongo/db/structure/btree/btreebuilder.cpp   (mongod, tools)
- src/mongo/db/structure/btree/btreebuilder.h   (mongod, tools)
- src/mongo/db/structure/btree/key.cpp   (mongod, tools)
- src/mongo/db/structure/btree/key.h   (mongod, tools, mongos)

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)

-------------

## Btree Indexes
Btree based index implementation

#### Files
- src/mongo/db/index/btree\_access\_method.cpp   (mongod, tools)
- src/mongo/db/index/btree\_access\_method.h   (mongod, tools)
- src/mongo/db/index/btree\_key\_generator.cpp   (mongod, tools, mongos)
- src/mongo/db/index/btree\_key\_generator.h   (mongod, tools, mongos)

#### [Interface](interface/7)

#### [Dependencies](dependencies/7)

-------------

## 2d Indexes
2d index implementation

#### Files
- src/mongo/db/index/2d\_access\_method.cpp   (mongod, tools)
- src/mongo/db/index/2d\_access\_method.h   (mongod, tools, mongos)
- src/mongo/db/index/2d\_common.h   (mongod, tools, mongos)
- src/mongo/db/index/2d\_key\_generator.cpp   (mongod, tools, mongos)
- src/mongo/db/index/2d\_key\_generator.h   (mongod, tools, mongos)

#### [Interface](interface/8)

#### [Dependencies](dependencies/8)

-------------

## S2 Indexes
S2 index implementation

#### Files
- src/mongo/db/index/s2\_access\_method.cpp   (mongod, tools)
- src/mongo/db/index/s2\_access\_method.h   (mongod, tools, mongos)
- src/mongo/db/index/s2\_key\_generator.cpp   (mongod, tools, mongos)
- src/mongo/db/index/s2\_key\_generator.h   (mongod, tools, mongos)

#### [Interface](interface/9)

#### [Dependencies](dependencies/9)

-------------

## Fts Indexes
Fts index implementation

#### Files
- src/mongo/db/index/fts\_access\_method.cpp   (mongod, tools)
- src/mongo/db/index/fts\_access\_method.h   (mongod, tools)
- src/mongo/db/index/fts\_key\_generator.cpp   (mongod, tools, mongos)
- src/mongo/db/index/fts\_key\_generator.h   (mongod, tools, mongos)

#### [Interface](interface/10)

#### [Dependencies](dependencies/10)

-------------

## Hashed Indexes
Hashed index implementation

#### Files
- src/mongo/db/index/hash\_access\_method.cpp   (mongod, tools)
- src/mongo/db/index/hash\_access\_method.h   (mongod, tools, mongos)
- src/mongo/db/index/hash\_key\_generator.cpp   (mongod, tools, mongos)
- src/mongo/db/index/hash\_key\_generator.h   (mongod, tools, mongos)

#### [Interface](interface/11)

#### [Dependencies](dependencies/11)

-------------

## Haystack Indexes
Haystack index implementation

#### Files
- src/mongo/db/index/haystack\_access\_method.cpp   (mongod, tools)
- src/mongo/db/index/haystack\_access\_method.h   (mongod, tools, mongos)
- src/mongo/db/index/haystack\_access\_method\_internal.h   (mongod, tools, mongos)
- src/mongo/db/index/haystack\_key\_generator.cpp   (mongod, tools, mongos)
- src/mongo/db/index/haystack\_key\_generator.h   (mongod, tools, mongos)

#### [Interface](interface/12)

#### [Dependencies](dependencies/12)

-------------

## Index Descriptor
In memory datastructure containing all information about a single index.

#### Files
- src/mongo/db/index/index\_descriptor.cpp   (mongod, tools)
- src/mongo/db/index/index\_descriptor.h   (mongod, tools, mongos)

#### [Interface](interface/13)

#### [Dependencies](dependencies/13)

-------------

## Index Expression Helpers
Helpers for indexes where the index entries are some function of the index, including s2 indexes and hashed indexes.

#### Files
- src/mongo/db/index/expression\_index.h   (mongod, tools, mongos)

#### [Interface](interface/14)

#### [Dependencies](dependencies/14)

-------------

## Index Spec Parsing
Helpers to parse index specifications, like the ones that come from users when they run the ensureIndex command

#### Files
- src/mongo/db/index/expression\_params.h   (mongod, tools, mongos)

#### [Interface](interface/15)

#### [Dependencies](dependencies/15)

-------------

## Index Key Check
Seems to be just a utility to check if a key is too large.  Used from things external to the indexing system to test the validity of index keys.

#### Files
- src/mongo/db/index/external\_key\_generator.cpp   ()
- src/mongo/db/index/external\_key\_generator.h   ()

#### [Interface](interface/16)

#### [Dependencies](dependencies/16)

-------------

## Background Index Build
Code for building an index.  Also can handle spawing a thread to build an index in the background.

#### Files
- src/mongo/db/index\_builder.cpp   (mongod, tools)
- src/mongo/db/index\_builder.h   (mongod, tools)

#### [Interface](interface/17)

#### [Dependencies](dependencies/17)

-------------

## Index Legacy Exceptions
Behavior that the current implementation of the code and that some indexes require that does not fit in with the model for the main index interface.

#### Files
- src/mongo/db/index\_legacy.cpp   (mongod, tools)
- src/mongo/db/index\_legacy.h   (mongod, tools)

#### [Interface](interface/18)

#### [Dependencies](dependencies/18)

-------------

## Index Names
Enum of all the index types we currently support as well as utilities to manage index strings and check whether we support a given index type.

#### Files
- src/mongo/db/index\_names.cpp   (mongod, tools, mongos)
- src/mongo/db/index\_names.h   (mongod, tools, mongos)

#### [Interface](interface/19)

#### [Dependencies](dependencies/19)

-------------

## Index Rebuilder
Background job that removes and potentially rebuilds incomplete indexes.  Whether we actually rebuild after removing the indexes is configurable at server startup time using a command line or config file option.

#### Files
- src/mongo/db/index\_rebuilder.cpp   (mongod, tools)
- src/mongo/db/index\_rebuilder.h   (mongod, tools)

#### [Interface](interface/20)

#### [Dependencies](dependencies/20)

-------------

## Index Path Set
Set of all field references (dotted field names) that have been indexed in this collection.  Used to check whether an in place update will change a field that is indexed and thus cannot be done in place.

#### Files
- src/mongo/db/index\_set.cpp   (mongod, tools, mongos)
- src/mongo/db/index\_set.h   (mongod, tools, mongos)
- src/mongo/db/index\_set\_test.cpp   ()

#### [Interface](interface/21)

#### [Dependencies](dependencies/21)

-------------

## Index Key Pregeneration
Helpers to pregenerate a bunch of index keys outside a lock.

#### Files
- src/mongo/db/catalog/index\_pregen.cpp   (mongod, tools)
- src/mongo/db/catalog/index\_pregen.h   (mongod, tools, mongos)

#### [Interface](interface/22)

#### [Dependencies](dependencies/22)

-------------

## Index Key Validation
Check to see if an index spec passed in by the user is valid for creating an index.

#### Files
- src/mongo/db/catalog/index\_key\_validate.cpp   (mongod, tools)
- src/mongo/db/catalog/index\_key\_validate.h   (mongod, tools)

#### [Interface](interface/23)

#### [Dependencies](dependencies/23)

-------------

## TODO: Name this group
Class representing an index spec, such as { "a" : 1, "b" : -1 }

#### Files
- src/mongo/db/keypattern.cpp   (mongod, tools, mongos)
- src/mongo/db/keypattern.h   (mongod, tools, mongos)

#### [Interface](interface/24)

#### [Dependencies](dependencies/24)

-------------

## TTL Background Job
Background job that periodically checks a ttl index.

#### Files
- src/mongo/db/ttl.cpp   (mongod, tools)
- src/mongo/db/ttl.h   (mongod, tools)

#### [Interface](interface/25)

#### [Dependencies](dependencies/25)
