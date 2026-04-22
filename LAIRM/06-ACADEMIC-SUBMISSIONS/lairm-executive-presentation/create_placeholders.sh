#!/bin/bash

# List of all required files
files=(
"parts/00-foundational-context/01-introduction.tex"
"parts/00-foundational-context/02-definitions.tex"
"parts/00-foundational-context/03-research-questions.tex"
"parts/00-foundational-context/04-methodology.tex"
"parts/00-foundational-context/05-literature-review.tex"
"parts/00-foundational-context/06-formal-methodology.tex"
"parts/01-axioms-core/01-axiom-I-suprematia.tex"
"parts/01-axioms-core/02-axiom-II-identitas.tex"
"parts/01-axioms-core/03-axiom-III-responsabilitas.tex"
"parts/01-axioms-core/04-axiom-IV-circulus.tex"
"parts/01-axioms-core/05-axiom-V-interoperabilitas.tex"
"parts/02-axioms-operational/06-axiom-VI-auditum.tex"
"parts/02-axioms-operational/07-axiom-VII-adaptatio.tex"
"parts/02-axioms-operational/08-axiom-VIII-ethica.tex"
"parts/02-axioms-operational/09-axiom-IX-gubernatio.tex"
"parts/03-axioms-prospective/10-axiom-X-energia.tex"
"parts/03-axioms-prospective/11-axiom-XI-arma.tex"
"parts/04-implementation/01-technical-architecture.tex"
"parts/04-implementation/02-deployment-strategy.tex"
"parts/04-implementation/03-governance-framework.tex"
"parts/04-implementation/04-adoption-roadmap.tex"
"parts/04-implementation/05-case-studies-validation.tex"
"parts/05-conclusion/01-summary.tex"
"parts/05-conclusion/02-impact.tex"
"parts/05-conclusion/03-call-to-action.tex"
"parts/05-conclusion/04-limitations-future-work.tex"
"parts/06-appendices/A-formal-proofs.tex"
"parts/06-appendices/B-implementation-specs.tex"
"parts/06-appendices/C-code-examples.tex"
"parts/06-appendices/D-technical-architecture.tex"
"backmatter/glossary.tex"
"backmatter/index.tex"
)

for file in "${files[@]}"; do
    if [ ! -f "$file" ]; then
        # Extract chapter name from filename
        filename=$(basename "$file" .tex)
        chaptername=$(echo "$filename" | sed 's/-/ /g' | sed 's/\b\(.\)/\u\1/g')
        
        # Create directory if it doesn't exist
        mkdir -p "$(dirname "$file")"
        
        # Create minimal placeholder
        cat > "$file" << ENDFILE
% ============================================================================
% LAIRM Document - $chaptername
% date_creation: 2026-04-22
% last_updated: 2026-04-22
% ============================================================================

\chapter{$chaptername}

% Content placeholder - to be developed

\section{Overview}

This section is under development.

\cleardoublepage
ENDFILE
        echo "Created: $file"
    else
        echo "Exists: $file"
    fi
done
