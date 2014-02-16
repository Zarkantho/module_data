
# Interface

### src/mongo/db/pipeline/pipeline.cpp

<div></div>

    mongo::Pipeline::addRequiredPrivileges(mongo::Command*, std::string const&, mongo::BSONObj, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> >*)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../sharding)

<div></div>

    mongo::Pipeline::addInitialSource(boost::intrusive_ptr<mongo::DocumentSource>)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../sharding)

<div></div>

    mongo::Pipeline::splitForSharded()

- Used By:

    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../sharding)

<div></div>

    mongo::Pipeline::serialize() const

- Used By:

    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../sharding)

<div></div>

    mongo::Pipeline::stitch()

- Used By:

    - [src/mongo/s/commands\_public.cpp](../sharding)

<div></div>

    mongo::Pipeline::parseCommand(std::string&, mongo::BSONObj const&, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../sharding)

<div></div>

    mongo::Pipeline::run(mongo::BSONObjBuilder&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../sharding)

<div></div>

    mongo::Pipeline::canRunInMongos() const

- Used By:

    - [src/mongo/s/commands\_public.cpp](../sharding)

<div></div>

    mongo::Pipeline::getInitialQuery() const

- Used By:

    - [src/mongo/s/commands\_public.cpp](../sharding)

<div></div>

    mongo::Pipeline::writeExplainOps() const

- Used By:

    - [src/mongo/s/commands\_public.cpp](../sharding)

<div></div>

    mongo::Pipeline::commandName

- Used By:

    - [src/mongo/s/commands\_public.cpp](../sharding)
