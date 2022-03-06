"""
kullanıcı yılsonu ortalaması girsin. ortalama 85 üstü ise takdir, 70 üstü teşekkür
bunların dışında ise hiçbişey alamadınız desin..
"""
ort=int(input("not ortalaması girin:"))
if ort>=85:
    print("takdir")
elif ort>=70:
    print("teşekkür")
else:
    print("belge almadınız")