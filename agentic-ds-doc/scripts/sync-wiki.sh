#!/usr/bin/env bash
# sync-wiki.sh
# Vérifie s'il y a de nouveaux commits sur le repo GitHub du vault
# (Orange-OpenSource/ouds-documentation, branche main) et les applique
# localement au dossier agentic-ds-doc/.
#
# Usage :
#   ./sync-wiki.sh          # demande confirmation avant d'appliquer
#   ./sync-wiki.sh -y       # applique sans confirmation (utile en cron)

set -euo pipefail

REMOTE_URL="https://github.com/Orange-OpenSource/ouds-documentation.git"
BRANCH="main"
SUBPATH="agentic-ds-doc"
AUTO_YES=false

for arg in "$@"; do
  case "$arg" in
    -y|--yes) AUTO_YES=true ;;
  esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if ! REPO_ROOT="$(cd "$SCRIPT_DIR" && git rev-parse --show-toplevel 2>/dev/null)"; then
  echo "Erreur : ce dossier ne fait pas partie d'un dépôt git."
  echo "Clone d'abord le repo complet :"
  echo "  git clone $REMOTE_URL"
  echo "puis relance ce script depuis l'intérieur du clone (dans $SUBPATH/scripts/)."
  exit 1
fi

cd "$REPO_ROOT"

echo "Dépôt local : $REPO_ROOT"
echo "Vérification des mises à jour sur origin/$BRANCH..."
git fetch origin "$BRANCH" --quiet

LOCAL=$(git rev-parse "$BRANCH")
REMOTE=$(git rev-parse "origin/$BRANCH")
BASE=$(git merge-base "$BRANCH" "origin/$BRANCH")

if [ "$LOCAL" = "$REMOTE" ]; then
  echo "✓ Déjà à jour. Aucune mise à jour disponible."
  exit 0
fi

if [ "$LOCAL" != "$BASE" ]; then
  if [ "$REMOTE" = "$BASE" ]; then
    echo "⚠ Ta branche locale a des commits non poussés. Rien à récupérer depuis origin."
    exit 0
  else
    echo "⚠ Historique divergent entre local et origin/$BRANCH."
    echo "Résous manuellement (git pull / git rebase) avant de relancer ce script."
    exit 1
  fi
fi

COUNT=$(git rev-list --count "$BRANCH..origin/$BRANCH")
echo ""
echo "→ $COUNT nouveau(x) commit(s) en amont :"
git log --oneline "$BRANCH..origin/$BRANCH"
echo ""
echo "Fichiers concernés dans $SUBPATH/ :"
git diff --stat "$BRANCH" "origin/$BRANCH" -- "$SUBPATH" || echo "  (aucun changement dans $SUBPATH/)"
echo ""

if [ "$AUTO_YES" = false ]; then
  read -r -p "Appliquer ces mises à jour localement ? [o/N] " REPLY
  echo
  if [[ ! "$REPLY" =~ ^[OoYy]$ ]]; then
    echo "Annulé. Rien n'a été modifié."
    exit 0
  fi
fi

git checkout "$BRANCH" --quiet
git merge --ff-only "origin/$BRANCH"
echo "✓ Mises à jour appliquées à $SUBPATH/."
