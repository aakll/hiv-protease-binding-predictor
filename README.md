# Predicting HIV-1 Protease Binding Affinity Using Molecular Descriptors

I investigated whether molecular descriptors alone can predict the binding affinity (ΔG) of ligands to HIV-1 protease (PDB: 1HVR), aiming to assess the potential of descriptor-based machine learning models to reduce the need for computationally expensive docking simulations. I also expanded the study to analyze pharmaceutical relevance, including drug-likeness and FDA-approved drug validation, to demonstrate applications in early-stage drug discovery.

---

## Project Overview

This project implements a hypothesis-driven computational workflow combining molecular docking, descriptor-based machine learning, and drug analysis:

- **Data generation:** Docked 50 ligands to HIV-1 protease using AutoDock Vina.  
- **Feature engineering:** Collected molecular descriptors from PubChem (MW, LogP, HBD, HBA).  
- **Machine learning:** Trained a Random Forest regression model to predict binding affinities.  
- **Drug analysis:**  
  - Assessed drug-likeness using Lipinski’s Rule of Five  
  - Validated predicted top binders against FDA-approved HIV protease inhibitors  
- **Virtual screening:** Applied the model to a library of 1000 virtual compounds to prioritize potential drug candidates.  

All analyses and results are documented in the `notebooks/` folder.


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
