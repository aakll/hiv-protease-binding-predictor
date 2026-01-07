# Descriptor-Based Prediction of Ligand Binding Affinity for HIV-1 Protease: Applications in Early Drug Discovery

This project investigates whether ligand molecular descriptors alone can predict the binding affinity (ΔG) to HIV-1 protease (PDB: 1HVR), aiming to assess the potential of descriptor-based machine learning models as a fast-screening tool to reduce the need for computationally expensive docking simulations. The study is further extended to assess pharmaceutical relevance, including drug-likeness and FDA-approved drug validation, to demonstrate the model's applications in early-stage drug discovery.

---

## Project Overview

This project implements a hypothesis-driven computational workflow combining molecular docking, descriptor-based machine learning, and drug analysis:

- **Data generation:** Docked 50 ligands to HIV-1 protease using AutoDock Vina.  
- **Feature engineering:** Collected molecular descriptors from PubChem (MW, LogP, HBD, HBA) for ligands.  
- **Machine learning:** Trained a Random Forest regression model to predict binding affinities.  
- **Drug analysis:**  
  - Assessed drug-likeness using Lipinski’s Rule of Five
  - validate my model by showing its ability to identify clinically relevant compounds (FDA-approved drugs rank in TOP 26% of all ligands).
- **Virtual screening:** Applied the model to a library of 1000 virtual compounds to show the model's potential in a real drug discovery pipeline.

All analyses and results are documented in the `notebooks/` folder.

---
## Research Question

Can molecular descriptors alone reliably predict protein–ligand binding affinity, and can this approach guide early-stage drug discovery by prioritizing potential drug candidates?

---
## Model Performance

| Metric        | Value            |
|---------------|----------------|
| R² (test)     | 0.866          |
| RMSE          | 0.891 kcal/mol |
| MAE           | 0.720 kcal/mol |

The model demonstrates that molecular descriptors can capture substantial variance in docking-derived binding affinities, supporting their predictive utility for ligand prioritization.

---

## Interactive Application

**Streamlit App:** https://hiv-protease-binding-predictor-kkdxazvsay5w74pckvf9ik.streamlit.app/

I developed a Streamlit application to demonstrate model predictions and ability to prioritize potential drug candidates:

- Automatically fetches molecular descriptors of ligands from PubChem 
- Predicts binding affinity for input compounds  
- Provides drug-likeness assessment and color-coded results  
- Guides users to focus on high-priority compounds for further docking or experimental testing
   
This workflow emphasizes hypothesis testing, model evaluation, and practical application in drug discovery.

---
## Repository Structure

```text
├── data/               # Raw datasets  
│   └── raw/
├── models/             # Trained model and scaler  
├── notebooks/          # Analysis and modeling notebooks
├── results/            # Figures, plots, and tables 
├── src/                # Streamlit app 
├── README.md 
├── requirements.txt    # Python dependencies  
└── runtime.txt         # For Streamlit cloud  
```
---
## Sustainable Development Goals Alignment

This project contributes to **SDG 3: Good Health and Well-being** (Target 3.3: End epidemics of AIDS, tuberculosis, malaria by 2030) by accelerating HIV drug discovery through AI-powered virtual screening. By reducing computational time by and enabling rapid identification of potential protease inhibitors, this approach can decrease drug development costs and timelines, ultimately improving access to affordable HIV treatments globally.

---
## Limitations and Future Work

  - Dataset is limited to 50 ligands and a single protein (1HVR)
  - Molecular descriptors do not include structural or interaction-based features
  - Future work could expand to multiple proteins, larger chemical libraries, and integrate ADME/Tox predictions or deep learning models
  - Experimental validation is needed to confirm predictive utility

---
## Author

Ali Kawar  
Bioinformatics Student, Lebanese American University  
Research interests: Machine Learning for Drug Discovery, Computational Biology
