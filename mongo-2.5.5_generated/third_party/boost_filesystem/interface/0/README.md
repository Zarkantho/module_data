
# Interface

### src/third\_party/boost/libs/filesystem/v3/src/operations.cpp

<div></div>

    boost::filesystem3::absolute(boost::filesystem3::path const&, boost::filesystem3::path const&)

- Used By:

    - [src/mongo/db/server\_options\_helpers.cpp](../../../startup\_initialization)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../startup\_initialization)
    - [src/mongo/util/net/ssl\_options.cpp](../../../network)
    - [src/mongo/util/mmap.cpp](../../../mmap)

<div></div>

    boost::filesystem3::detail::directory_iterator_construct(boost::filesystem3::directory_iterator&, boost::filesystem3::path const&, boost::system::error_code*)

- Used By:

    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../mongo\_shell)
    - [src/mongo/db/dur\_recover.cpp](../../../journaling)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dur\_journal.cpp](../../../journaling)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../mongo\_shell)
    - [src/mongo/dbtests/framework\_options.cpp](../../../unit\_tests)
    - [src/mongo/tools/restore.cpp](../../../tools)
    - [src/mongo/scripting/engine.cpp](../../../javascript\_libraries)

<div></div>

    boost::filesystem3::detail::temp_directory_path(boost::system::error_code*)

- Used By:

    - [src/mongo/unittest/temp\_dir.cpp](../../../unit\_tests)

<div></div>

    boost::filesystem3::detail::rename(boost::filesystem3::path const&, boost::filesystem3::path const&, boost::system::error_code*)

- Used By:

    - [src/mongo/db/pdfile.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/dur\_journal.cpp](../../../journaling)

<div></div>

    boost::filesystem3::detail::directory_iterator_increment(boost::filesystem3::directory_iterator&, boost::system::error_code*)

- Used By:

    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../mongo\_shell)
    - [src/mongo/db/dur\_recover.cpp](../../../journaling)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dur\_journal.cpp](../../../journaling)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../mongo\_shell)
    - [src/mongo/dbtests/framework\_options.cpp](../../../unit\_tests)
    - [src/mongo/tools/restore.cpp](../../../tools)
    - [src/mongo/scripting/engine.cpp](../../../javascript\_libraries)

<div></div>

    boost::filesystem3::detail::initial_path(boost::system::error_code*)

- Used By:

    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../mongo\_shell)

<div></div>

    boost::filesystem3::detail::status(boost::filesystem3::path const&, boost::system::error_code*)

- Used By:

    - [src/mongo/util/file\_allocator.cpp](../../../file\_allocation)
    - [src/mongo/unittest/temp\_dir.cpp](../../../unit\_tests)
    - [src/mongo/db/dur\_journal.cpp](../../../journaling)
    - [src/mongo/dbtests/perftests.cpp](../../../unit\_tests)
    - [src/mongo/scripting/engine.cpp](../../../javascript\_libraries)
    - [src/mongo/tools/import.cpp](../../../tools)
    - [src/mongo/db/dur\_recover.cpp](../../../journaling)
    - [src/mongo/client/gridfs.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/storage/extent\_manager.cpp](../../../storage\_layer\_structure)
    - [src/mongo/tools/tool\_options.cpp](../../../tools)
    - [src/mongo/db/durop.cpp](../../../journaling)
    - [src/mongo/db/pdfile.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/tools/restore.cpp](../../../tools)
    - [src/mongo/shell/shell\_utils.cpp](../../../mongo\_shell)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../mongo\_shell)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../startup\_initialization)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../../../storage\_layer\_structure)
    - [src/mongo/util/mmap.cpp](../../../mmap)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../mongo\_shell)
    - [src/mongo/db/storage/data\_file.cpp](../../../mmap\_file\_interface)
    - [src/mongo/dbtests/framework\_options.cpp](../../../unit\_tests)

<div></div>

    boost::filesystem3::path_traits::dispatch(boost::filesystem3::directory_entry const&, std::string&, std::codecvt<wchar_t, char, __mbstate_t> const&)

