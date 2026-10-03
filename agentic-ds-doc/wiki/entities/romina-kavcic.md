---
type: entity
tags: [personne, design-system, ia, auteur, conférencière]
created: 2026-06-17
updated: 2026-07-16
sources:
  - "[design-system-most-important-asset-ai-era](../sources/design-system-most-important-asset-ai-era.md)"
  - "[how-to-automate-design-system-documentation](../sources/how-to-automate-design-system-documentation.md)"
  - "[design-systems-that-document-ai](../sources/design-systems-that-document-ai.md)"
  - "[self-healing-design-system](../sources/self-healing-design-system.md)"
  - "[50-design-token-files-one-problem](../sources/50-design-token-files-one-problem.md)"
  - "[your-design-system-is-not-ready-for-ai-agents](../sources/your-design-system-is-not-ready-for-ai-agents.md)"
  - "[agentic-ds-from-chatbot-to-orchestration](../sources/agentic-ds-from-chatbot-to-orchestration.md)"
  - "[20-ai-workflows-design-system-teams](../sources/20-ai-workflows-design-system-teams.md)"
  - "[design-system-advantage-is-memory](../sources/design-system-advantage-is-memory.md)"
  - "[romina-kavcic-5-mcp-connections](../sources/romina-kavcic-5-mcp-connections.md)"
related:
  - "[systeme-de-design-agentique](../concepts/systeme-de-design-agentique.md)"
  - "[into-design-systems-conference](into-design-systems-conference.md)"
  - "[lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md)"
  - "[documentation-lag](../concepts/documentation-lag.md)"
  - "[pipeline-figma-docs-automatise](../concepts/pipeline-figma-docs-automatise.md)"
  - "[mintlify](mintlify.md)"
  - "[modele-maturite-ia-design-system](../concepts/modele-maturite-ia-design-system.md)"
  - "[quatre-regles-ia-ux](../concepts/quatre-regles-ia-ux.md)"
  - "[deux-lectures-du-design-system-ia](../syntheses/deux-lectures-du-design-system-ia.md)"
  - "[protocole-pas-produit](../concepts/protocole-pas-produit.md)"
  - "[boucle-feedback-infrastructure](../concepts/boucle-feedback-infrastructure.md)"
  - "[composant-comme-contrat](../concepts/composant-comme-contrat.md)"
  - "[orchestration-multi-agents](../concepts/orchestration-multi-agents.md)"
---

## Romina Kavcic

Romina Kavcic est designer spécialisée en design systems, auteure du newsletter et blog thedesignsystem.guide sur Substack. Elle produit des contenus hebdomadaires sur la construction et le scaling des design systems, et a développé le cours "Design Tokens Mastery".

Elle est conférencière à l'[into-design-systems-conference](into-design-systems-conference.md), où elle est intervenue deux années consécutives : en 2025 sur les "context-aware design systems" (une vision prospective), et en 2026 sur les "agentic design systems" (outils, chiffres, retours d'expérience réels). La série "Agentic Design Systems" publiée en 2026 est la transcription enrichie de cette conférence.

Son approche est pratique et basée sur l'expérimentation directe : elle documente des workflows concrets, des scripts CLI, des configurations MCP, et partage des résultats chiffrés (554 descriptions de composants générées en une session, tokens résolus en ligne de commande, patterns composés par script shell).

Sa thèse centrale : "AI generates code. Design systems generate understanding" ([design-system-most-important-asset-ai-era](../sources/design-system-most-important-asset-ai-era.md)).

Son article "How to Automate Design System Documentation" (octobre 2025) documente un pipeline pratique Figma → Claude Code → [mintlify](mintlify.md) pour éliminer le [documentation-lag](../concepts/documentation-lag.md) — la conviction opérationnelle que "the only way to kill latency is to connect your tools so they document themselves" ([how-to-automate-design-system-documentation](../sources/how-to-automate-design-system-documentation.md)).

