#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import Popen

def runCommand(cmd):
    ex = Popen(cmd, shell=True)
    _, _ = ex.communicate()
    status = ex.wait()
    return status == 0

