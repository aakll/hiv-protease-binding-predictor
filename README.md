# HIV-1 Protease Binding Affinity Predictor

An AI-powered drug discovery tool that predicts binding affinity (ΔG) of ligands to HIV-1 protease (1HVR) using machine learning. This tool enables rapid virtual screening of compound libraries, reducing computational time by 300,000× compared to traditional molecular docking.

## 🎯 Project Overview

This project demonstrates a complete AI-driven drug discovery pipeline:
- **Data Generation**: 50 ligands docked to HIV-1 protease using AutoDock Vina
- **Feature Engineering**: Molecular descriptors from PubChem (MW, LogP, HBD, HBA)
- **Machine Learning**: Random Forest regression model
- **Pharmaceutical Analysis**: Drug-likeness assessment and FDA drug validation
- **Virtual Screening**: High-throughput compound screening workflow
- **Deployment**: Interactive web application using Streamlit

## 📊 Model Performance

- **Algorithm**: Random Forest Regressor
- **Test R²**: 0.866 (86.6% variance explained)
- **Test RMSE**: 0.892 kcal/mol
- **Test MAE**: 0.721 kcal/mol
- **Validation**: Successfully identifies FDA-approved drugs as top binders

## 🚀 Features

- **ML-Powered Prediction**: Instant binding affinity prediction from ligand properties
- **Drug-Likeness Analysis**: Lipinski's Rule of Five assessment for oral bioavailability
- **FDA Drug Validation**: Validated against clinically approved HIV protease inhibitors
- **Virtual Screening**: Screen 1000+ compounds in seconds (300,000× faster than docking)
- **User-Friendly Interface**: Real-time predictions via web application
- **PubChem Integration**: Automatic property fetching from compound databases
- **Pharmaceutical Insights**: Color-coded results with drug development context

## 📁 Project Structure

```
.
├── app.py                           # Streamlit web application
├── rf_model.pkl                     # Trained Random Forest model
├── scaler.pkl                       # Feature scaler
├── requirements.txt                 # Python dependencies
├── data.csv                         # Training dataset (50 ligands)
├── eda_analysis.ipynb              # Exploratory Data Analysis
├── ml_modeling.ipynb               # Model training and evaluation
├── drug_discovery_analysis.ipynb   # Pharmaceutical context analysis
│   ├── Part 1: Drug-likeness (Lipinski's Rule)
│   ├── Part 2: FDA drug validation
│   └── Part 3: Virtual screening workflow
└── README.md                        # Documentation
```

## 🛠️ Installation & Setup

### Local Setup

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd <repo-name>
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run app.py
```

4. **Open your browser**
- The app will automatically open at `http://localhost:8501`

## 🌐 Deployment on Streamlit Cloud

1. **Push your code to GitHub**
   - Ensure all files (app.py, rf_model.pkl, scaler.pkl, requirements.txt) are committed

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Set main file path: `app.py`
   - Click "Deploy"

3. **Your app will be live!**
   - Share the URL with anyone

## 📖 How to Use

1. **Find a PubChem CID**
   - Visit [PubChem](https://pubchem.ncbi.nlm.nih.gov/)
   - Search for any compound
   - Copy the CID (Compound ID)

2. **Enter CID in the app**
   - Paste the CID into the input field
   - Click "Predict Binding Affinity"

3. **View Results**
   - Ligand properties are automatically fetched
   - Binding affinity (ΔG) is predicted
   - Results are color-coded for easy interpretation

## 🧪 Example Compounds

Try these HIV protease inhibitors:
- **92727** (Ritonavir)
- **5362440** (Darunavir)
- **64143** (Saquinavir)
- **392622** (Indinavir)

## 🔬 Model Details

### Features Used
- **MW**: Molecular Weight (g/mol) - Primary predictor (r = -0.87)
- **LogP**: Lipophilicity (partition coefficient)
- **HBD**: Hydrogen Bond Donors
- **HBA**: Hydrogen Bond Acceptors

### Training
- **Dataset**: 50 ligands docked to 1HVR with AutoDock Vina
- **Train/Test Split**: 80/20
- **Feature Scaling**: StandardScaler (z-score normalization)
- **Cross-Validation**: 5-fold CV

### Key Findings

**1. Drug-Likeness Analysis (Lipinski's Rule of Five)**
- 80% of ligands meet drug-likeness criteria
- Trade-off identified: stronger binders tend to be less drug-like
- Optimal candidates balance binding affinity AND pharmaceutical properties

**2. FDA Drug Validation**
- Model correctly identifies 3 FDA-approved HIV protease inhibitors:
  - Darunavir: Rank 4/50 (Top 8%)
  - Saquinavir: Rank 9/50 (Top 18%)
  - Ritonavir: Rank 13/50 (Top 26%)
- FDA drugs bind 2.37 kcal/mol stronger than average ligand
- **Validates model's ability to identify clinically relevant compounds**

**3. Virtual Screening Demonstration**
- Screened 1000 virtual compounds in <1 second
- Identified 133 drug candidates (13.3% hit rate)
- **300,000× faster** than traditional molecular docking
- 87% reduction in computational time
- Enables high-throughput drug discovery workflows

## 📈 Applications in Drug Discovery

This tool addresses key challenges in pharmaceutical research:

1. **Lead Identification**: Rapidly screen large compound libraries (millions of compounds)
2. **Lead Optimization**: Predict binding for structural variants without expensive simulations
3. **Virtual Library Design**: Guide synthesis of promising drug candidates
4. **Drug Repurposing**: Screen existing drugs for new therapeutic targets
5. **Cost Reduction**: Minimize expensive docking and experimental assays

### Real-World Impact
- **Traditional Approach**: Screen 1000 compounds → 83 hours computing time
- **ML Approach**: Screen 1000 compounds → <1 second → Validate top 133 with docking → 11 hours total
- **Result**: 87% time savings, same or better hit rates

## 📈 Future Work

1. **Expand Dataset**: Include diverse ligands and multiple protein targets for generalization
2. **ADME/Tox Prediction**: Integrate absorption, distribution, metabolism, excretion, and toxicity models
3. **Structure-Based Features**: Incorporate protein-ligand interaction fingerprints
4. **Deep Learning**: Explore neural networks and graph neural networks for improved accuracy
5. **Experimental Validation**: Collaborate on wet-lab testing of top predictions
6. **Multi-Target Screening**: Extend to other therapeutic targets (kinases, GPCRs, etc.)

## 🤝 Contributing

This is a research project. For questions or collaborations, please reach out.

## 📄 License

This project is for educational and research purposes.

## 👨‍🔬 Author

**Ali Kawar**  
Bioinformatics Student, Lebanese American University  
CGPA: 3.77

---

**Research Areas**: AI in Drug Discovery | Computational Biology | Machine Learning for Therapeutics
