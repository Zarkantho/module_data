
# Interface for SSL Command Line Options
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/util/net/ssl\_options.cpp

<div></div>

    mongo::addSSLClientOptions(mongo::optionenvironment::OptionSection*)

- Used By:

    - [src/mongo/tools/tool\_options.cpp](../../../../tools/tools)
    - [src/mongo/shell/shell\_options.cpp](../../../../mongo\_shell/mongo\_shell)

<div></div>

    mongo::storeSSLServerOptions(mongo::optionenvironment::Environment const&)

- Used By:

    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::addSSLServerOptions(mongo::optionenvironment::OptionSection*)

- Used By:

    - [src/mongo/s/mongos\_options.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::storeSSLClientOptions(mongo::optionenvironment::Environment const&)

- Used By:

    - [src/mongo/tools/tool\_options.cpp](../../../../tools/tools)
    - [src/mongo/shell/shell\_options.cpp](../../../../mongo\_shell/mongo\_shell)
