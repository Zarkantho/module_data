
# Interface for Oplog Reader
This interface information represents symbols thatare defined in this group but used in other modules.  Does not includesymbols defined in this group that are used inside this module.

### src/mongo/db/repl/oplogreader.cpp

<div></div>

    mongo::replAuthenticate(mongo::DBClientBase*)

- Used By:

    - [src/mongo/db/cloner.cpp](../../../storage/storage\_layer\_structure)

<div></div>

    mongo::OplogReader::connect(std::string const&)

- Used By:

    - [src/mongo/tools/oplog.cpp](../../../tools/tools)

<div></div>

    mongo::OplogReader::tailingQueryGTE(char const*, mongo::OpTime, mongo::BSONObj const*)

- Used By:

    - [src/mongo/tools/oplog.cpp](../../../tools/tools)

<div></div>

    mongo::OplogReader::OplogReader()

- Used By:

    - [src/mongo/tools/oplog.cpp](../../../tools/tools)
