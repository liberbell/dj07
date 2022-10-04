places = ["New Zealand", "Norway", "Botswana", "Zimbabwe", "Uzbekistan", "Paraguay"]
villain_at = "Mali"

for place in places:
    if place == villain_at:
        print("The villain has been captured!")
        break
else:
    print("Teh villain got away.")