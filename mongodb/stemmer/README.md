# stemmer

# Module Groups

-------------

Third Party - Stemmer for various languages used in full text search

- src/third\_party/shim\_stemmer.cpp   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/include/libstemmer.h
- src/third\_party/libstemmer\_c/libstemmer/libstemmer\_utf8.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/libstemmer/modules\_utf8.h
- src/third\_party/libstemmer\_c/runtime/api.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/runtime/api.h
- src/third\_party/libstemmer\_c/runtime/header.h
- src/third\_party/libstemmer\_c/runtime/utilities.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_ISO\_8859\_1\_danish.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_ISO\_8859\_1\_dutch.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_ISO\_8859\_1\_english.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_ISO\_8859\_1\_finnish.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_ISO\_8859\_1\_french.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_ISO\_8859\_1\_german.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_ISO\_8859\_1\_hungarian.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_ISO\_8859\_1\_italian.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_ISO\_8859\_1\_norwegian.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_ISO\_8859\_1\_porter.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_ISO\_8859\_1\_portuguese.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_ISO\_8859\_1\_spanish.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_ISO\_8859\_1\_swedish.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_ISO\_8859\_2\_romanian.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_KOI8\_R\_russian.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_danish.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_danish.h
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_dutch.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_dutch.h
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_english.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_english.h
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_finnish.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_finnish.h
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_french.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_french.h
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_german.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_german.h
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_hungarian.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_hungarian.h
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_italian.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_italian.h
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_norwegian.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_norwegian.h
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_porter.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_porter.h
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_portuguese.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_portuguese.h
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_romanian.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_romanian.h
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_russian.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_russian.h
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_spanish.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_spanish.h
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_swedish.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_swedish.h
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_turkish.c   (mongod, tools, mongos)
- src/third\_party/libstemmer\_c/src\_c/stem\_UTF\_8\_turkish.h

## Interface
### src/third\_party/libstemmer\_c/libstemmer/libstemmer\_utf8.c
<pre>_sb_stemmer_length</pre>
#### Used By:
- [src/mongo/db/fts/stemmer.cpp](../full\_text\_search\_module)

<pre>_sb_stemmer_delete</pre>
#### Used By:
- [src/mongo/db/fts/stemmer.cpp](../full\_text\_search\_module)

<pre>_sb_stemmer_stem</pre>
#### Used By:
- [src/mongo/db/fts/stemmer.cpp](../full\_text\_search\_module)

<pre>_sb_stemmer_new</pre>
#### Used By:
- [src/mongo/db/fts/stemmer.cpp](../full\_text\_search\_module)
