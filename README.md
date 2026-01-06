# HIV-1 Protease Binding Affinity Predictor

Machine-learning–based framework for predicting protein–ligand binding affinity (ΔG) to HIV-1 protease (PDB: 1HVR), designed to accelerate virtual screening in early-stage drug discovery.

---

## Project Overview

This project implements an end-to-end computational drug discovery workflow combining molecular docking, cheminformatics, and supervised machine learning.

The model is intended as a **high-throughput pre-screening tool** to prioritize compounds for subsequent docking or experimental validation.

---

## Methodology

### Data Generation
- 50 ligands docked to HIV-1 protease using AutoDock Vina
- Binding affinity (ΔG) used as regression target

### Feature Engineering
- Molecular descriptors retrieved from PubChem:
  - Molecular Weight (MW)
  - LogP
  - Hydrogen Bond Donors (HBD)
  - Hydrogen Bond Acceptors (HBA)

### Machine Learning
- Model: Random Forest Regressor
- Train/Test split: 80/20
- Feature scaling: StandardScaler
- Cross-validation: 5-fold CV

---

## Model Performance

| Metric | Value |
|------|------|
| R² (test) | 0.866 |
| RMSE | 0.892 kcal/mol |
| MAE | 0.721 kcal/mol |

The model successfully ranks FDA-approved HIV protease inhibitors among top predicted binders, supporting its relevance for drug discovery prioritization.

---

## Repository Structure

```text
├── data/               # Raw datasets
├── notebooks/          # EDA, modeling, and analysis
├── src/                # Application
├── models/             # Trained model and scaler
├── results/            # Figures 
└── requirements.txt
```
---
## Virtual Screening Application

A Streamlit-based web application enables:

 - Real-time binding affinity prediction
 - Automated PubChem property retrieval
 - Drug-likeness (Lipinski) assessment
 - Visual prioritization of candidate compounds
---
## Run locally
``` bash
pip install -r requirements.txt
streamlit run src/app.py
```
---
## Key Findings

  - Strong negative correlation between molecular weight and binding affinity (r ≈ −0.87)
  - FDA-approved HIV protease inhibitors ranked within the top quartile
  - ML-based screening reduces the number of compounds requiring docking by >85%
---
## Applications

  - Virtual screening and lead prioritization
  - Drug repurposing
  - Computational cost reduction in early-stage discovery
---

## Limitations and Future Work

  - Expand dataset size and chemical diversity: Include multiple protein targets for generalization
  - Integrate structure-based interaction features
  - Incorporate ADME/Toxicity prediction
  - Experimental validation of top-ranked candidates
---

 ## Author

   **Ali Kawar**  
   Bioinformatics Student, Lebanese American University  
   Research interests: Machine Learning for Drug Discovery, Computational Biology
