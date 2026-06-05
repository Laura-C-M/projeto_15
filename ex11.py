import cv2
import numpy as np

#Carrega a imagem do disco
#Certifique-se de que o caminho da imagem está correto
img = cv2.imread("imagem5.jpg", 0)

#Verifica se a imagem foi carregada corretamente
if img is None:
    print("Erro:Não foi possível carregar a imagem. Verifique o caminho do ficheiro.")
else:
    kernel = np.ones((5,5), np.uint8)
    #kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5,5))

    erosion = cv2.erode(img, kernel, iterations = 1)

    dilatation = cv2.dilate(img, kernel, iterations = 1)


cv2.imshow("Original", img)
cv2.imshow("Erosao", erosion)
cv2.imshow("Dilataçao", dilatation)
    #Espera indefinidamente por uma tecla pressionada
    #O valor 0 significa que espera para sempre
cv2.waitKey(0)

cv2.destroyAllWindows