import pytest

from cipher import Cipher, combine_character, separate_character


def test_encode():
    cipher = Cipher("TRAIN")
    encoded = cipher.encode("ENCODEDINPYTHON")
    assert encoded == "XECWQXUIVCRKHWA"


def test_encode_character():
    cipher = Cipher("TRAIN")
    encoded = cipher.encode("E")
    assert encoded == "X"


def test_encode_spaces():
    cipher = Cipher("TRAIN")
    encoded = cipher.encode("ENCODED IN PYTHON")
    assert encoded == "XECWQXUIVCRKHWA"


def test_encode_key_lowercase():
    cipher = Cipher("train")
    encoded = cipher.encode("ENCODED IN PYTHON")
    assert encoded == "XECWQXUIVCRKHWA"


def test_encode_text_all_lowercase():
    cipher = Cipher("TRAIN")
    encoded = cipher.encode("encoded in python")
    assert encoded == "XECWQXUIVCRKHWA"


def test_encode_text_mix_upper_lowercase():
    cipher = Cipher("TRAIN")
    encoded = cipher.encode("eNcoded IN pythoN")
    assert encoded == "XECWQXUIVCRKHWA"


def test_encode_text_spaces_and_lowercase():
    cipher = Cipher("train ")
    encoded = cipher.encode("encoded in python")
    assert encoded == "XECWQXUIVCRKHWA"


def test_combine_character():
    assert combine_character("E", "T") == "X"
    assert combine_character("N", "R") == "E"
    assert combine_character("O", "I") == "W"


def test_extend_keyword():
    cipher = Cipher("TRAIN")
    extend_keyword = cipher.extend_keyword(16)
    assert extend_keyword == "TRAINTRAINTRAINTRAIN"


def test_extend_keyword_with_space():
    cipher = Cipher("TRAIN  ")
    extend_keyword = cipher.extend_keyword(20)
    assert extend_keyword == "TRAINTRAINTRAINTRAINTRAIN"


def test_extend_keyword_lower():
    cipher = Cipher("trAin  ")
    extend_keyword = cipher.extend_keyword(20)
    assert extend_keyword == "TRAINTRAINTRAINTRAINTRAIN"


def test_plain_text_invalid():
    cipher = Cipher("TRAIN")
    with pytest.raises(ValueError) as ex:
        cipher.encode(None)
    assert ex.value.args[0] == "Data invalid!"


def test_key_invalid():
    cipher = Cipher(None)
    with pytest.raises(ValueError) as ex:
        cipher.encode("ENCODED")
    assert ex.value.args[0] == "Key invalid!"


def test_key_and_plain_text_invalid():
    cipher = Cipher(None)
    with pytest.raises(ValueError) as ex:
        cipher.encode("  ")
    assert ex.value.args[0] == "Key invalid!"


def test_separate_character():
    assert separate_character("X", "T") == "E"
    assert separate_character("E", "R") == "N"


def test_decode():
    cipher = Cipher("TRAIN")
    decoded = cipher.decode("XECWQXUIVCRKHWA")
    assert decoded == "ENCODEDINPYTHON"

# pytest test_cipher.py
# pytest -coverage-report=report
