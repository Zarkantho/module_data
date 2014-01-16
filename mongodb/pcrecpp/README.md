# pcrecpp

# Module Groups

-------------

Third Party - Perl compatible regular expressions

- src/third\_party/shim\_pcrecpp.cc   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/config.h
- src/third\_party/pcre-8.30/pcre.h
- src/third\_party/pcre-8.30/pcre\_byte\_order.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_chartables.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_compile.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_config.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_dfa\_exec.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_exec.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_fullinfo.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_get.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_globals.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_internal.h
- src/third\_party/pcre-8.30/pcre\_maketables.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_newline.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_ord2utf8.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_printint.c
- src/third\_party/pcre-8.30/pcre\_refcount.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_scanner.cc   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_scanner.h
- src/third\_party/pcre-8.30/pcre\_string\_utils.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_stringpiece.cc   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_stringpiece.h
- src/third\_party/pcre-8.30/pcre\_study.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_tables.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_ucd.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_valid\_utf8.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_version.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_xclass.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcrecpp.cc   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcrecpp.h
- src/third\_party/pcre-8.30/pcrecpp\_internal.h
- src/third\_party/pcre-8.30/pcrecpparg.h
- src/third\_party/pcre-8.30/pcreposix.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcreposix.h
- src/third\_party/pcre-8.30/ucp.h

## Interface
### src/third\_party/pcre-8.30/pcrecpp.cc
<pre>pcrecpp::RE::FullMatch(pcrecpp::StringPiece const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&) const</pre>
#### Used By:
- [src/mongo/util/options\_parser/constraints.cpp](../startup\_initialization)
- [src/mongo/scripting/bench.cpp](../javascript\_libraries)

<pre>pcrecpp::Arg::parse_string(char const*, int, void*)</pre>
#### Used By:
- [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
- [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
- [src/mongo/tools/tool\_options.cpp](../tools)

<pre>pcrecpp::RE::QuoteMeta(pcrecpp::StringPiece const&)</pre>
#### Used By:
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/s/config.cpp](../sharding)
- [src/mongo/s/grid.cpp](../sharding)
- [src/mongo/tools/files.cpp](../tools)

<pre>pcrecpp::RE::~RE()</pre>
#### Used By:
- [src/mongo/util/options\_parser/constraints.cpp](../startup\_initialization)
- [src/mongo/db/matcher/expression\_leaf.cpp](../query\_system)
- [src/mongo/tools/tool\_options.cpp](../tools)
- [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
- [src/mongo/shell/dbshell.cpp](../mongo\_shell)
- [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
- [src/mongo/scripting/bench.cpp](../javascript\_libraries)

<pre>pcrecpp::RE::no_arg</pre>
#### Used By:
- [src/mongo/util/options\_parser/constraints.cpp](../startup\_initialization)
- [src/mongo/db/matcher/expression\_leaf.cpp](../query\_system)
- [src/mongo/tools/tool\_options.cpp](../tools)
- [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
- [src/mongo/shell/dbshell.cpp](../mongo\_shell)
- [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
- [src/mongo/scripting/bench.cpp](../javascript\_libraries)

<pre>pcrecpp::RE::Init(std::string const&, pcrecpp::RE_Options const*)</pre>
#### Used By:
- [src/mongo/util/options\_parser/constraints.cpp](../startup\_initialization)
- [src/mongo/db/matcher/expression\_leaf.cpp](../query\_system)
- [src/mongo/tools/tool\_options.cpp](../tools)
- [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
- [src/mongo/shell/dbshell.cpp](../mongo\_shell)
- [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
- [src/mongo/scripting/bench.cpp](../javascript\_libraries)

<pre>pcrecpp::RE::Consume(pcrecpp::StringPiece*, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&) const</pre>
#### Used By:
- [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
- [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
- [src/mongo/tools/tool\_options.cpp](../tools)

<pre>pcrecpp::RE::PartialMatch(pcrecpp::StringPiece const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&) const</pre>
#### Used By:
- [src/mongo/db/matcher/expression\_leaf.cpp](../query\_system)
- [src/mongo/shell/dbshell.cpp](../mongo\_shell)
