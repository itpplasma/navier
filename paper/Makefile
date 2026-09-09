.PHONY: maps documents structural check
maps:
	python3 ../tools/generate_map.py ../docs/proof-graph.yaml proof_map.tex
	python3 ../tools/generate_map.py ../docs/proof-graph.yaml ../docs/proof_map.tex

documents: maps
	$(MAKE) all clock continuation structural

structural:
	cd structural-obstructions && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

check: check-clock check-defect check-conformal check-signed check-shell check-dynamics check-material

.PHONY: all continuation clean
all: main.pdf proof_map.pdf

main.pdf: main.tex references.bib sections/dissipation_clock.tex sections/defect_extensions.tex sections/conformal_moment.tex sections/signed_defect.tex sections/speed_shell.tex sections/shell_dynamics.tex sections/material_response.tex
	latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

proof_map.pdf: proof_map.tex
	latexmk -pdf -interaction=nonstopmode -halt-on-error proof_map.tex

# Standalone candidate: not yet integrated into main.tex or the claim graph.
continuation: dissipation_budget_continuation.pdf

dissipation_budget_continuation.pdf: dissipation_budget_continuation.tex
	latexmk -pdf -interaction=nonstopmode -halt-on-error dissipation_budget_continuation.tex

clean:
	latexmk -C main.tex proof_map.tex dissipation_budget_continuation.tex

.PHONY: clock check-clock
clock: dissipation_clock.pdf

dissipation_clock.pdf: dissipation_clock.tex sections/dissipation_clock.tex
	latexmk -pdf -interaction=nonstopmode -halt-on-error dissipation_clock.tex

check-clock:
	python3 tools/check_dissipation_clock.py --integrated

.PHONY: check-defect
check-defect:
	python3 tools/check_defect_extensions.py --integrated

.PHONY: check-conformal
check-conformal:
	python3 tools/check_conformal_moment.py --integrated

.PHONY: check-signed
check-signed:
	python3 tools/check_signed_defect.py --integrated

.PHONY: check-shell
check-shell:
	python3 tools/check_speed_shell.py --integrated

.PHONY: check-dynamics
check-dynamics:
	python3 tools/check_shell_dynamics.py --integrated

.PHONY: check-material
check-material:
	python3 tools/check_material_response.py --integrated
