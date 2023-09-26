#!/usr/bin/env python
# -*- coding: utf-8 -*-

from instant_ngp.Method.cmd import runCMD

def runInstantNGP(scene_folder_path):
    cmd = "cd ../ingp && " + \
        "./build/instant-ngp" + \
        " --scene " + scene_folder_path
    if not runCMD(cmd, True):
        print("[ERROR][nerf::runInstantNGP]")
        print("\t runCMD failed!")
        return False
    return True
