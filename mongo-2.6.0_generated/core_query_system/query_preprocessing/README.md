# Query Preprocessing
Classes that do processing of queries that is independent of the database state, and does not involve coming up with a plan for executing the query.  This parses the information contained in the query into a structured form that is easier to manage as well as does some normalization of the query (for example, flattening a deep tree of AND operations).


-------------

## Canonical Query
Entry point into the first stage of processing a query.  This is built on top of the Lite Parsed Query, which is the raw interface to information about the query, and the parsed representations of the query and projection.

#### Files
- [src/mongo/db/query/canonical\_query.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/canonical_query.cpp)   (mongod, tools, mongos)
- [src/mongo/db/query/canonical\_query.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/canonical_query.h)   (mongod, tools, mongos)
- [src/mongo/db/query/canonical\_query\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/canonical_query_test.cpp)   ()

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Lite Parsed Query
Lightweight class that parses a raw query message from the network and provides accessors to make the data in the message easier to work with.  Created and managed by the Canonical Query class.

#### Files
- [src/mongo/db/query/lite\_parsed\_query.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/lite_parsed_query.cpp)   (mongod, tools, mongos)
- [src/mongo/db/query/lite\_parsed\_query.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/lite_parsed_query.h)   (mongod, tools, mongos)
- [src/mongo/db/query/lite\_parsed\_query\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/lite_parsed_query_test.cpp)   ()

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Parsed Projection
Class that parses and validates a projection object and can answer questions that factor into query planning, such as what fields are required to satisfy the projection.

#### Files
- [src/mongo/db/query/parsed\_projection.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/parsed_projection.cpp)   (mongod, tools, mongos)
- [src/mongo/db/query/parsed\_projection.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/parsed_projection.h)   (mongod, tools, mongos)
- [src/mongo/db/query/parsed\_projection\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/parsed_projection_test.cpp)   ()

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Query Expression Parser
Matcher expressions. The point of all of this is to take a query string and turn it into a structured set of classes that represents a parsed query. These classes can be used to efficiently test if a document matches the original expression.

#### Files
- [src/mongo/db/matcher/expression.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression.cpp)   (mongod, tools, mongos)
- [src/mongo/db/matcher/expression.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression.h)   (mongod, tools, mongos)
- [src/mongo/db/matcher/expression\_array.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression_array.cpp)   (mongod, tools, mongos)
- [src/mongo/db/matcher/expression\_array.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression_array.h)   (mongod, tools, mongos)
- [src/mongo/db/matcher/expression\_array\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression_array_test.cpp)   ()
- [src/mongo/db/matcher/expression\_geo.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression_geo.cpp)   (mongod, tools, mongos)
- [src/mongo/db/matcher/expression\_geo.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression_geo.h)   (mongod, tools, mongos)
- [src/mongo/db/matcher/expression\_geo\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression_geo_test.cpp)   ()
- [src/mongo/db/matcher/expression\_leaf.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression_leaf.cpp)   (mongod, tools, mongos)
- [src/mongo/db/matcher/expression\_leaf.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression_leaf.h)   (mongod, tools, mongos)
- [src/mongo/db/matcher/expression\_leaf\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression_leaf_test.cpp)   ()
- [src/mongo/db/matcher/expression\_parser.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression_parser.cpp)   (mongod, tools, mongos)
- [src/mongo/db/matcher/expression\_parser.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression_parser.h)   (mongod, tools, mongos)
- [src/mongo/db/matcher/expression\_parser\_array\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression_parser_array_test.cpp)   ()
- [src/mongo/db/matcher/expression\_parser\_geo.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression_parser_geo.cpp)   (mongod, tools, mongos)
- [src/mongo/db/matcher/expression\_parser\_geo\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression_parser_geo_test.cpp)   ()
- [src/mongo/db/matcher/expression\_parser\_leaf\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression_parser_leaf_test.cpp)   ()
- [src/mongo/db/matcher/expression\_parser\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression_parser_test.cpp)   ()
- [src/mongo/db/matcher/expression\_parser\_text.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression_parser_text.cpp)   (mongod, tools, mongos)
- [src/mongo/db/matcher/expression\_parser\_text\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression_parser_text_test.cpp)   ()
- [src/mongo/db/matcher/expression\_parser\_tree.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression_parser_tree.cpp)   (mongod, tools, mongos)
- [src/mongo/db/matcher/expression\_parser\_tree\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression_parser_tree_test.cpp)   ()
- [src/mongo/db/matcher/expression\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression_test.cpp)   ()
- [src/mongo/db/matcher/expression\_text.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression_text.cpp)   (mongod, tools, mongos)
- [src/mongo/db/matcher/expression\_text.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression_text.h)   (mongod, tools, mongos)
- [src/mongo/db/matcher/expression\_tree.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression_tree.cpp)   (mongod, tools, mongos)
- [src/mongo/db/matcher/expression\_tree.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression_tree.h)   (mongod, tools, mongos)
- [src/mongo/db/matcher/expression\_tree\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression_tree_test.cpp)   ()
- [src/mongo/db/matcher/expression\_where.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/expression_where.cpp)   (mongod, tools, mongos)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Matchable Document
Class that holds a BSONObj and provides an interface that the parsed expressions use when determining whether a BSONObj matches.

#### Files
- [src/mongo/db/matcher/matchable.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/matchable.cpp)   (mongod, tools, mongos)
- [src/mongo/db/matcher/matchable.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/matchable.h)   (mongod, tools, mongos)

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## Document Iterators
This contains code to help with iterating arrays and nested documents

#### Files
- [src/mongo/db/matcher/path.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/path.cpp)   (mongod, tools, mongos)
- [src/mongo/db/matcher/path.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/path.h)   (mongod, tools, mongos)
- [src/mongo/db/matcher/path\_internal.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/path_internal.cpp)   (mongod, tools, mongos)
- [src/mongo/db/matcher/path\_internal.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/path_internal.h)   (mongod, tools, mongos)
- [src/mongo/db/matcher/path\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/path_test.cpp)   ()

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

## Document Matcher
Interface to actually test if a document matches.  Wraps a match expression generated from the expression parsing system.

#### Files
- [src/mongo/db/matcher/matcher.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/matcher.cpp)   (mongod, tools, mongos)
- [src/mongo/db/matcher/matcher.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/matcher.h)   (mongod, tools, mongos)
- [src/mongo/db/matcher.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher.h)   (mongod, tools, mongos)

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)

-------------

## Match Details
Helper for requesting more details about what matched our query from the matcher system.

#### Files
- [src/mongo/db/matcher/match\_details.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/match_details.cpp)   (mongod, tools, mongos)
- [src/mongo/db/matcher/match\_details.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/matcher/match_details.h)   (mongod, tools, mongos)

#### [Interface](interface/7)

#### [Dependencies](dependencies/7)

-------------

## Projection Helper
Standalone projection helper that does not represent a stage in the core query system.  Seems to be used only in findAndModify.

#### Files
- [src/mongo/db/projection.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/projection.cpp)   (mongod, tools, mongos)
- [src/mongo/db/projection.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/projection.h)   (mongod, tools, mongos)

#### [Interface](interface/8)

#### [Dependencies](dependencies/8)
