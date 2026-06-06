# Changelog

Todas as mudanças relevantes do projeto serão registradas aqui.

## 0.1.0 - MVP CLI

Primeira versão instalável/de desenvolvimento do RLLABS Audio Stem Lab.

### Adicionado

- Aplicação CLI para separação local de stems.
- Separação com Demucs:
  - voz + instrumental;
  - voz + bateria + baixo + outros;
  - voz + bateria + baixo + guitarra + piano/teclas + outros.
- Formatos de saída:
  - WAV;
  - MP3 320 kbps;
  - FLAC.
- Download opcional de áudio autorizado com `yt-dlp`.
- Estrutura portável de caminhos para desenvolvimento e futuro executável.
- Ambiente Python isolado documentado com Python 3.11.
- Dependências fixadas em `requirements.txt`.
- Dependência `torchcodec` para compatibilidade com versões recentes de `torchaudio`.
- Scaffold de build com PyInstaller.
- Testes básicos e workflow de CI.

### Observações

- Em desenvolvimento, entradas e saídas usam `input_audio/` e `output_stems/`.
- Em build empacotado, o app está preparado para usar diretórios de usuário por sistema operacional.
- Sopros, sintetizadores, voz principal e backing vocal ainda não são stems confiáveis nesta versão.