- Used By:

    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../mongo\_shell)
    - [src/mongo/db/dur\_recover.cpp](../../../journaling)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dur\_journal.cpp](../../../journaling)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../mongo\_shell)
    - [src/mongo/dbtests/framework\_options.cpp](../../../unit\_tests)
    - [src/mongo/tools/restore.cpp](../../../tools)
    - [src/mongo/scripting/engine.cpp](../../../javascript\_libraries)

<div></div>

    boost::filesystem3::detail::create_directory(boost::filesystem3::path const&, boost::system::error_code*)

- Used By:

    - [src/mongo/util/file\_allocator.cpp](../../../file\_allocation)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../mongo\_shell)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/pdfile.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/dur\_journal.cpp](../../../journaling)
    - [src/mongo/unittest/temp\_dir.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/framework\_options.cpp](../../../unit\_tests)

<div></div>

    boost::filesystem3::detail::file_size(boost::filesystem3::path const&, boost::system::error_code*)

- Used By:

    - [src/mongo/util/file\_allocator.cpp](../../../file\_allocation)
    - [src/mongo/db/pdfile.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../../../aggregation\_framework)
    - [src/mongo/db/dur\_recover.cpp](../../../journaling)
    - [src/mongo/tools/tool.cpp](../../../tools)
    - [src/mongo/db/dur\_journal.cpp](../../../journaling)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../mongo\_shell)
    - [src/mongo/db/extsort.cpp](../../../aggregation\_framework)
    - [src/mongo/tools/restore.cpp](../../../tools)
    - [src/mongo/db/storage/extent\_manager.cpp](../../../storage\_layer\_structure)
    - [src/mongo/util/mmap.cpp](../../../mmap)
    - [src/mongo/tools/import.cpp](../../../tools)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../../../aggregation\_framework)

<div></div>

    boost::filesystem3::detail::dir_itr_close(void*&, void*&)

- Used By:

    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../mongo\_shell)
    - [src/mongo/db/dur\_recover.cpp](../../../journaling)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dur\_journal.cpp](../../../journaling)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../mongo\_shell)
    - [src/mongo/dbtests/framework\_options.cpp](../../../unit\_tests)
    - [src/mongo/tools/restore.cpp](../../../tools)
    - [src/mongo/scripting/engine.cpp](../../../javascript\_libraries)

<div></div>

    boost::filesystem3::detail::copy_file(boost::filesystem3::path const&, boost::filesystem3::path const&, boost::filesystem3::copy_option::enum_type, boost::system::error_code*)

- Used By:

    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../mongo\_shell)
    - [src/mongo/db/pdfile.cpp](../../../storage\_layer\_structure)

<div></div>

    boost::filesystem3::detail::remove(boost::filesystem3::path const&, boost::system::error_code*)

- Used By:

    - [src/mongo/util/file\_allocator.cpp](../../../file\_allocation)
    - [src/mongo/db/pdfile.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../../../aggregation\_framework)
    - [src/mongo/db/durop.cpp](../../../journaling)
    - [src/mongo/db/dbcommands\_admin.cpp](../../../database\_commands)
    - [src/mongo/db/dur\_journal.cpp](../../../journaling)
    - [src/mongo/db/extsort.cpp](../../../aggregation\_framework)
    - [src/mongo/client/examples/mongoperf.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../../../aggregation\_framework)
    - [src/mongo/dbtests/mmaptests.cpp](../../../unit\_tests)

<div></div>

    boost::filesystem3::detail::remove_all(boost::filesystem3::path const&, boost::system::error_code*)

- Used By:

    - [src/mongo/db/pdfile.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../mongo\_shell)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../mongo\_shell)
    - [src/mongo/unittest/temp\_dir.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/framework\_options.cpp](../../../unit\_tests)

<div></div>

    boost::filesystem3::detail::create_directories(boost::filesystem3::path const&, boost::system::error_code*)

- Used By:

    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../../../aggregation\_framework)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../mongo\_shell)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../../../aggregation\_framework)
    - [src/mongo/db/extsort.cpp](../../../aggregation\_framework)
    - [src/mongo/db/dbhelpers.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/tools/export.cpp](../../../tools)
    - [src/mongo/tools/dump.cpp](../../../tools)

<div></div>

    boost::filesystem3::detail::current_path(boost::system::error_code*)

