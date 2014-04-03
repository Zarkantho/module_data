
# Interface for StringData
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/base/string\_data.cpp

<div></div>

    mongo::operator<<(std::ostream&, mongo::StringData const&)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../../security/authentication)
    - [src/mongo/db/json.cpp](../../../../bson/bson)
    - [src/mongo/db/auth/authorization\_manager.cpp](../../../../security/authorization)
    - [src/mongo/logger/message\_event\_utf8\_encoder.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/clientcursor.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../../security/authorization)
    - [src/mongo/logger/log\_severity.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/db/clientlistplugin.cpp](../../../../network/web\_server)
    - [src/mongo/db/storage/extent.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)
    - [src/mongo/db/d\_concurrency.cpp](../../../../queries/concurrency)
    - [src/mongo/db/ops/delete.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/field\_ref.cpp](../../../../queries/update\_system)

<div></div>

    mongo::StringData::Hasher::operator()(mongo::StringData const&) const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/fts/stop\_words.cpp](../../../../queries/full\_text\_search\_module)
    - [src/mongo/db/ops/modifier\_table.cpp](../../../../queries/update\_system)
    - [src/mongo/db/stats/top.cpp](../../../../utilities/utilities)
    - [src/mongo/db/projection.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/d\_concurrency.cpp](../../../../queries/concurrency)
    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/fts/stop\_words\_list.cpp](../../../../queries/full\_text\_search\_module)
    - [src/mongo/db/exec/projection\_exec.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/pipeline/expression.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/stats/snapshots.cpp](../../../../utilities/utilities)
