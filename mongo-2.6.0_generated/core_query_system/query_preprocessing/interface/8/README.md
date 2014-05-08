
# Interface for Projection Helper
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/projection.cpp

<div></div>

    mongo::Projection::init(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::Projection::transform(mongo::BSONObj const&, mongo::MatchDetails const*) const

- Used By:

    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../query\_and\_operation\_handling/database\_commands)
