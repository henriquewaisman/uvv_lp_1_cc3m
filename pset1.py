# IDENTIFICAÇÃO DO ESTUDANTE:
# Preencha seus dados e leia a declaração de honestidade abaixo. NÃO APAGUE
# nenhuma linha deste comentário de seu código!
#
#    Nome completo: 
#    Matrícula: 
#    Turma: 
#    Email: 
#
# DECLARAÇÃO DE HONESTIDADE ACADÊMICA:
# Eu afirmo que o código abaixo foi de minha autoria. Também afirmo que não
# pratiquei nenhuma forma de "cola" ou "plágio" na elaboração do programa,
# e que não violei nenhuma das normas de integridade acadêmica da disciplina.
# Estou ciente de que todo código enviado será verificado automaticamente
# contra plágio e que caso eu tenha praticado qualquer atividade proibida
# conforme as normas da disciplina, estou sujeito à penalidades conforme
# definidas pelo professor da disciplina e/ou instituição.
#


# Imports permitidos (não utilize nenhum outro import!):
import sys
import math
import base64
import tkinter
from io import BytesIO
from PIL import Image as PILImage


def kernelFunc(n):
    # Cria uma matriz em row major order de tamanho n
    kernel = [[1 / n ** 2 for index in range(n)] for index in range(n)]
    return kernel


