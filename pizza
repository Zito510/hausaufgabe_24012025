pizza_price = float(input("Wie viel kostet eine Pizza? "))
number_pieces = int(input("Wie viele Stuecke von Pizza wurden gegessen? "))

pieces_eaten = {}

while True:
    name = input("Was ist der Name der Person? (schreibe 'fertig', um die Eingabe zu beenden) ")

    if name == "fertig":
        break

    pieces_per_person = int(input("Wie viele Stuecke hat diese Person gegessen? "))
    pieces_eaten[name] = pieces_per_person

print(f"Pizzapreis: {pizza_price}")
print(f"Anzahl Stuecke: {number_pieces}")
print(f"Dictionary: {pieces_eaten}")

price_per_piece = pizza_price / number_pieces

for person in pieces_eaten:
    bill = price_per_piece * pieces_eaten[person]
    print(f"{person} hat {pieces_eaten[person]} Stueck Pizza gegessen. Zu zahlen sind {bill}.")
