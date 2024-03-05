import os

namen = ["Hans Peter", "Peter Hans", "Klaus Müller"]
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

for i, name in enumerate(namen):
    file_path = os.path.join(desktop_path, f'Einladung_{i+1}.txt')
    with open(file_path, 'w') as f:
        f.write("Einladung zur Party\n")
        f.write("Hallo " + name + ", ich lade dich zu meiner Party ein.\n")
        f.write("Ich freue mich auf dein Kommen.\n")