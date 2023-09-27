from instant_ngp.Method.cmd import runCMD

def trainINGP(scene_folder_path):
    cmd = '../ingp/build/instant-ngp' + \
        ' --scene ' + scene_folder_path

    if not runCMD(cmd, True):
        print('[ERROR][nerf::trainINGP]')
        print('\t runCMD failed!')
        print('\t cmd:', cmd)
        return False

    return True
