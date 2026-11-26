import sqlite3
connection = sqlite3.connect("keyscontrol.db")
cursor = connection.cursor()



def keys_register(block,apartment,condominium):
    cursor.execute('INSERT INTO keys (id,block,apartment,condominium) VALUES (?,?,?,?)',(create_key(block,apartment,condominium),block,apartment,condominium))

    connection.commit()

    print('registered key!!')



def get_list():
    cursor.execute('SELECT * FROM keys')
    keys = cursor.fetchall()

    connection.commit()
    return keys



def create_key(block,apartment,condominium):
    id = str(block) + str(apartment) + condominium
    return id




def get_key(id):
    cursor.execute('SELECT * FROM keys WHERE id = ?', (id,))
    key = cursor.fetchone()

    connection.commit()

    if key:
        print('Chave cadastrada!!')
        print(key)
    else:
        print('Não existe uma chave com esse id!')




connection.close()