import mysql.connector
from datetime import date
import tkinter as tk
from tkinter import *
import tkinter.messagebox as MessageBox

connection = mysql.connector.connect (
    host="localhost",
    user="root",
    password='',
    database= 'livraria_livraria'
)

cursor = connection.cursor()

# DATABASE ---------------------------------------------------------------------

# CRIAR TABELA 
# cursor.execute('CREATE DATABASE livraria_livraria')

# CRIAR TABELA CLIENTE
# cursor.execute('''CREATE TABLE cliente(
#              cod_cliente INT PRIMARY KEY AUTO_INCREMENT,
#              nome VARCHAR(255),
#              endereco VARCHAR(255),
#              telefone VARCHAR(11),
#              id_tipo INT,
#              id_numero VARCHAR(20))''')

# CRIAR TABELA EDITORA
# cursor.execute('''CREATE TABLE editora(
#               cod_editora INT PRIMARY KEY AUTO_INCREMENT,
#               endereco VARCHAR(255),
#               telefone VARCHAR(11),
#               nome_gerente VARCHAR(255))''')  

# CRIAR TABELA LIVRO
# cursor.execute('''CREATE TABLE livro(
#               cod_livro INT PRIMARY KEY AUTO_INCREMENT,
#               nome_autor VARCHAR(255),
#               nome_livro VARCHAR(255),
#               assunto VARCHAR(255),
#               editora VARCHAR(255),
#               isbn VARCHAR(13))''')

# CRIAR TABELA ESTOQUE
# cursor.execute('''CREATE TABLE estoque(
#               cod_livro INT PRIMARY KEY AUTO_INCREMENT,
#               qtd_estoque INT,
#               FOREIGN KEY (cod_livro) REFERENCES livro(cod_livro))''')

# CRIAR TABELA COMPRAS 
# cursor.execute('''CREATE TABLE compras(
#               cod_compra INT PRIMARY KEY AUTO_INCREMENT,
#               cod_cliente INT,
#               cod_livro INT,
#               qtd_compra INT,
#               data_compra DATE,
#               FOREIGN KEY (cod_cliente) REFERENCES cliente(cod_cliente),
#               FOREIGN KEY (cod_livro) REFERENCES livro(cod_livro))''')

# INSERIR DADOS - CLIENTE
# c = ('INSERT INTO cliente(nome, endereco, telefone, id_tipo, id_numero) VALUES (%s, %s, %s, %s, %s)')
# val = [
#    ('Ana Pereira','Rua 1', '1111-1111', 1, '11111'),
#    ('Carlos Souza','Rua 2', '2222-2222', 2, '22222'),
#    ('Maria Oliveira', 'Rua 3', '3333-3333', 2, '33333'),
#    ('Pedro Lima', 'Rua 4', '4444-444', 1, '44444'),
#    ('Juliana Costa', 'Rua 5', '5555-5555', 1, '55555'),
#    ('Lucas Almeida', 'Rua 6', '6666-6666', 2, '66666'),
# ]
# cursor.executemany(c, val)

# INSERIR DADOS - EDITORIA
# c = 'INSERT INTO editora(endereco, telefone, nome_gerente) VALUES (%s, %s, %s)'
# val = [
#    ('Rua 7', '7777-7777', 'Camila Martins'),
#    ('Rua 8', '8888-8888', 'Lucas Fernandes'),
#    ('Rua 9', '9999-9999', 'Rafael Costa'),
#    ('Rua 10', '1010-1010', 'Beatriz Almeida'),
#    ('Rua 11', '1101-1011', 'Fernando Oliveira'),
# ]  
# cursor.executemany(c, val)

# INSERIR DADOS - LIVRO
# c = 'INSERT INTO livro(nome_autor, nome_livro, assunto, editora, isbn) VALUES (%s, %s, %s, %s, %s)'
# val = [
#         ("George Orwell", "1984", "Distopia", "Secker & Warburg", "9780451524935"),
#         ("Stephen King", "Misery", "Terror", "Viking Penguin", "9780450417399"),
#         ("Harper Lee", "O Sol é Para Todos", "Romance", "J.B. Lippincott & Co.", "9780061120084"),
#         ("J.R.R. Tolkien", "O Senhor dos Anéis: A Sociedade do Anel", "Fantasia", "Allen & Unwin", "9780261102354"),
#         ("Gabriel García Márquez", "Cem Anos de Solidão", "Realismo Mágico", "Editorial Sudamericana", "9780060883287")
# ]
# cursor.executemany(c, val)

# INSERIR DADOS - ESTOQUE
# c = 'INSERT INTO estoque(cod_livro, qtd_estoque) VALUES (%s, %s)'
# val = [
#        (1, 10),
#        (2, 15),
#        (3, 5),
#        (4, 7),
#        (5, 12)
# ]
# cursor.executemany(c, val)

