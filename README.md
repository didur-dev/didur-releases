# didur-releases

Manifesto de versão do **Didur Driver**. O app lê o `latest.json` daqui para avisar o motorista
de versão nova (folha ao abrir, notificação e balão do painel rápido).

Gerado pelo `scripts/publish-latest.sh` do repositório do app a cada envio — não editar à mão.

- `version` / `build`: a versão mais nova distribuída.
- `minBuild`: abaixo dele a atualização é obrigatória.
- `android.url` / `ios.url`: o link da versão no Firebase App Distribution.
- `history`: o que mudou nas últimas 10 versões (Novo / Mudou / Corrigido), do CHANGELOG.md.
