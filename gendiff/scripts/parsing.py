#!/usr/bin/env python3

import json
import yaml


def fix_file(filename):
    extension = filename.split('.')[-1]
    if extension == 'json':
        return json.load(open(str(filename)))
    else:
        with open(filename) as f:
            return yaml.safe_load(f)
