#!/usr/bin/env python
# -*- coding: utf-8 -*-

from instant_ngp.Method.cmd import runCommand

def colmap2Nerf(
    image_folder_path,
    colmap_camera_text_folder_path,
    save_transform_json_folder_path,
    aabb_scale=16
):
    cmd = "cd ~/github/instant-ngp/scripts && " + \
        "python colmap2nerf.py" + \
        " --images " + image_folder_path + \
        " --text " + colmap_camera_text_folder_path + \
        " --out " + save_transform_json_folder_path + \
        " --aabb_scale " + str(aabb_scale)
    if not runCommand(cmd):
        print("[ERROR][nerf::colmap2Nerf]")
        print("\t runCommand failed!")
        return False
    return True

def runInstantNGP(scene_folder_path):
    cmd = "cd ~/github/instant-ngp && " + \
        "./build/instant-ngp" + \
        " --scene " + scene_folder_path
    if not runCommand(cmd):
        print("[ERROR][nerf::runInstantNGP]")
        print("\t runCommand failed!")
        return False
    return True

