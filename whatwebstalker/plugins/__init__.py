# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 22:13:55 2024

@author: kitty
"""


import os, sys
from importlib import util
import pkgutil
import traceback


class Base:
    """Basic resource class. Concrete resources will inherit from this one
    """
    plugins = []

    # For every class that inherits from the current,
    # the class name will be added to plugins
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.plugins.append(cls)


def load_module(path):
    name = os.path.split(path)[-1].split(".")[0]
    spec = util.spec_from_file_location(name,path)
    print(spec)
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return(module)

__path__ =  os.path.dirname(os.path.abspath(__file__))
__plugins_path__ = '{}\\'.format(__path__)

for fname in os.listdir(__plugins_path__):
    if not fname.startswith("__") and fname.endswith('.py'):
        #print(fname)
        try:
            current_path = "{}{}".format(__plugins_path__,fname)
            print(current_path)
        #    sys.exit(0)
            load_module(current_path)
        except Exception:
            traceback.print_exc()
        

