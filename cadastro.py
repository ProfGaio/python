import tkinter as tk
from tkinter import messagebox
import json
janela = tk.Tk()

janela.title("Cadastro de Usuário")

janela.geometry('300x200')
#Título
titulo = tk.Label(janela,text="Tela de Registro",font=('Verdana','11','bold'))
titulo.grid(row=0,column=1, padx=30,pady=10)

#Nome
labelNome = tk.Label(janela,text="Nome:")
labelNome.grid(row=1, column=0, padx=10, pady=10)
entradaNome = tk.Entry(janela)
entradaNome.grid(row=1, column=1, padx=5, pady=10)

#E-mail
labelEmail = tk.Label(janela,text="E-mail:")
labelEmail.grid(row=2, column=0, padx=10, pady=10)
entradaEmail = tk.Entry(janela)
entradaEmail.grid(row=2, column=1, padx=5, pady=10)

#Criação da função gravarDados
def gravarDados():
    nome = entradaNome.get()
    email = entradaEmail.get()

    messagebox.showinfo("Informação", f"Dados do usuário salvos com sucesso!\nNome: {nome}\nE-mail: {email}")
    #Adicionar dados em um dicionário e gravar em arquivo json
    dados={}  # dados é um dicionário vazio
    dados['nome']=nome # aqui estamos criando a chave nome no dicionário dados e armazenando o valor contido na variável nome
    dados['email']=email # aqui estamos criando a chave email no dicionário dados e armazenando o valor contido na variável email
    
    arquivo = open('cadastro.json','w') # abrindo o arquivo cadastro.json para escrita ('w'rite)
    json.dump(dados,arquivo,indent=4) #utilizando a função dump do módulo json para inserir os dados do dicionário no arquivo
    arquivo.close() #fechando o arquivo após o acesso para gravação (escrita).



#criando o botão salvar e executando a função gravarDados ao clicar no botão
btnSalvar = tk.Button(janela, text="Salvar", command=gravarDados) 
btnSalvar.grid(row=3, column=1, ipadx=25, padx=40, pady=20)

janela.mainloop()

