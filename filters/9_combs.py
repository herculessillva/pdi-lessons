import cv2
import numpy as np

def gamma_corr(image, gamma):
    lookUpTable = np.empty((1, 256), np.uint8)
    for i in range(256):
        lookUpTable[0, i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
    
    return cv2.LUT(image, lookUpTable)

# Imagem de entrada
IMG_PATH = './x-ray.tif'

if __name__ == "__main__":
    # Ler imagem em níveis de cinza
    img = cv2.imread(IMG_PATH, 0)
    cv2.imshow('Original', img)
    cv2.waitKey(0)

    # Kernel do filtro Laplaciano
    lpc_kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

    # Aplicar filtro Laplaciano com Kernel e salvar imagem
    img_b = cv2.filter2D(img, -1, lpc_kernel)
    cv2.imshow('Laplacian', img_b)
    cv2.waitKey(0)

    # Utilizar da máscara de aguçamento "img_b" e salvar imagem
    img_c = cv2.addWeighted(img, 1, img_b, 1, 0)
    cv2.imshow('Original e Laplacian', img_c)
    cv2.waitKey(0)

    # Obter imagem da filtragem de Sobel global a partir das imagens resultantes horizontal e vertical, e salvar imagem resultante
    sb_x = cv2.Sobel(img, cv2.CV_16S, 1,0, ksize=3, scale=1)
    sb_y = cv2.Sobel(img, cv2.CV_16S, 0,1, ksize=3, scale=1)
    abs_sb_x= cv2.convertScaleAbs(sb_x)
    abs_sb_y = cv2.convertScaleAbs(sb_y)
    img_d = cv2.addWeighted(abs_sb_x, 0.5, abs_sb_y, 0.5,0)
    cv2.imshow('Sobel', img_d)
    cv2.waitKey(0)

    # Aplicar filtro da média (5,5)
    img_e = cv2.blur(img_d,(5,5))
    cv2.imshow('Media', img_e)
    cv2.waitKey(0)

    # Obter máscara a partir da adição de "img_c" e "img_e"
    img_f =  cv2.addWeighted(img_c, 1, img_e, -1, 0)
    cv2.imshow('Agucada e Media', img_f)
    cv2.waitKey(0)

    # Obter imagem realçada a partir da adição de "img" e "img_f"
    img_g = cv2.addWeighted(img, 1, img_f, 1, 0)
    cv2.imshow('Original e (Agucada e Media)', img_g)
    cv2.waitKey(0)

    # Aplicar correção de gamma
    img_h = img_corr = gamma_corr(img_g, 0.5)
    cv2.imshow('Correcao de gamma', img_h)
    cv2.waitKey(0)