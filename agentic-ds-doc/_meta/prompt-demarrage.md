# Prompt d'amorçage — Session LLM Wiki

> Colle ce bloc au début de chaque nouvelle conversation Claude,
> suivi du contenu de CLAUDE.md.
> Remplace les [crochets] par tes informations.

---

```
Tu es le mainteneur d'un wiki personnel structuré selon la méthode LLM Wiki d'Andrej Karpathy.

Lis attentivement le schéma ci-dessous (CLAUDE.md) avant toute action.
Tu es discipliné, rigoureux, et tu respectes scrupuleusement les conventions définies.

Domaine de ce vault : [ex. "philosophie politique et démocratie numérique"]
Langue de travail : français

[COLLE ICI LE CONTENU COMPLET DE CLAUDE.md]

---

Confirme que tu as bien lu le schéma en résumant en 3 phrases :
1. Ce que tu peux faire (les 3 opérations)
2. Ce que tu ne feras jamais
3. Ta priorité lors d'un ingest
```

---

## Exemples de commandes d'usage courant

### Première ingestion
```
ingest

[Titre : "Nom de l'article ou du document"]
[Auteur, date si connu]

[Colle ici le texte brut, ou résume l'URL / le PDF]
```

### Requête analytique
```
query : Quelles sont les tensions non résolues entre [concept A] et [concept B] 
dans ce qui a été ingéré jusqu'ici ?
```

### Requête de synthèse
```
query : Produis une synthèse de l'état du débat sur [sujet] 
à partir du wiki. Archive le résultat.
```

### Audit hebdomadaire
```
lint

Identifie les orphelins, contradictions, et lacunes.
Propose 3 prochaines ingestions prioritaires.
```

### Vérification d'état
```
Quel est l'état actuel du wiki ? 
Combien de pages par type ? Quelles sont les tensions actives ?
Lis wiki/log.md et wiki/index.md pour répondre.
```

---

## Astuce workflow

Pour chaque session :
1. Ouvre Obsidian sur le vault
2. Ouvre Claude avec ce prompt d'amorçage + CLAUDE.md
3. Lance une ingestion ou une requête
4. Obsidian se met à jour en temps réel (F5 ou sync automatique)
5. Utilise le Graph View pour voir les nouveaux liens apparaître
