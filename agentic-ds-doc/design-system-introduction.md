# Design System & IA : de l'infrastructure au code généré

## Ce qu'est un design system

Un design system est un ensemble de décisions de conception formalisées et partagées : composants UI, tokens de style (couleurs, typographie, espacement), règles d'usage, et la documentation qui les accompagne. C'est la réponse organisationnelle à une question simple : comment éviter que chaque équipe réinvente indépendamment les mêmes boutons, formulaires et patterns ?

Il existe à l'intersection de trois disciplines : le design (ce à quoi les choses ressemblent), le code (comment elles sont implémentées), et la gouvernance (qui décide quoi et comment on fait évoluer l'ensemble). La plupart des "design systems" qui échouent négligent le troisième pilier.

Depuis juin 2024, en accord avec le plan Lead the Future et maintenant son successeur, Orange Unified Design System vise à rationaliser et mutualiser les multiples initiatives de design systems pour tout le groupe. Lancé officiellement début 2026, il a été certifié L4 (mandatory) par Federation IT en juin 2026.

## Pourquoi c'est bénéfique

**Pour la vitesse de production.** Les équipes ne partent pas de zéro. Un dev qui construit un formulaire d'inscription assemble des composants existants plutôt que d'en créer. Le gain n'est pas spectaculaire sur une tâche isolée, mais il est massif à l'échelle d'une organisation et sur la durée.

**Pour la cohérence de l'expérience.** Sans source de vérité partagée, chaque équipe produit des variations : des boutons légèrement différents, des espacements incohérents, des comportements contradictoires. L'utilisateur final le ressent comme une expérience fragmentée, même sans pouvoir l'articuler. Un DS garantit que le produit "parle d'une seule voix" quel que soit le nombre d'équipes qui y contribuent.

**Pour la qualité structurelle.** Les composants d'un DS sont conçus et testés une fois pour tous les contextes : accessibilité, responsive, états d'erreur, dark mode. Sans DS, ce travail est refait dans chaque équipe, souvent partiellement et avec des résultats inégaux. Un bug d'accessibilité corrigé dans un composant partagé disparaît partout simultanément. Le même bug sur un composant dupliqué dix fois doit être retrouvé, corrigé et testé dix fois.

**Pour la maintenance.** Modifier une couleur de marque ou faire évoluer une règle typographique se fait en un endroit et se propage partout. Sans DS, la même correction doit être appliquée manuellement dans chaque produit, souvent de façon incomplète. Sans DS, le coût de maintenance n'est pas additionné : il est multiplié.

**Pour la collaboration.** Designers et développeurs parlent le même vocabulaire. "Utilise le composant Card avec la variante elevated" est une instruction non ambiguë quand le DS existe. Sans lui, chaque transfert design vers dev est une négociation.

---

En résumé : un design system réduit la surface de décision locale pour que les équipes nvestissent leur énergie et leur temps sur ce qui est vraiment nouveau, plutôt que sur ce qui a déjà été résolu ailleurs dans l'organisation.

## Le design system comme infrastructure

La distinction entre outil et infrastructure n'est pas sémantique. Elle détermine comment on investit, comment on gouverne, et ce qu'on accepte de laisser se dégrader.

Un outil, on peut décider de ne pas s'en servir. Une infrastructure, on en hérite qu'on le veuille ou non. On n'évalue pas un réseau électrique en demandant si les gens "l'utilisent". On regarde si la tension est stable, si la charge est absorbée, si l'alimentation est fiable. Et surtout : un réseau de mauvaise qualité ne se contente pas d'être inutile — il endommage ce qui est branché dessus.

**C'est partagé et invisible quand ça marche.** Personne ne pense à l'infrastructure électrique quand il allume la lumière. De même, un bon DS disparaît dans le flux de travail. Les devs ne "l'utilisent" pas consciemment, ils construisent dessus. Il ne devient visible que quand ça casse ou qu'on s'en écarte.

**C'est un point de convergence entre plusieurs systèmes.** Le DS est le lieu où le design, le code, la marque, l'accessibilité et la documentation se rejoignent. Supprimer ou dégrader ce point de convergence ne détruit pas un outil : cela désynchronise des systèmes entiers qui dépendaient d'une source commune de vérité.

**Il produit des effets réseau.** Plus il est adopté, plus sa valeur augmente. Chaque équipe qui le contourne réduit sa valeur pour les autres, crée des fourches, fragmente l'expérience utilisateur. C'est exactement le comportement d'une infrastructure, pas d'un outil.

