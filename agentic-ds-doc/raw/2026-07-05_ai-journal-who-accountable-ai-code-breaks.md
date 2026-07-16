---
source_url: https://aijourn.com/ai-now-writes-the-code-whos-accountable-when-it-breaks/
author: Pramin Pradeep (Co-fondateur et CEO, BotGauge AI) via The AI Journal
published: 2026-07-05
ingested: 2026-07-16
---

# AI Now Writes the Code. Who's Accountable When It Breaks?

Source brute — issue de The AI Journal.

## Contexte chiffré

Fin 2025, l'IA générait ~40-41% du code dans de nombreuses équipes d'ingénierie. Selon le rapport 2026 Aikido Security "State of AI in Security & Development", le code généré par IA est désormais la cause d'une brèche d'entreprise sur cinq. Selon un sondage Lightrun (avril 2026), 43% des changements de code générés par IA nécessitent du débogage en production.

## Le "shadow code"

Terme désignant la logique logicielle qui entre en production via développement assisté par IA mais n'est jamais pleinement comprise, documentée, ou examinée architecturalement par les humains responsables du système. Pas nécessairement du code buggé — certains fonctionnent parfaitement indéfiniment. Le problème : son comportement sous conditions spécifiques n'a jamais été interrogé, parce que le processus qui l'a produit ne requiert pas cette interrogation de la même façon que l'ingénierie délibérée. À l'échelle (des centaines ou milliers de snippets mergés), les systèmes deviennent "locally understood, but globally opaque" (recherche CodeRabbit).

## Pourquoi les contrôles existants ratent le problème

Les outils d'analyse statique scannent les artefacts de code pour des patterns de vulnérabilité reconnaissables — ils ne sont pas conçus pour détecter les risques comportementaux qui émergent quand des composants interagissent dynamiquement à l'exécution. La revue par les pairs a son propre problème structurel : le code généré par IA paraît souvent correct, bien formaté, immédiatement fonctionnel — cette plausibilité réduit le scepticisme du reviewer. L'adoption de l'IA est corrélée à une hausse de près de 10% de l'instabilité du code.

## Le vide d'accountability

Quand du code généré par IA cause un incident de production, la question de qui a échoué n'a pas de réponse propre. Selon le sondage Aikido Security, en cas de brèche liée à l'IA : 53% des répondants blâment les équipes sécurité, 45% blâment le développeur, 42% blâment qui a mergé le code. Aucun consensus, aucune propriété claire — juste du blâme distribué et une accountability non résolue.

Pour les industries régulées (finance, santé, infrastructures critiques), cette ambiguïté est une exposition de conformité : les régulateurs attendent une traçabilité démontrable pour la logique embarquée dans les systèmes critiques.

## Référence au cas Amazon

Amazon a lancé un "90-day code safety reset" sur 335 systèmes critiques, exigeant que les changements de code assistés par IA soient approuvés par des ingénieurs seniors avant déploiement — reconnaissance que l'infrastructure d'accountability autour du code généré par IA était inadéquate.

## La réponse proposée : accountability distribuée, pas assignée

Pas de partie unique à blâmer — construire un système d'assurance à travers les personnes, processus et outils. Pour les développeurs : traiter l'output IA comme point de départ qui exige interrogation, pas solution finie qui attend l'approbation. Pour le leadership technique : élargir le focus des artefacts de code au comportement système (validation comportementale à l'exécution, tests exploratoires continus). Pour l'organisation : gouvernance qui matche le tempo du développement — suivre les métriques de défauts attribués à l'IA avec la même rigueur que les incidents de sécurité.

## Citation clé

"AI didn't remove ownership from your engineering organization — it diffused it across so many hands that no one owns the outcome." (paraphrase du problème central, formulation convergente avec Big Agile/Lance Dacy)
