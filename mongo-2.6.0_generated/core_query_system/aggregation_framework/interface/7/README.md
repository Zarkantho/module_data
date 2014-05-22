
# Interface for Aggregation Common Entry Point
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/pipeline/pipeline.cpp

<div></div>

    mongo::Pipeline::addInitialSource(boost::intrusive_ptr<mongo::DocumentSource>)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::Pipeline::splitForSharded()

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/dbtests/pipelinetests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Pipeline::addRequiredPrivileges(mongo::Command*, std::string const&, mongo::BSONObj, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> >*)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::Pipeline::serialize() const

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/dbtests/pipelinetests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Pipeline::canRunInMongos() const

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::Pipeline::writeExplainOps() const

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::Pipeline::stitch()

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::Pipeline::getInitialQuery() const

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::Pipeline::commandName

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::Pipeline::parseCommand(std::string&, mongo::BSONObj const&, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/dbtests/pipelinetests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Pipeline::run(mongo::BSONObjBuilder&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
