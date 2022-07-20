from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


img = io.imread('shiba-p.jpg')  # Carregamento da imagem

print(type(img))

plt.imshow(img)  # Exibição da imagem

plt.show()