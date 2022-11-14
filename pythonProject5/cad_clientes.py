import tkinter as tk
import sqlite3
from turtle import title
import pandas as pd
import openpyxl

# conexao = sqlite3.connect('banco.cliente.db')
#
# c = conexao.cursor()
#
# c.execute(''' CREATE TABLE clientes (
#      nome text,
#      sobrenome text,
#      email text,
#      telefone text
#      )
#  ''')
# conexao.commit()
#
# conexao.close()
def abrir_janela():
    janela2 = tk.Toplevel()
    janela2 = title('Pesquisa de Cliente')
    label_nome = tk.Label(janela2,text = 'Nome')
    label_nome.grid(row = 0 , column= 0)
    botao_voltar = tk.Button(janela2, text='Fechar', command=janela2.destroy)
    botao_voltar.grid(row=1, column=0)




def cadastrar_clientes():
    conexao = sqlite3.connect('banco.cliente.db')

    c = conexao.cursor()

    c.execute(' INSERT INTO clientes VALUES (:nome, :sobrenome, :email, :telefone)',
              {
                'nome':entry_nome.get(),
                'sobrenome':entry_sobrenome.get(),
                'email':entry_email.get(),
                'telefone':entry_telefone.get()
              }
              )
    conexao.commit()

    conexao.close()

    entry_nome.delete(0,"end")
    entry_sobrenome.delete(0, "end")
    entry_email.delete(0, "end")
    entry_telefone.delete(0, "end")


def pesquisar_clientes():
    conexao = sqlite3.connect('banco.cliente.db')

    c = conexao.cursor()

    c.execute('SELECT *, oid FROM clientes')
    clientes_cadastrados = c.fetchall()
    clientes_cadastrados = pd.DataFrame(clientes_cadastrados, columns=['nome','sobrenome','email','telefone','Id_banco'])
    clientes_cadastrados.to_excel('banco_clientes.xlsx')

    conexao.commit()

    conexao.close()


def exporta_clientes():
    conexao = sqlite3.connect('banco.cliente.db')

    c = conexao.cursor()

    c.execute('SELECT *, oid FROM clientes')
    clientes_cadastrados = c.fetchall()
    clientes_cadastrados = pd.DataFrame(clientes_cadastrados, columns=['nome','sobrenome','email','telefone','Id_banco'])
    clientes_cadastrados.to_excel('banco_clientes.xlsx')

    conexao.commit()

    conexao.close()


janela  = tk.Tk()
janela.title('Ferramenta para cadastro de cliente')
janela.geometry('800x800')

# Labels:
label_nome = tk.Label(janela, text='Nome')
label_nome.grid(row=0 , column=0 , padx=0, pady=0)

label_sobrenome = tk.Label(janela, text='Sobrenome')
label_sobrenome.grid(row=1 , column=0 , padx=0, pady=0)

label_email = tk.Label(janela, text='E-mail')
label_email.grid(row=2 , column=0 , padx=0, pady=0)

label_telefone = tk.Label(janela, text='Telefone')
label_telefone.grid(row=3 , column=0 , padx=0, pady=0)

# Entrys:
entry_nome = tk.Entry(janela, text='Nome', width=30)
entry_nome.grid(row=0 , column=1 , padx=10, pady=10)

entry_sobrenome = tk.Entry(janela, text='Sobrenome', width=30)
entry_sobrenome.grid(row=1 , column=1 , padx=10, pady=10)

entry_email = tk.Entry(janela, text='E-mail', width=30)
entry_email.grid(row=2 , column=1 , padx=10, pady=10)

entry_telefone = tk.Entry(janela, text='Telefone', width=30)
entry_telefone.grid(row=3 , column=1 , padx=10, pady=10)

# Botões:
botao_cadastrar = tk.Button(janela, text='Cadastrar Cliente', command=cadastrar_clientes)
botao_cadastrar.grid(row=4 , column=0 , padx=10, pady=10, columnspan=2, ipadx=80,)

botao_exportar = tk.Button(janela, text='Exporta Base de Clientes', command=exporta_clientes)
botao_exportar.grid(row=5 , column=0 , padx=10, pady=10, columnspan=2, ipadx=80)

botao_pesquisar = tk.Button(janela, text='Pesquisar Cliente', command=abrir_janela)
botao_pesquisar.grid(row=6 , column=0 , padx=10, pady=10, columnspan=2, ipadx=80)


janela.mainloop()