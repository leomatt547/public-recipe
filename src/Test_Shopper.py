import pytest
import Shopper

def test_init_shopperpage():
    Shopper.shopperpage.__init__(self=Shopper.shopperpage, username="aslan")
    assert (Shopper.shopperpage.username == "aslan")

def test_init_riwayat():
    Shopper.riwayat.__init__(self=Shopper.riwayat, usernameInput="aslan2")
    assert (Shopper.riwayat.username == "aslan2")