
# Interface for Count Command
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/ops/count.cpp

<div></div>

    mongo::runCount(std::string const&, mongo::BSONObj const&, std::string&, int&)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/counttests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::applySkipLimit(long long, mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
