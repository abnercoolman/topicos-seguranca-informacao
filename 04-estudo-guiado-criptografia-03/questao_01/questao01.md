## Crie dois scripts separados python e pense em alguma forma de compartilhar a chave secreta entre os dois programas. Tente usar pelo menos uma das estratégias a seguir:

### a. abrir um prompt no terminal e digitar/colar a chave

### b. transferir usando sockets

### c. fazer com que os dois códigos leiam a chave a partir de um arquivo de texto

---

Optamos pela opção **(C)**:

- Criamos tres arquivos:
  - Arquivo Gerador da chave: gerador_chave.py;
  - Arquuivo p/ criptografar: criptografar.py;
  - Arquivo p/ descriptografar: descriptografar.py;

Para usar a solução, se certifique que o arquivo a ser encriptografado "arquivo.txt" esteja na pasta raiz (`\topicos-seguranca-informacao\04-estudo-guiado-criptografia-03\questao_01`), então execute:

- Primeiro, o gerador da chave:
  > `python gerador_chave.py`
- Segundo, o arquivo para criptografar:
  > `python criptografar.py`
- Terceiro, o arquivo para descriptografar:
  > `python descriptografar.py`