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
print("Ten program oblicza BMI")
waga = float(input("Podaj wagę:"))
wzrost = float(input("Podaj wzrost:"))

BMI= (waga/(wzrost**2))*10000
 
print(f"Twoje BMI wynosi: { BMI:.1f} "  )
 
if(BMI<18.5):
    print("Masz niedowagę")
elif (BMI>=18.5 and BMI<25):
    print("Masz prawidłową wagę")
elif(BMI>=25 and BMI<30):
    print("Masz nadwagę")
elif(BMI>=30):
    print("Masz otyłość")