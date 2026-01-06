# HIV-1 Protease Binding Affinity Predictor

A machine learning web application that predicts the binding affinity (ΔG) of ligands to HIV-1 protease (1HVR) based on molecular properties, eliminating the need for computationally expensive molecular docking simulations.

## 🎯 Project Overview

This project demonstrates an end-to-end machine learning workflow for drug discovery:
- **Data Generation**: 50 ligands docked to HIV-1 protease using AutoDock Vina
- **Feature Engineering**: Extracted molecular properties from PubChem
- **Model Development**: Random Forest regression model
- **Deployment**: Interactive web application using Streamlit

## 📊 Model Performance

- **Algorithm**: Random Forest Regressor
- **Test R²**: 0.866
- **Test RMSE**: 0.892 kcal/mol
- **Test MAE**: 0.721 kcal/mol

## 🚀 Features

- Real-time prediction of binding affinity
- Automatic fetching of ligand properties from PubChem API
- User-friendly interface
- Color-coded prediction results
- Direct links to PubChem compound pages

## 📁 Project Structure

```
.
├── app.py                  # Streamlit web application
├── rf_model.pkl           # Trained Random Forest model
├── scaler.pkl             # Feature scaler
├── requirements.txt       # Python dependencies
├── data.csv              # Training dataset
├── eda_analysis.ipynb    # Exploratory Data Analysis
├── ml_modeling.ipynb     # Model training notebook
└── README.md             # This file
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
- **MW**: Molecular Weight (g/mol)
- **LogP**: Lipophilicity (partition coefficient)
- **HBD**: Hydrogen Bond Donors
- **HBA**: Hydrogen Bond Acceptors

### Training
- Dataset: 50 ligands docked to 1HVR
- Train/Test Split: 80/20
- Feature Scaling: StandardScaler
- Cross-validation: 5-fold CV

## 🔬 Key Findings

1. **Molecular properties alone can predict binding affinity with good accuracy** (R² = 0.866)
2. **Model eliminates need for computationally expensive docking simulations** - predictions in seconds vs hours
3. **Can be used for rapid screening of large ligand libraries** before committing to full docking studies
4. **Molecular Weight (MW) is the strongest predictor** of binding affinity to HIV-1 protease

## 📈 Future Work

1. Expand dataset with more diverse ligands
2. Include multiple protein targets for generalization
3. Explore deep learning approaches
4. Validate predictions with experimental binding data
5. Add batch prediction functionality

## 🤝 Contributing

This is a research project. For questions or collaborations, please reach out.

## 📄 License

This project is for educational and research purposes.

## 👨‍🔬 Author

**Ali Kawar**  
Bioinformatics Student, Lebanese American University  
