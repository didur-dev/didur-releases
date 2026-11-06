#!/usr/bin/env python3
"""Baixa do OpenStreetMap todas as cabines de pedágio do Brasil (barrier=toll_booth) e grava
pedagios-br.json, a lista que o Didur Driver usa para achar as praças da rota sem consultar o
Overpass na hora (#490). Roda toda semana pelo workflow pedagios.yml; à mão: python3 scripts/pedagios-brasil.py
"""
import json, sys, time, urllib.parse, urllib.request
from datetime import datetime, timezone

HOSTS = [
    "https://maps.mail.ru/osm/tools/overpass/api/interpreter",
    "https://overpass-api.de/api/interpreter",
    "https://overpass.private.coffee/api/interpreter",
]
QUERY = '[out:json][timeout:170];area["ISO3166-1"="BR"][admin_level=2]->.br;node["barrier"="toll_booth"](area.br);out;'
TAGS = ("name", "note", "operator", "charge", "comment", "description", "fee")
MINIMO = 500  # menos que isso é resposta cortada, não o Brasil


def baixar():
    corpo = urllib.parse.urlencode({"data": QUERY}).encode()
    for host in HOSTS:
        for tentativa in range(2):
            try:
                req = urllib.request.Request(host, data=corpo, headers={"User-Agent": "didur-driver/2.0 (lista de pedagios)"})
                with urllib.request.urlopen(req, timeout=200) as r:
                    elementos = json.load(r)["elements"]
                if len(elementos) >= MINIMO:
                    return elementos
                print(f"{host}: só {len(elementos)} cabines", file=sys.stderr)
            except Exception as e:  # noqa: BLE001 — qualquer falha passa ao próximo host
                print(f"{host}: {e}", file=sys.stderr)
            time.sleep(10)
    sys.exit("nenhum servidor do Overpass respondeu")


cabines = [
    {"id": e["id"], "lat": round(e["lat"], 6), "lon": round(e["lon"], 6),
     "tags": {k: v for k, v in e.get("tags", {}).items() if k in TAGS}}
    for e in baixar()
]
cabines.sort(key=lambda c: c["id"])
saida = {"versao": datetime.now(timezone.utc).strftime("%Y-%m-%d"), "cabines": cabines}
with open("pedagios-br.json", "w", encoding="utf-8") as f:
    json.dump(saida, f, ensure_ascii=False, separators=(",", ":"))
print(f"{len(cabines)} cabines, {sum(1 for c in cabines if 'charge' in c['tags'])} com valor")
