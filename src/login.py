import pandas as pd

def loginPembeli(username, password) :
    df = pd.read_csv("../data/pembeli.csv")
    dfUser = df[df["username"] == username]
    dfUser = dfUser[dfUser["password"] == password]
    if len(dfUser) == 0 :
        return False
    else :
        return True

def loginShopper(username, password) :
    df = pd.read_csv("../data/shopper.csv")
    dfUser = df[df["username"] == username]
    dfUser = dfUser[dfUser["password"] == password]
    if len(dfUser) == 0 :
        return False
    else :
        return True