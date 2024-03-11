import hashlib


def calcular_hash(arquivo):
    md5 = hashlib.md5()
    with open(arquivo, "rb") as f:
        # Leitura do arquivo em blocos para eficiência
        for bloco in iter(lambda: f.read(4096), b""):
            md5.update(bloco)
    return md5.hexdigest()


def salvar_hash(arquivo, hash_calculado):
    with open(arquivo + "_hashmd5.txt", "w") as f:
        f.write(hash_calculado)


def verificar_integridade(arquivo, hash_salvo):
    hash_calculado = calcular_hash(arquivo)
    print(f"Hash calculado:\t {hash_calculado}")
    print(f"Hash arquivo:\t {hash_salvo}")
    return hash_calculado == hash_salvo


def main():
    arquivo_original = "exemplo.txt"
    hash_calculado = calcular_hash(arquivo_original)
    salvar_hash(arquivo_original, hash_calculado)
    print ("Hash 'md5' salvo em arquivo!")


if __name__ == '__main__':
    main()