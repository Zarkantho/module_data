import yaml
import sys
import logging
import os
import multiprocessing 

logger = logging.getLogger(os.path.basename(__file__))
logging.basicConfig(level=logging.DEBUG)

def main():
    in_file = sys.argv[1]
    out_path = sys.argv[2]

    if not os.path.exists(out_path): 
        logger.info('created {0}'.format(out_path))
        os.makedirs(out_path)
    elif not os.path.isdir(out_path):
        logger.error('[error]: {0} exists, but is not a directory'.format(out_path))
        exit(1)

    r = []
    p = multiprocessing.Pool()
    logger.debug('created pool')

    with open(in_file, 'r') as rf:
        logger.info('reading in data now')
        data = yaml.load(rf)
        logger.info('data loaded. uff')

        for idx, doc in enumerate(data): 
            wfn = os.path.join(out_path, str(idx) + '.yaml')
            r.append(p.apply_async(write_doc, args=(doc, wfn)))
            logger.debug('added {0} to queue'.format(wfn))

        logger.debug('closing pool')
        p.close()
        logger.debug('waiting for pool to finish')
        p.join()
        
    r = [ o.get() for o in r ]

def write_doc(doc, fn):
    with open(fn, 'w') as f:
        logger.info("wrote to {0}".format(fn))
        yaml.dump(doc, f)

if __name__ == '__main__':
    main()