# INSERIR DADOS - COMPRAS
# c = 'INSERT INTO compras(cod_cliente, cod_livro, qtd_compra, data_compra) VALUES (%s, %s, %s, %s)'
# val =[
#         (1, 1, 2, date(2023, 1, 15)),
#         (2, 2, 1, date(2023, 2, 17)),
#         (3, 3, 1, date(2023, 3, 19)),
#         (4, 4, 3, date(2023, 4, 21)),
#         (5, 5, 2, date(2023, 5, 23))
# ]
# cursor.executemany(c, val)
# connection.commit()

# SELECT
'''
cursor.execute('select * from cliente')
r = cursor.fetchall()

for c in r:
    print(c)
'''

'''
cursor.execute('select * from editora')
r = cursor.fetchall()

for e in r:
    print(e)
'''

'''
cursor.execute('select * from livro')
r = cursor.fetchall()

for l in r:
    print(l)
'''

'''
cursor.execute('select cod_cliente from cliente')
r = cursor.fetchall()

for d in r:
    print(d)
'''

'''
cursor.execute('select qtd_estoque from estoque')
r = cursor.fetchall()

for d in r:
    print(d)
'''

'''
cursor.execute('update cliente set nome="Rita Lee" where cod_cliente=3')
con.commit()
'''

'''
cursor.execute('select * from livro order by nome_livro desc')
r = cursor.fetchall()

for i in r:
    print(i)
'''


# TKINTER -----------------------------------------------------------------

# JANELA EXCLUIR
def janela_excluir():
    excluir = tk.Toplevel(i)
    excluir.title('Excluir')
    excluir.geometry('300x200')

    botao_excluir_cliente = tk.Button(excluir, text="Excluir Cliente", command=janela_excluir_cliente)
    botao_excluir_cliente.grid(row=0, column=0, padx=100, pady=10)

    botao_excluir_editora = tk.Button(excluir, text="Excluir Editora", command=janela_excluir_editora)
    botao_excluir_editora.grid(row=1, column=0, padx=100, pady=10)

    botao_excluir_livro = tk.Button(excluir, text="Excluir Livro", command=janela_excluir_livro)
    botao_excluir_livro.grid(row=2, column=0, padx=100, pady=10)

    botao_excluir_compras = tk.Button(excluir, text="Excluir Compras", command=janela_excluir_compras)
    botao_excluir_compras.grid(row=3, column=0, padx=100, pady=10)

#
# EXCLUIR DADOS
#

# CLIENTE
def janela_excluir_cliente():

    def excluir_cliente():
        cod_cliente = e_cod_cliente.get()

        if cod_cliente == '':
                MessageBox.showerror('Status inserir!','Todos os campos são obrigatórios!')
        else:
            q = 'DELETE FROM cliente WHERE cod_cliente = %s'
            v = (cod_cliente,)
            cursor.execute(q,v)
            cursor.execute('commit')
            MessageBox.showinfo('Status excluido!', 'Excluido com sucesso!')
        
    excluir = tk.Toplevel(i)
    excluir.title('Excluir')
    excluir.geometry('300x100')

    tk.Label(excluir, text='Codigo Cliente: ').place(x=20, y=30)
    
    e_cod_cliente = tk.Entry(excluir)
    e_cod_cliente.place(x=120, y=30)

    tk.Button(excluir,text='Excluir',command=excluir_cliente).place(x=20,y=60)

# EDITORA
def janela_excluir_editora():

    def excluir_editora():
        cod_editora = e_cod_editora.get()

        if cod_editora == '':
                MessageBox.showerror('Status inserir!','Todos os campos são obrigatórios!')
        else:
            q = 'DELETE FROM editora WHERE cod_editora = %s'
            v = (cod_editora,)
            cursor.execute(q,v)
            cursor.execute('commit')
            MessageBox.showinfo('Status excluido!', 'Excluido com sucesso!')
        
    excluir = tk.Toplevel(i)
    excluir.title('Excluir')
    excluir.geometry('300x100')

    tk.Label(excluir, text='Codigo editora: ').place(x=20, y=30)
    
    e_cod_editora = tk.Entry(excluir)
    e_cod_editora.place(x=120, y=30)

    tk.Button(excluir,text='Excluir',command=excluir_editora).place(x=20,y=60)

