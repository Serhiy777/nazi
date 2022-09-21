from colorama import init  # імпорт модуля колорама
from colorama import Fore  # імпорт Fore для покраски тексту

init()  # виклик модуля колорама

# введення данних для опрацьовування
x = int(input(Fore.CYAN + "Сума депозиту - UAH: "))
p = int(input(Fore.CYAN + "Процент - %: "))
y = int(input(Fore.CYAN + "Сума депозиту на виході - UAH: "))

# функція
monthly = x * (p / 100)
months = 0

while x < y:  # цикл, сума депозиту на старті повинна бути строго менша за суму на виході
    x = round(x + monthly, 2) # додавання до початкової суми процентної ставки
    months += 1  # те саме, що months = months + 1

print(Fore.GREEN + f"Вам потрібно {months} місяці(ів), для накопичення {y} UAH;\nПриватбанк - беремо і робимо!")
