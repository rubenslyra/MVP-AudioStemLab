# Plano de Commits

Este projeto ainda não possui um repositório Git inicializado neste diretório. Quando o Git for iniciado, estes commits sugeridos organizam o histórico desde a criação das pastas até o estado atual.

## Commit 1: Estrutura inicial do laboratório de stems

Mensagem sugerida:

```text
chore: create initial audio stem lab structure
```

Inclui:

- `app.py`.
- `core/__init__.py`.
- `core/terminal_ui.py`.
- `core/file_manager.py`.
- `core/separator.py`.
- `input_audio/coloque_aqui_suas_musicas_autorizadas.txt`.
- `docs/README.md`.
- `README.md`.
- `LICENSE`.
- `.gitignore`.

Objetivo:

- Criar a base CLI do projeto.
- Criar as pastas planejadas de entrada e saída.
- Separar responsabilidades entre UI, arquivos e separador.

## Commit 2: Adicionar CI e testes básicos

Mensagem sugerida:

```text
test: add basic project tests and ci workflow
```

Inclui:

- `.github/workflows/ci.yml`.
- `tests/test_core.py`.
- `requirements-dev.txt`.

Objetivo:

- Garantir que os diretórios são criados corretamente.
- Garantir que métodos básicos da UI não quebram.
- Preparar execução automatizada de testes.

## Commit 3: Preparar caminhos portáveis

Mensagem sugerida:

```text
feat: add portable application paths
```

Inclui:

- `core/paths.py`.
- Ajustes em `core/file_manager.py`.
- Ajustes em `core/separator.py`.
- Ajustes em `app.py`.
- Atualização dos testes.

Objetivo:

- Definir caminhos adequados para desenvolvimento e futuro executável.
- Usar `input_audio/` e `output_stems/` no desenvolvimento.
- Reservar diretórios do usuário para builds empacotados.
- Criar cache, logs, modelos e temporários de forma controlada.

## Commit 4: Isolar ambiente Python e fixar dependências

Mensagem sugerida:

```text
chore: pin runtime and build dependencies
```

Inclui:

- `requirements.txt`.
- `requirements-build.txt`.
- `requirements-dev.txt`.
- Atualização de `README.md`.
- Atualização de `docs/README.md`.
- Atualização de `.gitignore`.

Objetivo:

- Fixar versões diretas usadas no MVP.
- Documentar `.venv311`.
- Ignorar `.python/`, `.venv311/`, `.cache/`, `output_stems/` e áudios locais de teste.

Observação:

- `.python/` e `.venv311/` não devem ser commitados.

## Commit 5: Corrigir salvamento com TorchCodec e cache temporário

Mensagem sugerida:

```text
fix: support torchaudio saving with torchcodec
```

Inclui:

- `torchcodec==0.14.0` em `requirements.txt`.
- `temp_dir` em `core/paths.py`.
- Variáveis `TMPDIR`, `TEMP`, `TMP` e `TORCHINDUCTOR_CACHE_DIR` no subprocess do Demucs.
- Testes atualizados.

Objetivo:

- Corrigir falha do Demucs ao salvar stems com versões recentes de `torchaudio`.
- Evitar dependência frágil de `/tmp`.

## Commit 6: Adicionar formatos de saída e modo de seis stems

Mensagem sugerida:

```text
feat: add output format selection and extended stem mode
```

Inclui:

- `choose_output_format` em `core/terminal_ui.py`.
- Modo `extended6` em `core/separator.py`.
- Comandos Demucs com `--mp3`, `--mp3-bitrate 320` e `--flac`.
- Testes de montagem de comandos.
- Documentação dos limites técnicos.

Objetivo:

- Permitir saída em WAV, MP3 e FLAC.
- Usar `htdemucs_6s` para guitarra e piano/teclas.
- Evitar prometer sopros, sintetizadores e backing vocal como stems confiáveis.

## Commit 7: Documentar roadmap e próximos passos

Mensagem sugerida:

```text
docs: add roadmap and commit plan
```

Inclui:

- `docs/ROADMAP.md`.
- `docs/COMMIT_PLAN.md`.

Objetivo:

- Registrar o estado atual.
- Planejar próximas fases.
- Dar previsibilidade ao histórico Git.

## Arquivos Que Não Devem Entrar Nos Commits

- `.python/`.
- `.venv/`.
- `.venv311/`.
- `.cache/`.
- `.pytest_cache/`.
- `output_stems/`.
- Arquivos de áudio em `input_audio/`, exceto o placeholder.
- Arquivos gerados por Demucs.
