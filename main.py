meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
        "LOL": "Una respuesta común a algo gracioso",
        "ROFL": "Una respuesta a una broma",
        "SHEESH": "ligera desaprobación",
        "CREEPY": "aterrador, siniestro",
        "AGGRO":  "ponerse agresivo/enojado"
            }

word = input("Por favor escribir una palabra moderna que no entiendes en mayúsculas")
if word in meme_dict.keys():
   print(meme_dict[word])
else:
    print("Yo no se lol")
