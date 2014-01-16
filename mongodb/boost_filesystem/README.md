# boost\_filesystem

# Module Groups

-------------

Third Party - The boost filesystem library

- src/third\_party/boost/boost/filesystem.hpp
- src/third\_party/boost/boost/filesystem/config.hpp
- src/third\_party/boost/boost/filesystem/convenience.hpp
- src/third\_party/boost/boost/filesystem/detail/utf8\_codecvt\_facet.hpp
- src/third\_party/boost/boost/filesystem/operations.hpp
- src/third\_party/boost/boost/filesystem/path.hpp
- src/third\_party/boost/boost/filesystem/v2/config.hpp
- src/third\_party/boost/boost/filesystem/v2/convenience.hpp
- src/third\_party/boost/boost/filesystem/v2/operations.hpp
- src/third\_party/boost/boost/filesystem/v2/path.hpp
- src/third\_party/boost/boost/filesystem/v3/config.hpp
- src/third\_party/boost/boost/filesystem/v3/convenience.hpp
- src/third\_party/boost/boost/filesystem/v3/operations.hpp
- src/third\_party/boost/boost/filesystem/v3/path.hpp
- src/third\_party/boost/boost/filesystem/v3/path\_traits.hpp
- src/third\_party/boost/libs/filesystem/v2/src/v2\_operations.cpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/libs/filesystem/v2/src/v2\_path.cpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/libs/filesystem/v2/src/v2\_portability.cpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/libs/filesystem/v3/src/codecvt\_error\_category.cpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/libs/filesystem/v3/src/operations.cpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/libs/filesystem/v3/src/path.cpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/libs/filesystem/v3/src/path\_traits.cpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/libs/filesystem/v3/src/portability.cpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/libs/filesystem/v3/src/unique\_path.cpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/libs/filesystem/v3/src/utf8\_codecvt\_facet.cpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/libs/filesystem/v3/src/windows\_file\_codecvt.cpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/libs/filesystem/v3/src/windows\_file\_codecvt.hpp
- src/third\_party/boost/libs/detail/utf8\_codecvt\_facet.cpp

## Interface


### src/third\_party/boost/libs/filesystem/v3/src/operations.cpp

<pre>boost::filesystem3::absolute(boost::filesystem3::path const&, boost::filesystem3::path const&)</pre>

#### Used By:

