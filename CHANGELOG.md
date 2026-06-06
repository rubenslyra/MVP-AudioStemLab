# Changelog

Todas as mudanças relevantes do projeto serão registradas aqui.

## 0.3.6 - Artefatos de release e snapshots no README

### Adicionado

- Snapshots de uso incorporados diretamente ao README principal.
- Notas de release para publicacao dos artefatos portaveis `v0.3.6`.

### Alterado

- Versao avancada para `0.3.6`.
- README e documentacao de empacotamento atualizados para os nomes dos pacotes `v0.3.6`.

## 0.3.5 - Pacotes CPU e CUDA separados

### Adicionado

- `requirements-cpu.txt` para builds portaveis CPU-only.
- `requirements-cuda.txt` para builds portaveis CUDA.
- Matriz de release com variantes `cpu` e `cuda`.
- Nomes de artefatos com aceleracao explicita: `linux-cpu`, `windows-cuda`, etc.

### Alterado

- Versao avancada para `0.3.5`.
- Pacote CPU passa a ser o recomendado para testadores comuns.
- Pacote CUDA fica separado e documentado como opcional para computadores Linux/Windows com GPU NVIDIA compativel.
- macOS fica limitado ao pacote CPU.

## 0.3.4 - Experiencia de terminal para testes

### Adicionado

- Pipeline de release para gerar pacotes portaveis Linux, Windows e macOS em tags `v*`.
- Script de empacotamento `scripts/package_release.py`.
- UI de terminal com `rich`, paineis, tabelas e prompts mais claros.
- Limpeza de tela mantendo cabecalho, identidade do sistema e versao.
- Seletor nativo de arquivo de origem via `tkinter`.
- Seletor nativo de pasta de destino via `tkinter`.
- Launchers auxiliares para Linux, Windows e macOS.
- Fonte Fira Code v6.2 no pacote de assets.
- Licenca do Fira Code em `assets/licenses/FIRA_CODE_LICENSE`.
- Mensagens de progresso mais familiares, com percentual inteiro e tempo decorrido.

### Alterado

- Versao avancada para `0.3.4`.
- README reposicionado para usuarios finais baixarem pacotes prontos, sem instalar Python.
- Spec do PyInstaller ajustado para gerar pacote portavel em diretorio e incluir assets/documentacao.
- O terminal agora informa claramente que a versao de teste e desktop, sem mobile.
- O subprocesso do Demucs passa a ter saida capturada para reduzir quebras visuais no terminal.

### Observacoes

- A ativacao de ligaduras depende do terminal/instalador de cada sistema operacional.
- O app CLI prepara a fonte no pacote, mas nao consegue forcar a fonte de um terminal ja aberto pelo usuario.

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
