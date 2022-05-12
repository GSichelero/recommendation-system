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

user_department = int(input("Você está em qual bloco? (1 a 10)"))
if user_department > 10 or user_department < 1:
    raise Exception("Bloco inválido!")

user_hall = int(input("Você está em qual corredor? (1 a 10)"))
if user_hall > 10 or user_hall < 1:
    raise Exception("Corredor inválido!")
