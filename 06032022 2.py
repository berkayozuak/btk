#
#kullanıcıdan isim ,soyisim, telefon numarası alarak bir liste atayınız..
bilgiler=[]#boş liste tanımlar
isim=(input("isim"))
soyisim=(input("soyisim"))
telefon=(input("telefon"))
bilgiler.append(isim)
bilgiler.append(soyisim)
bilgiler.append(telefon)
print(bilgiler)
print(----------------------)
print("Adı:",bilgiler[0])
print("Soyadı:",bilgiler[1])
print("telefon numarası:",bilgiler[2])