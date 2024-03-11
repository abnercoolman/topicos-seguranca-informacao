import hashlib
import timeit


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
    
    # Verificação de Integridade
    hash_salvo = open(arquivo_original + "_hashmd5.txt").read()
    if verificar_integridade(arquivo_original, hash_salvo):
        print("A integridade do arquivo foi preservada.")
    else:
        print("Atenção! O arquivo foi modificado")

# Cálculo do tempo de excução do código
tempo = timeit.timeit(main, number=1)
print(f"\nTempo de execução: {tempo:.5f} s.\n")