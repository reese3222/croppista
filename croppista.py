def croppista():
    import numpy as np
    import cv2
    import os
    folder = input("Select a folder for CROPPISTA: ")
    os.makedirs(f'{folder}/croppista', exist_ok = True)
    for file in filter(lambda x: "." in x, os.listdir(folder)):
        extension = file[file.index('.'):]
        if extension in ['.jpg', '.jpeg', '.png'] and 'insta' not in file:
            im = cv2.imread(f'{folder}/{file}')
            height, width = im.shape[0], im.shape[1] 

            if height > width:
                add = int((width - (width * 4/5))/2)
                im = cv2.copyMakeBorder(im,0,0,add,add,cv2.BORDER_CONSTANT,value=[255,255,255])

            else:
                add = int(((width - height)/2))
                im = cv2.copyMakeBorder(im,add,add,0,0,cv2.BORDER_CONSTANT,value=[255,255,255])

            cv2.imwrite(f'{folder}/croppista/{file.rstrip(extension)}_insta{extension}', im)



if __name__ == '__main__':
    croppista()