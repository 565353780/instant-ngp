#!/usr/bin/env python
# -*- coding: utf-8 -*-

from instant_ngp_recon.Method.image import videoToImages

def demo():
    video_file_path = "/home/chli/chLi/NeRF/keyboard/keyboard.mp4"
    save_image_folder_path = "/home/chli/chLi/NeRF/keyboard/images/"
    skip_num = 1
    scale = 1
    show_image = False
    print_progress = True

    videoToImages(
        video_file_path,
        save_image_folder_path,
        skip_num,
        scale,
        show_image,
        print_progress
    )
    return True

if __name__ == "__main__":
    demo()

