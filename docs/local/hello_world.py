"""
This is an example of how to extend the docs build system. The protocol for
extensions is:

- You must declare an module level variable named "stage". If the value starts
  with "pre" then it will run before sphinx.

- You must define an callable named "jobs" that takes a single "conf" argument
  and returns an interable (e.g. function returning a list, generator function,
  iterable object, etc.) The value of the parameter is the configuration object for the
  build system.

  The iterable should produce dicts in the following form: 

  { 
    'job': <callable>,
    'args': <arguments>,
    'target': <Optional>,
    'dependency': <Optional>
  }

  These fields are:

  - ``job``: a callable, defined or imported in the current module. 

  - ``args``: a list of arguments, may either be a tuple or list for positional
    arguments, or a dict for keyword arguments.

  - ``target`` and ``dependency`` paths. If specified and dependency has an
    ``mtime`` that is newer than ``target``, then the job will run otherwise the
    job will not run. If ``target`` doesn't exist or either value is ``None``
    the target will *always* run.

"""

import json

stage = 'deactivated'
   
def hello_world():
    return 'generic hello world message'

def pprint(doc):
    print(json.dumps(doc, indent=3))

def jobs(conf):
    yield { 'args': [{'msg': hello_world() }], 'job': pprint }
