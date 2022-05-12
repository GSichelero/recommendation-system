user_gender = str(input("Qual o seu gênero? (M/F)"))
if user_gender = 'M':
    user_gender = 0
elif user_gender = 'F':
    user_gender = 1
else:
    raise Exception("Gênero não encontrado!")

user_age = int(input("Qual a sua idade? (16 a 100)"))
if 100 < user_age < 16:
    raise Exception("Idade está fora do limite cadastrável!")