**Sa dette est systémique.** Négliger un outil, cela se voit. Négliger une infrastructure produit des effets diffus, dans des projets qui n'identifient jamais la cause. La dette d'un DS se manifeste en incohérences visuelles, en composants dupliqués, en bugs d'accessibilité récurrents. Jamais attribués au DS lui-même, mais toujours causés par son absence.

---

En résumé : traiter un DS comme un outil, c'est accepter qu'il soit optionnel. Le traiter comme une infrastructure, c'est reconnaître que sa qualité conditionne celle de tout ce qui est construit dessus. À l'heure de l'IA agentique, il est urgent de canaliser l'afflux des nouveaux utilisateurs de OUDS que sont les LLM.

## Comment l'IA impacte les design systems

L'essor des assistants de code (Copilot, Cursor, Claude) introduit une nouvelle variable dans l'équation du design system. Ces outils génèrent du code en continu, pour chaque développeur, à chaque tâche. La question n'est plus "est-ce que nos devs utilisent le DS ?" mais "est-ce que l'IA qu'ils utilisent connaît le DS ?"

**L'IA amplifie ce qui existe déjà.** Si le DS est bien structuré, documenté, et exposé aux outils, l'IA génère du code conforme : bons composants, bons tokens, bonnes variantes. Si le DS est opaque ou mal documenté, l'IA l'ignore et produit du code générique qui contourne l'infrastructure. Elle n'est pas neutre : elle amplifie soit la cohérence, soit la dette.

**Un DS "LLM-readable" change la nature du gain.** Jusqu'ici, un DS accélérait la production en évitant aux devs de repartir de zéro. Avec l'IA, il peut aller plus loin : un assistant bien contextualisé peut suggérer le bon composant, alerter sur un usage incorrect, ou générer un écran complet en respectant les contraintes du système. Le DS devient le référentiel que l'IA consulte à chaque ligne de code produite.

**Rendre un DS lisible par l'IA n'est pas un projet à part.** C'est d'abord une question de structure : des design tokens nommés sémantiquement pour éviter les ambiguités, des composants documentés avec leurs règles d'usage, des exemples de code associés. Ce travail améliore aussi l'expérience des développeurs humains. C'est un investissement à double bénéfice, pas un surcoût.

**Le risque de ne rien faire est asymétrique.** Sans investissement sur le DS, les outils IA des développeurs produiront du code qui l'ignore, accumulant de la dette à une vitesse proportionnelle à l'adoption de ces outils. Un DS structuré et exposé aux modèles devient au contraire un avantage cumulatif : chaque ligne de code générée respecte le système, sans effort supplémentaire de la part du développeur.

---

En résumé : l'IA ne remplace pas le design system. Elle en révèle la qualité. Un DS bien construit devient un levier d'amplification. Un DS négligé devient un angle mort que l'IA exploite involontairement.

## Notre plan pour rendre le DS "LLM readable and usable"

Rendre un design system exploitable par l'IA ne se réduit pas à écrire de la documentation supplémentaire. C'est un effort structuré en plusieurs couches, des fondations (les design tokens) jusqu'à l'exposition outillée (les agents et les MCP), avec une gouvernance qui garantit que l'ensemble reste synchronisé dans le temps.

### 1. Consolider l'architecture de tokens sémantiques (en cours)

Tout commence ici. Les design tokens sont le vocabulaire que l'IA devra maîtriser. OUDS repose déjà sur une architecture sémantique solide. L'objectif de cette étape est de l'enrichir pour la rendre pleinement exploitable par les modèles : ajouter des descriptions explicites à chaque token, documenter les usages corrects et les erreurs fréquentes (do/don't), et clarifier les relations entre les différentes couches de variables qui, sans description, restent des décisions muettes : compréhensibles pour qui connaît le système, opaques pour un modèle qui doit l'inférer.

### 2. Produire une documentation optimisée pour les LLMs (en cours)

La documentation standard d'un DS explique ce que font les composants. Une documentation orientée LLM va plus loin : elle explique *quand* les utiliser, *pourquoi* un composant plutôt qu'un autre, et *ce qu'il ne faut pas faire* de manière structurée et pragmatique. Ce dernier point est crucial pour les modèles pour éviter les interprétations. Ainsi, les anti-patterns, les usages incorrects fréquents, et les pièges de composition permettent à un LLM de détecter des violations, pas seulement de suggérer du code correct.

