print("hello world")
print("Jest to program obliczający średnią z trzech liczb ")
a = float(input("Podaj zmienną a:"))
b = float(input("Podaj zmienną b:"))
c = float(input("Podaj zmienną c:"))
avg = (a+b+c)/3

print("Twoja średnia wynosi: " , avg)

print("Jest to program przyjmujący od użytkownika jedną liczbę, ma on sprawdzić czy liczba jest dodatnia, ujemna czy równa zero")
d = float(input("Podaj zmienną d:"))

if(d==0):
    print("Liczba jest równa zero")
elif(d>0):
    print("Liczba jest dodatnia")
else:
    print("Liczba jest ujemna")