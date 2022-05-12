import psycopg2

user_gender = str(input("Qual o seu gênero? (M/F)"))
if user_gender == 'M':
    user_gender = 0
elif user_gender == 'F':
    user_gender = 1
else:
    raise Exception("Gênero não encontrado!")

user_age = int(input("Qual a sua idade? (16 a 100)"))
if 100 < user_age < 16:
    raise Exception("Idade está fora do limite cadastrável!")

user_has_car = str(input("Você veio de carro? (S/N)"))
if user_has_car == 'S':
    user_has_car = 1
elif user_has_car == 'N':
    user_has_car = 0
else:
    raise Exception("Resposta inválida!")

user_has_children = str(input("Você stá com crianças? (S/N)"))
if user_has_children == 'S':
    user_has_children = 1
elif user_has_children == 'N':
    user_has_children = 0
else:
    raise Exception("Resposta inválida!")
    
user_has_partner = str(input("Você está acompanhado? (S/N)"))
if user_has_partner == 'S':
    user_has_partner = 1
elif user_has_partner == 'N':
    user_has_partner = 0
else:
    raise Exception("Resposta inválida!")

user_has_pet = str(input("Você está com animal de estimação? (S/N)"))
if user_has_pet == 'S':
    user_has_pet = 1
elif user_has_pet == 'N':
    user_has_pet = 0
else:
    raise Exception("Resposta inválida!")


print("""
Frutas: Blocos 1-2, Corredores 1-5\n
Vegetais: Blocos 1-3, Corredores 6-10\n
Laticínios: Blocos 3-4, Corredores 1-5\n
Bebidas: Blocos 4-5, Corredores 6-10\n
Carnes: Blocos 5-6, Corredores 1-7\n
Eletrônicos: Blocos 7-8, Corredores 1-4\n
Games: Blocos 7-9, Corredores 4-8\n
Filmes: Blocos 7-9, Corredores 6-10\n
Livros: Blocos 8-9, Corredores 1-9\n
Cuidado Pessoal: Blocos 9-10, Corredores 1-10\n
""")
user_department = int(input("Você está em qual bloco? (1 a 10)"))
if user_department > 10 or user_department < 1:
    raise Exception("Bloco inválido!")

user_hall = int(input("Você está em qual corredor? (1 a 10)"))
if user_hall > 10 or user_hall < 1:
    raise Exception("Corredor inválido!")

conn = psycopg2.connect("dbname=recommendation user=postgres password=ggi2011 port=5432")
cur = conn.cursor()

# select all items from store_products and store in a list of dictionaries
# id,
# name,
# price,
# type,
# department,
# has_car,
# has_son,
# has_partner,
# halls,
# has_pet,
# age,
# gender,
data = []
cur.execute("SELECT * FROM store_products")
products = cur.fetchall()
for product in products:
    data.append({
        'id': product[0],
        'name': product[1],
        'price': product[2],
        'type': product[3],
        'department': product[4],
        'has_car': product[5],
        'has_son': product[6],
        'has_partner': product[7],
        'halls': product[8],
        'has_pet': product[9],
        'age': product[10],
        'gender': product[11],
        'score': 0
    })

# for each item in data, calculate the similarity with the users inputs
for item in data:
    if user_has_car == item['has_car']:
        item['score'] += 1
    if user_has_children == item['has_son']:
        item['score'] += 1
    if user_has_partner == item['has_partner']:
        item['score'] += 1
    if user_has_pet == item['has_pet']:
        item['score'] += 1
    if user_gender == item['gender']:
        item['score'] +=1
    
    if abs(user_age - item['age']) <= 5:
        item['score'] += 1
    elif abs(user_age - item['age']) <= 10:
        item['score'] += 0.5
    elif abs(user_age - item['age']) <= 30:
        item['score'] += 0.25
    
    item['score'] += ((1 - (((abs(item['department'] - user_department) * 3) + abs(item['halls'] - user_hall)) / 36)) * 3)
    
    item['score'] = round(item['score'], 2)


# sort the list of dictionaries by score
data.sort(key=lambda x: x['score'], reverse=True)

# print the first 5 items
for index, item in enumerate(data[:5]):
    print(f"Opção {index + 1}:")
    print(f"Nome: {item['name']}")
    print(f"Preço: R${item['price']},00")
    print(f"Score: {item['score']}")
    print('\n')

user_choice = int(input("Você vai comprar qual item? (0 = Nenhum)"))
if user_choice == 0:
    print("Nenhuma opção escolhida!")
elif user_choice > 0 and user_choice <= 5:
    user_choice = data[user_choice - 1]
    # insert the user's choice in the store_products with the options the user has
    postgres_insert_query = """INSERT INTO store_products (name, price, type, department, has_car, has_son, has_partner, halls, has_pet, age, gender) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    record_to_insert = (item["name"], item["price"], item["type"], item["department"], user_has_car, user_has_children, user_has_partner, item["halls"], user_has_pet, user_age, user_gender)
    cur.execute(postgres_insert_query, record_to_insert)



    

    