Chaque composant doit être documenté avec ses règles d'usage, ses variantes et leurs contextes d'application, ses contraintes d'accessibilité, et des exemples de code annotés. Pas des snippets bruts, mais des exemples qui expliquent *pourquoi* tel token, tel composant, telle structure. Ces exemples annotés servent à la fois de référence humaine et d'exemples d'apprentissage pour les modèles.

### 3. Produire des agents.md et des skills (en cours)

La documentation seule ne suffit pas : il faut des artefacts actionnables que les outils peuvent charger et exécuter. Les fichiers `agents.md` définissent le contexte système à injecter dans un assistant. Ils embarquent les règles du DS, les conventions, les contraintes, pour que tout LLM qui les charge génère du code conforme sans configuration manuelle. Les skills vont plus loin : ils encapsulent des workflows complets, notamment la génération de composants conformes au DS et les audits de conformité sur du code existant.

Un skill d'audit est particulièrement stratégique : il permet de détecter le code qui s'écarte du DS (mauvais tokens, composants non standards, patterns non conformes) et de produire un rapport actionnable. C'est la boucle de rétroaction qui maintient la qualité dans la durée.

### 4. Exposer le DS via un serveur MCP

Les fichiers statiques (documentation, agents.md) sont un bon point de départ. L'étape suivante est d'exposer le DS comme un serveur MCP, un protocole qui permet aux outils des développeurs d'interroger le DS en temps réel. Plutôt que de charger un contexte statique au début d'une session, un dev peut poser la question "quel composant pour ce cas ?" et obtenir une réponse à jour, directement depuis le DS vivant. C'est ce qui fait passer le DS d'un référentiel documenté à une infrastructure requêtable, et qui ancre les outils IA dans la réalité du système plutôt que dans une copie figée.

### 5. Définir un framework d'évaluation

Pour savoir si l'effort produit ses effets, il faut mesurer. Un framework d'évaluation définit des cas de test : étant donné une demande de génération de code, le résultat est-il conforme au DS ? Utilise-t-il les bons composants, les bons tokens, les bonnes variantes ? Ces evaluations permettent d'itérer sur la qualité des agents et des skills avec une base objective, et de détecter les régressions quand le DS évolue.

### 6. Gouverner la mise à jour dans le temps

Le risque le moins visible de ce plan est la désynchronisation. Quand le DS évolue (nouveau composant, token déprécié, règle d'usage révisée), la documentation IA, les agents.md et les skills doivent être mis à jour en même temps. Sans processus explicite, la couche IA risque de progressivement diverger du DS réel, recréant exactement le problème qu'elle était censée résoudre.

La gouvernance de mise à jour n'est pas un sujet technique : c'est une question d'organisation. Qui est responsable de la cohérence entre le DS et ses artefacts IA ? À quel moment du cycle de contribution une mise à jour du DS déclenche-t-elle une mise à jour de la documentation LLM ? Ces réponses doivent être documentées et intégrées au processus de contribution dès le lancement du chantier, pas ajoutées après coup quand la première désynchronisation s'est déjà produite.

---

Ces six couches forment un système cohérent : les tokens sont les fondations, la documentation et les exemples sont le contenu, les agents et les skills sont les points d'entrée opérationnels, le MCP est le canal temps réel, les evaluations sont la mesure, et la gouvernance est ce qui maintient l'ensemble vivant. Chaque couche renforce les autres. L'absence de l'une fragilise toutes les autres.

## Conclusion

Un design system n'est pas un projet qu'on livre et qu'on referme. C'est une infrastructure vivante. Sa valeur dépend de l'exigence avec laquelle on la maintient et de la façon dont on l'expose aux outils que les équipes utilisent réellement.

L'IA n'est pas une menace pour le DS. Elle est un révélateur. Un DS structuré, documenté et exposé aux modèles produit du code plus cohérent, plus vite, avec moins d'arbitrages manuels pour les développeurs. Sans cet investissement de la core team, les outils IA contournent silencieusement l'infrastructure et génèrent de la dette design et technique à chaque ligne de code générée.

Le plan présenté ici n'est pas un pari sur l'avenir de l'IA. C'est un investissement sur la qualité de ce qui est produit aujourd'hui, avec les outils qui existent déjà dans les mains des développeurs.
