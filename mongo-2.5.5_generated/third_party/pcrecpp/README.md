# pcrecpp

# Module Groups

-------------

# Group Description
Third Party - Perl compatible regular expressions

# Files
- src/third\_party/shim\_pcrecpp.cc   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/config.h   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre.h   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_byte\_order.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_chartables.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_compile.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_config.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_dfa\_exec.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_exec.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_fullinfo.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_get.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_globals.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_internal.h   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_maketables.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_newline.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_ord2utf8.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_printint.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_refcount.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_scanner.cc   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_scanner.h   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_string\_utils.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_stringpiece.cc   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_stringpiece.h   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_study.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_tables.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_ucd.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_valid\_utf8.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_version.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcre\_xclass.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcrecpp.cc   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcrecpp.h   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcrecpp\_internal.h   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcrecpparg.h   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcreposix.c   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/pcreposix.h   (mongod, tools, mongos)
- src/third\_party/pcre-8.30/ucp.h   (mongod, tools, mongos)

# Interface

### src/third\_party/pcre-8.30/pcrecpp.cc

<div></div>

    pcrecpp::RE::FullMatch(pcrecpp::StringPiece const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&) const

- Used By:

    - [src/mongo/util/options\_parser/constraints.cpp](../startup\_initialization)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)

<div></div>

    pcrecpp::Arg::parse_string(char const*, int, void*)

- Used By:

    - [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/tools/tool\_options.cpp](../tools)

<div></div>

    pcrecpp::RE::QuoteMeta(pcrecpp::StringPiece const&)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/tools/files.cpp](../tools)

<div></div>

    pcrecpp::RE::~RE()

- Used By:

    - [src/mongo/util/options\_parser/constraints.cpp](../startup\_initialization)
    - [src/mongo/db/matcher/expression\_leaf.cpp](../query\_system)
    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)

<div></div>

    pcrecpp::RE::no_arg

- Used By:

    - [src/mongo/util/options\_parser/constraints.cpp](../startup\_initialization)
    - [src/mongo/db/matcher/expression\_leaf.cpp](../query\_system)
    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)

<div></div>

    pcrecpp::RE::Init(std::string const&, pcrecpp::RE_Options const*)

- Used By:

    - [src/mongo/util/options\_parser/constraints.cpp](../startup\_initialization)
    - [src/mongo/db/matcher/expression\_leaf.cpp](../query\_system)
    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)
    - [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/scripting/bench.cpp](../javascript\_libraries)

<div></div>

    pcrecpp::RE::Consume(pcrecpp::StringPiece*, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&) const

- Used By:

    - [src/mongo/util/net/miniwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/db/dbwebserver.cpp](../database\_web\_accesss)
    - [src/mongo/tools/tool\_options.cpp](../tools)

<div></div>

    pcrecpp::RE::PartialMatch(pcrecpp::StringPiece const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&) const

- Used By:

    - [src/mongo/db/matcher/expression\_leaf.cpp](../query\_system)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)

# Dependencies
(no dependencies outside this module)