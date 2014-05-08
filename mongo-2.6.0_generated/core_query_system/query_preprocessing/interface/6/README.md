
# Interface for Document Matcher
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/matcher/matcher.cpp

<div></div>

    mongo::Matcher2::matches(mongo::BSONObj const&, mongo::MatchDetails*) const

- Used By:

    - [src/mongo/dbtests/matchertests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/db/pipeline/document\_source\_match.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)

<div></div>

    mongo::Matcher2::Matcher2(mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/dbtests/matchertests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/db/pipeline/document\_source\_match.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/curop.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)
