import PIL.Image

#*Caracteres do mais forte pro mais fraco
ASCII_CHARACTERS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', '.']

#*Mudar o tamanho da imagem
def resizeImage(image, newWidth=100):
    widht, height = image.size
    ratio = height / widht / 1.65
    newHeight = int(newWidth * ratio)
    resizedImage = image.resize((newWidth, newHeight))
    return(resizedImage)

#*Filtro "Grayscale"
def grayify(image):
    grayscaleImage = image.convert("L")
    return(grayscaleImage)

#*Transforma cada pixel em um caractere
def pixelsToAscii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARACTERS[pixel//25] for pixel in pixels])
    return(characters)

#*Função principal
def main(newWidth=100):
    path = input("Digite um caminho válido para a imagem: ")

    try:
        image = PIL.Image.open(path)
    except:
        print(path, "Não é um caminho válido")

    #*Converte os caracteres para ASCII
    newImageData = pixelsToAscii(grayify(resizeImage(image)))

    #*Formatar
    pixelCount = len(newImageData)
    asciiImage = "\n".join(newImageData[i:(i+newWidth)] for i in range(0, pixelCount, newWidth))

    #*Printar resultado
    print(asciiImage)

    #*Salvar resultado para imagem.txt
    with open("imagemAscii.txt", "w") as f:
        f.write(asciiImage)

main()