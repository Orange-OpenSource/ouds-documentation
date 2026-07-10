# Design System & IA : synthèse exécutive

## Ce qu'est un design system

Un design system est un ensemble de décisions de conception formalisées et partagées : composants UI, tokens de style, règles d'usage et documentation. Il existe à l'intersection du design, du code et de la gouvernance. C'est la réponse à une question simple : comment éviter que chaque équipe réinvente les mêmes solutions ?

Les bénéfices sont directs. Les équipes construisent plus vite en assemblant des composants existants. L'expérience utilisateur est cohérente, quelle que soit l'équipe qui a produit l'écran. Les corrections de qualité (accessibilité, marque) se font en un seul endroit et se propagent partout. Sans DS, le coût de maintenance n'est pas additionné : il est multiplié.

Depuis juin 2024, en accord avec le plan Lead the Future, le Orange Unified Design System vise à rationaliser et mutualiser les initiatives passées de design systems pour tout le groupe. Lancé officiellement début 2026, il a été certifié L4 (mandatory) par Federation IT en juin 2026.

## Pourquoi c'est une infrastructure, pas un outil

Un outil, on peut décider de ne pas s'en servir. Une infrastructure, on en hérite. On n'évalue pas un réseau électrique en demandant si les gens "l'utilisent". On regarde si la tension est stable, si l'alimentation est fiable. Et surtout : un réseau de mauvaise qualité endommage ce qui est branché dessus.

Le DS est le point de convergence où le design, le code, la marque et l'accessibilité se rejoignent. Sa dégradation ne ralentit pas un dev : elle désynchronise des systèmes entiers. Négliger un outil, ça se voit. Négliger une infrastructure produit des effets diffus, dans des projets qui n'identifient jamais la cause.

## Ce que l'IA change

Les développeurs utilisent déjà des assistants de code (Copilot, Cursor, Claude) au quotidien. Ces outils génèrent du code en continu, pour chaque tâche. Ils ne sont pas neutres : ils amplifient ce qui existe. Si le DS est bien structuré et exposé, l'IA génère du code conforme. S'il est opaque ou mal documenté, l'IA l'ignore et produit du code générique qui contourne l'infrastructure.

Sans investissement sur le DS, les outils IA des développeurs produiront du code qui l'ignore, accumulant de la dette à une vitesse proportionnelle à l'adoption de ces outils. Un DS structuré et exposé aux modèles devient au contraire un avantage cumulatif : chaque ligne de code générée respecte le système, sans effort supplémentaire de la part du développeur.

## Notre plan en six étapes

**Tokens.** OUDS repose déjà sur une architecture sémantique solide. L'objectif est de l'enrichir : descriptions explicites, do/don't, clarification des relations entre tokens primitifs et décisionnels. Un token sans description est une décision muette pour un modèle.

**Documentation LLM.** Documenter chaque composant avec ses règles d'usage, ses anti-patterns et des exemples annotés qui expliquent le "pourquoi". Ces exemples servent à la fois de référence humaine et de base d'apprentissage pour les modèles.

**Agents et skills.** Produire des fichiers `agents.md` (contexte système à injecter dans les outils des devs) et des skills opérationnels : génération de code conforme au DS, audits de conformité sur le code existant.

**Serveur MCP.** Exposer le DS comme un serveur MCP pour que les outils puissent l'interroger en temps réel, plutôt que de s'appuyer sur une documentation statique potentiellement obsolète.

**Évaluation.** Définir des cas de test mesurables : le code généré utilise-t-il les bons composants, les bons tokens, les bonnes variantes ? Sans mesure, impossible d'itérer.

**Gouvernance.** Définir qui maintient la cohérence entre le DS et ses artefacts IA, et à quel moment une évolution du DS déclenche une mise à jour de la documentation LLM. Ces réponses doivent être intégrées au processus de contribution dès le lancement, pas après la première désynchronisation.

---

Un design system n'est pas un projet qu'on livre et qu'on referme. C'est une infrastructure vivante. Sa valeur dépend de l'exigence avec laquelle on la maintient et de la façon dont on l'expose aux outils que les équipes utilisent réellement. Le plan présenté ici n'est pas un pari sur l'avenir de l'IA. C'est un investissement sur la qualité de ce qui est produit aujourd'hui, avec les outils qui existent déjà dans les mains des développeurs.
