<<<<<<< HEAD
from skimage import io
import numpy as np
import matplotlib.pyplot as plt


def read_image():
    imagem = io.imread('shiba-p.jpg')
    img_copy = imagem.copy()

    return img_copy


def open_image(select_image, cmap=None):
    plt.imshow(select_image, cmap)

    return plt.show()


def present_image():
    imagem = io.imread('shiba-p.jpg')
    alt, larg, cns_cor = imagem.shape
    dimension = (f'Altura da imagem: {alt}\n'
                 f'Largura da imagem: {larg}\n'
                 f'Canais de cor: {cns_cor}')
    print(dimension)


def tratament_image():
    from time import sleep as slp
    print('Para encerrar digite NÃO na aba opção!')
    print(f'{"=" * 5}MENU{"=" * 5}\n\n'
          f'DIGITE A OPÇÃO DESEJADA:\n'
          f'1 - Para corte vertical\n'
          f'2 - Para corte horizontal\n'
          f'3 - Para remover nariz\n'
          f'4 - Apresentar imagem P e B.\n\n')
    slp(0.5)
    option = input('Digite a opção desejada: ').upper()
    while option != 'NÃO':
        imagem = io.imread('shiba-p.jpg')
        img_copy = imagem.copy()
        arrays = np.array(img_copy)
        if option == '1':
            image_vertical_cut = img_copy[:, :320, :]
            print(arrays)
            return open_image(image_vertical_cut)

        elif option == '2':
            image_horizontal_cut = img_copy[:320, :, :]
            return open_image(image_horizontal_cut)

        elif option == '3':
            image_nose_cut = img_copy
            image_nose_cut[290:360, 340:415, :] = 255

            return open_image(image_nose_cut)

        elif option == '4':
            image_b_w = img_copy * [0.299, 0.587, 0.114]
            image_b_w = image_b_w.astype('uint8')
            image_b_w = image_b_w.sum(axis=2)
            return open_image(image_b_w, cmap='gray')

        else:
            print('OPS! opção inválida!\nTente Novamente!!')
            slp(0.5)
            option = input('Digite a opção desejada: ').upper()


if __name__ == '__main__':
    read_image()
    print('Digite Enter para começar.')
    print('[ENTER]')
    start = input()
    tratament_image()
>>>>>>> 5d7dbad (Projeto Aula)