# LIVRO
def janela_excluir_livro():

    def excluir_livro():
        cod_livro = e_cod_livro.get()

        if cod_livro == '':
                MessageBox.showerror('Status inserir!','Todos os campos são obrigatórios!')
        else:
            q = 'DELETE FROM livro WHERE cod_livro = %s'
            v = (cod_livro,)
            cursor.execute(q,v)
            cursor.execute('commit')
            MessageBox.showinfo('Status excluido!', 'Excluido com sucesso!')
        
    excluir = tk.Toplevel(i)
    excluir.title('Excluir')
    excluir.geometry('300x100')

    tk.Label(excluir, text='Codigo livro: ').place(x=20, y=30)
    
    e_cod_livro = tk.Entry(excluir)
    e_cod_livro.place(x=120, y=30)

    tk.Button(excluir,text='Excluir',command=excluir_livro).place(x=20,y=60)

# COMPRAS
def janela_excluir_compras():

    def excluir_compras():
        cod_compra = e_cod_compra.get()

        if cod_compra == '':
                MessageBox.showerror('Status inserir!','Todos os campos são obrigatórios!')
        else:
            q = 'DELETE FROM compras WHERE cod_compra = %s'
            v = (cod_compra,)
            cursor.execute(q,v)
            cursor.execute('commit')
            MessageBox.showinfo('Status excluido!', 'Excluido com sucesso!')
        
    excluir = tk.Toplevel(i)
    excluir.title('Excluir')
    excluir.geometry('300x100')

    tk.Label(excluir, text='Codigo Compras: ').place(x=20, y=30)
    
    e_cod_compra = tk.Entry(excluir)
    e_cod_compra.place(x=120, y=30)

    tk.Button(excluir,text='Excluir',command=excluir_compras).place(x=20,y=60)  


# JANELA ATUALIZAR 
def janela_atualizar():
    atualizar = tk.Toplevel(i)
    atualizar.title('Atualizar')
    atualizar.geometry('300x200')

    botao_atualizar_cliente = tk.Button(atualizar, text="Atualizar Cliente", command=janela_atualizar_cliente)
    botao_atualizar_cliente.grid(row=0, column=0, padx=100, pady=10)

    botao_atualizar_editora = tk.Button(atualizar, text="Atualizar Editora", command=janela_atualizar_editora)
    botao_atualizar_editora.grid(row=1, column=0, padx=100, pady=10)

    botao_atualizar_estoque = tk.Button(atualizar, text="Atualizar Estoque", command=janela_atualizar_estoque)
    botao_atualizar_estoque.grid(row=2, column=0, padx=100, pady=10)

#
# ATUALIZAR DADOS 
#

# CLIENTE
def janela_atualizar_cliente():

    def atualizar_cliente():
        cod_cliente = e_cod_cliente.get()
        nome = e_nome.get()
        endereco = e_end.get()
        telefone = e_tel.get()
        id_tipo = e_tipo.get()
        id_numero = e_numero.get()

        if cod_cliente == '': 
            MessageBox.showerror('Status atualizado', 'Campo "Codigo Cliente" obrigatório!')
        else: 
            y = 'UPDATE cliente SET nome = %s, endereco = %s, telefone = %s, id_tipo = %s, id_numero = %s WHERE cod_cliente = %s'
            val = (nome, endereco, telefone, id_tipo, id_numero, cod_cliente)
            cursor.execute(y,val)
            cursor.execute('commit')
            MessageBox.showinfo('Status atualizado!', 'Atualizado com sucesso!')

    atualizar = tk.Toplevel(i)
    atualizar.title('Atualizar')
    atualizar.geometry('300x320')

    tk.Label(atualizar, text='Codigo Cliente: ').place(x=20, y=30)
    tk.Label(atualizar, text='Nome: ').place(x=20, y=60)
    tk.Label(atualizar, text='Endereco: ').place(x=20, y=90)
    tk.Label(atualizar, text='Telefone: ').place(x=20, y=120)
    tk.Label(atualizar, text='Tipo ID: ').place(x=20, y=150)
    tk.Label(atualizar, text='Numero ID: ').place(x=20, y=180)
    
    e_cod_cliente = tk.Entry(atualizar)
    e_cod_cliente.place(x=120, y=30)
    e_nome = tk.Entry(atualizar)
    e_nome.place(x=120, y=60)
    e_end = tk.Entry(atualizar)
    e_end.place(x=120,y=90)
    e_tel = tk.Entry(atualizar)
    e_tel.place(x=120,y=120)
    e_tipo = tk.Entry(atualizar)
    e_tipo.place(x=120,y=150)
    e_numero = tk.Entry(atualizar)
    e_numero.place(x=120,y=180)

    # BOTAO
    tk.Button(atualizar,text='Atualizar',command=atualizar_cliente).place(x=20,y=210)


