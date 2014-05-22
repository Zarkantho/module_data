
# Interface for SSL Command Line Options
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/util/net/ssl\_options.cpp

<div></div>

    mongo::addSSLClientOptions(mongo::optionenvironment::OptionSection*)

- Used By:

    - [src/mongo/shell/shell\_options.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/tools/tool\_options.cpp](../../../../tools/tools)

<div></div>

    mongo::storeSSLClientOptions(mongo::optionenvironment::Environment const&)

- Used By:

    - [src/mongo/shell/shell\_options.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/tools/tool\_options.cpp](../../../../tools/tools)

<div></div>

    mongo::canonicalizeSSLServerOptions(mongo::optionenvironment::Environment*)

- Used By:

    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/s/mongos\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::addSSLServerOptions(mongo::optionenvironment::OptionSection*)

- Used By:

    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/s/mongos\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::storeSSLServerOptions(mongo::optionenvironment::Environment const&)

- Used By:

    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
