import os

# Definieren von 'desktop_path' vor der Verwendung
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Pfad zur Textdatei
file_path = os.path.join(desktop_path, 'namen.txt')

# Öffnen der Datei und Lesen der Zeilen
with open(file_path, 'r') as f:
    lines = f.readlines()

# Entfernen des Zeilenumbruchs am Ende jeder Zeile und Hinzufügen zur Liste 'namen'
namen = [line.strip() for line in lines]

for i, name in enumerate(namen):
    file_path = os.path.join(desktop_path, f'Einladung_{i+1}.txt')
    with open(file_path, 'w') as f:
        f.write("Einladung zur Party\n")
        f.write("Hallo " + name + ", ich lade dich zu meiner Party ein.\n")
        f.write("Ich freue mich auf dein Kommen.\n")