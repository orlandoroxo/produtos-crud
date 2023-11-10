# Aluno: Orlando da Silva Roxo
# Pré-requisitos: psycopg2 (PostgreSQL Driver) - pip install psycopg2
# Para compilar e executar: python programa.py

import psycopg2
import tkinter as tk
from tkinter import ttk

class SistemaCRUD:
    def __init__(self, nome_sistema):
        self.nome_sistema = nome_sistema
        self.conn = None
        self.connect()

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host="localhost",
                database="meubanco",
                user="orlando",
                password="orlando2552",
                port=5432,
                #encoding="utf-8"
            )
            print("Conexão com o Banco de Dados aberta com sucesso!")
            self.create_table()
            print("Tabela Produto criada com sucesso!")
        except psycopg2.Error as e:
            print(f"Falha ao se conectar ao Banco de Dados: {e}")
            if self.conn:
                self.conn.close()

    def create_table(self):
        try:
            comando = self.conn.cursor()
            comando.execute("""CREATE TABLE IF NOT EXISTS Produto
                            (id INT PRIMARY KEY NOT NULL,
                            Nome TEXT NOT NULL,
                            Preco NUMERIC(10, 2));""")  
            self.conn.commit()
            print("Tabela criada com sucesso no BD!!!")
        except psycopg2.Error as e:
            print(f"Falha ao criar tabela: {e}")


    def insert_data(self, id, nome, preco):
        try:
            comando = self.conn.cursor()
            comando.execute("""INSERT INTO Produto (id, Nome, Preco)
                            VALUES (%s, %s, %s);""", (id, nome, preco))  
            self.conn.commit()
            print("Inserção realizada com sucesso!!!")
        except psycopg2.Error as e:
            print(f"Falha ao inserir dados: {e}")

    def update_data(self, id, nome, preco):
        try:
            comando = self.conn.cursor()
            comando.execute("UPDATE Produto SET Nome = %s, Preco = %s WHERE id = %s;",
                            (nome, preco, id))  
            self.conn.commit()
            print("Registro Atualizado com sucesso!!!")
        except psycopg2.Error as e:
            print(f"Falha ao atualizar dados: {e}")


    def read_data(self, id):
        try:
            comando = self.conn.cursor()
            comando.execute("SELECT * FROM Produto WHERE id = %s;", (id,))
            return comando.fetchone()  
        except psycopg2.Error as e:
            print(f"Falha ao ler dados: {e}")


    def delete_data(self, id):
        try:
            comando = self.conn.cursor()
            comando.execute("DELETE FROM Produto WHERE id = %s;", (id,))
            self.conn.commit()
            print("Registro excluído com sucesso!")
        except psycopg2.Error as e:
            print(f"Falha ao excluir dados: {e}")

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("Conexão com o banco de dados fechada.")

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Cyber Lista")
        
        self.sistema_crud = SistemaCRUD("SistemaCRUD")

        self.notebook = ttk.Notebook(master)
        self.notebook.grid(row=0, column=0, sticky='nsew')
        
        self.tab_inserir = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_inserir, text='Inserir')
        self.build_inserir_tab()
        
        self.tab_atualizar = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_atualizar, text='Atualizar')
        
        self.tab_deletar = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_deletar, text='Deletar')
        
        self.tab_buscar = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_buscar, text='Buscar')
        
        self.build_inserir_tab()
        self.build_atualizar_tab()
        self.build_deletar_tab()
        self.build_buscar_tab()

        self.tree = ttk.Treeview(master, columns=('ID', 'Nome', 'Preço', 'Preço Acrescido'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Nome', text='Nome')
        self.tree.heading('Preço', text='Preço')
        self.tree.heading('Preço Acrescido', text='Preço Acrescido (10%)')
        self.tree.grid(row=6, column=0, columnspan=4, sticky='nsew')

        self.scrollbar = tk.Scrollbar(master, orient=tk.VERTICAL, command=self.tree.yview)
        self.scrollbar.grid(row=6, column=4, sticky='ns')
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.atualizar_tabela()

    def atualizar_tabela(self):

        for i in self.tree.get_children():
            self.tree.delete(i)
        
        try:
            comando = self.sistema_crud.conn.cursor()
            comando.execute("SELECT id, Nome, Preco, Preco * 1.10 as Preco_Acrescido FROM Produto;")
            for row in comando.fetchall():
                self.tree.insert('', tk.END, values=row)
        except psycopg2.Error as e:
            print(f"Falha ao consultar dados para a tabela: {e}")
    
    def build_inserir_tab(self):
        self.lbl_id_inserir = tk.Label(self.tab_inserir, text="ID:")
        self.lbl_id_inserir.grid(row=0, column=0)
        
        self.ent_id_inserir = tk.Entry(self.tab_inserir)
        self.ent_id_inserir.grid(row=0, column=1)
        
        self.lbl_nome_inserir = tk.Label(self.tab_inserir, text="Nome:")
        self.lbl_nome_inserir.grid(row=1, column=0)
        
        self.ent_nome_inserir = tk.Entry(self.tab_inserir)
        self.ent_nome_inserir.grid(row=1, column=1)
        
        self.lbl_preco_inserir = tk.Label(self.tab_inserir, text="Preço:")
        self.lbl_preco_inserir.grid(row=2, column=0)
        
        self.ent_preco_inserir = tk.Entry(self.tab_inserir)
        self.ent_preco_inserir.grid(row=2, column=1)
        
        self.lbl_preco_acrescido_inserir = tk.Label(self.tab_inserir, text="Preço Acrescido (10%):")
        self.lbl_preco_acrescido_inserir.grid(row=3, column=0)
        
        self.lbl_valor_preco_acrescido_inserir = tk.Label(self.tab_inserir, text="")
        self.lbl_valor_preco_acrescido_inserir.grid(row=3, column=1)
        
        self.btn_inserir_inserir = tk.Button(self.tab_inserir, text="Inserir", command=self.inserir)
        self.btn_inserir_inserir.grid(row=4, column=0, columnspan=2)

        self.lbl_mensagem_inserir = tk.Label(self.tab_inserir, text="")
        self.lbl_mensagem_inserir.grid(row=5, column=0, columnspan=2)

    def build_atualizar_tab(self):
        self.lbl_id_atualizar = tk.Label(self.tab_atualizar, text="ID:")
        self.lbl_id_atualizar.grid(row=0, column=0)
        
        self.ent_id_atualizar = tk.Entry(self.tab_atualizar)
        self.ent_id_atualizar.grid(row=0, column=1)
        
        self.lbl_nome_atualizar = tk.Label(self.tab_atualizar, text="Nome:")
        self.lbl_nome_atualizar.grid(row=1, column=0)
        
        self.ent_nome_atualizar = tk.Entry(self.tab_atualizar)
        self.ent_nome_atualizar.grid(row=1, column=1)
        
        self.lbl_preco_atualizar = tk.Label(self.tab_atualizar, text="Preço:")
        self.lbl_preco_atualizar.grid(row=2, column=0)
        
        self.ent_preco_atualizar = tk.Entry(self.tab_atualizar)
        self.ent_preco_atualizar.grid(row=2, column=1)
        
        self.lbl_preco_acrescido_atualizar = tk.Label(self.tab_atualizar, text="Preço Acrescido (10%):")
        self.lbl_preco_acrescido_atualizar.grid(row=3, column=0)
        
        self.lbl_valor_preco_acrescido_atualizar = tk.Label(self.tab_atualizar, text="")
        self.lbl_valor_preco_acrescido_atualizar.grid(row=3, column=1)
        
        self.btn_atualizar_atualizar = tk.Button(self.tab_atualizar, text="Atualizar", command=self.atualizar)
        self.btn_atualizar_atualizar.grid(row=4, column=0, columnspan=2)

        self.lbl_mensagem_atualizar = tk.Label(self.tab_atualizar, text="")
        self.lbl_mensagem_atualizar.grid(row=5, column=0, columnspan=2)

    def build_deletar_tab(self):
        self.lbl_id_deletar = tk.Label(self.tab_deletar, text="ID:")
        self.lbl_id_deletar.grid(row=0, column=0)
        
        self.ent_id_deletar = tk.Entry(self.tab_deletar)
        self.ent_id_deletar.grid(row=0, column=1)
        
        self.btn_deletar_deletar = tk.Button(self.tab_deletar, text="Deletar", command=self.deletar)
        self.btn_deletar_deletar.grid(row=1, column=0, columnspan=2)

        self.lbl_mensagem_deletar = tk.Label(self.tab_deletar, text="")  
        self.lbl_mensagem_deletar.grid(row=2, column=0, columnspan=2)


    def build_buscar_tab(self):
        self.lbl_id_buscar = tk.Label(self.tab_buscar, text="ID:")
        self.lbl_id_buscar.grid(row=0, column=0)
        
        self.ent_id_buscar = tk.Entry(self.tab_buscar)
        self.ent_id_buscar.grid(row=0, column=1)
        
        self.btn_buscar_buscar = tk.Button(self.tab_buscar, text="Buscar", command=self.buscar)
        self.btn_buscar_buscar.grid(row=1, column=0, columnspan=2)
        
        self.lbl_resultado_buscar = tk.Label(self.tab_buscar, text="")
        self.lbl_resultado_buscar.grid(row=2, column=0, columnspan=2)

    def inserir(self):
        id = self.ent_id_inserir.get()
        nome = self.ent_nome_inserir.get()
        preco = float(self.ent_preco_inserir.get())
        
        registro_existente = self.sistema_crud.read_data(id)
        if registro_existente:
            self.lbl_mensagem_inserir.config(text="ID já existente. Por favor, insira um ID diferente.", fg="red")
            return
        
        self.sistema_crud.insert_data(id, nome, preco)
        self.lbl_valor_preco_acrescido_inserir.config(text=str(preco * 1.1))
        self.lbl_mensagem_inserir.config(text="Produto inserido com sucesso!", fg="green")
        self.atualizar_tabela()

    def atualizar(self):
        id = self.ent_id_atualizar.get()
        nome = self.ent_nome_atualizar.get()
        preco = float(self.ent_preco_atualizar.get())
        
        self.sistema_crud.update_data(id, nome, preco)
        self.lbl_valor_preco_acrescido_atualizar.config(text=str(preco * 1.1))
        self.lbl_mensagem_atualizar.config(text="Produto atualizado com sucesso!", fg="green")
        self.atualizar_tabela()

    def deletar(self):
        id = self.ent_id_deletar.get()
        self.sistema_crud.delete_data(id)
        self.ent_id_deletar.delete(0, tk.END)  
        self.lbl_mensagem_deletar.config(text="Produto deletado com sucesso!")
        self.atualizar_tabela()

    def buscar(self):
        id = self.ent_id_buscar.get()
        registro = self.sistema_crud.read_data(id)
        if registro:
            resultado = f"Nome: {registro[1]}, Preço: {registro[2]}, Preço Acrescido (10%): {float(registro[2])*1.1}"
            self.lbl_resultado_buscar.config(text=resultado)
        else:
            self.lbl_resultado_buscar.config(text="Produto não encontrado.")

    def limpar_campos(self):
        self.ent_id.delete(0, tk.END)
        self.ent_nome.delete(0, tk.END)
        self.ent_preco.delete(0, tk.END)
        self.ent_preco_acrescido.delete(0, tk.END)
        self.atualizar_tabela()

if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
