countries = [
{"name":"Poland", "population":38000000}
]
country = ["rosia", "Ukraine", "France", "Geramany"]
pop = [1, 25000000, 60000000, 80000000]

for c in range(len(country)):
    countries.append({"name": country[c], "population": pop[c]})

for i in countries: 
    for k,v in i.items():
        print(f"{k}: {v}", end=" ")
    print()