# # # names_set = {"Barry", "Michal", "Marcin", "Kufel", "Barry"}#Barry wyswietli sie tylko raz,set nie duplikuje wartosci
# # # print(names_set)

# names_set = set()
# names_set.add("Michal")
# names_set.add("Maciek")
# names_set.add("Barman")
# names_set.add("Maciek")
# names_set.remove("Barman")#remove i discard - jak nie ma imienia to przy discard nic sie nie dzieje a przy remove error
names_set2 = {"Tytus", "Romek", "Atomek"}
# names_set3 = names_set.union(names_set2) # zamiast plusa(+) jest union.
# # # print(names_set)
# for name in names_set3:
#     print(name)

# #elementy setu musz byc niemutowalne i nie sa uporzadkowane

names_list = ["Olga", "Diana", "Edyta"]
names_list.extend(names_set2) #laczenie listy i setow
print(names_list)

