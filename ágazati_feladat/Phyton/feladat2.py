szám1=int(input("Írd be az első számot: "))
szám2=int(input("Írd be a második számot:"))

talált_számok=[]
for szám in range(szám1 + 1, szám2):
    talált_számok.append(szám)

print(talált_számok)

háromal_osztható=[]
for x in (talált_számok):
    if x % 3 == 0:
        háromal_osztható.append(x)
print(f"A két szám között {len(háromal_osztható)} db szám van ami osztható 3-mal")        


    