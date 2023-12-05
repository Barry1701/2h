countries_and_capitals = {"Poland" : "Warsaw", "Germany" : "Berlin", "Ireland" : "Dublin"}

try:
    print(countries_and_capitals["USA"] )
except KeyError:
    print("Nie ma takiego panstwa ziom")
finally:
    print("zamykamy polaczenie do bazy danych")

