
# Interface for Users
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/auth/user.cpp

<div></div>

    mongo::User::setCredentials(mongo::User::CredentialData const&)

- Used By:

    - [src/mongo/db/auth/security\_key.cpp](../../../../security/authentication)

<div></div>

    mongo::User::getName() const

- Used By:

    - [src/mongo/db/auth/security\_key.cpp](../../../../security/authentication)
    - [src/mongo/db/commands/authentication\_commands.cpp](../../../../security/authentication)

<div></div>

    mongo::User::getCredentials() const

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../../security/authentication)
    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)

### src/mongo/db/auth/user\_document\_parser.cpp

<div></div>

    mongo::V2UserDocumentParser::checkValidUserDocument(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/catalog/collection.cpp](../../../../storage/storage\_layer\_structure)

### src/mongo/db/auth/user\_name.cpp

<div></div>

    mongo::UserName::UserName(mongo::StringData const&, mongo::StringData const&)

- Used By:

    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/db/commands/authentication\_commands.cpp](../../../../security/authentication)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)
