#kullanıcıadı ve şifre alınız.. kullancı adı olarak "admin"şifre olarak
#123456 girilince "sisteme başarıyla giriş yaptınız yazsın..
# #yanlış girildikçe"kullanıcıadı veya şifre hatalı" yazsın..
#tekrar kullanıcıadı ve şifre sorsun!
while True:
    kullaniciadi=input("kullanıcıadınız:")
    sifre=input("Parolanız:")
    if kullaniciadi=="admin" and sifre=="123456":
            break
    else:
        print()
print("sisteme başarıyla girişi yaptınız..")

