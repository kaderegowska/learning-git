shopping = {
    "piekarnia" : ["chleb", "bułki", "pączek"],
    "warzywniak" : ["marchew", "seler", "rukola"]
}
shopping["mięsny"] = ["szynka", "kiełbasa"]
list1 = shopping['piekarnia']
list2 = shopping['warzywniak']
amount = len(list1) + len(list2)
for i in range(len(list1)):
    list1[i] = list1[i].capitalize()
for j in range(len(list2)):
    list2[j] = list2[j].capitalize()
for sklep, produkty in shopping.items():
    print(f"Idę do {sklep.title()} i kupuję tam {produkty}")
print(f"W sumie kupuję {amount} produktów")