# EDITORA
def janela_atualizar_editora():
    
    def atualizar_editora():
        cod_editora = e_cod_editora.get()
        nome_gerente = e_nome.get()
        endereco = e_end.get()
        telefone = e_tel.get()

        if cod_editora == '':
            MessageBox.showerror('Status atualizado!', 'Campo "Codigo Editoria" obrigatório!')
        else: 
            y = 'UPDATE editora SET nome_gerente = %s, endereco = %s, telefone = %s WHERE cod_editora = %s'
            val = (nome_gerente, endereco, telefone, cod_editora)
            cursor.execute(y,val)
            cursor.execute('commit')
            MessageBox.showinfo('Status atualizado!', 'Atualizado com sucesso!')

    atualizar = tk.Toplevel(i)
    atualizar.title('Atualizar')
    atualizar.geometry('300x180')

    tk.Label(atualizar, text='Codigo Editora: ').place(x=20, y=30)
    tk.Label(atualizar, text='Nome: ').place(x=20, y=60)
    tk.Label(atualizar, text='Endereco: ').place(x=20, y=90)
    tk.Label(atualizar, text='Telefone: ').place(x=20, y=120)
    
    e_cod_editora = tk.Entry(atualizar)
    e_cod_editora.place(x=120, y=30)
    e_nome = tk.Entry(atualizar)
    e_nome.place(x=120, y=60)
    e_end = tk.Entry(atualizar)
    e_end.place(x=120,y=90)
    e_tel = tk.Entry(atualizar)
    e_tel.place(x=120,y=120)

    # BOTAO
    tk.Button(atualizar,text='Atualizar',command=atualizar_editora).place(x=20,y=150)

# ESTOQUE
def janela_atualizar_estoque():

    def atualizar_estoque():
        cod_livro = e_cod_livro.get()
        qtd_estoque = e_qtd.get()

        if cod_livro == '':
            MessageBox.showerror('Status atualizado!', 'Campo "Codigo Livro" obrigatório!')
        # FAZER UM ELIF PARA SE O COD_LIVRO AINDA NAO ESTIVER CADASTRADO, USANDO UM MESSAGEBOX
        else:
            y = 'UPDATE estoque SET qtd_estoque = %s WHERE cod_livro = %s'
            val = (qtd_estoque, cod_livro) 
            cursor.execute(y,val)
            cursor.execute('commit')
            MessageBox.showinfo('Status atualizado!',  'Atualizado com sucesso!')

    atualizar = tk.Toplevel(i)
    atualizar.title('Atualizar')
    atualizar.geometry('300x130')

    tk.Label(atualizar, text='Codigo Livro: ').place(x=20, y=30)
    tk.Label(atualizar, text='Quantidade no Estoque: ').place(x=20, y=60)

    
    e_cod_livro = tk.Entry(atualizar)
    e_cod_livro.place(x=160, y=30)
    e_qtd = tk.Entry(atualizar)
    e_qtd.place(x=160, y=60)

    # BOTAO
    tk.Button(atualizar,text='Atualizar',command=atualizar_estoque).place(x=20,y=90)


