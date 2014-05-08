
# Interface for Boost Filesystem
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/third\_party/boost/libs/filesystem/v3/src/operations.cpp

<div></div>

    boost::filesystem3::absolute(boost::filesystem3::path const&, boost::filesystem3::path const&)

- Used By:

    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/util/mmap.cpp](../../../../storage/data\_files)
    - [src/mongo/util/net/ssl\_options.cpp](../../../../network/ssl)

<div></div>

    boost::filesystem3::detail::directory_iterator_construct(boost::filesystem3::directory_iterator&, boost::filesystem3::path const&, boost::system::error_code*)

- Used By:

    - [src/mongo/scripting/engine.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/dbtests/framework\_options.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)

<div></div>

    boost::filesystem3::detail::temp_directory_path(boost::system::error_code*)

- Used By:

    - [src/mongo/unittest/temp\_dir.cpp](../../../../tests/unit\_tests)

<div></div>

    boost::filesystem3::detail::rename(boost::filesystem3::path const&, boost::filesystem3::path const&, boost::system::error_code*)

- Used By:

    - [src/mongo/db/repair\_database.cpp](../../../../storage/repair\_database)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)

<div></div>

    boost::filesystem3::detail::directory_iterator_increment(boost::filesystem3::directory_iterator&, boost::system::error_code*)

- Used By:

    - [src/mongo/scripting/engine.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/dbtests/framework\_options.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)

<div></div>

    boost::filesystem3::detail::initial_path(boost::system::error_code*)

- Used By:

    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../../mongo\_shell/mongo\_shell)

<div></div>

    boost::filesystem3::detail::status(boost::filesystem3::path const&, boost::system::error_code*)

- Used By:

    - [src/mongo/util/mmap.cpp](../../../../storage/data\_files)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/unittest/temp\_dir.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/framework\_options.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/util/file\_allocator.cpp](../../../../storage/file\_allocation)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/scripting/engine.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/storage/extent\_manager.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/tools/import.cpp](../../../../tools/tools)
    - [src/mongo/shell/shell\_utils.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/storage/data\_file.cpp](../../../../storage/data\_files)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/tools/tool\_options.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/durop.cpp](../../../../storage/journaling)
    - [src/mongo/db/repair\_database.cpp](../../../../storage/repair\_database)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/client/gridfs.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    boost::filesystem3::path_traits::dispatch(boost::filesystem3::directory_entry const&, std::string&, std::codecvt<wchar_t, char, __mbstate_t> const&)

- Used By:

    - [src/mongo/scripting/engine.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/dbtests/framework\_options.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)

<div></div>

    boost::filesystem3::detail::create_directory(boost::filesystem3::path const&, boost::system::error_code*)

- Used By:

    - [src/mongo/util/file\_allocator.cpp](../../../../storage/file\_allocation)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/unittest/temp\_dir.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repair\_database.cpp](../../../../storage/repair\_database)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/dbtests/framework\_options.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    boost::filesystem3::detail::file_size(boost::filesystem3::path const&, boost::system::error_code*)

- Used By:

    - [src/mongo/db/storage/extent\_manager.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/extsort.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/tools/import.cpp](../../../../tools/tools)
    - [src/mongo/util/file\_allocator.cpp](../../../../storage/file\_allocation)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/util/mmap.cpp](../../../../storage/data\_files)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)
    - [src/mongo/db/repair\_database.cpp](../../../../storage/repair\_database)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    boost::filesystem3::detail::dir_itr_close(void*&, void*&)

- Used By:

    - [src/mongo/scripting/engine.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/dbtests/framework\_options.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)

<div></div>

    boost::filesystem3::detail::copy_file(boost::filesystem3::path const&, boost::filesystem3::path const&, boost::filesystem3::copy_option::enum_type, boost::system::error_code*)

- Used By:

    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/repair\_database.cpp](../../../../storage/repair\_database)

<div></div>

    boost::filesystem3::detail::remove(boost::filesystem3::path const&, boost::system::error_code*)

