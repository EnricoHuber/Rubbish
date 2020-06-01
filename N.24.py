""" ESERCIZI DEL SITO https://www.programmareinpython.it/esercizi-python/ """

""" Esercizio n.24 """


import os
import platform


def sys_info():
    print(f"Il sistema attualmente in uso è: {platform.system()}")
    print(f"OS rilevato: {os.name}")
    print("Aggiornato alla versione: " + platform.release())


sys_info()