# JANELA SELECIONAR
def janela_selecionar():

    def selecionar_cliente():

        # CONFIGURACAO DA JANELA
        selecionar_cliente = tk.Toplevel(i)
        selecionar_cliente.title('Cliente Selecionado')
        selecionar_cliente.geometry('300x240')

        # LABEL
        tk.Label(selecionar_cliente, text='Nome: ').place(x=20, y=30)
        tk.Label(selecionar_cliente, text='Endereço: ').place(x=20, y=60)
        tk.Label(selecionar_cliente, text='Telefone: ').place(x=20, y=90)
        tk.Label(selecionar_cliente, text='Tipo ID:').place(x=20, y=120)
        tk.Label(selecionar_cliente, text='Numero:').place(x=20,y=150)

        # ENTRY
        e_nome = tk.Entry(selecionar_cliente)
        e_nome.place(x=120, y=30)
        e_end = tk.Entry(selecionar_cliente)
        e_end.place(x=120, y=60)
        e_tel = tk.Entry(selecionar_cliente)
        e_tel.place(x=120, y=90)
        radio_var = tk.Entry(selecionar_cliente)
        radio_var.place(x=120, y=120)
        e_numero = tk.Entry(selecionar_cliente)
        e_numero.place(x=120, y=150) 


        cod_cliente = cod_cliente_e.get()

        if cod_cliente == '':
            MessageBox.showinfo('Status selecionado!', 'Campo  obrigatórios!')
        else:
            cursor.execute('SELECT * FROM cliente WHERE cod_cliente = %s', (cod_cliente_e.get(),))
            resultado = cursor.fetchall()

            for row in resultado:
                e_nome.insert(0,row[1])
                e_end.insert(0,row[2])
                e_tel.insert(0,row[3])
                radio_var.insert(0,row[4])
                e_numero.insert(0,row[5])
    
    def selecionar_editora(): 

        # CONFIGURACAO DA JANELA
        selecionar_editora = tk.Toplevel(i)
        selecionar_editora.title('Editora Selecionado')
        selecionar_editora.geometry('300x170')

        # LABEL
        tk.Label(selecionar_editora, text='Endereço: ').place(x=20, y=30)
        tk.Label(selecionar_editora, text='Telefone: ').place(x=20, y=60)
        tk.Label(selecionar_editora, text='Nome do Gerente: ').place(x=20, y=90)

        # ENTRY
        e_end = Entry(selecionar_editora)
        e_end.place(x=130, y=30)
        e_tel = Entry(selecionar_editora)
        e_tel.place(x=130, y=60)
        e_nome =Entry(selecionar_editora)
        e_nome.place(x=130, y=90)

        cod_editora = cod_editora_e.get()
        if cod_editora == '':
            MessageBox.showinfo('Status selecionado!', 'Campo  obrigatórios!')
        else:
            cursor.execute('SELECT * FROM editora WHERE cod_editora = %s', (cod_editora_e.get(),))
            resultado = cursor.fetchall()

            for row in resultado:
                e_end.insert(0,row[1])
                e_tel.insert(0,row[2])
                e_nome.insert(0,row[3])

    def selecionar_livro():

        # CONFIGURACAO DA JANELA
        selecionar_livro = tk.Toplevel(i)
        selecionar_livro.title('Livro Selecionado')
        selecionar_livro.geometry('300x240')

        # LABEL
        tk.Label(selecionar_livro, text='Nome do Autor: ').place(x=20, y=30)
        tk.Label(selecionar_livro, text='Nome do Livro: ').place(x=20, y=60)
        tk.Label(selecionar_livro, text='Assunto: ').place(x=20, y=90)
        tk.Label(selecionar_livro, text='Editora: ').place(x=20, y=120)
        tk.Label(selecionar_livro, text='ISBN: ').place(x=20, y=150)
        
        # ENTRY
        e_nome_autor = Entry(selecionar_livro)
        e_nome_autor.place(x=160, y=30)
        e_nome_livro = Entry(selecionar_livro)
        e_nome_livro.place(x=160,y=60)
        e_assunto = Entry(selecionar_livro)
        e_assunto.place(x=160, y=90)
        e_editora = Entry(selecionar_livro)
        e_editora.place(x=160, y=120)
        e_isbn = Entry(selecionar_livro)
        e_isbn.place(x=160, y=150)

        cod_livro = cod_livro_e.get()
        if cod_livro == '':
            MessageBox.showinfo('Status selecionado!', 'Campo  obrigatórios!')
        else:
            cursor.execute('SELECT * FROM livro WHERE cod_livro = %s', (cod_livro_e.get(),))
            resultado_livro = cursor.fetchall()

            for row in resultado_livro:
                e_nome_autor.insert(0,row[1])
                e_nome_livro.insert(0,row[2])
                e_assunto.insert(0,row[3])
                e_editora.insert(0,row[4])
                e_isbn.insert(0,row[5])


    def selecionar_estoque():

        # CONFIGURACAO DA JANELA
        selecionar_estoque = tk.Toplevel(i)
        selecionar_estoque.title('Estoque Selecionado')
        selecionar_estoque.geometry('300x80')

        # LABEL
        tk.Label(selecionar_estoque, text='Quantidade em Estoque:').place(x=20,y=30)

        # ENTRY
        e_qtd = tk.Entry(selecionar_estoque)
        e_qtd.place(x=160,y=80)

        cod_livro = cod_estoque_e.get()
        if cod_livro == '':
            MessageBox.showinfo('Status selecionado!', 'Todos campos  obrigatórios!')
        else:
            cursor.execute('SELECT * FROM estoque WHERE cod_livro = %s', (cod_estoque_e.get(),))
            resultado = cursor.fetchall()

            for row in resultado:
                e_qtd.insert(0,row[1])

    
    def selecionar_compra():
        
        # CONFIGURACAO DA JANELA
        selecionar_compra = tk.Toplevel(i)
        selecionar_compra.title('Compra Selecionado')
        selecionar_compra.geometry('300x240')

        # LABEL
        tk.Label(selecionar_compra, text='Codigo Cliente:').place(x=20, y=30)
        tk.Label(selecionar_compra, text='Codigo Livro:').place(x=20,y=60)
        tk.Label(selecionar_compra, text='Quatintidade:').place(x=20,y=90)
        tk.Label(selecionar_compra, text='Data:').place(x=20,y=120)

        # ENTRY
        e_cod_cliente = tk.Entry(selecionar_compra)
        e_cod_cliente.place(x=120, y=30)
        e_cod_livro = tk.Entry(selecionar_compra)
        e_cod_livro.place(x=120,y=60)
        e_qtd = tk.Entry(selecionar_compra)
        e_qtd.place(x=120,y=90)
        e_data = tk.Entry(selecionar_compra)
        e_data.place(x=120,y=120)

        cod_compra = cod_compras_e.get()
        if cod_compra == '':
            MessageBox.showinfo('Status selecionado!', 'Campo  obrigatórios!')
        else:
            cursor.execute('SELECT * FROM compras WHERE cod_compra = %s', (cod_compras_e.get(),))
            resultado = cursor.fetchall()

            for row in resultado:
                e_cod_cliente.insert(0,row[1])
                e_cod_livro.insert(0,row[2])
                e_qtd.insert(0,row[3])
                e_data.insert(0,row[4])

    selecionar = tk.Toplevel(i)
    selecionar.title('Selecionar')
    selecionar.geometry('300x320')

    tk.Label(selecionar, text='Codigo Cliente:').place(x=20,y=10)
    tk.Label(selecionar, text='Codigo Editora:').place(x=20,y=70)
    tk.Label(selecionar, text='Codigo Livro:').place(x=20,y=130)
    tk.Label(selecionar, text='Codigo Estoque:').place(x=20,y=190)
    tk.Label(selecionar, text='Codigo Compra:').place(x=20,y=250)


    cod_cliente_e = Entry(selecionar)
    cod_cliente_e.place(x=20,y=30)

    cod_editora_e = Entry(selecionar)
    cod_editora_e.place(x=20,y=90)

    cod_livro_e = Entry(selecionar)
    cod_livro_e.place(x=20,y=150)

    cod_estoque_e = Entry(selecionar)
    cod_estoque_e.place(x=20,y=210)

    cod_compras_e = Entry(selecionar)
    cod_compras_e.place(x=20,y=270)


    botao_selecionar_cliente = tk.Button(selecionar, text="Selecionar Cliente", command=selecionar_cliente)
    botao_selecionar_cliente.place(x=160,y=30)

    botao_selecionar_editora = tk.Button(selecionar, text="Selecionar Editora", command=selecionar_editora)
    botao_selecionar_editora.place(x=160,y=90)

    botao_selecionar_livro = tk.Button(selecionar, text="Selecionar Livro", command=selecionar_livro)
    botao_selecionar_livro.place(x=160,y=150)

    botao_selecionar_estoque = tk.Button(selecionar, text="Selecionar Estoque", command=selecionar_estoque)
    botao_selecionar_estoque.place(x=160,y=210)

    botao_selecionar_compras = tk.Button(selecionar, text="Selecionar Compras", command=selecionar_compra)
    botao_selecionar_compras.place(x=160,y=270)


