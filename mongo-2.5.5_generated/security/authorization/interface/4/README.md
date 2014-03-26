
# Interface

### src/mongo/db/auth/user.cpp

<div></div>

    mongo::User::setCredentials(mongo::User::CredentialData const&)

- Used By:

    - [src/mongo/db/auth/security\_key.cpp](../../../authentication)

<div></div>

    mongo::User::getCredentials() const

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../authentication)
    - [src/mongo/db/dbwebserver.cpp](../../../web\_server)

<div></div>

    mongo::User::getName() const

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../authentication)
    - [src/mongo/db/auth/security\_key.cpp](../../../authentication)

### src/mongo/db/auth/user\_document\_parser.cpp

<div></div>

    mongo::V2UserDocumentParser::checkValidUserDocument(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/catalog/collection.cpp](../../../storage\_layer\_structure)

### src/mongo/db/auth/user\_name.cpp

<div></div>

    mongo::UserName::UserName(mongo::StringData const&, mongo::StringData const&)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../../../authentication)
    - [src/mongo/db/dbwebserver.cpp](../../../web\_server)
    - [src/mongo/tools/restore.cpp](../../../tools)
