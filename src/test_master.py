import pytest
import resep
import Shopper

#Test Shopper

def test_init_shopperpage():
    Shopper.shopperpage.__init__(self=Shopper.shopperpage, username="aslan")
    assert (Shopper.shopperpage.username == "aslan")

def test_init_riwayat():
    Shopper.riwayat.__init__(self=Shopper.riwayat, usernameInput="aslan2")
    assert (Shopper.riwayat.username == "aslan2")

#Test Resep

def test_count_resep():
    query = "nasi goreng"
    countnya,resepnya =  resep.exact(query)
    assert (countnya == 1)

def test_count_resep2():
    query = "ketupat"
    countnya,resepnya =  resep.exact(query)
    assert (countnya == 1)
