# POP Scraper

> [!WARNING]
> Les données de POP sont en train d’être publiées sur [data.culture.gouv.fr](https://data.culture.gouv.fr/), ce qui rendra ce scraper obsolète.

Aspirateur de données de la [Plateforme Ouverte du Patrimoine](https://www.pop.culture.gouv.fr).

Développé dans le cadre de [Collectif Objets](https://collectif-objets.beta.gouv.fr/)

Codé en Python 3 🐍 avec la librairie [Scrapy](https://docs.scrapy.org/)

## Production

Déployé et disponible sur [zyte.com](https://app.zyte.com/)

## Développement local

- `poetry install`
- `poetry run scrapy crawl pop_api`

## Options

### `base_pop`

Base POP à scrapper. Seules `palissy` et `merimee` sont supportées. Défault `palissy`

`poetry run scrapy crawl pop_api -a base_pop=merimee`

### `max_items`

Limite le nombre d'objets à parcourir

`poetry run scrapy crawl pop_api -a max_items=200`


## Rajouter une base POP (Joconde, MNR etc)

- récupérer un item en JSON depuis le navigateur sur la page de recherche
- récupérer le CSV de description des champs de la base dans la codebase de POP
- rajouter la classe d'Item dans items.py à partir de ces deux fichiers comparés - la source de vérité est ce qu'on peut récupérer depuis l'API de recherche
- faire un premier import puis pour chaque array, vérifier qu'il y a vraiment des valeurs multiples avec `select count(*) from palissy where DENO is not null and json_array_length(DENO) > 1;` par exemple. sinon, changer le serializer

## Useful commands

use `watch` and `xsv` to follow the number of lines in the CSV outputs during the crawl as it grows
(wc -l does not work because csv rows can contain new lines)

`watch -n 10 "find tmp2 -name '*.csv' -exec sh -c 'echo -n "{}: "; xsv count {}' \;"`