# Classe Imagem:
class Imagem:
    def __init__(self, largura, altura, pixels):
        self.largura = largura
        self.altura = altura
        self.pixels = pixels

    def get_pixel(self, x, y):
        # Se o pixel não está dentro do limite do eixo X setar o valor de X = ao valor correto mais próximo
        if x < 0:
            x = 0
        elif x >= self.largura:
            x = self.largura - 1
        # Fazer o mesmo com a altura Y do pixel
        if y < 0:
            y = 0
        elif y >= self.altura:
            y = self.altura - 1
        # Retorna o pixel específico
        return self.pixels[(x + y * self.largura)]

    def set_pixel(self, x, y, c):
        # Armazena um pixel na variável C
        self.pixels[(x + y * self.largura)] = c

    def aplicar_por_pixel(self, func):
        resultado = Imagem.nova(self.largura, self.altura)
        for x in range(resultado.largura):
            for y in range(resultado.altura):
                cor = self.get_pixel(x, y)
                nova_cor = func(cor)
                resultado.set_pixel(x, y, nova_cor)
        return resultado

    def invertida(self):
        return self.aplicar_por_pixel(lambda c: 255 - c)

    def correlacao(self, n):
        tamanhoKernel = len(n)                          # Recebe o kernel k e determina seu tamanho
        i = Imagem.nova(self.largura, self.altura)      # Cria uma imagem com as mesmas dimensões da imagem de entrada
        for x in range(self.largura):                   # Percorre todas as linhas da imagem
            for y in range(self.altura):                # Percorre todas as colunas da imagem
                somaCorrelacao = 0                      # Soma da correlação pixel-kernel
                for a in range(tamanhoKernel):          # Percorre as linhas do kernel
                    for b in range(tamanhoKernel):      # Percorre as colunas do kernel
                        # A somaCorrelacao será incrementada a partir da multiplicação de um pixel (x, y) a um
                        # elemento correspondente no kernel (kx, ky)
                        somaCorrelacao += self.get_pixel((x-(tamanhoKernel//2)+a), (y-(tamanhoKernel//2))+b)*n[a][b]
                i.set_pixel(x, y, somaCorrelacao)       # O valor da correlação é atribuido ao pixel na imagem de saída
        return i                                        # Retorna a nova imagem

    def borrada(self, n):
        kernel = self.correlacao(kernelFunc(n))         # Chama a kernelFunc para produzir um Kernel
                                                        # Correlaciona cada pixel da matriz gerada
        kernel.pixel_tratado()                          # Trata a correlação
        return kernel                                   # Retorna o kernel tratado

    def pixel_tratado(self):
        for x in range(self.largura):                   # Percorre a largura X da imagem
            for y in range(self.altura):                # Percorre a altura Y da altura
                pixel = self.get_pixel(x, y)            # Trata pixel a pixel
                if pixel < 0:                           # Se o valor do pixel for menor que 0, é agora igual a 0
                    pixel = 0
                elif pixel > 255:                       # Se o valor do pixel for maior que 255, agora é igual a 255
                    pixel = 255
                pixel = round(pixel)                    # Se o pixel está com valor float, aqui ele é arredondado
                self.set_pixel(x, y, pixel)             # Seta o pixel tratado

    def focada(self, n):
        imBorrada = self.borrada(n)                     # Borra uma imagem
        i = Imagem.nova(self.largura, self.altura)      # Cria uma imagem vazia
        for x in range(self.largura):                   # Percorre largura
            for y in range(self.altura):                # Percorre altura
                imFocada = round(2*self.get_pixel(x, y) - (imBorrada.get_pixel(x, y))) 
                # Função dada no pset1.pdf
                i.set_pixel(x, y, imFocada)             # Seta os pixels focados
        i.pixel_tratado()                               # Trata os pixels da nova imagem
        return i                                        # Retorna a imagem focada

    def bordas(self):
        i = Imagem.nova(self.largura, self.altura)      # Cria uma imagem vazia
        kx = [[1, 0, -1],                               # Destada as bordas de X
              [2, 0, -2],
              [1, 0, -1]]
        ky = [[1, 2, 1],                                # Destaca as bordas de Y
              [0, 0, 0],
              [-1, -2, -1]]
        correlacaox = self.correlacao(kx)               # Faz a Correlação com o kernel Kx
        correlacaoy = self.correlacao(ky)               # Faz o mesmo com Ky
        for x in range(self.largura):
            for y in range(self.altura):
                operador = round(math.sqrt(correlacaox.get_pixel(x, y) ** 2 + correlacaoy.get_pixel(x, y) ** 2))
                # Função descrita no pset1.pdf
                i.set_pixel(x, y, operador)             # Seta os pixels novos
        i.pixel_tratado()                               # Trata os pixels novos
        return i                                        # Retorna a imagem filtrada

    # Abaixo deste ponto estão utilitários para carregar, salvar e mostrar
    # as imagens, bem como para a realização de testes.

    def __eq__(self, other):
        return all(getattr(self, i) == getattr(other, i)
                   for i in ('altura', 'largura', 'pixels'))

    def __repr__(self):
        return "Imagem(%s, %s, %s)" % (self.largura, self.altura, self.pixels)

    @classmethod
    def carregar(cls, nome_arquivo):
        """
        Carrega uma imagem do arquivo fornecido e retorna uma instância dessa
        classe representando essa imagem. Também realiza a conversão para tons
        de cinza.

        Invocado como, por exemplo:
           i = Imagem.carregar('test_images/cat.png')
        """
        with open(nome_arquivo, 'rb') as guia_para_imagem:
            img = PILImage.open(guia_para_imagem)
            img_data = img.getdata()
            if img.mode.startswith('RGB'):
                pixels = [round(.299 * p[0] + .587 * p[1] + .114 * p[2]) for p in img_data]
            elif img.mode == 'LA':
                pixels = [p[0] for p in img_data]
            elif img.mode == 'L':
                pixels = list(img_data)
            else:
                raise ValueError('Modo de imagem não suportado: %r' % img.mode)
            l, a = img.size
            return cls(l, a, pixels)

    @classmethod
    def nova(cls, largura, altura):
        """
        Cria imagens em branco (tudo 0) com a altura e largura fornecidas.

        Invocado como, por exemplo:
            i = Imagem.nova(640, 480)
        """
        return cls(largura, altura, [0 for i in range(largura * altura)])

    def salvar(self, nome_arquivo, modo='PNG'):
        """
        Salva a imagem fornecida no disco ou em um objeto semelhante a um arquivo.
        Se o nome_arquivo for fornecido como uma string, o tipo de arquivo será
        inferido a partir do nome fornecido. Se nome_arquivo for fornecido como
        um objeto semelhante a um arquivo, o tipo de arquivo será determinado
        pelo parâmetro 'modo'.
        """
        saida = PILImage.new(mode='L', size=(self.largura, self.altura))
        saida.putdata(self.pixels)
        if isinstance(nome_arquivo, str):
            saida.save(nome_arquivo)
        else:
            saida.save(nome_arquivo, modo)
        saida.close()

    def gif_data(self):
        """
        Retorna uma string codificada em base 64, contendo a imagem
        fornecida, como uma imagem GIF.

        Função utilitária para tornar show_image um pouco mais limpo.
        """
        buffer = BytesIO()
        self.salvar(buffer, modo='GIF')
        return base64.b64encode(buffer.getvalue())

    def mostrar(self):
        """
        Mostra uma imagem em uma nova janela Tk.
        """
        global WINDOWS_OPENED
        if tk_root is None:
            # Se Tk não foi inicializado corretamente, não faz mais nada.
            return
        WINDOWS_OPENED = True
        toplevel = tkinter.Toplevel()
        # O highlightthickness=0 é um hack para evitar que o redimensionamento da janela
        # dispare outro evento de redimensionamento (causando um loop infinito de
        # redimensionamento). Para maiores informações, ver:
        # https://stackoverflow.com/questions/22838255/tkinter-canvas-resizing-automatically
        tela = tkinter.Canvas(toplevel, height=self.altura,
                              width=self.largura, highlightthickness=0)
        tela.pack()
        tela.img = tkinter.PhotoImage(data=self.gif_data())
        tela.create_image(0, 0, image=tela.img, anchor=tkinter.NW)

        def ao_redimensionar(event):
            # Lida com o redimensionamento da imagem quando a tela é redimensionada.
            # O procedimento é:
            #  * converter para uma imagem PIL
            #  * redimensionar aquela imagem
            #  * obter os dados GIF codificados em base 64 (base64-encoded GIF data)
            #    a partir da imagem redimensionada
            #  * colocar isso em um label tkinter
            #  * mostrar a imagem na tela
            nova_imagem = PILImage.new(mode='L', size=(self.largura, self.altura))
            nova_imagem.putdata(self.pixels)
            nova_imagem = nova_imagem.resize((event.largura, event.altura), PILImage.NEAREST)
            buffer = BytesIO()
            nova_imagem.save(buffer, 'GIF')
            tela.img = tkinter.PhotoImage(data=base64.b64encode(buffer.getvalue()))
            tela.configure(height=event.altura, width=event.largura)
            tela.create_image(0, 0, image=tela.img, anchor=tkinter.NW)

        # Por fim, faz o bind da função para que ela seja chamada quando a tela
        # for redimensionada:
        tela.bind('<Configure>', ao_redimensionar)
        toplevel.bind('<Configure>', lambda e: tela.configure(height=e.altura, width=e.largura))

        # Quando a tela é fechada, o programa deve parar
        toplevel.protocol('WM_DELETE_WINDOW', tk_root.destroy)


# Não altere o comentário abaixo:
# noinspection PyBroadException
try:
    tk_root = tkinter.Tk()
    tk_root.withdraw()
    tcl = tkinter.Tcl()


    def refaz_apos():
        tcl.after(500, refaz_apos)


    tcl.after(500, refaz_apos)
except:
    tk_root = None

WINDOWS_OPENED = False

if __name__ == '__main__':
    # O código neste bloco só será executado quando você executar
    # explicitamente seu script e não quando os testes estiverem
    # sendo executados. Este é um bom lugar para gerar imagens, etc.

    # Questão 2
    im = Imagem.carregar('test_images/bluegill.png')
    inIm = im.invertida()
    Imagem.salvar(inIm, 'img_resultado/bluegill1.png')

    # Questão 4
    kernel = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    im = Imagem.carregar('test_images/pigbird.png')
    coIm = im.correlacao(kernel)
    Imagem.salvar(coIm, 'img_resultado/pigbird1.png')

    # Questão 5.1
    im = Imagem.carregar('test_images/cat.png')
    blIm = im.borrada(5)
    Imagem.salvar(blIm, 'img_resultado/cat1.png')

    # Questão 5
    im = Imagem.carregar('test_images/python.png')
    boIm = im.focada(11)
    Imagem.salvar(boIm, 'img_resultado/python1.png')

    # Questão 6
    kx = [[-1, 0, 1],
          [-2, 0, 2],
          [-1, 0, 1]]

    ky = [[-1, -2, -1],
          [0, 0, 0],
          [1, 2, 1]]

    im = Imagem.carregar('test_images/construct.png')
    borX = im.correlacao(kx)
    Imagem.salvar(borX, 'img_resultado/construct1.png')
    borY = im.correlacao(ky)
    Imagem.salvar(borY, 'img_resultado/construct2.png')
    borIm = im.bordas()
    Imagem.salvar(borIm, 'img_resultado/construct3.png')

    pass

    # O código a seguir fará com que as janelas de Imagem.mostrar
    # sejam exibidas corretamente, quer estejamos executando
    # interativamente ou não:
    if WINDOWS_OPENED and not sys.flags.interactive:
        tk_root.mainloop()
