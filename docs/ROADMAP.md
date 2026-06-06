# Roadmap de Implementação

Este documento organiza o que já foi feito e o que ainda deve ser implementado para transformar o projeto em um aplicativo local portável inspirado nas funcionalidades vitais do Moises.ai.

## Estado Atual

O projeto já possui:

- Estrutura inicial de aplicação CLI.
- Pastas de entrada e saída: `input_audio/` e `output_stems/`.
- Separação de stems com Demucs.
- Download opcional com `yt-dlp`.
- Ambiente Python local isolado em `.python/` e `.venv311/`.
- Dependências fixadas para desenvolvimento.
- Correção para `torchcodec`, necessário para salvar stems com a versão atual do `torchaudio`.
- Diretórios portáveis para futuro executável.
- Saída local em `output_stems/` durante desenvolvimento.
- Opções de saída em WAV, MP3 320 kbps e FLAC.
- Modos de separação:
  - Voz + instrumental.
  - Voz + bateria + baixo + outros.
  - Voz + bateria + baixo + guitarra + piano/teclas + outros.
- Testes básicos para caminhos, UI e montagem dos comandos do Demucs.

## Cuidados Técnicos

Nem todos os stems desejados são suportados de forma confiável pelo Demucs atual.

Separações suportadas com boa referência:

- `htdemucs`: voz, bateria, baixo e outros.
- `htdemucs` com `--two-stems vocals`: voz e instrumental.
- `htdemucs_6s`: voz, bateria, baixo, guitarra, piano/teclas e outros.

Separações ainda não confiáveis nesta base:

- Sopro.
- Sintetizadores como stem próprio.
- Teclado detalhado além de piano/teclas do `htdemucs_6s`.
- Voz principal separada de backing vocal.
- Voz 1 e voz 2.

Esses itens devem ser tratados como pesquisa/modelos futuros, não como promessa do MVP atual.

## Próximas Implementações

### Fase 1: Robustez do CLI

- Exibir o caminho exato onde cada execução salvou os stems.
- Melhorar tratamento de erro para dependência ausente, modelo ausente, falha de codec e arquivo inválido.
- Adicionar validação de extensão de entrada.
- Adicionar opção para processar arquivos já presentes em `input_audio/` sem digitar o caminho manualmente.
- Adicionar logs em `logs/`.

### Fase 2: Organização de Jobs

- Criar uma pasta por música processada.
- Salvar metadados da execução:
  - arquivo original;
  - modelo usado;
  - formato de saída;
  - data/hora;
  - duração;
  - status.
- Evitar sobrescrita silenciosa de resultados.
- Criar uma listagem de processamentos anteriores.

### Fase 3: Portabilidade de Build

- Separar dependências de runtime, desenvolvimento e build.
- Criar instalação CPU-only do PyTorch para reduzir tamanho.
- Testar PyInstaller em Linux.
- Preparar pipeline de build por sistema:
  - Linux;
  - Windows;
  - macOS.
- Definir estratégia para `ffmpeg`:
  - detectar instalado;
  - empacotar binário;
  - ou oferecer instalação/download guiado.

### Fase 4: Interface Desktop

- Escolher toolkit desktop, preferencialmente PySide6 para MVP nativo.
- Implementar tela inicial com:
  - seleção de arquivo;
  - escolha de modo;
  - escolha de formato;
  - botão de processar;
  - progresso;
  - link para pasta de saída.
- Evitar prometer player avançado antes da separação estar robusta.

### Fase 5: Funcionalidades Tipo Moises Lite

- Player multistem.
- Mute/solo por stem.
- Volume por stem.
- Exportação de mix customizado.
- Loop de trecho.
- Controle de velocidade.
- Controle de pitch.
- Detecção de BPM.
- Detecção de tonalidade.

### Fase 6: Pesquisa de Modelos Avançados

- Avaliar modelos para vocal lead/backing.
- Avaliar separação de sopros.
- Avaliar separação de sintetizadores.
- Criar matriz de qualidade por modelo, stem e custo computacional.
- Documentar limites e resultados reais de cada modelo.
