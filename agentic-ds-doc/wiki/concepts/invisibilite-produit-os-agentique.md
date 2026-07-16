---
type: concept
tags: [apple, app-intents, ios27, siri, agentique, visibilite, plateforme, os, discoverabilite]
created: 2026-06-30
updated: 2026-06-30
sources:
  - "[wwdc-2026-apple-ai-native-os-levinriegner](../sources/wwdc-2026-apple-ai-native-os-levinriegner.md)"
related:
  - "[figma-library-invisible-ai-agents](../sources/figma-library-invisible-ai-agents.md)"
  - "[ia-comme-utilisateur](ia-comme-utilisateur.md)"
  - "[architecture-contexte-agentique](architecture-contexte-agentique.md)"
  - "[protocole-pas-produit](protocole-pas-produit.md)"
  - "[concevoir-les-conditions](concevoir-les-conditions.md)"
  - "[lisibilite-machine-design-system](lisibilite-machine-design-system.md)"
  - "[mcp-model-context-protocol](mcp-model-context-protocol.md)"
---

## Invisibilité produit dans un OS agentique

L'invisibilité produit est la condition dans laquelle une application est techniquement installée sur un appareil mais inaccessible à la couche d'intelligence agentique du système d'exploitation. La formule d'Ivan Leider (L+R) est la plus précise : "your product may be technically installed and practically invisible" ([wwdc-2026-apple-ai-native-os-levinriegner](../sources/wwdc-2026-apple-ai-native-os-levinriegner.md)). Dans l'écosystème Apple post-WWDC 2026, cette invisibilité survient quand une app n'expose pas ses actions et entités via le framework App Intents.

## Le mécanisme

L'entrée dans une application n'est plus garantie par son icône sur l'écran d'accueil. Dans un OS agentique, elle peut commencer par une question à Siri, une recherche Spotlight, une sélection de contenu à l'écran, une description de tâche depuis une autre app, ou une demande visuelle via la caméra. Apple Intelligence orchestre ces points d'entrée en consultant le registre des App Intents — les actions et entités que chaque app a déclaré comprendre et pouvoir exécuter.

Si une app n'a pas exposé ses capacités via App Intents, le système n'a aucun moyen de la surface dans ce nouveau layer. Elle reste accessible directement, mais elle est absente de la couche agentique — ce qui, au fur et à mesure que les utilisateurs adoptent les workflows Siri/Spotlight, équivaut fonctionnellement à ne pas exister pour ces cas d'usage.

Apple le formule explicitement dans sa documentation développeur WWDC 2026 : "Apps need to express their actions and entities to the system so Siri, Spotlight, Shortcuts, controls, and Apple Intelligence can understand and surface them — this is not a cosmetic integration."

## Parallèle avec l'invisibilité dans les design systems

Ce mécanisme est structurellement identique à celui décrit par Nurkhon ([figma-library-invisible-ai-agents](../sources/figma-library-invisible-ai-agents.md)) pour les bibliothèques Figma : un composant peut être parfaitement construit et rester invisible à un agent de code si son nom décrit son apparence plutôt que sa fonction. Les deux cas partagent la même racine : **les agents parsent, ils n'infèrent pas**. Siri ne devine pas ce que l'app peut faire ; elle parse les App Intents exposés. Un agent de code ne devine pas à quoi sert un composant ; il parse son nom et ses métadonnées.

La différence est le niveau d'opération : l'invisibilité Figma affecte les agents de génération de code. L'invisibilité App Intents affecte les agents d'orchestration OS. Les deux constituent des formes distinctes d'invisibilité agentique, et les deux ont la même correction : rendre explicite ce qui était implicite.

## App Intents comme équivalent Apple du MCP

App Intents fonctionne comme un [mcp-model-context-protocol](mcp-model-context-protocol.md) côté client Apple : il définit un contrat structuré entre l'app et le système d'exploitation, permettant à l'orchestrateur (Siri/Spotlight/Apple Intelligence) d'invoquer des actions sans ouvrir l'app. La différence architecturale est que MCP est un standard ouvert orienté serveur, tandis qu'App Intents est un framework propriétaire Apple côté device.

Les deux répondent au même problème fondamental : sans contrat structuré, l'orchestrateur ne peut pas agir. Avec un contrat, il peut invoquer, composer, et orchestrer. C'est pourquoi Leider recommande l'audit App Intents comme première action — avant même de construire quoi que ce soit de nouveau — exactement comme [concevoir-les-conditions](concevoir-les-conditions.md) recommande d'auditer le design system avant de générer.

## L'audit comme acte de conception

La recommandation de Leider reformule l'activité de design dans un OS agentique. Le travail n'est pas d'ajouter un chatbot. C'est d'auditer l'exposabilité du produit : quel contenu doit être indexable par Spotlight ? Quelles actions doivent être disponibles sans ouvrir l'app ? Quel contexte peut être exposé de façon sûre ? Quels workflows peuvent être déclenchés par une description en langage naturel ?

Cette liste de questions est fonctionnellement équivalente à l'audit que le corpus du vault préconise pour les design systems agentiques ([ai-ready-design-system-olha-bondar](../sources/ai-ready-design-system-olha-bondar.md), [protocole-arc](protocole-arc.md)) : identifier ce qui est exposé, ce qui est implicite, et ce qui doit être rendu explicite pour qu'un agent puisse agir correctement. La différence est l'artefact cible — App Intents plutôt que métadonnées de composant — mais la logique est identique.

## ⚡ Tension / Contradiction

L'invisibilité App Intents est une contrainte Apple propriétaire : une app qui expose parfaitement ses capacités via App Intents reste invisible à Google Assistant, à Copilot, et à tout autre orchestrateur IA non-Apple. L'écosystème MCP (ouvert) permet théoriquement d'exposer les mêmes capacités à n'importe quel agent. La question non résolue : les deux couches vont-elles converger (Apple adopte MCP pour les app capabilities, comme il l'a fait pour Xcode), ou reste-t-on avec deux régimes parallèles — App Intents pour l'OS Apple, MCP pour les agents tiers ?

WWDC 2026 confirme MCP natif dans Xcode pour les agents de développement — mais pas (encore) pour les capacités d'app exposées à Siri. Cette asymétrie est à surveiller.
