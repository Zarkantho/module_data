import os.path
import yaml

from utils.structures import AttributeDict, BuildConfiguration
from utils.jobs.runners import async_process_runner as runner
from utils.files import expand_tree
from utils.rstcloth.rstcloth import RstCloth

stage = 'pre'

def jobs(conf):
    conf.km = AttributeDict()
    conf.km.spec = os.path.abspath(os.path.join(conf.paths.projectroot, '..', 
                                                'mongo-' + conf.version.release, 
                                                'modules'))

    data = runner([{'job': BuildConfiguration, 'args': [fn]}
                   for fn in expand_tree(conf.km.spec)], force=False, pool=8)

    for item in data:
        yield { 
            'job': render_page,
            'args': [item, conf]
        }
 
def render_page(doc, conf): 
    r = RstCloth()
    out_fn = os.path.join(conf.paths.projectroot, conf.paths.source, doc.system_name + '.txt')

    r.title(doc.system_title)
    r.newline()
    r.content(doc.system_description)
    r.newline()

    r.write(out_fn)
