import customtkinter as ctk 
from tkinter import *



class BackEnd():
    '''Função para pegar os valores das entrys, criando uma nova váriavel e chmamando as entry dentro das novas variaveis 
    com o método "get'", que irá pegar os valores digitado pelo usuário'''
    def pegar_valores(self):  
        self.valor1 = float(self.entry1.get())
        self.valor2 = float(self.entry2.get())
        self.valor3 = self.entry3.get()

        '''Uilizando as estruturas condicionais: if, elif e else para verificar o valor do resultado dos cálculos realizados
        e printar na tela do usuário a informaçao correta.'''
        self.resultado =  self.valor2 / (self.valor1** 2) 
        if  self.resultado  <= 16:
            self.lb.configure(text=f'{self.valor3}, seu IMC é: {self.resultado:.2f} -  \nVocê está com magreza leve')
        elif 16 < self.resultado <= 16.8:
            self.lb.configure(text=f'{self.valor3}, seu IMC é: {self.resultado:.2f} -  \nVocê está com magreza moderada')
        elif 16.8 < self.resultado < 18.5:
            self.lb.configure(text=f'{self.valor3}, seu IMC é: {self.resultado:.2f} -  \nVocê está com magreza leve')
        elif 18.5 < self.resultado < 24.9:
            self.lb.configure(text=f'{self.valor3}, seu IMC é: {self.resultado:.2f} -  \nVocê está com o peso ideal')
        elif 25 < self.resultado < 29.9:
            self.lb.configure(text=f'{self.valor3}, seu IMC é: {self.resultado:.2f} -  \nVocê está com sobrepeso')
        elif 30 < self.resultado < 34.9:
            self.lb.configure(text=f'{self.valor3}, seu IMC é: {self.resultado:.2f} -  \nVocê está com obsidade grau l')
        elif 35 < self.resultado < 39.0:
            self.lb.configure(text=f'{self.valor3}, seu IMC é: {self.resultado:.2f} -  \nVocê está com obsidade grau ll ou severa')
        else:
            self.resultado >= 40
            self.lb.configure(text=f'{self.valor3}, seu IMC é: {self.resultado:.2f} -  \nVocê está com obsidade lll ou mórbida')

    '''Função criada para deletar os valores que estão dentro das entrys1 e entry2, utilizando o método
    "delete" passandos os parâmetros para iniciar no 0 e END, indicando que é para apagar todos os valores do campo
    inicializando no indice 0, até o final.'''
    def apagar_campos(self): # Função para apagar os campos
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)

''' classe app, inicizando com ctk, e chamando a classe BackEnd dentro da classe app. 
inician com o método __init__ e super()., para garantir a hierarquia da classe pai"App"
e logo após, todas as funções "def" que forem criadas, precisam ser chamadas dentro da funçaõ def __init__... 
para serem inicializadas.'''
class App(ctk.CTk, BackEnd): 
    def __init__(self):
        super().__init__()
        self.config_inicio()
        self.frame_yellow()
        self.frame_lateral()

    '''iniciando a função confi_inicio, chamando o método construtor self
    dentro desta função é realizado toda a parte de estilização da tela inicial 
    da interface gráfica, iniciando com "self", pois ele é o método construtor pai da interface'''
    def config_inicio(self): # Configurando a tela inicial 
        self.geometry('452x500')
        self.title('Care')
        self.resizable('False', 'False')
        self._set_appearance_mode('Dark')
        self.iconbitmap('icon.ico')

    '''Nessa função esta sendo realizado a crição de um novo frame chamado frame_yellow'''
    def frame_yellow(self):
        self.frame_yellow = ctk.CTkFrame(self, width=898, height=20, fg_color='yellow')
        self.frame_yellow.place(x=1, y=1)

    '''Nessa função está sendo realizado a criação de outro frame chamado de frame_lateral
    que irá receber as entrys, buttons e os prints dos resultados.'''
    def frame_lateral(self):
        self.frame_l = ctk.CTkFrame(self, width=450, height=474, corner_radius=100)
        self.frame_l.place(x=1, y=23)

        # Nessa etapa está sendo criado as entrys
        self.entry1 = ctk.CTkEntry(self.frame_l, width=200, height=20, border_width=1, placeholder_text='Digite sua altura (ex: 1.80)')
        self.entry1.place(x=125, y=50)
        self.entry2 = ctk.CTkEntry(self.frame_l, width=200, height=20, border_width=1, placeholder_text='Digite seu peso (ex: 94.5)')
        self.entry2.place(x=125, y=90)
        self.entry3 = ctk.CTkEntry(self.frame_l, width=200, height=20, border_width=1, placeholder_text='Digite seu nome')
        self.entry3.place(x=125, y=130)
        '''Nessa etapa está sendo criado os buttons e colocando os comandos "pegar_valor" e "apagar_campos" 
        para serem executados quandos os buttons forem pressionados'''
        self.bt = ctk. CTkButton(self.frame_l, text='calcular', width=50, height=20, command=self.pegar_valores)
        self.bt.place(x=140, y=190)    
        self.bt_del = ctk. CTkButton(self.frame_l, text='Apagar', width=50, height=20, command=self.apagar_campos)
        self.bt_del.place(x=250, y=190) 
        '''Nessa parte, foi criado a self.lb que está com o campo "text='' " em branco, pois irá receber 
        o resultado dos cálculos, realizados na função "pegar valor", chamando o método "config" '''
        self.lb = ctk.CTkLabel(self.frame_l, text='')   
        self.lb.place(x=125, y=250)

'''Nessa parte do código, if __name__ == "__main__: é uma conversão do Python para garantir que o bloco de código seja executado apenas
quando o script é executado é executado diretamente, if __name__ é uma variavel especial que recebe o valor de "__main__ quando o script é 
executado diretamente
Básicamente essa verificação determina se o script está sendo executado diretamente ou se está sendo importado
se o script está sendo executado diretamente, o código dentro do bloco é executado.""'''    
if __name__ == "__main__":
    App = App()
    App.mainloop()