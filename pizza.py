# Input: Stücke, Personen, Preis, Stücke pro Person
# Annahmen: 1 Pizza, gleich große Stücke

people = {}

def get_number(question, int_only = False):
    while True:
        try:
            if int_only:
                number = int(input(question))
            else:
                number = float(input(question))
            if number < 0:
                print()
                print("Die Zahl darf nicht negativ sein.")
            else:
                break
        except:
            print()
            print("Bitte gib die Zahl nur mit Ziffern an (0-9).")
            if not int_only:
                print("Benutze '.' für das Dezimaltrennzeichen.")
    return number

def euro(cents):
    if cents % 100 == 0:
        return str(int(cents/100))
    return str(cents // 100) + "." + str(cents % 100)

def piece_s(amount, verb_singular = "", verb_plural = ""):
    output = str(amount) + " Stück"
    if amount != 1:
        output += "e"
        verb = verb_plural
    else:
        verb = verb_singular
    if verb:
        output = verb + " " + output
    return output

def add_person(dict):
    person = input("Gib den Namen einer Person an, die Pizza isst: ")
    if person == "":
        print("Eingabe beendet.")
        print()
        return False
    pieces = get_number(f"Wie viele Stücke isst {person}? ", True)
    if pieces == 0:
        print(f"{person} isst nicht mit.")
        dict.pop(person, None)
    else:
        print(f"{person} isst {piece_s(pieces)}.")
        dict[person] = pieces
    print()
    return True

def change_people(dict):
    print("Gib die Personen und Stücke an. Beenden durch leere Eingabe.")
    print()
    while add_person(dict):
        pass
    while len(dict) == 0:
        print("Die Anzahl Personen darf nicht 0 sein.")
        print()
        while add_person(dict):
            pass
    if len(dict) == 1:
        print(f"{list(dict)[0]} isst alleine.")
    else:
        print(f"Die Pizza wird duch {len(dict)} Personen geteilt.")
    print()

def get_sum(dict):
    pieces = 0
    for p in dict.values():
        pieces += p
    return pieces

def get_pieces_total():
    return get_number("Wie viele Stücke hat die Pizza? ", True)

pieces_total = get_pieces_total()
price_total = get_number("Wieviel kostet die Pizza in Euro? ", False)
price_total = round(price_total * 100)
print(f"Die Pizza kostet {euro(price_total)} Euro")
print()

yes = ["ja", "Ja", "JA", "j", "J", "yes", "Yes", "YES", "y", "Y"]
yes_low = ["ja", "j", "yes", "y"]

def check_answer(answer):
    answer_low = answer.lower()
    if answer_low in yes_low:
        return True
    return False

change_people(people)
pieces_eaten = get_sum(people)

while pieces_eaten != pieces_total:
    print(f"Die Personen möchten insgesamt {piece_s(pieces_eaten)} essen.\n"
        + f"Die Pizza besteht aber aus {piece_s(pieces_total)}."
    )
    print()
    if pieces_eaten < pieces_total:
        print(f"Es {piece_s(pieces_total - pieces_eaten, "bleibt", "bleiben")} übrig.")
        answer = input("Ist das so in Ordnung? ")
        print()
        if check_answer(answer):
            break
    answer = input("Möchstest du die Pizza neu schneiden? ")
    print()
    if check_answer(answer):
        if check_answer(input("Soll die Pizza vollständig auf alle aufgeteilt werden? ")):
            pieces_total = pieces_eaten
        else:
            pieces_total = get_pieces_total()
        print(f"Die Pizza besteht aus {piece_s(pieces_total)}.")
        print()
    else:
        print("Dann musst du die Anzahlen Stücke pro Person anpassen.\n"
            + "Dies sind die Personen und wiviele Stücken sie essen:"
        )
        for person, pieces in people.items():
            print(f"{person} isst {piece_s(pieces)}.")
        print()
        change_people(people)
        pieces_eaten = get_sum(people)
        print(f"Es {piece_s(pieces_eaten, "wird", "werden")} gegessen.")
        print()

for person, pieces in people.items():
    people[person] = round(price_total * pieces / pieces_eaten)
price_people = get_sum(people)
print("Hier sind die Kosten pro Person:")
for person, price in people.items():
    print(f"{person} bezahlt {euro(price)} Euro.")
cents = price_people - price_total
if cents > 0:
    print(f"Es wird Trinkgeld in Höhe von {cents} Cent gegeben.")
elif cents < 0:
    print(f"Wir müssen noch insgesamt {- cents} Cent dazugeben.")
