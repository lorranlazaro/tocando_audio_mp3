# 🎵 Reprodutor de Áudio MP3

Projeto desenvolvido para reproduzir arquivos de áudio **MP3** usando a biblioteca pygame, com suporte a reprodução em loop e controle manual de interrupção.

------------------------------------------------------------------------

## 📘 O que é este projeto?

Este projeto é um **reprodutor de áudio simples** que permite:

- Reproduzir arquivos MP3
- Reproduzir em loop infinito
- Interromper a reprodução manualmente (Ctrl+C)
- Verificar se o arquivo existe antes de reproduzir
- Feedback visual com emojis durante a execução

É uma solução prática para tocar músicas ou áudios durante atividades ou estudos.

------------------------------------------------------------------------

## 🧠 Como funciona?

O programa utiliza o módulo **pygame.mixer** para:

1. Inicializar o sistema de áudio
2. Localizar automaticamente o arquivo na pasta `assets`
3. Verificar a existência do arquivo antes de reproduzir
4. Carregar o arquivo MP3 na memória
5. Reproduzir em loop infinito até interrupção manual

### Exemplo de uso:

```
Procurando arquivo em: C:\projeto\src\assets\labirinto_de_amor.mp3
✓ Arquivo encontrado! Carregando...
Reproduzindo áudio...
Pressione Ctrl+C para parar
```

Para parar a reprodução, pressione **Ctrl+C** no terminal.

------------------------------------------------------------------------

## 📊 Funcionalidades

| Funcionalidade                    | Descrição                                    |
|-----------------------------------|----------------------------------------------|
| Reprodução em loop                | Música toca infinitamente até interrupção    |
| Verificação de arquivo            | Checa se o arquivo existe antes de carregar  |
| Interrupção manual                | Para a música com Ctrl+C                     |
| Feedback visual                   | Exibe mensagens e emojis durante execução    |
| Suporte a múltiplos formatos      | MP3, OGG, WAV                                |

------------------------------------------------------------------------------------

## 📁 Estrutura do projeto

```
CursoEmVideo/
│── src/
│   ├── assets/
│   │   └── labirinto_de_amor.mp3
│   └── tocar_mp3.py
│── .gitignore
│── README.md
│── requirements.txt
```

------------------------------------------------------------------------

## ▶️ Como executar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/lorranlazaro/tocando_audio_mp3.git
   ```

2. Navegue até o diretório:
   ```bash
   cd tocando_audio_mp3
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o programa:
   ```bash
   python src/tocar_mp3.py
   ```

------------------------------------------------------------------------

## 🔧 Requisitos

- **Python 3.11 ou superior**
- **pygame** (biblioteca para reprodução de áudio)
- **emoji** (biblioteca para emojis no terminal)
- Arquivo de áudio MP3 na pasta `src/assets/`

------------------------------------------------------------------------

## 📝 Principais funções do código

### Inicialização do Mixer
```python
pygame.mixer.init()
```
Inicializa o módulo de áudio do pygame.

### Localização do Arquivo
```python
diretorio_script = os.path.dirname(__file__)
caminho_audio = os.path.join(diretorio_script, 'assets', 'labirinto_de_amor.mp3')
```
Localiza automaticamente o arquivo de áudio na pasta `assets` no mesmo diretório do script.

### Reprodução em Loop
```python
pygame.mixer.music.play(loops=-1)
```
O parâmetro `loops=-1` faz com que a música seja reproduzida em loop infinito.

### Interrupção Manual
```python
except KeyboardInterrupt:
    pygame.mixer.music.stop()
    print("\nReprodução interrompida!")
```
Captura Ctrl+C e para a reprodução de forma controlada.

------------------------------------------------------------------------

## 🧰 Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Biblioteca:** pygame (para reprodução de áudio)
- **Biblioteca:** emoji (para emojis no terminal)
- **Módulos padrão:** os, time
- **Ferramentas recomendadas:** VS Code, terminal do sistema operacional

------------------------------------------------------------------------

## ⚠️ Observações Importantes

- O arquivo de áudio deve estar na pasta `src/assets/` com o nome correto (`labirinto_de_amor.mp3` ou altere o código)
- Para parar a reprodução, use **Ctrl+C** (não feche o terminal abruptamente)
- O pygame suporta os formatos: **MP3**, **OGG**, **WAV**
- A biblioteca `emoji` é opcional, mas recomendada para melhor visualização

------------------------------------------------------------------------

## 🔍 Troubleshooting

**Problema:** "Arquivo não encontrado"  
**Solução:** Verifique se o arquivo MP3 está na pasta `src/assets/` com o nome correto

**Problema:** "No module named 'pygame'"  
**Solução:** Execute `pip install pygame` para instalar a biblioteca

**Problema:** "No module named 'emoji'"  
**Solução:** Execute `pip install emoji` para instalar a biblioteca

**Problema:** Áudio não toca  
**Solução:** Verifique se o volume do sistema está ligado e se o arquivo não está corrompido

------------------------------------------------------------------------

## ✍️ Autor

Desenvolvido por **[Lorran Lázaro]** 💻  
📧 E-mail: [lorranfelippe81@gmail.com]  
🌐 GitHub: [https://github.com/lorranlazaro]

------------------------------------------------------------------------

## 📜 Licença MIT

Este projeto está licenciado sob a **Licença MIT** — sinta-se livre para usar, modificar e distribuir.

```
MIT License

Copyright (c) 2025 Lorran Lázaro

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

✨ Desenvolvido para fins de estudo e evolução contínua na linguagem Python.
