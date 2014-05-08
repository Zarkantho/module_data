
# Interface for Index Key Validation
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/catalog/index\_key\_validate.cpp

<div></div>

    mongo::validateKeyPattern(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/structure/collection\_compact.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/shell/shell\_utils.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
