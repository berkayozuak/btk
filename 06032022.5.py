#KARŞILAŞTIRMA OPERATÖRLERİ
"""
< : Küçüktür
> : Büyüktür
<= :küçük eşit
>= :büyük eşit
==:eşittir
!= : eşit değildir
"""
cinsiyet=input("bir harf giriniz:")

if cinsiyet=="e": or cinsiyet=="E":#or 2 şarttan biri doğru ise çalışır
    print("cinsiyet olarak erkek girdiniz")
    print("if içerisinden selamlar")
elif cinsiyet=="k" or cinsiyet=="K":#2.veya dahasonraki şartları eklemek için elif kullanılır
   print("Cinsiyet olarak kadın girdiniz")
   print("Şuanda elif bloğu içinden mesaj veriyorum")
else: #şartları dışında herhangi birşey girilirse çalışır
    print("ben sana e ya da k gir demedim mi?")
print("şuanda if dışındasın")