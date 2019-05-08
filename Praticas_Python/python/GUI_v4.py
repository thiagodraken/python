from tkinter import *
import API_ThumbnailPillow


class Application:

    def __init__(self, master=None):

        self.fontePadrao = ("Arial", "10")
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["pady"] = 20
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["pady"] = 20
        self.container5.pack()

        self.labelTitle = Label(self.container1, text="Projeto API")
        self.labelTitle["font"] = ("Arial", "10", "bold")
        self.labelTitle.pack()

        self.labelURL = Label(self.container2, text="URL", font=self.fontePadrao)
        self.labelURL.pack(side=LEFT)

        self.entryURL = Entry(self.container2)
        self.entryURL["width"] = 50
        self.entryURL["font"] = self.fontePadrao
        self.entryURL.pack(side=LEFT)

        self.buttonThumbnail = Button(self.container4)
        self.buttonThumbnail["text"] = "Gerar Thumbnail"
        self.buttonThumbnail["font"] = ("Calibri", "8")
        self.buttonThumbnail["width"] = 20
        self.buttonThumbnail["command"] = self.invocarAPI
        self.buttonThumbnail.pack()

        self.labelMessage = Label(self.container5, text="Resultado", font=self.fontePadrao)
        self.labelMessage.pack()

        # Cria um quadro vazio onde será posicionada a thumbnail
        self.imageFrame = Canvas(self.container5, bg='white',width=300, height=300)
        self.imageFrame.pack(side='top', fill='both', expand='no')


    # Método para invocar a API e exibir o thumbnail como resultado
    # O thumbnail é salvo como um arquivo ".png" na pasta raíz do programa
    def invocarAPI(self):

        # Apaga a imagem já existente, se houver
        self.imageFrame.delete("all")

        # Chama a API, passando a URL como parâmetro
        API_ThumbnailPillow.gerarThumbnail(self.entryURL.get())

        # Obtém o arquivo recém criado
        imagem_res = PhotoImage(file="thumbnail.png")

        # Projeta a imagem no quadro criado
        self.imageFrame.create_image(0, 0, anchor=NW, image=imagem_res)
        mainloop()

root = Tk()
Application(root)
root.mainloop()

