# didur-releases

Manifesto de versão do **Didur Driver**. O app lê o `latest.json` daqui para avisar o motorista
de versão nova (folha ao abrir, notificação e balão do painel rápido).

Gerado pelo `scripts/publish-latest.sh` do repositório do app a cada envio — não editar à mão.

- `version` / `build`: a versão mais nova distribuída.
- `minBuild`: abaixo dele a atualização é obrigatória.
- `android.url` / `ios.url`: o link da versão no Firebase App Distribution.
- `history`: o que mudou nas últimas 10 versões (Novo / Mudou / Corrigido), do CHANGELOG.md.

## areas/ — bairros e relevo por região (Didur Driver, fase 103)

`areas-index.json` lista as regiões (retângulo e arquivo); `areas-<regiao>.json` traz a grade de hexágonos de 300 m
em terra (bairro oficial do IBGE, município, altitude e desnível pelos tiles Terrarium) e o contorno simplificado de
cada bairro (malha de bairros do IBGE, Censo 2022). Gerado por `scripts/areas-regiao.sh` do repo do app.
