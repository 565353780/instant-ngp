#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import cv2

def videoToImages(video_file_path,
                  save_image_folder_path,
                  scale=1,
                  show_image=False):
    if save_image_folder_path[-1] != "/":
        save_image_folder_path += "/"

    os.makedirs(save_image_folder_path, exist_ok=True)

    cap = cv2.VideoCapture(video_file_path)

    image_idx = 0
    skip_num = 20

    while True:
        status, frame = cap.read()
        image_idx += 1

        if image_idx % skip_num != 0:
            continue

        if not status:
            break

        if scale != 1:
            frame = cv2.resize(frame,(
                int(frame.shape[1]/scale),
                int(frame.shape[0]/scale)
            ))

        if show_image:
            cv2.imshow("image", frame)
            cv2.waitKey(1)

        save_image_file_path = save_image_folder_path + \
            "image_" + str(image_idx) + ".png"
        cv2.imwrite(save_image_file_path, frame)
    return True

