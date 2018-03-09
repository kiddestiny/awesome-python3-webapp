#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Configuration
'''

import config_default


class Dict(dict):
    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, item):
        try
            return self[item]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % item)

    def __setattr__(self, key, value):
        self[key] = value

    @classmethod
    def from_dict(cls, src_dict):
        d = Dict()
        for k, v in src_dict.items():
            d[k] = cls.from_dict(v) if isinstance(v, dict) else v
        return d