# FAZER UMA TABELA INSERIR ESTOQUE

# JANELA INSERIR
# CLIENTE
def janela_inserir_cliente():

    # INSERIR DADOS
    def inserir_cliente():
        nome = e_nome.get()
        endereco = e_end.get()
        telefone = e_tel.get()
        id_tipo = radio_var.get()
        id_numero = e_id.get()
        
        if  nome == '' or endereco == '' or telefone == '' or id_tipo == '' or radio_var == '':
            MessageBox.showinfo('Status inserir!','Todos os campos são obrigatórios!')
        else: 
            y = 'INSERT INTO cliente(nome,endereco,telefone,id_tipo,id_numero) VALUES (%s, %s, %s, %s, %s)'
            val = (nome,endereco,telefone,id_tipo,id_numero)
            cursor.execute(y,val)
            cursor.execute('commit')
            MessageBox.showinfo('Status inserir!','Inserido com sucesso!')

            e_nome.delete(0,END)
            e_end.delete(0,END)
            e_tel.delete(0,END)
            radio_var.delete(0,END)
            e_id.delete(0,END)


    def escolha_id():
        selecionar = radio_var.get()
        if selecionar == 1:
            id_tipo.config(text="CPF:")
        elif selecionar == 2:
            id_tipo.config(text="CNPJ:")

    cadastro_cliente = tk.Toplevel(i)
    cadastro_cliente.title('Cliente Cadastro')
    cadastro_cliente.geometry("300x230")

    radio_var = tk.IntVar(value=1)
    tk.Label(cadastro_cliente, text='Nome: ').place(x=20, y=30)
    tk.Label(cadastro_cliente, text='Endereço: ').place(x=20, y=60)
    tk.Label(cadastro_cliente, text='Telefone: ').place(x=20, y=90)
    id_tipo = tk.Label(cadastro_cliente, text='CPF:')
    id_tipo.place(x=20, y=150)

    cpf_radio = tk.Radiobutton(cadastro_cliente, text="CPF", variable = radio_var, value = 1, command=escolha_id).place(x=130, y=120)
    cnpj_radio = tk.Radiobutton(cadastro_cliente, text="CNPJ", variable = radio_var, value = 2, command=escolha_id).place(x=180, y=120)

    e_nome = tk.Entry(cadastro_cliente)
    e_nome.place(x=120, y=30)
    e_end = tk.Entry(cadastro_cliente)
    e_end.place(x=120, y=60)
    e_tel = tk.Entry(cadastro_cliente)
    e_tel.place(x=120, y=90)
    e_id = tk.Entry(cadastro_cliente)
    e_id.place(x=120, y=150)

    # BOTÃO
    tk.Button(cadastro_cliente,text='Inserir',command=inserir_cliente).place(x=20,y=180)

