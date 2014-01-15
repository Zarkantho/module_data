# indexing

# Module Groups

-------------

Indexes and index management code. TODO: go into more details about this. The code is new.  The two parts of the interface that are nice entry points are the "index\_access\_method.h"  (interface for manipulating and accessing the index itself), and "index\_cursor.h" (interface for  getting data from an index) files.   can you say a bit more about the structure in here, wrt. a hypothetical   member of the 'open source community' who wants to add a new type of   index to mongodb?

- src/mongo/db/index/2d\_access\_method.cpp   (mongod, tools)
- src/mongo/db/index/2d\_access\_method.h
- src/mongo/db/index/2d\_common.h
- src/mongo/db/index/btree\_access\_method.cpp   (mongod, tools)
- src/mongo/db/index/btree\_access\_method.h
- src/mongo/db/index/btree\_access\_method\_internal.h
- src/mongo/db/index/btree\_based\_builder.cpp   (mongod, tools)
- src/mongo/db/index/btree\_based\_builder.h
- src/mongo/db/index/btree\_index\_cursor.cpp   (mongod, tools)
- src/mongo/db/index/btree\_index\_cursor.h
- src/mongo/db/index/btree\_interface.cpp   (mongod, tools)
- src/mongo/db/index/btree\_interface.h
- src/mongo/db/index/btree\_key\_generator.cpp   (mongod, tools, mongos)
- src/mongo/db/index/btree\_key\_generator.h
- src/mongo/db/index/expression\_index.h
- src/mongo/db/index/fts\_access\_method.cpp   (mongod, tools)
- src/mongo/db/index/fts\_access\_method.h
- src/mongo/db/index/hash\_access\_method.cpp   (mongod, tools)
- src/mongo/db/index/hash\_access\_method.h
- src/mongo/db/index/haystack\_access\_method.cpp   (mongod, tools)
- src/mongo/db/index/haystack\_access\_method.h
- src/mongo/db/index/haystack\_access\_method\_internal.h
- src/mongo/db/index/index\_access\_method.h
- src/mongo/db/index/index\_cursor.h
- src/mongo/db/index/index\_descriptor.h
- src/mongo/db/index/s2\_access\_method.cpp   (mongod, tools)
- src/mongo/db/index/s2\_access\_method.h
- src/mongo/db/index\_builder.cpp   (mongod, tools)
- src/mongo/db/index\_builder.h
- src/mongo/db/index\_legacy.cpp   (mongod, tools)
- src/mongo/db/index\_legacy.h
- src/mongo/db/index\_names.cpp   (mongod, tools, mongos)
- src/mongo/db/index\_names.h
- src/mongo/db/index\_rebuilder.cpp   (mongod, tools)
- src/mongo/db/index\_rebuilder.h
- src/mongo/db/index\_set.cpp   (mongod, tools, mongos)
- src/mongo/db/index\_set.h
- src/mongo/db/index\_set\_test.cpp   ()

-------------

Class representing an index spec, such as { "a" : 1, "b" : -1 }

- src/mongo/db/keypattern.cpp   (mongod, tools, mongos)
- src/mongo/db/keypattern.h

-------------

Background job that periodically checks a ttl index.

- src/mongo/db/ttl.cpp   (mongod, tools)
- src/mongo/db/ttl.h
