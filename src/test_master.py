import pytest
import resep

def test_count_resep():
    query = "nasi goreng"
    countnya,resepnya =  resep.exact(query)
    assert (countnya == 1)

def test_count_resep2():
    query = "ketupat"
    countnya,resepnya =  resep.exact(query)
    assert (countnya == 1)