
# Interface for StringData
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/base/string\_data.cpp

<div></div>

    mongo::operator<<(std::ostream&, mongo::StringData const&)

- Used By:

    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/authentication\_commands.cpp](../../../../security/authentication)
    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/storage/extent.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/field\_ref.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/json.cpp](../../../../bson/bson)
    - [src/mongo/db/auth/authorization\_manager.cpp](../../../../security/authorization)
    - [src/mongo/db/clientlistplugin.cpp](../../../../network/web\_server)
    - [src/mongo/logger/message\_event\_utf8\_encoder.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/logger/log\_severity.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../../security/authorization)

<div></div>

    mongo::StringData::Hasher::operator()(mongo::StringData const&) const

- Used By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)
    - [src/mongo/db/stats/top.cpp](../../../../utilities/utilities)
    - [src/mongo/db/exec/projection\_exec.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/fts/stop\_words.cpp](../../../../core\_query\_system/full\_text\_search\_module)
    - [src/mongo/db/stats/snapshots.cpp](../../../../utilities/utilities)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/exec/projection.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/projection.cpp](../../../../core\_query\_system/query\_preprocessing)
    - [src/mongo/db/pipeline/expression.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/ops/modifier\_table.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/query/planner\_ixselect.cpp](../../../../core\_query\_system/query\_planner)
    - [build/darwin/ssl/mongo/db/fts/stop\_words\_list.cpp](../../../../core\_query\_system/full\_text\_search\_module)
