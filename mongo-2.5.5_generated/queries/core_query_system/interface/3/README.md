
# Interface for Document Matcher
This interface information represents symbols thatare defined in this group but used in other modules.  Does not includesymbols defined in this group that are used inside this module.

### src/mongo/db/matcher/matcher.cpp

<div></div>

    mongo::Matcher2::matches(mongo::BSONObj const&, mongo::MatchDetails*) const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_match.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/db/curop.cpp](../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/instance.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/matchertests.cpp](../../../tests/unit\_tests)
    - [src/mongo/client/parallel.cpp](../../../network/cpp\_client\_driver)
    - [src/mongo/tools/restore.cpp](../../../tools/tools)
    - [src/mongo/tools/tool.cpp](../../../tools/tools)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../queries/database\_commands)

<div></div>

    mongo::Matcher2::Matcher2(mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/db/pipeline/document\_source\_match.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/db/curop.cpp](../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/instance.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/matchertests.cpp](../../../tests/unit\_tests)
    - [src/mongo/client/parallel.cpp](../../../network/cpp\_client\_driver)
    - [src/mongo/tools/restore.cpp](../../../tools/tools)
    - [src/mongo/tools/tool.cpp](../../../tools/tools)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../queries/database\_commands)