- Used By:

    - [src/mongo/db/extsort.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/dbtests/mmaptests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/util/file\_allocator.cpp](../../../../storage/file\_allocation)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/client/examples/mongoperf.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/dbcommands\_admin.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/durop.cpp](../../../../storage/journaling)
    - [src/mongo/db/repair\_database.cpp](../../../../storage/repair\_database)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    boost::filesystem3::detail::remove_all(boost::filesystem3::path const&, boost::system::error_code*)

- Used By:

    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/unittest/temp\_dir.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repair\_database.cpp](../../../../storage/repair\_database)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/dbtests/framework\_options.cpp](../../../../tests/unit\_tests)

<div></div>

    boost::filesystem3::detail::create_directories(boost::filesystem3::path const&, boost::system::error_code*)

- Used By:

    - [src/mongo/db/extsort.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)
    - [src/mongo/db/pipeline/document\_source\_group.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/tools/export.cpp](../../../../tools/tools)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/pipeline/document\_source\_sort.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../../mongo\_shell/mongo\_shell)

<div></div>

    boost::filesystem3::detail::current_path(boost::system::error_code*)

- Used By:

    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/util/mmap.cpp](../../../../storage/data\_files)
    - [src/mongo/util/net/ssl\_options.cpp](../../../../network/ssl)

### src/third\_party/boost/libs/filesystem/v3/src/path.cpp

<div></div>

    boost::filesystem3::path::operator/=(char const*)

- Used By:

    - [src/mongo/db/dbcommands\_admin.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)

<div></div>

    boost::filesystem3::path::wchar_t_codecvt_facet()

- Used By:

    - [src/mongo/db/durop.cpp](../../../../storage/journaling)
    - [src/mongo/scripting/engine.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/unittest/temp\_dir.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)
    - [src/mongo/util/file\_allocator.cpp](../../../../storage/file\_allocation)
    - [src/mongo/dbtests/framework\_options.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/repair\_database.cpp](../../../../storage/repair\_database)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)
    - [src/mongo/db/storage/extent\_manager.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    boost::filesystem3::path::operator/=(boost::filesystem3::path const&)

- Used By:

    - [src/mongo/dbtests/mmaptests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)
    - [src/mongo/util/file\_allocator.cpp](../../../../storage/file\_allocation)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/unittest/temp\_dir.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repair\_database.cpp](../../../../storage/repair\_database)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)

<div></div>

    boost::filesystem3::path::parent_path() const

- Used By:

    - [src/mongo/tools/restore.cpp](../../../../tools/tools)
    - [src/mongo/util/file\_allocator.cpp](../../../../storage/file\_allocation)

<div></div>

    boost::filesystem3::path::m_erase_redundant_separator(unsigned long)

- Used By:

    - [src/mongo/db/storage/extent\_manager.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/util/file\_allocator.cpp](../../../../storage/file\_allocation)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)
    - [src/mongo/db/durop.cpp](../../../../storage/journaling)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/repair\_database.cpp](../../../../storage/repair\_database)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    boost::filesystem3::path::m_append_separator_if_needed()

- Used By:

    - [src/mongo/db/storage/extent\_manager.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/util/file\_allocator.cpp](../../../../storage/file\_allocation)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)
    - [src/mongo/db/durop.cpp](../../../../storage/journaling)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/repair\_database.cpp](../../../../storage/repair\_database)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    boost::filesystem3::path::filename() const

- Used By:

    - [src/mongo/tools/import.cpp](../../../../tools/tools)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/repair\_database.cpp](../../../../storage/repair\_database)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/tools/restore.cpp](../../../../tools/tools)

### src/third\_party/boost/libs/filesystem/v3/src/unique\_path.cpp

<div></div>

    boost::filesystem3::detail::unique_path(boost::filesystem3::path const&, boost::system::error_code*)

- Used By:

    - [src/mongo/unittest/temp\_dir.cpp](../../../../tests/unit\_tests)
