
# Interface

### src/mongo/base/string\_data.cpp

<div></div>

    mongo::operator<<(std::ostream&, mongo::StringData const&)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../database\_commands)
    - [src/mongo/db/json.cpp](../../../bson)
    - [src/mongo/db/auth/authorization\_manager.cpp](../../../authentication)
    - [src/mongo/logger/message\_event\_utf8\_encoder.cpp](../../../logging\_system)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../sharding)
    - [src/mongo/db/clientcursor.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/commands.cpp](../../../database\_commands)
    - [src/mongo/scripting/engine\_v8.cpp](../../../javascript\_libraries)
    - [src/mongo/db/catalog/database.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../authentication)
    - [src/mongo/logger/log\_severity.cpp](../../../logging\_system)
    - [src/mongo/db/clientlistplugin.cpp](../../../web\_server)
    - [src/mongo/db/storage/extent.cpp](../../../storage\_layer\_structure)
    - [src/mongo/s/distlock.cpp](../../../sharding)
    - [src/mongo/db/d\_concurrency.cpp](../../../concurrency)
    - [src/mongo/db/ops/delete.cpp](../../../core\_query\_system)
    - [src/mongo/db/field\_ref.cpp](../../../update\_system)

<div></div>

    mongo::StringData::Hasher::operator()(mongo::StringData const&) const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../javascript\_libraries)
    - [src/mongo/db/catalog/database.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/fts/stop\_words.cpp](../../../full\_text\_search\_module)
    - [src/mongo/db/ops/modifier\_table.cpp](../../../update\_system)
    - [src/mongo/db/stats/top.cpp](../../../utilities)
    - [src/mongo/db/projection.cpp](../../../core\_query\_system)
    - [src/mongo/db/d\_concurrency.cpp](../../../concurrency)
    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/fts/stop\_words\_list.cpp](../../../full\_text\_search\_module)
    - [src/mongo/db/exec/projection\_exec.cpp](../../../core\_query\_system)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/pipeline/expression.cpp](../../../aggregation\_framework)
    - [src/mongo/db/stats/snapshots.cpp](../../../utilities)
