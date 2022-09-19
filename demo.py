#!/usr/bin/env python
# -*- coding: utf-8 -*-

from instant_ngp_recon.Method.image import videoToImages

if __name__ == "__main__":
    video_file_path = "/home/chli/chLi/NeRF/keyboard.mp4"
    save_image_folder_path = "/home/chli/chLi/NeRF/keyboard/"

    videoToImages(video_file_path, save_image_folder_path)

