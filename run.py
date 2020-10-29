#!/usr/bin/env python
import sys
import json
from etl import get_data
def main(targets):
    if 'DBLP' in targets:
        with open('config/data-params.json') as fh:
            data_cfg = json.load(fh)
        # make the data target
        get_data(data_cfg)
    return
if __name__ == '__main__':
    targets = sys.argv[1]
    main(targets)
