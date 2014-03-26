
# Interface for Write Commands Downconvert
This interface information represents symbols thatare defined in this group but used in other modules.  Does not includesymbols defined in this group that are used inside this module.

### src/mongo/s/write\_ops/batch\_downconvert.cpp

<div></div>

    mongo::BatchSafeWriter::safeWriteBatch(mongo::DBClientBase*, mongo::BatchedCommandRequest const&, mongo::BatchedCommandResponse*)

- Used By:

    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../sharding/sharding)

<div></div>

    mongo::enforceLegacyWriteConcern(mongo::MultiCommandDispatch*, mongo::StringData const&, mongo::BSONObj const&, std::map<mongo::ConnectionString, mongo::HostOpTime, mongo::ConnectionStringComp, std::allocator<std::pair<mongo::ConnectionString const, mongo::HostOpTime> > > const&, std::vector<mongo::LegacyWCResponse, std::allocator<mongo::LegacyWCResponse> >*)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../sharding/sharding)

### src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp

<div></div>

    vtable for mongo::DBClientSafeWriter

- Used By:

    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../sharding/sharding)
