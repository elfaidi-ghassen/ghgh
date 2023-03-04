import pandas as pd

from PyQt5.QtWidgets import *
from PyQt5.uic import *
from pickle import dump,load


def ajouter():
    ide = w.id.text()
    tel = w.tel.text()
    if w.btrf.isChecked():
        genre = "f"
    elif w.btrm.isChecked():
        genre = "m"
    else: 
        QMessageBox.warning(w, "erreur", "vous dever choisir un genre")

    ville = w.cbville.currentText()
    etat = w.cb.isChecked()
    if id == "" or tel == "":
        QMessageBox.warning(w, "erreur", "remplir les champs")
    else:
        f = open("client.dat", "ab")
        e = {
            "ide" : str(),
            "ntel": str(),
            "ville": str(),
            "genre": str(),
            "etat": str()
        }

        e["ide"] = ide
        e["ntel"] = tel
        e["ville"] = ville
        e["genre"] = genre
        e["etat"] = etat
        dump(e, f)

        obj = pd.read_pickle('client.dat')
        print(obj)

        f.close()
        QMessageBox.information(w, "valide!", "remlir est complete")
        w.id.setText("")
        w.id.setFocus()
        w.tel.clear()
        w.btrf.setAutoExclusive(False)
        w.btrf.setChecked(False)
        w.btrm.setAutoExclusive(False)
        w.btrm.setChecked(False)
        w.cb.setChecked(False)

        w.cbville.setCurrentIndex(0)

def afficher():
    f = open("chance.txt", "r")
    ch = f.readline()
    while ch != "":
        w.lwchance.addItem(ch)
        ch = f.readline()
    f.close()






#------Exploitation de l'interface graphique------
app = QApplication([])
w = loadUi("Interface_Prototype.ui")
w.show()
w.btn_ajout.clicked.connect(ajouter)
w.btn_chance.clicked.connect(afficher)
# w.NomBouton3.clicked.connect(...........)
# w.NomBouton4.clicked.connect(........)
app.exec_()