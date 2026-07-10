---
type: journal
periode: semaine
date_debut: 2026-07-01
date_fin: 2026-07-07
sources_ingérées: 8
pages_créées: 26
pages_mises_à_jour: 19
---

```
ÉVOLUTIONS — semaine (2026-07-01 → 2026-07-07)
────────────────────────────────────────────────
Sources ingérées : 8
Pages créées     : 26
Pages mises à jour : 19
```

## Ce qui a été ingéré

La semaine couvre huit sources réparties sur trois journées d'activité (03, 06 et 07 juillet), avec une nette concentration le 06 (cinq ingests en une session).

Le 03 juillet, "Agentic Design System — From Chatbot to Orchestration" de [[romina-kavcic]] pose le passage du modèle chatbot à l'orchestration multi-agents comme seuil architectural, en reformulant le composant comme contrat ([[composant-comme-contrat]]) et en formalisant la "governed autonomy" comme posture opérationnelle.

Le 06 juillet, cinq sources ont été ingérées. "20 AI workflows" (Kavcic) enrichit l'architecture Skills avec des exemples nommés et introduit trois outils nouveaux ([[context7]], [[openclaw]], [[plugma]]) ainsi que le renversement paradigmatique [[bypass-patterns-comme-user-research]]. "Making product documentation work for humans and AI" de [[geri-reid]] apporte le principe dual-audience — améliorer la doc pour les humains améliore simultanément la lisibilité machine — et le cadre des [[cinq-questions-documentation-produit]] pour les équipes non-expertes. "Your design system might be AI-ready. Your organisation probably isn't." de [[murphy-trueman]] introduit l'[[accountability-gap-ia]] comme concept central : les failures composites (composants accessibles, parcours inaccessible) qu'aucune contrainte technique ne capture. "The State of AI in Design Systems 2026" de zeroheight (N=123) fournit le premier benchmark sectoriel complet et introduit [[shadow-ia-design-system]] comme phénomène touchant déjà 50 % des équipes. "Meta Just Open-Sourced Its Design System" de Harsha Sridhar apporte un regard de marché comparatif (MUI / Atlaskit / Shadcn / Astryx) et l'axe composants scellés vs ouverts comme dimension d'opérabilité agentique.

Le 07 juillet, deux sources complètent la semaine. "Your design system is fragmenting into agent files" de Trueman cartographie la pile complète des formats agent-facing et identifie trois angles jusqu'ici absents : [[agents-md-format]] comme concept propre, [[dispersion-decision-design]] comme problème de gouvernance, et [[prompt-injection-design-system]] comme angle de sécurité. "The human layer in agentic design systems" de [[cristian-morales-achiardi]] ferme sa série et précise la limite de la gouvernance agentique : elle garantit l'exécution de ce qui a été encodé, pas la qualité de l'encodage.

## Ce qui a évolué

[[gouvernance-design-system-ia]] est la page qui a le plus bougé cette semaine : elle a absorbé cinq apports distincts — la gouvernance organisationnelle (Trueman, 06), le shadow AI comme problème de gouvernance externe (zeroheight, 06), la gouvernance des coutures entre formats (Trueman, 07), la limite de la gouvernance sur la qualité d'encodage (Morales Achiardi, 07), et les quatre risques de l'autonomie agentique (Kavcic, 03). Elle reste la page la plus dense du vault et commence à avoir besoin d'une sous-structure plus explicite.

[[metriques-adoption-ia-design-system]] a reçu les données sectorielles les plus complètes à ce jour : adoption tools breakdown (Claude 74 %, Figma Make 56 %), MCP 47 %, 17 % AI-readiness, 50 % shadow AI, et le gap buy-in DS (42 % → 32 %). La page passe d'une collection de métriques éparses à un tableau de bord du domaine.

[[documentation-lag]] a été enrichi depuis trois angles simultanés cette semaine (Kavcic, Reid, zeroheight), confirmant le lag documentaire comme goulot structurel que le corpus adresse maintenant de façon très couverte.

[[architecture-skills-rules-instructions]] a reçu des exemples nommés concrets (token-migration-assistant, component-audit, brand-guidelines) et la nuance portabilité vs exécution inconsistante pour SKILL.md — la page passe d'un cadre conceptuel à un guide opérationnel.

[[accountability-gap-ia]], créé le 06, a déjà été mis à jour le 07 pour intégrer le cas inverse de Morales Achiardi : un gap résolu par traçabilité architecturale, qui raffine le concept en distinguant failures encodées et failures composites.

## Ce qui émerge

Trois lignes de force transversales se dégagent de l'ensemble de la semaine.

La première est la **maturité du corpus technique** : les pages [[lisibilite-machine-design-system]], [[schema-metadata-composant]], [[trois-couches-composants-agents]], [[mcp-model-context-protocol]] et [[intent-token]] ont maintenant une couverture dense depuis des angles multiples et des auteurs indépendants. Ce corpus est probablement arrivé à un niveau de complétude qui ne nécessite plus d'ingestions d'approfondissement — les prochains apports sur ces thèmes seront marginaux.

La deuxième est l'**émergence de la gouvernance comme sous-domaine propre**. [[gouvernance-design-system-ia]] réunit désormais trop de problèmes distincts : gouvernance technique (auditeurs, contraintes exécutables), gouvernance organisationnelle (droits décisionnels, accountability gap), gouvernance des coutures entre formats (dispersion, ownership de la pile), et gouvernance contre le bypass (shadow AI, prompt injection). Ces quatre registres de gouvernance ont des acteurs, des mécanismes et des points d'échec différents. Un éclatement en sous-pages thématiques s'impose.

La troisième est l'**apparition d'un angle sécurité** entièrement nouveau avec [[prompt-injection-design-system]]. C'est le seul concept de la semaine sans corpus derrière lui dans le vault. Le changement de statut des fichiers de documentation (de texte passif à instruction exécutable) est formulé, mais non encore étayé par des sources sur la supply chain security ou les pratiques de review des fichiers d'infrastructure.

## Recommandations

Éclater [[gouvernance-design-system-ia]] en trois ou quatre sous-pages thématiques (technique, organisationnelle, formats, bypass/sécurité), en conservant la page principale comme index des quatre registres avec liens vers les sous-pages — c'est la refactorisation la plus utile à faire maintenant avant que la page devienne illisible. Ingérer une source sur la sécurité de la chaîne d'approvisionnement logicielle (supply chain security, SLSA, SBOM) pour nourrir [[prompt-injection-design-system]] qui reste orphelin de corpus. Appliquer le cadre [[dispersion-decision-design]] à OUDS concrètement : cartographier où vit la décision "couleur primaire OUDS" dans les artefacts existants pour rendre le problème actionnable plutôt que conceptuel. Créer [[astryx-vs-mui-atlaskit-shadcn]] comme comparaison structurée à partir de la source Sridhar, en complétant avec les données connues du vault sur les autres systèmes — la comparaison existe mais n'est pour l'instant qu'une ébauche issue d'une seule source.