- [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
- [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
- [src/mongo/util/net/ssl\_options.cpp](../network)
- [src/mongo/util/mmap.cpp](../mmap)

<pre>boost::filesystem3::detail::directory_iterator_construct(boost::filesystem3::directory_iterator&, boost::filesystem3::path const&, boost::system::error_code*)</pre>

#### Used By:

- [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
- [src/mongo/db/dur\_recover.cpp](../journaling)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/dur\_journal.cpp](../journaling)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
- [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
- [src/mongo/tools/restore.cpp](../tools)
- [src/mongo/scripting/engine.cpp](../javascript\_libraries)

<pre>boost::filesystem3::detail::temp_directory_path(boost::system::error_code*)</pre>

#### Used By:

- [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)

<pre>boost::filesystem3::detail::rename(boost::filesystem3::path const&, boost::filesystem3::path const&, boost::system::error_code*)</pre>

#### Used By:

- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/db/dur\_journal.cpp](../journaling)

<pre>boost::filesystem3::detail::directory_iterator_increment(boost::filesystem3::directory_iterator&, boost::system::error_code*)</pre>

#### Used By:

- [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
- [src/mongo/db/dur\_recover.cpp](../journaling)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/dur\_journal.cpp](../journaling)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
- [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
- [src/mongo/tools/restore.cpp](../tools)
- [src/mongo/scripting/engine.cpp](../javascript\_libraries)

<pre>boost::filesystem3::detail::initial_path(boost::system::error_code*)</pre>

#### Used By:

- [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)

<pre>boost::filesystem3::detail::status(boost::filesystem3::path const&, boost::system::error_code*)</pre>

#### Used By:

- [src/mongo/util/file\_allocator.cpp](../file\_allocation)
- [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
- [src/mongo/db/dur\_journal.cpp](../journaling)
- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/scripting/engine.cpp](../javascript\_libraries)
- [src/mongo/tools/import.cpp](../tools)
- [src/mongo/util/file\_allocator.cpp](../file\_allocation)
- [src/mongo/db/dur\_recover.cpp](../journaling)
- [src/mongo/client/gridfs.cpp](../cpp\_client\_driver)
- [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
- [src/mongo/tools/tool\_options.cpp](../tools)
- [src/mongo/db/durop.cpp](../journaling)
- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/tools/restore.cpp](../tools)
- [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)
- [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
- [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
- [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/util/mmap.cpp](../mmap)
- [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
- [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)
- [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
- [src/mongo/client/gridfs.cpp](../cpp\_client\_driver)

<pre>boost::filesystem3::path_traits::dispatch(boost::filesystem3::directory_entry const&, std::string&, std::codecvt<wchar_t, char, __mbstate_t> const&)</pre>

#### Used By:

- [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
- [src/mongo/db/dur\_recover.cpp](../journaling)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/dur\_journal.cpp](../journaling)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
- [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
- [src/mongo/tools/restore.cpp](../tools)
- [src/mongo/scripting/engine.cpp](../javascript\_libraries)

<pre>boost::filesystem3::detail::create_directory(boost::filesystem3::path const&, boost::system::error_code*)</pre>

#### Used By:

- [src/mongo/util/file\_allocator.cpp](../file\_allocation)
- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)
- [src/mongo/util/file\_allocator.cpp](../file\_allocation)
- [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
- [src/mongo/db/dur\_journal.cpp](../journaling)
- [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
- [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)

<pre>boost::filesystem3::detail::file_size(boost::filesystem3::path const&, boost::system::error_code*)</pre>

#### Used By:

- [src/mongo/util/file\_allocator.cpp](../file\_allocation)
- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
- [src/mongo/db/dur\_recover.cpp](../journaling)
- [src/mongo/tools/tool.cpp](../tools)
- [src/mongo/util/file\_allocator.cpp](../file\_allocation)
- [src/mongo/db/dur\_journal.cpp](../journaling)
- [src/mongo/util/mmap.cpp](../mmap)
- [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
- [src/mongo/db/extsort.cpp](../aggregation\_framework)
- [src/mongo/tools/restore.cpp](../tools)
- [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/tools/import.cpp](../tools)
- [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)

<pre>boost::filesystem3::detail::dir_itr_close(void*&, void*&)</pre>

#### Used By:

- [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
- [src/mongo/db/dur\_recover.cpp](../journaling)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/dur\_journal.cpp](../journaling)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
- [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
- [src/mongo/tools/restore.cpp](../tools)
- [src/mongo/scripting/engine.cpp](../javascript\_libraries)

<pre>boost::filesystem3::detail::copy_file(boost::filesystem3::path const&, boost::filesystem3::path const&, boost::filesystem3::copy_option::enum_type, boost::system::error_code*)</pre>

#### Used By:

- [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)

<pre>boost::filesystem3::detail::remove(boost::filesystem3::path const&, boost::system::error_code*)</pre>

#### Used By:

- [src/mongo/util/file\_allocator.cpp](../file\_allocation)
- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
- [src/mongo/db/durop.cpp](../journaling)
- [src/mongo/util/file\_allocator.cpp](../file\_allocation)
- [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)
- [src/mongo/db/dur\_journal.cpp](../journaling)
- [src/mongo/db/extsort.cpp](../aggregation\_framework)
- [src/mongo/client/examples/mongoperf.cpp](../cpp\_client\_driver)
- [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)
- [src/mongo/dbtests/mmaptests.cpp](../unit\_tests)

<pre>boost::filesystem3::detail::remove_all(boost::filesystem3::path const&, boost::system::error_code*)</pre>

#### Used By:

- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
- [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
- [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
- [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)

<pre>boost::filesystem3::detail::create_directories(boost::filesystem3::path const&, boost::system::error_code*)</pre>

#### Used By:

- [src/mongo/db/pipeline/document\_source\_sort.cpp](../aggregation\_framework)
- [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
- [src/mongo/db/pipeline/document\_source\_group.cpp](../aggregation\_framework)
- [src/mongo/db/extsort.cpp](../aggregation\_framework)
- [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
- [src/mongo/tools/export.cpp](../tools)
- [src/mongo/tools/dump.cpp](../tools)

<pre>boost::filesystem3::detail::current_path(boost::system::error_code*)</pre>

#### Used By:

- [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
- [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
- [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
- [src/mongo/util/net/ssl\_options.cpp](../network)
- [src/mongo/util/mmap.cpp](../mmap)

### src/third\_party/boost/libs/filesystem/v3/src/path.cpp

<pre>boost::filesystem3::path::operator/=(char const*)</pre>

#### Used By:

- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)
- [src/mongo/db/dur\_journal.cpp](../journaling)

<pre>boost::filesystem3::path::wchar_t_codecvt_facet()</pre>

#### Used By:

- [src/mongo/util/file\_allocator.cpp](../file\_allocation)
- [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
- [src/mongo/db/durop.cpp](../journaling)
- [src/mongo/db/dur\_recover.cpp](../journaling)
- [src/mongo/util/file\_allocator.cpp](../file\_allocation)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/dur\_journal.cpp](../journaling)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
- [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
- [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
- [src/mongo/tools/restore.cpp](../tools)
- [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
- [src/mongo/scripting/engine.cpp](../javascript\_libraries)
- [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)
- [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
- [src/mongo/tools/dump.cpp](../tools)

<pre>boost::filesystem3::path::operator/=(boost::filesystem3::path const&)</pre>

#### Used By:

- [src/mongo/util/file\_allocator.cpp](../file\_allocation)
- [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
- [src/mongo/dbtests/mmaptests.cpp](../unit\_tests)
- [src/mongo/util/file\_allocator.cpp](../file\_allocation)
- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/db/dur\_journal.cpp](../journaling)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
- [src/mongo/tools/restore.cpp](../tools)
- [src/mongo/tools/dump.cpp](../tools)

<pre>boost::filesystem3::path::parent_path() const</pre>

#### Used By:

- [src/mongo/util/file\_allocator.cpp](../file\_allocation)
- [src/mongo/util/file\_allocator.cpp](../file\_allocation)
- [src/mongo/tools/restore.cpp](../tools)

<pre>boost::filesystem3::path::m_erase_redundant_separator(unsigned long)</pre>

#### Used By:

- [src/mongo/util/file\_allocator.cpp](../file\_allocation)
- [src/mongo/util/file\_allocator.cpp](../file\_allocation)
- [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)
- [src/mongo/db/dur\_recover.cpp](../journaling)
- [src/mongo/db/dur\_journal.cpp](../journaling)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
- [src/mongo/tools/dump.cpp](../tools)
- [src/mongo/db/durop.cpp](../journaling)

<pre>boost::filesystem3::path::m_append_separator_if_needed()</pre>

#### Used By:

- [src/mongo/util/file\_allocator.cpp](../file\_allocation)
- [src/mongo/util/file\_allocator.cpp](../file\_allocation)
- [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)
- [src/mongo/db/dur\_recover.cpp](../journaling)
- [src/mongo/db/dur\_journal.cpp](../journaling)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/storage/extent\_manager.cpp](../storage\_layer\_structure)
- [src/mongo/tools/dump.cpp](../tools)
- [src/mongo/db/durop.cpp](../journaling)

<pre>boost::filesystem3::path::filename() const</pre>

#### Used By:

- [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
- [src/mongo/db/dur\_recover.cpp](../journaling)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
- [src/mongo/db/dur\_journal.cpp](../journaling)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
- [src/mongo/tools/restore.cpp](../tools)
- [src/mongo/tools/import.cpp](../tools)

### src/third\_party/boost/libs/filesystem/v3/src/unique\_path.cpp

<pre>boost::filesystem3::detail::unique_path(boost::filesystem3::path const&, boost::system::error_code*)</pre>

#### Used By:

- [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
