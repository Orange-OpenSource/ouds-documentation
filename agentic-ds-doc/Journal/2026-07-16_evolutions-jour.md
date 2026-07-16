---
type: journal
tags: [evolutions, bilan, jour]
created: 2026-07-16
periode: jour
---

# ÉVOLUTIONS — jour (2026-07-16 → 2026-07-16)

Sources ingérées : 9
Pages créées : 16 (9 sources, 4 concepts, 3 entités)
Pages mises à jour : 13 pages de contenu (concepts, entités) + index.md, log.md, overview.md et le registre des sources

---

## Ce qui a été ingéré

Neuf sources en deux veilles successives. La première, sur le thème général "agentic design system", a apporté quatre sources : le billet officiel de Figma sur son serveur MCP (première source primaire éditeur du vault sur le sujet, avec l'écart chiffré de 68 % d'adoption contre 32 % de confiance chez les développeurs) ; l'analyse de Thiago Victorino sur le passage du MCP Figma de la lecture à l'écriture directe dans le canvas ; l'inventaire pratique de six connecteurs MCP de Romina Kavcic, antérieur à toute sa série "Agentic Design Systems" ; et la démonstration technique de Storybook MCP par LogRocket, avec code et chiffres avant/après. La seconde veille, décidée après une analyse explicite des angles morts du vault, a ciblé les échecs documentés et la gouvernance organisationnelle réelle : le cas Amazon (quatre incidents Sev-1 en 90 jours, ~6,3 millions de commandes perdues), le modèle d'accountability à trois couches de Lance Dacy, la taxonomie de dérive design-system de Superdesign, l'analyse du "shadow code" de Pramin Pradeep, et le répertoire de dix-neuf incidents documentés de Crackr AI.

## Ce qui a évolué

Le concept [mcp-model-context-protocol](../wiki/concepts/mcp-model-context-protocol.md) a reçu trois enrichissements distincts dans la même journée — usages Figma, inventaire de connecteurs Kavcic, démonstration Storybook — devenant la page la plus densément mise à jour du vault ce jour. [accountability-gap-ia](../wiki/concepts/accountability-gap-ia.md) est passé du statut de concept entièrement théorique à celui de concept avec un cas réel documenté, une réponse structurelle nommée, et un mécanisme d'opacité distinct (shadow code) — trois enrichissements convergents en une seule journée sur une page qui stagnait depuis le 7 juillet. [composant-comme-contrat](../wiki/concepts/composant-comme-contrat.md) et [boucle-feedback-infrastructure](../wiki/concepts/boucle-feedback-infrastructure.md) ont reçu leurs premières preuves d'exécution vérifiables (avant/après, chiffres, code) après n'avoir eu jusqu'ici que des formulations conceptuelles ou des cas semi-manuels. Deux disambiguations ont été nécessaires : shadow AI vs shadow code, et le protocole ARC d'Achiardi vs le protocole ARC RPC — signe que le vault atteint une densité où des concepts nommés de façon proche doivent être explicitement distingués pour rester utilisables.

## Ce qui émerge

Le motif le plus net de la journée est un rééquilibrage délibéré. Les quatre premières sources documentaient presque exclusivement des succès et des capacités nouvelles (écriture agentique, boucle self-healing vérifiée, inventaire d'outils) ; la cinquième à la neuvième ont été choisies spécifiquement pour combler l'absence quasi totale d'échecs documentés dans le vault — un déséquilibre identifié explicitement avant la seconde veille plutôt que découvert après coup. Le cas Amazon révèle aussi une tension nouvelle et inattendue : l'entreprise dément publiquement que ses incidents impliquaient du code généré par IA tout en le documentant en interne, une donnée sur la gestion du narratif organisationnel qui n'a pas d'équivalent dans le reste du corpus, plus habitué aux études de cas volontairement publiées par leurs auteurs. Une lacune reste cependant ouverte malgré cette journée dense : aucune des sources ingérées ne documente un incident spécifiquement causé par une interface générée depuis un design system agentique (accessibilité composite, incohérence de marque shippée) — le scénario de Murphy Trueman, cœur d'[accountability-gap-ia](../wiki/concepts/accountability-gap-ia.md), reste sans cas réel propre au design system, seulement analogue via des incidents d'ingénierie plus généraux comme Amazon.

## Recommandations

Prioriser une veille sur les dispositions high-risk de l'EU AI Act (applicables août 2026, amendes jusqu'à 35M€ ou 7 % du chiffre d'affaires mondial), mentionnées par plusieurs sources du jour mais jamais comme sujet central — c'est un angle réglementaire distinct de la gouvernance volontaire déjà bien couverte. Chercher spécifiquement un incident de production causé par une défaillance composite d'interface générée depuis un design system plutôt qu'un échec d'ingénierie général, pour clore la lacune la plus précise identifiée aujourd'hui. Revisiter les deux sources écartées en "à surveiller" cette session (RACI pour agents IA, article accessibilité de brics-econ.org) une fois une source plus fiable ou plus spécifique aux design systems trouvée sur ces angles. Enfin, envisager un `lint` prochainement : la croissance rapide de la grappe accountability (quatre concepts créés ou enrichis en une journée sur ce seul thème) mérite une vérification de cohérence et de non-redondance avant la prochaine ingestion sur ce sujet.
