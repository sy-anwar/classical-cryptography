from vigenere_standard import VigenereStandard
from vigenere_extended import VigenereExtended

if __name__ == "__main__":
    # vs = VigenereStandard()
    # print(vs.encrypt("sony", "thisplaintext", 0))
    # print(vs.decrypt("sony", "LVVQH ZNGFH RVL", 0))
    ve = VigenereExtended()
    print(ve.encrypt("sony", "this plain text", 0))
    print(ve.decrypt("sony", "ç××ì\x93ßÚÚÜÝ\x8eíØçâ", 0))
    