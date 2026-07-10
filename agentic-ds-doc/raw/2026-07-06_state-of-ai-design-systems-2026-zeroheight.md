---
title: "The State of AI in Design Systems 2026 — Full Report"
source: "https://zeroheight.com/resources/state-of-ai-design-systems/report/"
author:
  - "zeroheight"
published: 2026-05-01
created: 2026-07-06
tags:
  - "clippings"
  - "rapport"
  - "ia"
  - "design-system"
  - "statistiques"
---

# The State of AI in Design Systems 2026 — Full Report — zeroheight

Rapport annuel dédié à l'IA dans les design systems. N=123 praticiens DS, majoritairement in-house, entreprises 100+ employés, systèmes centralisés. Mai 2026.

Distinct du "Design Systems Report 2026: The Findings" (mars 2026) qui couvrait l'état général des DS. Ce rapport est entièrement focalisé sur l'IA.

---

## Section 01 — Qui répond

- 61 % product design & UX
- 84 % équipes in-house
- 86 % entreprises 100+ personnes
- 50 % design system centralisé
- 44 % entreprises < 1 000 personnes ; 56 % > 1 000
- 60 % des systèmes ont 3+ ans (tech debt pré-IA)
- 19 % < 1 an (construits en contexte AI-first)
- Échantillon auto-sélectionné, biaisé vers les grandes entreprises tech

---

## Section 02 — L'IA est le défaut

- **82 %** utilisent l'IA sous une forme quelconque
- **61 %** disent que l'usage a "crû significativement" dans les 12 derniers mois
- **32 %** "part of workflow" (opérationnalisé) ; 50 % expérimentent ; 18 % n'utilisent pas
- **68 %** en avance ou au niveau des autres équipes sur l'adoption IA

### Outils utilisés (multi-select)
- Claude : 74 %
- Figma Make : 56 %
- ChatGPT : 37 %
- GitHub Copilot : 36 %
- Gemini : 31 %
- Cursor : 29 %
- Stack moyen : 2 à 4 outils
- Large vs. petites entreprises : les grandes privilégient les licences existantes (GitHub Copilot, Figma Make)

### Cas d'usage principal (multi-select)
- Documentation : 25 %
- Outils & plugins : 11 %
- Développement : 13 %
- Travail sur les tokens : 10 %
- Prototypage & idéation : 10 %
- Création de composants : 9 %
- Audits, reviews & QA : 8 %
- MCP & handoff : 7 %
- Synthèse & validation : 6 %
- Génération de contenu : 4 %
- Testing : 4 %
- 11 % n'ont pas trouvé de bon cas d'usage

---

## Section 03 — Où l'IA rapporte

### Satisfaction par cas d'usage (% plus / moins satisfait)
| Cas d'usage | Moins satisfait | Plus satisfait |
|---|---|---|
| Rédaction documentation | 19 % | **63 %** |
| Audit / review docs | 8 % | 42 % |
| Génération de code | 25 % | 38 % |
| Linting & compliance | 10 % | 28 % |
| Specs de composants | 20 % | 27 % |
| MCP répondre questions | 14 % | 15 % |
| Token management | 27 % | 12 % |
| Design generation | **67 %** | 14 % |
| Release notes | 8 % | 5 % |

- **63 % satisfaits** de l'IA pour la documentation
- **67 % insatisfaits** de l'IA pour la génération de design
- Gap documentation/design generation : la donnée structurante du rapport

### Impact sur le craft work
- 31 % passent moins de temps sur le craft depuis l'adoption IA
- 54 % : pas de changement
- 15 % : plus de temps
- 65 % passent autant ou plus de temps sur le craft

### Sentiment sur la menace IA
- 43 % ne voient pas l'IA comme une menace
- 22 % : menace mineure
- 11 % : menace significative
- 4 % : menace existentielle
- 20 % : trop tôt pour dire

---

## Section 04 — La documentation est le goulot

- **47 %** font tourner un serveur MCP aujourd'hui
- **31 %** prévoient d'en adopter un
- **22 %** n'utilisent pas MCP
- Seulement **17 %** estiment leur documentation "très prête pour l'IA"
- 27 % : structurée ; 35 % : plutôt bien mais inconsistante ; 20 % : pas organisée

### 6 cas d'usage MCP documentés
1. Design-to-code translation
2. Sync bidirectionnelle design ↔ code
3. DS comme source de vérité pour les agents dans l'IDE
4. Réduction du support load de l'équipe DS
5. Visual QA et détection de drift design/code
6. MCPs empilés pour le handoff (Zeroheight + Code Connect + GitHub)

### Blocages à l'adoption MCP
- Sur la roadmap : 28 %
- Ne sait pas comment configurer : 22 %
- Sécurité : 13 %
- L'équipe n'utilise pas d'outils IA de coding : 12 %
- Politique entreprise : 7 %
- Non convaincu de la valeur : 3 %
- Seulement 3 % non convaincus de la valeur — le "si" est réglé, c'est le "comment"

### Grande vs. petite entreprise (MCP)
- Utilise MCP : petites 40 %, grandes 53 % (+13 pp)
- Prévoit d'adopter : petites 26 %, grandes 37 %
- Docs "très prêtes IA" : petites 13 %, grandes 20 %

