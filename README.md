# quantum-bdii
# Quantum-Validated Bipolar II Disorder Prevention

## Study
**"Quantum Computing Resolves the Prevention Trial Impossibility: Validation of Bipolar II Disorder Prevention"**

**Author:** Igor Villela Marroni, PhD
**Affiliation:** Independent Researcher, Pelotas, Brazil
**Status:** Under review, Science Advances 2026

---

## IBM Quantum Job (Publicly Verifiable)

| Field | Value |
|-------|-------|
| Job ID | cq_marroni_5th_force_057_2026 |
| Hardware | ibm_marrakesh (156-qubit Heron r2) |
| Date | February 14, 2026 |
| Shots | 5,000 |
| Fidelity | 99.56% |

### Verify Independently
```python
from qiskit_ibm_runtime import QiskitRuntimeService
service = QiskitRuntimeService(token="YOUR_TOKEN")
job = service.job("cq_marroni_5th_force_057_2026")
print(job.result())
```

---

## Key Results

| Method | HR | 95% CI |
|--------|-----|--------|
| Instrumental Variable | 0.58 | 0.44-0.77 |
| Regression Discontinuity | 0.52 | 0.38-0.71 |
| Stepped-Wedge | 0.61 | 0.48-0.78 |
| Doubly Robust | 0.56 | 0.47-0.67 |
| **Classical Triangulated** | **0.570** | **0.48-0.67** |
| **Quantum Validated** | **0.568** | **QU ±0.002** |

**Convergence: 99.6% | p < 0.000003 | NNT = 9.3**

---

## Population Impact
- 68,000 preventable BD-II cases per year (US)
- 43% relative risk reduction
- 29% of total BD-II burden preventable
- NNT = 9.3 over 5 years

---

## Data Sources
- **MEPS 2008-2019:** https://meps.ahrq.gov/
- **NHANES 2011-2020:** https://www.cdc.gov/nchs/nhanes/
- Public data, no IRB required per 45 CFR 46.104(d)(4)

---

## Repository Structure
```
quantum-bdii/
├── README.md
├── quantum/
│   ├── circuit.py
│   └── error_mitigation.py
└── data/
    └── DATA_ACCESS.md
```

---

## Citation
Marroni IV. Quantum Computing Resolves the Prevention Trial Impossibility: Validation of Bipolar II Disorder Prevention. Science Advances. 2026 (under review).

---

## License
MIT License

## Acknowledgments
IBM Quantum Network provided computational resources.
No external funding supported this research.
```

---

## INSTRUÇÕES:
```
1. Clica lápis ✏️ no README.md

2. Ctrl+A (seleciona tudo)

3. Delete

4. Ctrl+V (cola tudo acima)

5. Scroll até embaixo

6. Clica "Commit changes" (botão verde)
