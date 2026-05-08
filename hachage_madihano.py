#Hachage Madihano - Une fonction de hachage personnalisée basée sur le nom "Madihano".
#Tp_de Cryptographie - 2026 Presenté par : Madihano Atiingale Tresor

Nom =input("Entrez votre nom : ")

def hash_madihano(texte: str) -> str:
    """
    Fonction de hachage personnalisée (non cryptographique) basee sur le nom "Madihano".
    Retourne une empreinte hexadecimale sur 64 bits.
    """
    # Graine derivee de "Madihano" (constante de depart)
    h = 0x4D61646968616E6F  # "Madihano" en ASCII hex

    for i, caractere in enumerate(texte):
        code = ord(caractere)
        h ^= (code + i * 131)
        h = (h * 0x100000001B3) & 0xFFFFFFFFFFFFFFFF  # multiplication 64 bits
        h = ((h << 7) | (h >> 57)) & 0xFFFFFFFFFFFFFFFF  # rotation a gauche

    return f"{h:016x}"


if __name__ == "__main__":
    message = Nom
    empreinte = hash_madihano(message)
    print(f"Texte    : {message}")
    print(f"Hachage  : {empreinte}")