À l'AI Design Systems Conference 2026, elle présente **Tidy**, un plugin Figma avec 66 outils MCP : audit du naming, health score sur 6 catégories, validation de nouvelles variables, composition de patterns (formulaire login, confirmation destructive) à partir de composants existants ([design-systems-mcp-complete-guide](../sources/design-systems-mcp-complete-guide.md)). Tidy est couplé à **Observatory**, un dashboard qui visualise le knowledge graph du design system à travers Figma, GitHub, Storybook, Linear, Chromatic, Playwright et PostHog. C'est l'instance la plus avancée du [knowledge-graph-design-system](../concepts/knowledge-graph-design-system.md) documentée dans le vault — non plus comme concept mais comme produit en usage.

La partie 3 de la série, "The Self-Healing Design System" (avril 2026), décrit l'architecture de production qu'elle maintient depuis un an : Claude Code au centre, connecté via MCP à 12 outils (Figma/Tidy, GitHub, Storybook, PostHog, Granola, Sentry, Notion, Jira, Stylelint, Linear, Mintlify, Chromatic). Elle y formalise la boucle self-healing Watch/Analyze/Execute/Observe, documente son benchmark multi-modèles (Claude Code > Cursor/Codex/Gemini/GPT/Llama/Mistral sur les tâches de design system), et énonce le principe [protocole-pas-produit](../concepts/protocole-pas-produit.md) : construire sur MCP signifie que la couche d'orchestration IA est remplaçable sans reconstruire les intégrations. La partie 3 est tronquée dans le vault — les sections "what AI genuinely cannot do" et "three phases" manquent dans le raw ([self-healing-design-system](../sources/self-healing-design-system.md)).

Son article "50 design token files, one problem: your agents can't read the meaning" (juin 2026) est son travail empirique le plus rigoureux sur les tokens. Elle audite les fichiers sources de 50 design systems publics — pas leurs sites de documentation, mais les fichiers réels qu'un agent chargerait. Elle y documente l'absence quasi-universelle de couche de sens dans ces fichiers : ~15/50 ont une description, ~10/50 ont un champ de dépréciation, **1/50 a une règle de non-usage** (GitHub Primer). Elle démontre par expérience contrôlée (fichier nu vs fichier annoté DTCG) que la présence d'un `$description` par token est la différence entre un agent qui devine (2/3 erreurs) et un agent qui sait (0/2 erreurs). Elle formule la distinction centrale : **readable ≠ usable** — et publie le template DTCG complet avec `$description`, `$deprecated`, `$extensions`. Voir [readable-vs-usable-token](../concepts/readable-vs-usable-token.md), [dtcg-annotation-schema](../concepts/dtcg-annotation-schema.md), [delegation-lens](../concepts/delegation-lens.md), [priori-conflictuels-nommage](../concepts/priori-conflictuels-nommage.md).

À l'AI Design Systems Conference 2026, organisée par [sil-bormuller](sil-bormuller.md), Kavcic intervient sur les "failure modes" des design systems face aux agents IA. Deux contributions spécifiques à cette conférence s'ajoutent à sa série publiée : le chiffrage à **30-40 % du temps d'équipe consacré à la maintenance pure** (régressions d'accessibilité, mauvais usages de tokens, documentation désynchronisée), et la formalisation de son self-healing loop via le framework **IBM MAPE-K** (Observe, Detect, Suggest, Fix, Learn) avec un drift-scoring engine alimenté par l'API Figma, les hooks CI et les analytics d'usage. Elle y présente également le cadre de [niveaux-confiance-actions-agentiques](../concepts/niveaux-confiance-actions-agentiques.md) par action agentique (auto-merge / draft PR / suggest only). Voir [your-design-system-is-not-ready-for-ai-agents](../sources/your-design-system-is-not-ready-for-ai-agents.md) pour la synthèse complète.

