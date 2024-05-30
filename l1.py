meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "bir şakaya karşılık cevap",
            "SHEESH": "onaylamamak",
            "CREEPY": "korkunç",
            "AGGRO": "agresifleşmek/sinirlenmek"
            }
print("selamlar,burada istediğiniz yeni nesil sözcükleri yazın ve anlamlarını öğrenin")
for i in range(5):
    word = input("Anlamadığınız bir kelime yazın, (hepsini büyük harflerle yazın!): ").upper()
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("o kelimeyi bilmeyiz biz!")
