
# Interface for Write Commands Downconvert
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/s/write\_ops/batch\_downconvert.cpp

<div></div>

    mongo::enforceLegacyWriteConcern(mongo::MultiCommandDispatch*, mongo::StringData const&, mongo::BSONObj const&, std::map<mongo::ConnectionString, mongo::HostOpTime, mongo::ConnectionStringComp, std::allocator<std::pair<mongo::ConnectionString const, mongo::HostOpTime> > > const&, std::vector<mongo::LegacyWCResponse, std::allocator<mongo::LegacyWCResponse> >*)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/sharding\_uncategorized)
