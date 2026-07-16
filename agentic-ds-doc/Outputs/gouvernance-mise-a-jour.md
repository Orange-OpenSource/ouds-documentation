# Gouvernance de mise à jour des artefacts IA

## Le problème central

Les artefacts IA (documentation LLM, agents.md, skills) sont des dérivés du DS. Comme tout dérivé, ils se désynchronisent dès que la source évolue sans que les dérivés suivent. La différence avec une documentation classique : la désynchronisation d'un artefact IA est silencieuse. Le LLM continue à générer du code, mais à partir de règles obsolètes, sans signal d'erreur apparent. La dette s'accumule sans qu'on la voie.

La gouvernance de mise à jour vise à rendre cette désynchronisation impossible par construction, plutôt que par vigilance individuelle.

## Piste 1 : automatiser la détection des dérives

Le repo GitHub qui centralise les markdowns OUDS est un déclencheur naturel. À chaque merge sur la branche principale, un script peut comparer la version précédente et identifier les composants ou tokens modifiés. Il ne s'agit pas de mettre à jour automatiquement la documentation LLM, mais de produire une liste des fichiers à revoir et d'ouvrir une issue ou une notification correspondante.

L'objectif est de transformer une dérive potentielle en tâche explicite, assignée, traçable.

## Piste 2 : intégrer la mise à jour dans le contrat de contribution

Toute PR qui modifie un composant ou un token dans OUDS doit embarquer la mise à jour des artefacts LLM correspondants. Ce principe se traduit concrètement par une checklist de PR qui inclut la documentation IA, et potentiellement une CI check qui bloque le merge si les fichiers concernés n'ont pas été touchés. La règle n'est pas informelle : elle est encodée dans le workflow.

## Piste 3 : nommer un propriétaire

L'automatisation couvre les cas prévisibles. Elle ne remplace pas un regard humain pour détecter les dérives de fond : une règle d'usage qui a évolué sans passer par une PR formelle, un anti-pattern qui a émergé dans les usages réels, un composant déprécié dont la documentation LLM n'a pas été marquée obsolète.

Un membre de la core team DS doit être propriétaire de la cohérence entre le DS et ses artefacts IA, avec une cadence de revue explicite (mensuelle par exemple). Ce rôle peut tourner, mais il doit être nommé.

## Piste 4 : versionner les artefacts avec le DS

Les agents.md et les skills doivent suivre le versionnement du DS. Si OUDS passe en v3, un agents.md v3 doit exister. Cela permet aux équipes qui n'ont pas encore migré de continuer à utiliser la version précédente sans risque de régression, et rend les évolutions traçables. La version courante doit être explicitement indiquée dans chaque artefact.

## Ordre de priorité suggéré

La checklist de PR est la mesure la plus simple et la plus immédiatement efficace : elle ne nécessite pas d'outillage supplémentaire et crée une habitude dès le début. L'automatisation de la détection vient ensuite, une fois que le périmètre des artefacts est stabilisé. Le versionnement formel peut attendre la première évolution majeure du DS.
