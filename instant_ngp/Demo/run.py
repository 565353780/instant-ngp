from instant_ngp.Method.nerf import runInstantNGP

def demo():
    data_folder_path = '../colmap-manage/output/3vjia_simple/'

    runInstantNGP(data_folder_path)
    return True
