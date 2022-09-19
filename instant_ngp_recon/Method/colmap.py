#!/usr/bin/env python
# -*- coding: utf-8 -*-

from instant_ngp_recon.Method.cmd import runCommand

def runCOLMAP():
    cmd = "colmap gui"
    if not runCommand(cmd):
        print("[ERROR][colmap::runCOLMAP]")
        print("\t runCommand failed!")
        return False
    return True

