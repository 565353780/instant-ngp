from instant_ngp.Method.train import trainINGP

def demo():
    data_folder_path = '../colmap-manage/output/3vjia_simple/ingp/'

    trainINGP(data_folder_path)
    return True
