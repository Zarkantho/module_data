
# Interface for Password Digest
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/util/password\_digest.cpp

<div></div>

    mongo::createPasswordDigest(mongo::StringData const&, mongo::StringData const&)

- Used By:

    - [src/mongo/client/dbclient.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/auth/security\_key.cpp](../../../../security/authentication)
    - [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../../../../security/authorization)
