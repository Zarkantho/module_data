
# Interface for JSON to BSON parser
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/json.cpp

<div></div>

    mongo::fromjson(std::string const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/pipelinetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/client/examples/mongoperf.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/s/grid.cpp](../../../../sharding/sharding)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/stat.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jsontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/export.cpp](../../../../tools/tools)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)

<div></div>

    mongo::fromjson(char const*, int*)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/import.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../../replication/replication)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/restapi.cpp](../../../../network/web\_server)
    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/dbtests/jsobjtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/perf/perftest.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/s/shardkey.cpp](../../../../sharding/sharding)
    - [src/mongo/dbtests/counttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/oplogreader.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/matchertests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/jstests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../../tests/unit\_tests)