# EDITORIA
def janela_inserir_editora():
     
    # INSERIR DADOS
    def inserir_editora():
        endereco = e_end.get()
        telefone = e_tel.get()
        nome_gerente = e_nome.get()

        if endereco == '' or telefone == '' or nome_gerente == '':
            MessageBox.showinfo('Status inserir!','Todos os campos são obrigatórios!')
        else: 
            y = 'INSERT INTO editora(endereco,telefone,nome_gerente) VALUES (%s, %s, %s)'
            val = (endereco,telefone,nome_gerente)
            cursor.execute(y,val)
            cursor.execute('commit')
            MessageBox.showinfo('Status inserir!','Inserido com sucesso!')
            
            e_end.delete(0,END)
            e_nome.delete(0,END) 
            e_tel.delete(0,END)
    
    cadastro_editora = tk.Toplevel(i)
    cadastro_editora.title("Cadastro Editora")
    cadastro_editora.geometry("300x180")

    tk.Label(cadastro_editora, text='Endereço: ').place(x=20, y=30)
    tk.Label(cadastro_editora, text='Telefone: ').place(x=20, y=60)
    tk.Label(cadastro_editora, text='Nome do Gerente: ').place(x=20, y=90)

    e_end = Entry(cadastro_editora)
    e_end.place(x=130, y=30)
    e_tel = Entry(cadastro_editora)
    e_tel.place(x=130, y=60)
    e_nome =Entry(cadastro_editora)
    e_nome.place(x=130, y=90)

    # BOTÃO 
    tk.Button(cadastro_editora,text='Inserir',command=inserir_editora).place(x=20,y=120)
    
# LIVRO
def janela_inserir_livro():
     
    # INSERIR DADOS
    def inserir_livro():
        nome_autor = e_nome_autor.get()
        nome_livro = e_nome_livro.get()
        assunto = e_assunto.get()
        editora = e_editora.get()
        isbn = e_isbn.get()

        if nome_autor == '' or nome_livro == '' or assunto =='' or editora == '' or isbn == '':
            MessageBox.showinfo('Status inserir!','Todos os campos são obrigatórios!')
        else: 
            y = 'INSERT INTO livro(nome_autor,nome_livro,assunto,editora,isbn) VALUES (%s, %s, %s, %s, %s)'
            val = (nome_autor,nome_autor,assunto,editora,isbn)
            cursor.execute(y,val)
            cursor.execute('commit')
            MessageBox.showinfo('Status inserir!','Inserido com sucesso!')

            e_nome_autor.delete(0,END)
            e_nome_livro.delete(0,END)
            e_assunto.delete(0,END)
            e_editora.delete(0,END)
            e_isbn.delete(0,END)
    
    cadastro_livro = tk.Toplevel(i)
    cadastro_livro.title("Cadastro Livro")
    cadastro_livro.geometry("300x250")

    tk.Label(cadastro_livro, text='Nome do Autor: ').place(x=20, y=30)
    tk.Label(cadastro_livro, text='Nome do Livro: ').place(x=20, y=60)
    tk.Label(cadastro_livro, text='Assunto: ').place(x=20, y=90)
    tk.Label(cadastro_livro, text='Editora: ').place(x=20, y=120)
    tk.Label(cadastro_livro, text='ISBN: ').place(x=20, y=150)

    e_nome_autor = Entry(cadastro_livro)
    e_nome_autor.place(x=160, y=30)
    e_nome_livro = Entry(cadastro_livro)
    e_nome_livro.place(x=160,y=60)
    e_assunto = Entry(cadastro_livro)
    e_assunto.place(x=160, y=90)
    e_editora = Entry(cadastro_livro)
    e_editora.place(x=160, y=120)
    e_isbn = Entry(cadastro_livro)
    e_isbn.place(x=160, y=150)

    # BOTAO
    tk.Button(cadastro_livro,text='Inserir',command=inserir_livro).place(x=20,y=180)

