# boost\_program\_options

# Module Groups

-------------

# Group Description
Third Party - The boost program\_options library

# Files
- src/third\_party/boost/boost/program\_options.hpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/boost/program\_options/cmdline.hpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/boost/program\_options/config.hpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/boost/program\_options/detail/cmdline.hpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/boost/program\_options/detail/config\_file.hpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/boost/program\_options/detail/convert.hpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/boost/program\_options/detail/parsers.hpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/boost/program\_options/detail/utf8\_codecvt\_facet.hpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/boost/program\_options/detail/value\_semantic.hpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/boost/program\_options/environment\_iterator.hpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/boost/program\_options/eof\_iterator.hpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/boost/program\_options/errors.hpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/boost/program\_options/option.hpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/boost/program\_options/options\_description.hpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/boost/program\_options/parsers.hpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/boost/program\_options/positional\_options.hpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/boost/program\_options/value\_semantic.hpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/boost/program\_options/variables\_map.hpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/boost/program\_options/version.hpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/libs/program\_options/src/cmdline.cpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/libs/program\_options/src/config\_file.cpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/libs/program\_options/src/convert.cpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/libs/program\_options/src/options\_description.cpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/libs/program\_options/src/parsers.cpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/libs/program\_options/src/positional\_options.cpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/libs/program\_options/src/split.cpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/libs/program\_options/src/utf8\_codecvt\_facet.cpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/libs/program\_options/src/value\_semantic.cpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/libs/program\_options/src/variables\_map.cpp   (mongod, cppclientdriver, tools, mongos)
- src/third\_party/boost/libs/program\_options/src/winmain.cpp   (mongod, cppclientdriver, tools, mongos)

# Interface

### src/third\_party/boost/libs/program\_options/src/cmdline.cpp

<div></div>

    boost::program_options::detail::cmdline::run()

- Used By:

    - [src/mongo/util/options\_parser/options\_parser.cpp](../startup\_initialization)

<div></div>

    boost::program_options::detail::cmdline::set_options_description(boost::program_options::options_description const&)

- Used By:

    - [src/mongo/util/options\_parser/options\_parser.cpp](../startup\_initialization)

<div></div>

    boost::program_options::detail::cmdline::cmdline(std::vector<std::string, std::allocator<std::string> > const&)

- Used By:

    - [src/mongo/util/options\_parser/options\_parser.cpp](../startup\_initialization)

<div></div>

    boost::program_options::detail::cmdline::style(int)

- Used By:

    - [src/mongo/util/options\_parser/options\_parser.cpp](../startup\_initialization)

<div></div>

    boost::program_options::detail::cmdline::set_positional_options(boost::program_options::positional_options_description const&)

- Used By:

    - [src/mongo/util/options\_parser/options\_parser.cpp](../startup\_initialization)

### src/third\_party/boost/libs/program\_options/src/convert.cpp

<div></div>

    boost::program_options::to_internal(std::string const&)

- Used By:

    - [src/mongo/util/options\_parser/options\_parser.cpp](../startup\_initialization)

### src/third\_party/boost/libs/program\_options/src/options\_description.cpp

<div></div>

    boost::program_options::options_description::add_options()

- Used By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    boost::program_options::options_description::options_description(std::string const&, unsigned int, unsigned int)

- Used By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    boost::program_options::operator<<(std::ostream&, boost::program_options::options_description const&)

- Used By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    boost::program_options::options_description::add(boost::program_options::options_description const&)

- Used By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    boost::program_options::options_description::m_default_line_length

- Used By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)
    - [src/mongo/util/options\_parser/options\_parser.cpp](../startup\_initialization)

<div></div>

    boost::program_options::options_description::options_description(unsigned int, unsigned int)

- Used By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)
    - [src/mongo/util/options\_parser/options\_parser.cpp](../startup\_initialization)

<div></div>

    boost::program_options::options_description_easy_init::operator()(char const*, boost::program_options::value_semantic const*, char const*)

- Used By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

### src/third\_party/boost/libs/program\_options/src/parsers.cpp

<div></div>

    boost::program_options::basic_parsed_options<char> boost::program_options::parse_config_file<char>(std::basic_istream<char, std::char_traits<char> >&, boost::program_options::options_description const&, bool)

- Used By:

    - [src/mongo/util/options\_parser/options\_parser.cpp](../startup\_initialization)

### src/third\_party/boost/libs/program\_options/src/positional\_options.cpp

<div></div>

    boost::program_options::positional_options_description::max_total_count() const

- Used By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    boost::program_options::positional_options_description::add(char const*, int)

- Used By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    boost::program_options::positional_options_description::positional_options_description()

- Used By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)
    - [src/mongo/util/options\_parser/options\_parser.cpp](../startup\_initialization)

<div></div>

    boost::program_options::positional_options_description::name_for_position(unsigned int) const

- Used By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

### src/third\_party/boost/libs/program\_options/src/value\_semantic.cpp

<div></div>

    vtable for boost::program_options::validation_error

- Used By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    boost::program_options::validate(boost::any&, std::vector<std::string, std::allocator<std::string> > const&, bool*, int)

- Used By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    boost::program_options::validators::check_first_occurrence(boost::any const&)

- Used By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    boost::program_options::validation_error::what() const

- Used By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    boost::program_options::arg

- Used By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    boost::program_options::value_semantic_codecvt_helper<char>::parse(boost::any&, std::vector<std::string, std::allocator<std::string> > const&, bool) const

- Used By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    boost::program_options::validation_error::validation_error(boost::program_options::validation_error::kind_t, std::string const&, std::string const&)

- Used By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    typeinfo for boost::program_options::validation_error

- Used By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    typeinfo for boost::program_options::value_semantic_codecvt_helper<char>

- Used By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    boost::program_options::multiple_occurrences::get_option_name() const

- Used By:

    - [src/mongo/util/options\_parser/options\_parser.cpp](../startup\_initialization)

<div></div>

    boost::program_options::invalid_option_value::invalid_option_value(std::string const&)

- Used By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    vtable for boost::program_options::value_semantic_codecvt_helper<char>

- Used By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    boost::program_options::validate(boost::any&, std::vector<std::string, std::allocator<std::string> > const&, std::string*, int)

- Used By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

<div></div>

    boost::program_options::bool_switch()

- Used By:

    - [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)

### src/third\_party/boost/libs/program\_options/src/variables\_map.cpp

<div></div>

    boost::program_options::variables_map::variables_map()

- Used By:

    - [src/mongo/util/options\_parser/options\_parser.cpp](../startup\_initialization)

<div></div>

    boost::program_options::store(boost::program_options::basic_parsed_options<char> const&, boost::program_options::variables_map&, bool)

- Used By:

    - [src/mongo/util/options\_parser/options\_parser.cpp](../startup\_initialization)

<div></div>

    boost::program_options::abstract_variables_map::operator[](std::string const&) const

- Used By:

    - [src/mongo/util/options\_parser/options\_parser.cpp](../startup\_initialization)

<div></div>

    vtable for boost::program_options::variables_map

- Used By:

    - [src/mongo/util/options\_parser/options\_parser.cpp](../startup\_initialization)

# Dependencies
(no dependencies outside this module)
