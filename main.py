skore = []
for i in range(10):
    skore = (input("zadej skore (0-60): "))
    skore.append(skore)
print("všechny skore jsou", skore)
print("nejlepší skore je", max(skore))
print("nejnižší skore je", min(skore))
print("průměrné skore je", sum(skore)  / 10)

for i in (skore):
    nad_50 = sum(1 for skore in skore if skore > 50)
 if nad_50 >= len(skore) / 2:
       print("výborný výkon!")
else:
    print("můžete to příště zkusit lépe")
