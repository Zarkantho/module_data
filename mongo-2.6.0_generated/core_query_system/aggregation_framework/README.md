# Aggregation Framework
This is the aggregation framework for MongoDB.  It handles code to perform aggregation on a single instance as well as on a sharded cluster.

The basic operation for sharded aggregation is that the mongos does the coordination of the aggregation and makes decisions on what can be done distributed (mapped) and what must be done centralized (reduced/merged).  It then sends out the necessary aggregation commands to the appropriate places.  The distributed step is handled by the source shards that have the inital data, and the merger step is handled by the primary shard for that database.

There are various optimizations that are done as part of this process.  They are split into two categories:  Local, which rewrites the pipeline for more optimal performance on a single node, and Sharded, which rewrites and spits the pipeline for more optimal performance on the level of the whole cluster.  To see these optimizations in action, you can run "db.foo.aggregate([...], { explain : true }) from the mongo shell.  This will show how the pipeline was rewritten throughout the course of the operation.


-------------

## Mongod Aggregation Commands
Entry point into aggregation for mongod.  These are all database Commands run using db.$cmd.findOne(...)

#### Files
- [src/mongo/db/commands/pipeline\_command.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/commands/pipeline_command.cpp)   (mongod, tools)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Accumulators
An accumulator represents a stateful operation.  For example, in an operation such as $sum, you can feed in values until there is no more data, then extract the final result

#### Files
- [src/mongo/db/pipeline/accumulator.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/accumulator.h)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/accumulator\_add\_to\_set.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/accumulator_add_to_set.cpp)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/accumulator\_avg.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/accumulator_avg.cpp)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/accumulator\_first.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/accumulator_first.cpp)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/accumulator\_last.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/accumulator_last.cpp)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/accumulator\_min\_max.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/accumulator_min_max.cpp)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/accumulator\_push.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/accumulator_push.cpp)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/accumulator\_sum.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/accumulator_sum.cpp)   (mongod, tools, mongos)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## BSON Representation
In memory representation of BSON for aggregation.  Similar to a the BSONElement/BSONObj interface except the Value class does not contain its key like a BSONElement, and the Document class is just a map of keys to values

#### Files
- [src/mongo/db/pipeline/value.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/value.cpp)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/value.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/value.h)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/value\_internal.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/value_internal.h)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/document.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/document.cpp)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/document.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/document.h)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/document\_internal.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/document_internal.h)   (mongod, tools, mongos)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Pipeline Stages
Files containing the pipeline stages.  Document Source is the name for a pipeline stage in our code

#### Files
- [src/mongo/db/pipeline/document\_source.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/document_source.cpp)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/document\_source.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/document_source.h)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/document\_source\_bson\_array.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/document_source_bson_array.cpp)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/document\_source\_command\_shards.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/document_source_command_shards.cpp)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/document\_source\_cursor.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/document_source_cursor.cpp)   (mongod, tools)
- [src/mongo/db/pipeline/document\_source\_geo\_near.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/document_source_geo_near.cpp)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/document\_source\_group.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/document_source_group.cpp)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/document\_source\_limit.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/document_source_limit.cpp)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/document\_source\_match.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/document_source_match.cpp)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/document_source_merge_cursors.cpp)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/document\_source\_out.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/document_source_out.cpp)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/document\_source\_project.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/document_source_project.cpp)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/document\_source\_redact.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/document_source_redact.cpp)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/document\_source\_skip.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/document_source_skip.cpp)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/document\_source\_sort.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/document_source_sort.cpp)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/document\_source\_unwind.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/document_source_unwind.cpp)   (mongod, tools, mongos)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Expressions
An expression represents a stateless operation.  For example, in an operation such as $add, you provide a set of values, and immediately recieve a result

#### Files
- [src/mongo/db/pipeline/expression.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/expression.cpp)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/expression.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/expression.h)   (mongod, tools, mongos)

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## Pipeline Stage Context
This file is currently misnamed.  The context for a pipeline stage, such as whether its being run on a Source (source shard) or a Merger (primary shard responsible for merging results), whether there has been an interrupt, and other global information.

#### Files
- [src/mongo/db/pipeline/expression\_context.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/expression_context.h)   (mongod, tools, mongos)

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

## Dotted Field Utilities
Wrapper classes for parsed and validated dotted field names

#### Files
- [src/mongo/db/pipeline/field\_path.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/field_path.cpp)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/field\_path.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/field_path.h)   (mongod, tools, mongos)

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)

-------------

## Aggregation Common Entry Point
These files contain the central entry point for aggregation.  While the initial entry points for mongos and mongod differ, most of the aggregation code is shared between them.  This holds the two paths together, and also contains the optimization code

#### Files
- [src/mongo/db/pipeline/pipeline.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/pipeline.cpp)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/pipeline.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/pipeline.h)   (mongod, tools, mongos)

#### [Interface](interface/7)

#### [Dependencies](dependencies/7)

-------------

## Mongod Specific Aggregation Extensions
Mongod specific extensions to aggregation

#### Files
- [src/mongo/db/pipeline/pipeline\_d.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/pipeline_d.cpp)   (mongod, tools)
- [src/mongo/db/pipeline/pipeline\_d.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/pipeline_d.h)   (mongod, tools)

#### [Interface](interface/8)

#### [Dependencies](dependencies/8)

-------------

## Pipeline Optimizations
Optimizations that are done as part of the aggregation process.  There are two optimization types, local and sharded.  In a sharded cluster, first the local optimizations are done which rewrites the pipeline stages, then the sharded optimizations are done, which controls exactly what gets farmed out to the source shards, then each source shard runs the local optimization again

#### Files
- [src/mongo/db/pipeline/pipeline\_optimizations.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/pipeline_optimizations.h)   (mongod, tools, mongos)

#### [Interface](interface/9)

#### [Dependencies](dependencies/9)

-------------

## Data Dependency Tracking
Code to track what information is needed in the aggregation pipeline.  For example, for some queries only certain fields of the document are actually needed

#### Files
- [src/mongo/db/pipeline/dependencies.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/dependencies.cpp)   (mongod, tools, mongos)
- [src/mongo/db/pipeline/dependencies.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/pipeline/dependencies.h)   (mongod, tools, mongos)

#### [Interface](interface/10)

#### [Dependencies](dependencies/10)

-------------

## Sorter
Generic interface for getting and merging sorted streams of documents. Only used in aggregation

#### Files
- [src/mongo/db/sorter/sorter.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/sorter/sorter.cpp)   (mongod, tools, mongos)
- [src/mongo/db/sorter/sorter.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/sorter/sorter.h)   (mongod, tools, mongos)
- [src/mongo/db/sorter/sorter\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/sorter/sorter_test.cpp)   ()

#### [Interface](interface/11)

#### [Dependencies](dependencies/11)

-------------

## External Sorter
Code for external sort. This sits inside the sorter, and the sorter "spills over" to disk if external sorting is allowed

#### Files
- [src/mongo/db/extsort.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/extsort.cpp)   (mongod, tools)
- [src/mongo/db/extsort.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/extsort.h)   (mongod, tools)

#### [Interface](interface/12)

#### [Dependencies](dependencies/12)

-------------

## Index Key Sorter
Wrapper around the External Sorter specialized for index keys.  Used in bottom up fast index builds where keys are pre sorted.

#### Files
- [src/mongo/db/sort\_phase\_one.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/sort_phase_one.h)   (mongod, tools)

#### [Interface](interface/13)

#### [Dependencies](dependencies/13)