# COMPRAS
def janela_inserir_compras():

    # INSERIR DADOS  
    def inserir_compras():
        id_numero = e_id.get()
        isbn = e_isbn.get()
        qtd_compra = e_qtd.get()
        data_compra = e_data.get()
        
        if id_numero== '':
            MessageBox.showinfo('Status inserir!','Todos os campos são obrigatórios!')

        else:
            try:
                cursor.execute('SELECT cod_cliente FROM cliente WHERE id_numero = %s', (id_numero,))
                resultado_cliente = cursor.fetchone()

                cursor.execute('SELECT cod_livro FROM livro WHERE isbn = %s', (isbn,))
                resultado_livro = cursor.fetchone()
                

                if resultado_cliente and resultado_livro:
                    cod_cliente = resultado_cliente[0]
                    cod_livro = resultado_livro[0]

                    y = 'INSERT INTO compras(cod_cliente,cod_livro,qtd_compra,data_compra) VALUES (%s, %s, %s, %s)'  
                    val = (cod_cliente,cod_livro,qtd_compra,data_compra)
                    cursor.execute(y,val)
                    cursor.execute('commit')
                    MessageBox.showinfo('Status inserir!','Inserido com sucesso!')

            except Exception as e:
                print("Erro ao Inserir Compra:", e)
                connection.rollback()
            finally:
                connection.close() 

    def escolha_id():
        selecionar = radio_var.get()
        if selecionar == 1:
            id_tipo.config(text="CPF:")
        elif selecionar == 2:
            id_tipo.config(text="CNPJ:")

    cadastro_compras = tk.Toplevel(i)
    cadastro_compras.title("Cadastro Compras")
    cadastro_compras.geometry("300x250")

    radio_var = tk.IntVar(value=1)
    id_tipo = tk.Label(cadastro_compras, text='CPF:')
    id_tipo.place(x=20, y=30)
    tk.Label(cadastro_compras, text='ISBN:').place(x=20,y=60)
    tk.Label(cadastro_compras, text='Quatintidade:').place(x=20,y=90)
    tk.Label(cadastro_compras, text='Data:').place(x=20,y=120)


    cpf_radio = tk.Radiobutton(cadastro_compras, text="CPF", variable = radio_var, value = 1, command=escolha_id).place(x=130, y=5)
    cnpj_radio = tk.Radiobutton(cadastro_compras, text="CNPJ", variable = radio_var, value = 2, command=escolha_id).place(x=180, y=5)
    
    e_id = tk.Entry(cadastro_compras)
    e_id.place(x=120, y=30)
    e_isbn = tk.Entry(cadastro_compras)
    e_isbn.place(x=120,y=60)
    e_qtd = tk.Entry(cadastro_compras)
    e_qtd.place(x=120,y=90)
    e_data = tk.Entry(cadastro_compras)
    e_data.place(x=120,y=120)

    # BOTAO
    tk.Button(cadastro_compras,text='Inserir',command=inserir_compras).place(x=20,y=150)




# CONFIGURACAO GERAL

i = tk.Tk()
i.title('LIVRARIA')
i.geometry('300x200')

botao_cadastro_cliente = tk.Button(i, text="Cadastro Cliente", command=janela_inserir_cliente)
botao_cadastro_cliente.grid(row=0, column=0, padx=100, pady=10)

botao_cadastro_editora = tk.Button(i, text="Cadastro Editora", command=janela_inserir_editora)
botao_cadastro_editora.grid(row=1, column=0, padx=100, pady=10)

botao_cadastro_livro = tk.Button(i, text="Cadastro Livro", command=janela_inserir_livro)
botao_cadastro_livro.grid(row=2, column=0, padx=100, pady=10)

botao_cadastro_compras = tk.Button(i, text="Cadastro Compras", command=janela_inserir_compras)
botao_cadastro_compras.grid(row=3, column=0, padx=100, pady=10)


# MENU
menu_bar = Menu(i)
i.config(menu=menu_bar)

# MENU EXCLUIR
menu_excluir = Menu(menu_bar)
menu_bar.add_command(label='Excluir', command=janela_excluir)

# MENU SELECIONAR
menu_selecionar = Menu(menu_bar)
menu_bar.add_command(label='Selecionar', command=janela_selecionar)

# MENU ATULIZAR - CLIENTE (NOME, ENDERECO, TELEFONE), EDITORA (NOME GERENTE, ENDERECO, TELEFONE),  ESTOQUE
menu_atualizar = Menu(menu_bar)
menu_bar.add_command(label='Atualizar', command=janela_atualizar)

i.mainloop()