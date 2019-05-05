#  finding nemo
from datetime import datetime
import time

character_list = ["Dory", "Crush", "Marlin", "Bruce", "Nigel",
                  "Corala", "Deb", "Bubbles", "Darla", "Dentist", "Mr.Ray", "Tad", "Peach", "Bloat", "Anchor", "Squit", "Nemo"]

for i in range(500000):
    character_list.append("Nemo")


def findingNemo(list):
    start = time.time()
    for char in list:
        if char == "Nemo":
            print("found nemo")
    end = time.time()
    c = (start - end)
    print(c)


findingNemo(character_list)
