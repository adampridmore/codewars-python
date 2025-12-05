def allowed_character(c):
     return ("aeiouAEIUO".find(c) == -1)

def process(text):
    return ''.join(filter(allowed_character, text))

print(process("This website is for losers LOL!"))


# "Ths wbst s fr lsrs LL!"