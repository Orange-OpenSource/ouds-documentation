---
type: entity
tags: [personne, design-system, ia, machine-readable, indeed, netflix, benchmark, json]
created: 2026-06-17
updated: 2026-07-07
sources:
  - "[[machine-readable-design-systems-designing-for-ai-as-a-user]]"
  - "[[your-design-system-is-not-ready-for-ai-agents]]"
  - "[[into-design-systems-agentic-guide]]"
  - "[[your-design-system-fragmenting-agent-files]]"
related:
  - "[[ia-comme-utilisateur]]"
  - "[[mcp-on-demand-vs-rules-always-on]]"
  - "[[lisibilite-machine-design-system]]"
  - "[[schema-metadata-composant]]"
  - "[[cristian-morales-achiardi]]"
  - "[[into-design-systems-conference]]"
---

## Diana Wolosin

Senior Product Designer, Architecture and Systems chez Netflix (ex-Indeed). Dix ans d'expérience dans la construction de systèmes à grande échelle. Ses travaux actuels portent sur les design systems machine-readable comme infrastructure IA, avec un accent particulier sur les frameworks d'évaluation, les benchmarks de format, et la gouvernance du contexte.

## Contribution au domaine

Wolosin est l'auteure de la thèse "AI is a new user" — le cadrage qui reformule le design system comme une infrastructure à double audience : les humains qui lisent et interprètent d'un côté, les IA qui requêtent et raisonnent programmatiquement de l'autre. Cette reformulation implique que la qualité de la documentation ne peut plus se mesurer uniquement à sa lisibilité humaine.

Elle a mené le premier benchmark public rigoureux comparant des formats de métadonnées pour MCP de design system : 8 configurations, 1 056 prompts, 5 formats (Markdown, plain Markdown, hybride Markdown+JSON, JSON, TOON). Résultat : JSON comme format gagnant, 80 % de tokens en moins et 5× moins cher que Markdown pour une précision équivalente. Voir [[machine-readable-design-systems-designing-for-ai-as-a-user]].

Elle a également formalisé la distinction MCP on-demand vs Rules always-on — l'une des contributions conceptuelles les plus opérationnelles dans le corpus du vault : voir [[mcp-on-demand-vs-rules-always-on]].

## Articles et conférences

Série d'articles sur Design Systems Collective (Medium) incluant "Machine-Readable Design Systems: Designing for AI as a User" (mars 2026) et "Intent-Driven Context for AI Design Systems" (janvier 2026) et "Design Systems for AI: Introducing the Context Engine". Conférence à l'[[into-design-systems-conference]] AI Conference for Designers 2026 (mars 2026).

Le résultat opérationnel du benchmark d'Indeed : après migration vers JSON, Indeed a produit **4 300 prototypes IA en 4 mois**. La pipeline est déclenchée automatiquement à chaque mise à jour MDX et convertit la documentation composant en métadonnées JSON structurées. Sa formulation synthétique : "Our docs are written for humans. The new user, AI, needs structured metadata, not documentation prose." ([[your-design-system-is-not-ready-for-ai-agents]])

Sa formule la plus condensée sur la supériorité du JSON : "JSON is like a contract. It has explicit keys, explicit values, explicit boundaries, and there is no ambiguity." ([[into-design-systems-agentic-guide]]). Cette métaphore du contrat dit quelque chose que le benchmarking quantitatif ne dit pas : la valeur du JSON n'est pas seulement sa compression, c'est son caractère *non-ambiguë par construction*. Un fichier JSON malformé ne se lit pas — il crashe. Une phrase Markdown imprécise se lit mais induit des hallucinations.

## Confirmation du benchmark par Trueman (2026-05-14)

[[murphy-trueman]] cite le benchmark de Wolosin dans [[your-design-system-fragmenting-agent-files]] avec des chiffres précis : 77 composants parsés depuis MDX, 1 056 prompts, 8 configurations de métadonnées différentes. Résultats : Markdown consomme ~30 000 tokens avec 82 % de couverture et des hallucinations visibles ; JSON livre une précision plus haute avec 80 % de tokens en moins et un coût annuel environ 5 fois inférieur. La règle opérationnelle dérivée — "JSON for MCP, Markdown for LLM" — est citée comme standard de fait pour l'architecture des formats agent-facing. Cette citation dans un article de synthèse distinct confirme que le benchmark de Wolosin est devenu une référence établie dans le corpus du domaine, pas seulement un résultat d'équipe individuelle.

## Lien avec les autres auteurs du vault

Wolosin et [[cristian-morales-achiardi]] convergent sur la nécessité de rendre le design system lisible par les machines, mais avec des angles différents : Morales Achiardi développe l'architecture agentique complète (couches, protocole ARC, gouvernance) ; Wolosin apporte la validation empirique quantifiée (benchmark de formats) et la distinction opérationnelle MCP/Rules qui manquait dans la série Morales Achiardi.