- Used By:

    - [src/mongo/db/server\_options\_helpers.cpp](../../../startup\_initialization)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../mongo\_shell)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../mongo\_shell)
    - [src/mongo/util/net/ssl\_options.cpp](../../../network)
    - [src/mongo/util/mmap.cpp](../../../mmap)

### src/third\_party/boost/libs/filesystem/v3/src/path.cpp

<div></div>

    boost::filesystem3::path::operator/=(char const*)

- Used By:

    - [src/mongo/db/pdfile.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/dbcommands\_admin.cpp](../../../database\_commands)
    - [src/mongo/db/dur\_journal.cpp](../../../journaling)

<div></div>

    boost::filesystem3::path::wchar_t_codecvt_facet()

- Used By:

    - [src/mongo/util/file\_allocator.cpp](../../../file\_allocation)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../mongo\_shell)
    - [src/mongo/db/durop.cpp](../../../journaling)
    - [src/mongo/db/dur\_recover.cpp](../../../journaling)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/dur\_journal.cpp](../../../journaling)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../mongo\_shell)
    - [src/mongo/unittest/temp\_dir.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/framework\_options.cpp](../../../unit\_tests)
    - [src/mongo/tools/restore.cpp](../../../tools)
    - [src/mongo/db/dbhelpers.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/scripting/engine.cpp](../../../javascript\_libraries)
    - [src/mongo/db/storage/extent\_manager.cpp](../../../storage\_layer\_structure)
    - [src/mongo/tools/dump.cpp](../../../tools)

<div></div>

    boost::filesystem3::path::operator/=(boost::filesystem3::path const&)

- Used By:

    - [src/mongo/util/file\_allocator.cpp](../../../file\_allocation)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../mongo\_shell)
    - [src/mongo/dbtests/mmaptests.cpp](../../../unit\_tests)
    - [src/mongo/db/pdfile.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/dur\_journal.cpp](../../../journaling)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/unittest/temp\_dir.cpp](../../../unit\_tests)
    - [src/mongo/tools/restore.cpp](../../../tools)
    - [src/mongo/tools/dump.cpp](../../../tools)

<div></div>

    boost::filesystem3::path::parent_path() const

- Used By:

    - [src/mongo/util/file\_allocator.cpp](../../../file\_allocation)
    - [src/mongo/tools/restore.cpp](../../../tools)

<div></div>

    boost::filesystem3::path::m_erase_redundant_separator(unsigned long)

- Used By:

    - [src/mongo/util/file\_allocator.cpp](../../../file\_allocation)
    - [src/mongo/db/durop.cpp](../../../journaling)
    - [src/mongo/db/dur\_recover.cpp](../../../journaling)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/dur\_journal.cpp](../../../journaling)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/dbhelpers.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/storage/extent\_manager.cpp](../../../storage\_layer\_structure)
    - [src/mongo/tools/dump.cpp](../../../tools)

<div></div>

    boost::filesystem3::path::m_append_separator_if_needed()

- Used By:

    - [src/mongo/util/file\_allocator.cpp](../../../file\_allocation)
    - [src/mongo/db/durop.cpp](../../../journaling)
    - [src/mongo/db/dur\_recover.cpp](../../../journaling)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/dur\_journal.cpp](../../../journaling)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/dbhelpers.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/storage/extent\_manager.cpp](../../../storage\_layer\_structure)
    - [src/mongo/tools/dump.cpp](../../../tools)

<div></div>

    boost::filesystem3::path::filename() const

- Used By:

    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../mongo\_shell)
    - [src/mongo/db/dur\_recover.cpp](../../../journaling)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/pdfile.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/dur\_journal.cpp](../../../journaling)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../mongo\_shell)
    - [src/mongo/tools/restore.cpp](../../../tools)
    - [src/mongo/tools/import.cpp](../../../tools)

### src/third\_party/boost/libs/filesystem/v3/src/unique\_path.cpp

<div></div>

    boost::filesystem3::detail::unique_path(boost::filesystem3::path const&, boost::system::error_code*)

- Used By:

    - [src/mongo/unittest/temp\_dir.cpp](../../../unit\_tests)