Citation pratique : "AI flipped documentation from writing to reviewing — half a day per component down to under an hour."

---

## Section 05 — Le problème du Shadow AI

- **50 %** disent que l'usage IA d'autres équipes crée des problèmes pour leur DS
- **59 %** rapportent de l'UI qui contourne le DS
- **44 %** disent que l'organisation tolère ce contournement
- **15 %** : le contournement est normalisé ou généralisé
- **16 %** ne sont pas au courant si ça se passe

### 6 problèmes causés par le bypass DS
1. "Ça ressemble au système, ce n'est pas le système" — valeurs hardcodées, mauvais composants
2. PMs et ingénieurs contournent entièrement — prototypes vibe-codés qui deviennent des specs
3. Prototypes créent des attentes chez les stakeholders et ne sont jamais refaits sur le DS
4. L'accessibilité est silencieusement supprimée par l'IA
5. L'équipe DS ne peut pas tout surveiller
6. Shadow skills et plugins contradictoires — des bundles prépackagés contredisent les guidelines DS

### Réponse organisationnelle au bypass (n=69 où bypass existe)
- 44 % tolèrent
- 23 % normalisent
- 17 % n'en parlent pas
- 15 % le découragent

### Scale effect
- "Généralisé" : petites 10 %, grandes 18 % (+8 pp)
- Problème signalé : petites 46 %, grandes 54 % (+8 pp)

Citation : "Product teams use Gemini to generate code. Gemini does not know about our in-house DS and uses other design systems instead."

---

## Section 06 — La situation organisationnelle

- **25 %** citent "pas de temps" comme principal frein (premier frein par écart)
- **17 %** sécurité/politiques ; **16 %** qualité ; **5 %** budget
- Budget n'est quasiment pas un frein

### Qui drive l'adoption IA
- L'équipe DS elle-même : 56 %
- Mandat leadership : 50 %
- Initiative individuelle : 37 %
- Engineering : 36 %
- Product : 22 %
- Personne ne drive vraiment : 14 %

### Budget et politique
- 40 % budget dédié
- 41 % informel / ad hoc
- 11 % outils gratuits seulement
- 8 % bloqués par l'absence de budget
- 26 % politique formelle qui aide
- 35 % politique formelle qui restreint
- 24 % norms informelles
- 15 % wild west (pas de politique)

### Alignement leadership
- 50 % : aligné avec les attentes
- **39 % : gap — le leadership attend plus que ce qui est délivré**
- 7 % : plus capables que ce que le leadership pense
- 4 % : l'IA n'est pas sur leur radar

### Impact IA sur les équipes
- Réduction headcount : 12 %
- Augmentation headcount : 6 %
- Budget supplémentaire sécurisé : 34 %
- Formation interne sur l'IA : 43 %
- Temps dédié à l'exploration : 55 %
- Critères de recrutement en évolution : 20 %

### La question de la nécessité de l'équipe DS
- 50 % : non, question jamais posée
- 37 % : pas encore, mais je m'y attends
- 10 % : oui, ça a été soulevé
- 3 % : oui, sérieusement

---

## Section 07 — Ce que les équipes ressentent

- **63 %** se disent favorables à l'IA dans les design systems
- **67 %** pensent que l'IA est overhyped
- 63 % ET favorable ET overhyped — ambivalence cohérente, pas contradictoire

### Préoccupations principales (multi-select)
- Qualité des outputs : **61 %**
- Attentes des stakeholders : 43 %
- Sur-dépendance à l'IA : 37 %
- Homogénéisation du design : 34 %
- Deskilling des équipes : 22 %
- Confidentialité des données : 22 %
- Impact environnemental : 22 %
- Déplacement d'emplois : 22 %

- **43 %** pensent que l'IA renforce la position de l'équipe DS dans l'organisation
- **38 %** s'attendent à ce que l'organisation remette en question l'équipe DS

### Grande vs. petite entreprise (sentiment)
- Favorable à l'IA : petites 56 %, grandes 68 % (+12 pp)
- Leadership attend plus que délivré : petites 36 %, grandes 42 % (+6 pp)

---

## Section 08 — Si vous commencez aujourd'hui : 8 moves

1. **Commencer par la documentation, pas la génération de design** — la satisfaction nette est +44 pp pour docs vs -53 pp pour design generation
2. **Auditer votre documentation pour AI-readiness** — 83 % ont quelque chose de pire que "très prêt"
3. **MCP est le futur actuel** — 78 % utilisent ou planifient
4. **Partenariat avec les équipes produit sur le shadow AI** — politique seule ne marche pas
5. **Protéger le temps d'exploration** — 25 % citent "pas de temps" comme frein #1, 33 % dans les grandes entreprises
6. **Définir une politique IA, même légère** — 14 % n'en ont aucune, 28 % seulement des normes informelles
7. **Faire de la qualité la métrique avant l'adoption** — 61 % citent la qualité comme préoccupation principale
8. **Anticiper le gap d'attentes des stakeholders** — 43 % signalent ce gap

Citation finale : "The teams winning with AI are the ones who made their design systems legible to it. Documentation, MCP, partnership, policy, time. In that order."
