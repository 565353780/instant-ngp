#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil

from instant_ngp.Method.image import videoToImages
from instant_ngp.Method.colmap import runCOLMAP
from instant_ngp.Method.nerf import colmap2Nerf, runInstantNGP


def getImages():
    video_file_path = "/home/chli/chLi/NeRF/chair1/chair1.mp4"
    save_image_folder_path = "/home/chli/chLi/NeRF/chair1/images/"
    down_sample_scale = 10
    scale = 1
    show_image = False
    print_progress = True

    videoToImages(video_file_path, save_image_folder_path, down_sample_scale,
                  scale, show_image, print_progress)
    return True


def getNeRF():
    image_folder_path = "/home/chli/chLi/NeRF/chair1/images"
    colmap_camera_text_folder_path = "/home/chli/chLi/NeRF/chair1/sparse"
    save_transform_json_folder_path = "/home/chli/chLi/NeRF/chair1/transform.json"
    aabb_scale = 16

    colmap2Nerf(image_folder_path, colmap_camera_text_folder_path,
                save_transform_json_folder_path, aabb_scale)
    return True


def showNeRF():
    scene_folder_path = "/home/chli/chLi/NeRF/chair1"
    runInstantNGP(scene_folder_path)
    return True


def demo():
    cut_image = False
    run_colmap = False
    run_instant_ngp = True

    nerf_folder_and_video_name = "3vjia_person_4"
    video_file_name = "1.mp4"

    # videoToImages
    video_file_path = "/home/chli/chLi/NeRF/" + nerf_folder_and_video_name + \
        "/" + video_file_name
    save_image_folder_path = "/home/chli/chLi/NeRF/" + nerf_folder_and_video_name + "/images/"
    down_sample_scale = 4
    scale = 1
    show_image = False
    print_progress = True

    # colmap2Nerf
    image_folder_path = "/home/chli/chLi/NeRF/" + nerf_folder_and_video_name + "/images"
    colmap_camera_text_folder_path = "/home/chli/chLi/NeRF/" + nerf_folder_and_video_name + "/sparse"
    save_transform_json_folder_path = "/home/chli/chLi/NeRF/" + nerf_folder_and_video_name + "/transform.json"
    aabb_scale = 16

    # runInstantNGP
    scene_folder_path = "/home/chli/chLi/NeRF/" + nerf_folder_and_video_name

    if cut_image:
        try:
            shutil.rmtree(save_image_folder_path)
        except:
            pass
        videoToImages(video_file_path, save_image_folder_path,
                      down_sample_scale, scale, show_image, print_progress)

    if run_colmap:
        runCOLMAP()

        colmap2Nerf(image_folder_path, colmap_camera_text_folder_path,
                    save_transform_json_folder_path, aabb_scale)

    if run_instant_ngp:
        runInstantNGP(scene_folder_path)
    return True


if __name__ == "__main__":
    demo()
