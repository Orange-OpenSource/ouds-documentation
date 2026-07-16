---
source_url: https://big-agile.com/blog/who-owns-ai-generated-code-when-it-ships-building-a-chain-of-human-accountability
author: Lance Dacy (Big Agile)
published: 2026-06-01
ingested: 2026-07-16
---

# Who Owns AI-Generated Code When It Ships to Production?

Source brute — issue du blog Big Agile.

## Le problème central

"AI didn't remove accountability from your engineering organization. It diffused it across so many hands that no one owns the outcome." La responsabilité diffuse n'est pas de la responsabilité — c'est un échec de coordination. Dans le modèle traditionnel, le code a un auteur clair : quand quelque chose casse, on peut remonter à une décision prise par quelqu'un. L'IA casse cette chaîne dès le premier maillon.

## Les données citées

Ox Security, rapport "Army of Juniors" (octobre 2025) : analyse de 300+ repos open-source dont 50 utilisant Copilot/Cursor/Claude. Documente 10 patterns architecturaux et sécuritaires typiques de l'IA ("insecure by dumbness" — citation directe du VP Research). Apiiro, étude sur des dizaines de milliers de repos (entreprises Fortune 50, ~6 mois) : développeurs assistés par IA committent 3-4x plus vite mais avec des PRs plus grosses et moins fréquentes ; findings de sécurité mensuels passés de ~1000 à 10000+ ; failles architecturales (élévation de privilèges) +322% ; failles de design +153%.

## Le modèle à trois couches d'accountability

**Couche 1 — Individuelle.** Pour tout travail incluant de l'output généré par IA, un humain nommé doit avoir revu le travail et être prêt à mettre son nom dessus. Pratique concrète testée : ajouter une ligne "Reviewer of record: [nom]" dans chaque PR assistée par IA. Coût quasi nul, effet immédiat sur la qualité des conversations d'équipe.

**Couche 2 — Équipe.** L'équipe s'accorde sur les catégories de travail pouvant utiliser l'IA sans review additionnelle, et celles qui en requièrent une. Exemple : refactoring d'une fonction utilitaire privée = pas de review approfondie nécessaire ; tout ce qui touche authentification, autorisation, paiement, PII = review obligatoire. Vit dans le working agreement ou la definition of done de l'équipe.

**Couche 3 — Organisationnelle.** Le leadership fixe la politique : catégories où l'IA est appropriée, comment la qualité est mesurée, qui possède les événements qualité liés à l'IA au niveau leadership, comment ils sont revus trimestriellement.

## Le test des 30 secondes

Pour tout artefact généré par IA atteignant un client, on doit pouvoir tracer une chaîne d'accountability humaine en 30 secondes — pas 30 minutes.

## Cadres de gouvernance cités

NIST AI Risk Management Framework (gouvernance du risque IA de bout en bout). OWASP Top 10 for LLM Applications (risques spécifiques aux LLM : prompt injection, insecure output handling, sur-dépendance à l'output IA).

## Citation clé

"You don't need a 50-page AI governance policy to start closing this gap. What you need is to engineer it into the workflow: a single named human attached to every AI-generated change that actually ships."

## Référence croisée

Cite le reset de sécurité de code de 90 jours d'Amazon sur 335 systèmes critiques comme exemple de correction structurelle a posteriori.
