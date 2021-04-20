import pytest
import resep
import Shopper
import pembeli

#Test Shopper

def test_init_riwayat():
    Shopper.riwayat.__init__(Shopper.riwayat, usernameInput="aslan2")
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

#Test Pembeli

def test_count_pembeli():
    query = "nasi goreng"
    countnya,resepnya =  pembeli.exact(query)
    assert (countnya == 1)

def test_count_pembeli2():
    query = "ketupat"
    countnya,resepnya =  pembeli.exact(query)
    assert (countnya == 1)
