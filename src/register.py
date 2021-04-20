import pandas as pd


def registerPembeli(name, phone, email, address, username, password) :
    data = {'nama_pembeli' : name,
            'no_telp_pembeli' : phone,
            'email_pembeli' : email,
            'alamat' : address,
            'username' : username,
            'password' : password}

    df = pd.read_csv("../data/pembeli.csv")
    dfUser = df[df["username"] == username ]
    dfUser = dfUser[dfUser["password"] == password]
    print(dfUser)
    if len(dfUser) == 0 :
        df = df.append(data, ignore_index = True)
        df.to_csv("../data/pembeli.csv", index = False)
        return True
    else :
        return False

def registerShopper(name, phone, email, address, username, password) :
    data = {'nama_shopper' : name,
            'no_telp_shopper' : phone,
            'email_shopper' : email,
            'alamat_shopper' : address,
            'username' : username,
            'password' : password}

    df = pd.read_csv("../data/shopper.csv")
    dfUser = df[df["username"] == username ]
    dfUser = dfUser[dfUser["password"] == password]
    if len(dfUser) == 0 :
        df = df.append(data, ignore_index = True)
        df.to_csv("../data/shopper.csv", index = False)
        return True
    else :
        return False