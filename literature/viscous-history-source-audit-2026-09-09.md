# Fixed-viscosity history transfer: September 9 source audit

Research input: `itpplasma/navier@1fc5f5b1f1e6cf2ca52ae4bdbd71c8d7b7a07352`.
This is a new source-inspection record, not a new external proof audit or
kernel replication. PLAN remains the only live allocation. The manuscript
has been updated in `paper/sections/viscous_history.tex` immediately, with
the unforced target, forced input and Euler input kept distinct.

## Sources actually revisited

1. OpenAI, *Finite Time Blowup for Navier--Stokes*, September 8, 2026:
   https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf
   and https://openai.com/index/navier-stokes-solution/ .
   Main theorem and release rechecked: smooth forcing, zero datum, bounded
   energy; not the unforced research target. Preserve the existing owner
   acceptance and inherited forced kernel record. This run did not rerun Lean.
2. OpenAI, *Finite Time Blowup for the Euler Equation*:
   https://cdn.openai.com/pdf/315b36cd-ec98-4023-8342-93345194ece1/euler.pdf .
   Main theorem, particle/displacement equations, primary transverse system,
   coefficient hypotheses, asymmetric profile, frequency ordering and initial
   increments inspected. The source remains inviscid. Its auxiliary correction
   regularization does not introduce the fixed physical viscosity needed here.
   Connected prehistory and the free initial mean are genuine source features;
   do not misdescribe the construction as a sequence of externally reset Euler
   pulses. The leading transverse velocity still has to obey its actual
   positive-viscosity equation in an NS adaptation.
3. The connected GitHub read confirmed
   `openai/NavierStokesAndEuler/main` is still
   `8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538`.
   This is a revision check, not proof that the served PDF has the same bytes
   as a previously fingerprinted file, nor a new axiom report.
4. Stan Palasek, arXiv:2605.13827v1:
   https://arxiv.org/html/2605.13827v1 .
   Theorem 1.3 requires a force for the viscous variable-gap Obukhov model;
   Theorem 1.8 is an unforced inviscid MODEL. Section 1.3.2 explicitly isolates
   pre-activation damping and removes it by a force. Thus the principle that
   preparation time matters is prior art, not a novelty claim of this project.
   The cited Looi result is listed as 'to appear, 2026'; no exact theorem from
   that unpublished reference is imported. Section 4 discusses a possible PDE
   transfer, not an achieved original-NS embedding.
5. Caltech's author announcement was revisited. The linked paper/project
   endpoints failed in this retrieval. Keep the preceding source-specific
   inspection and fingerprints as HISTORICAL evidence; do not claim a fresh
   completed stability certificate. At its recorded concentration exponent
   one half, the NS relative viscosity is constant, not asymptotically zero.
6. The previously logged September one-component and directional criteria,
   the outgoing self-similarity paper arXiv:2602.17570, and the lower-regularity
   Euler abstracts arXiv:2603.10945 and arXiv:2605.15130 were revisited as leads.
   They are not imported as arbitrary smooth-data unforced NS results. This
   follow-up is targeted, not a new exhaustive census of all recent literature.

## PDF version limitation

The current Euler PDF text parser reports 57 pages, while the rendered title
page places the references on page 45; subsequent equation pagination also
bears this mismatch. Main target and displayed leading structure agree, but
page and equation numbers must not be silently mixed. A direct byte download
failed in this environment. Therefore the earlier SHA-256 in
`openai-euler-transfer-2026-09-09.md` is an INHERITED fingerprint only and is
not claimed revalidated now. The present analytic calculations must be stated
self-contained, with explicit hypotheses, rather than relying on a hidden
version-dependent coefficient. No third-party PDF is added to the repository.

## Research gate

The source bounds include the propagation factor g(t)/g(s). A polynomial
coefficient bound is NOT a polynomial total transverse-gain bound. Viscous
comparisons must retain the actual propagator or derive their own energy
bound. Pressure-only displacement coercivity must likewise be recomputed
with viscosity, not inferred from F_tt=-HF. The immediate mathematical test is
the full preparation history at fixed viscosity, followed by an actual NS
mean/displacement identity. Neither a ray system nor a scalar model may be
promoted to a full nonlinear Cauchy realization.

Independent mathematical audit: none obtained in this update. Novelty: not
certified. Source inspection and executable checks have their stated narrower
scopes. No canonical graph or formal status changes.
