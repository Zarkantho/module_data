
# Interface for Regular Expression Library
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/third\_party/pcre-8.30/pcrecpp.cc

<div></div>

    pcrecpp::RE::FullMatch(pcrecpp::StringPiece const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&) const

- Used By:

    - [src/mongo/util/options\_parser/constraints.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/scripting/bench.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    pcrecpp::Arg::parse_string(char const*, int, void*)

- Used By:

    - [src/mongo/util/net/miniwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/tools/tool\_options.cpp](../../../../tools/tools)

<div></div>

    pcrecpp::RE::QuoteMeta(pcrecpp::StringPiece const&)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/tools/files.cpp](../../../../tools/tools)

<div></div>

    pcrecpp::RE::~RE()

- Used By:

    - [src/mongo/util/options\_parser/constraints.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/db/matcher/expression\_leaf.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/tools/tool\_options.cpp](../../../../tools/tools)
    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/util/net/miniwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/scripting/bench.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    pcrecpp::RE::no_arg

- Used By:

    - [src/mongo/util/options\_parser/constraints.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/db/matcher/expression\_leaf.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/tools/tool\_options.cpp](../../../../tools/tools)
    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/util/net/miniwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/scripting/bench.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    pcrecpp::RE::Init(std::string const&, pcrecpp::RE_Options const*)

- Used By:

    - [src/mongo/util/options\_parser/constraints.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/db/matcher/expression\_leaf.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/tools/tool\_options.cpp](../../../../tools/tools)
    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/util/net/miniwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/scripting/bench.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    pcrecpp::RE::Consume(pcrecpp::StringPiece*, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&) const

- Used By:

    - [src/mongo/util/net/miniwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/tools/tool\_options.cpp](../../../../tools/tools)

<div></div>

    pcrecpp::RE::PartialMatch(pcrecpp::StringPiece const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&, pcrecpp::Arg const&) const

- Used By:

    - [src/mongo/db/matcher/expression\_leaf.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/shell/dbshell.cpp](../../../../mongo\_shell/mongo\_shell)
