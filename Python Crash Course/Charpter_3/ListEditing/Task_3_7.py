guests = ['Hanna', 'Artem', 'Algis', 'Zhekas', 'Vladoss']

print(f"К сожалению новый стол привезти не успеют. У нас всего 2 места. Мне очень жаль!")
print(f"Sorry, {guests.pop()}, see you later :(")
print(f"Sorry, {guests.pop()}, see you later :(")
print(f"Sorry, {guests.pop()}, see you later :(")

print(guests)
print(f"Hey, {guests[0]}! See you soon!")
print(f"Hey, {guests[1]}! See you soon!")

del guests[0]
del guests[0]

print(guests)