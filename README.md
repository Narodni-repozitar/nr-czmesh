# NR CZMESH

Jedná se o jednoduchý program/skript, který převadí publikovaný heslář Medical Subject Headings z formátu .mrc 
(Marc21) do CSV pro použití v NR-taxonomies.

Aktuální heslář se dá stáhnout na stránkách Národní lékařské knihovny ([MeSH-CZ](https://nlk.cz/pro-knihovny/mesh/)).

## Instalace
Balíček se instaluje ze zdroje. Nutné stáhnout balíček a nainstalovat ho příkazem ze složky balíčku.
```bash
pip install .
```


## Použití
Jedná se o program pro příkazovou řádku, který po nainstalování lze ovládat těmito příkazy:

```bash
Usage: czmesh [OPTIONS]

  Programme for translating information from mrc file to csv.

Options:
  -i, --input TEXT   It is path of .mrc file
  -o, --output TEXT  File where
  --help             Show this message and exit.

```
