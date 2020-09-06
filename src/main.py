from vigenere_standard import VigenereStandard

if __name__ == "__main__":
    vs = VigenereStandard()
    print(vs.encrypt("sonysonysonysony", "thisplaintext", 5))
    print(vs.decrypt("sony", "LVVQH ZNGFH RVL", 5))