Son article "From Chatbot to Orchestration" (mai 2026) ([agentic-ds-from-chatbot-to-orchestration](../sources/agentic-ds-from-chatbot-to-orchestration.md)) reformule le paradigme agentique autour de deux décalages conceptuels. Le premier : la question centrale n'est pas "comment générer plus vite" mais "est-ce que l'agent comprend *pourquoi* ce composant existe". Le second — et c'est sa contribution conceptuelle la plus originale — est le renversement composant → contrat : un composant agentique n'est plus quelque chose qu'on importe mais un accord entre design, code, intent produit, accessibilité et comportement. Voir [composant-comme-contrat](../concepts/composant-comme-contrat.md). L'article introduit aussi l'architecture d'orchestration multi-agents (designer agent / developer agent / doc agent / QA agent + orchestrateur) et l'inventaire des quatre risques de l'autonomie agentique : design debt machine-speed, fausse confiance dans la doc générée, manipulation UX par adaptation runtime, governance gaps. Voir [orchestration-multi-agents](../concepts/orchestration-multi-agents.md) et [gouvernance-design-system-ia](../concepts/gouvernance-design-system-ia.md).

Son article "20 AI workflows that save design system teams 10+ hours a week" (février 2026) ([20-ai-workflows-design-system-teams](../sources/20-ai-workflows-design-system-teams.md)) est son catalogue opérationnel le plus exhaustif : 20 workflows concrets groupés en cinq domaines (composants, documentation, stratégie, tokens, adoption). Il introduit le pattern [audit-tokens-playwright](../concepts/audit-tokens-playwright.md) (Planner/Generator/Healer), le concept de [bypass-patterns-comme-user-research](../concepts/bypass-patterns-comme-user-research.md), et [assistant-ia-24h](../concepts/assistant-ia-24h.md) (OpenClaw). Il confirme l'architecture `.ai/` directory comme couche d'instructions projet, et propose les build-time metrics comme alternative aux métriques runtime invasives.

Son article "Design Systems That Document AI" (juin 2026) change d'angle : après avoir traité de l'IA comme opérateur du design system, Kavcic analyse comment les design systems documentent les *fonctionnalités IA pour les utilisateurs humains*. L'étude porte sur 156 systèmes publics — 83 % sans aucune couche IA. Elle établit un [modèle de maturité en cinq niveaux](../concepts/modele-maturite-ia-design-system.md) et identifie les [quatre règles convergentes](../concepts/quatre-regles-ia-ux.md) issues des organisations les plus avancées. La distinction entre ces deux lectures du "design system et IA" est formalisée dans [deux-lectures-du-design-system-ia](../syntheses/deux-lectures-du-design-system-ia.md).

Son article le plus ancien ingéré dans le vault, "5 MCP Connections Every Design System Team Needs Right Now" (août 2025, [romina-kavcic-5-mcp-connections](../sources/romina-kavcic-5-mcp-connections.md)), précède toute sa série "Agentic Design Systems" et adopte un angle purement pratique : inventaire de 6 connecteurs MCP (Figma, Mintlify, GitHub, GitLab, PostHog, Slack) avec niveau de complexité d'installation et exemples de prompts concrets par outil. C'est le premier document du corpus à traiter GitLab et Slack comme connecteurs MCP à part entière plutôt que comme mentions en passant.

Son article "The Design System Advantage Is Memory" (mai 2026) ([design-system-advantage-is-memory](../sources/design-system-advantage-is-memory.md)) est peut-être sa contribution conceptuelle la plus tranchante. Partant de son expérience directe (105 outils MCP connectés, résultat insuffisant), elle reformule la question de l'IA-readiness : l'avantage n'est pas le modèle, le nombre d'outils ou le prompt — c'est la mémoire institutionnelle rendue retrievable. Elle structure le problème autour de la distinction "visible 10% / invisible 90%" (tokens et docs d'un côté, décisions et historiques de l'autre), propose une architecture en trois couches obligatoires (données → structure → agent), et documente son usage de QMD comme test minimal de signal avant d'investir dans un graphe complet. La thèse terminale — "The design system is no longer the deliverable. It is the dataset." — est la formulation la plus condensée de l'argument. Voir [memoire-design-system](../concepts/memoire-design-system.md) et [design-system-comme-dataset](../concepts/design-system-comme-dataset.md).
