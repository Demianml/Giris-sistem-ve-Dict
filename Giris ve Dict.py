menimDict = {
    "Ad" : "Nicat",
    "Yas" : 15
}

menimDict.update({"il": 2009})

print(menimDict)


def salam():
    print("Salam", menimDict["Ad"])


salam()

def yas():
    print("Yasiniz: ", menimDict ["Yas"])

yas()


ad = input("Adiniz nedir: ")

if ad == menimDict ["Ad"]:
    print("Salamlar!", ad )

else:
    print("Xeyr!")