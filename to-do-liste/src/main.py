# Familienmitglieder erfassen
familienmitglieder = []
anzahl = int(input("Wie viele Familienmitglieder gibt es? "))
for i in range(anzahl):
    name = input(f"Gib den Namen von Mitglied {i+1} ein: ")
    familienmitglieder.append(name)

# Für jedes Mitglied eine Aufgabenliste anlegen
aufgaben = {mitglied: [] for mitglied in familienmitglieder}
erledigte_aufgaben = {mitglied: [] for mitglied in familienmitglieder}

while True:
    print("\nFamilienmitglieder:", ", ".join(familienmitglieder))
    person = input("Für wen möchtest du etwas tun? (Name eingeben): ")
    if person not in familienmitglieder:
        print("Mitglied nicht gefunden!")
        continue

    print(f"\n1. Aufgabe hinzufügen\n2. Aufgaben anzeigen\n3. Aufgabe erledigen\n4. Erledigte Aufgaben anzeigen\n5. Anderes Mitglied auswählen\n6. Programm beenden")
    choice = input("Wähle eine Option: ")

    if choice == "1":
        task = input("Welche Aufgabe? ")
        date = input("Bis wann? ")
        aufgaben[person].append({"task": task, "date": date})
        print("Aufgabe hinzugefügt!")
    elif choice == "2":
        if aufgaben[person]:
            print(f"Aufgaben für {person}:")
            for i, t in enumerate(aufgaben[person], 1):
                print(f"{i}. {t['task']} (bis {t['date']})")
        else:
            print("Keine Aufgaben!")
    elif choice == "3":
        if aufgaben[person]:
            print(f"Aufgaben für {person}:")
            for i, t in enumerate(aufgaben[person], 1):
                print(f"{i}. {t['task']} (bis {t['date']})")
            index = int(input("Welche Aufgabe wurde erledigt? (Nummer): ")) - 1
            if 0 <= index < len(aufgaben[person]):
                erledigte_aufgaben[person].append(aufgaben[person].pop(index))
                print("Aufgabe als erledigt markiert!")
            else:
                print("Ungültige Nummer!")
        else:
            print("Keine Aufgaben!")
    elif choice == "4":
        if erledigte_aufgaben[person]:
            print(f"Erledigte Aufgaben für {person}:")
            for i, t in enumerate(erledigte_aufgaben[person], 1):
                print(f"{i}. {t['task']} (bis {t['date']})")
        else:
            print("Keine erledigten Aufgaben!")
    elif choice == "5":
        restart = input("Möchtest du ein anderes Mitglied auswählen? (y/n): ")  
        if restart.lower() == 'y':
            continue
        else:
            continue
    elif choice == "6":
        x=input("Are you sure you want to exit? (y/n): ")
        if x.lower() == 'y':
            break
        else:
            continue
    else:print("Ungültige Auswahl!")