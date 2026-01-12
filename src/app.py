# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests

from pathlib import Path  

BASE_DIR = Path(__file__).resolve().parent.parent  
MODEL_DIR = BASE_DIR / "models"


# Page configuration
st.set_page_config(
    page_title="HIV Protease Binding Predictor",
    page_icon="🧬",
    layout="wide"
)

# Fetch ligand properties from PubChem
def get_ligand_properties(cid):
    """
    Fetch ligand properties from PubChem given a CID.
    Returns: MW, LogP, HBD, HBA as numeric types
    """
    try:
        url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/MolecularWeight,XLogP,HBondDonorCount,HBondAcceptorCount/JSON"
        
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        props = data['PropertyTable']['Properties'][0]
        
        return {
            'MW': float(props.get('MolecularWeight', 0)),
            'LogP': float(props.get('XLogP', 0)),
            'HBD': int(props.get('HBondDonorCount', 0)),
            'HBA': int(props.get('HBondAcceptorCount', 0)),
            'success': True
        }
    
    except requests.exceptions.RequestException as e:
        return {'success': False, 'error': f"PubChem API error: {str(e)}"}
    except Exception as e:
        return {'success': False, 'error': f"Error: {str(e)}"}

# Predict binding affinity
def predict_affinity(properties, model, scaler):
    """
    Predict binding affinity given ligand properties
    """
    features = np.array([[properties['MW'], properties['LogP'], properties['HBD'], properties['HBA']]])
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0]
    return prediction

# Main app
def main():
    st.title("🧬 HIV-1 Protease Binding Affinity Predictor")
    st.markdown("---")
    
    st.markdown("""
    ### About This Tool
    This ML tool predicts the binding affinity (ΔG) of ligands to **HIV-1 protease (1HVR)** 
    based on molecular properties, and assesses drug-likeness using Lipinski's Rule of Five. 
    This reduces the need for computationally expensive molecular docking simulations.

    **Features:**
    - 🔗 Direct PubChem integration
    - ⚡ Instant binding affinity prediction
    - 💊 Drug-likeness assessment (Lipinski's Rule of Five)
    - 🎯 Overall drug candidate evaluation

    **How to use:** Enter a PubChem Compound ID (CID) below to get predictions.
    """)
    
    st.markdown("---")
    
    # Load model
    try:
        with open(MODEL_DIR / "rf_model.pkl", "rb") as f:
            model = pickle.load(f)
        with open(MODEL_DIR / "scaler.pkl", "rb") as f:
            scaler = pickle.load(f)
    except FileNotFoundError:
        st.error("⚠️ Model files not found. Please ensure rf_model.pkl and scaler.pkl are in the models/ folder.")
        return
    
    # Input section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📥 Input")
        cid_input_raw = st.text_input(
            "Enter PubChem Compound ID (CID):",
            placeholder="e.g., 92727, 5362440, 64143",
            help="Find CIDs at https://pubchem.ncbi.nlm.nih.gov/"
        )
        cid_input = cid_input_raw.strip()
        predict_button = st.button("🔍 Predict Binding Affinity", type="primary")
    
    with col2:
        st.subheader("ℹ️ Example CIDs")
        st.markdown("""
        - **92727** (Lopinavir)
        - **5362440** (Indinavir)
        - **64143** (Nelfinavir)
        - **392622** (Ritonavir)
        """)
    
    # Prediction
    if predict_button:
        if not cid_input:
            st.warning("⚠️ Please enter a PubChem CID.")
        else:
            with st.spinner("Fetching ligand properties from PubChem..."):
                properties = get_ligand_properties(cid_input)
            
            if not properties.get('success', False):
                st.error(f"❌ {properties.get('error', 'Unknown error')}")
                st.info("💡 Make sure the CID is valid. Search at https://pubchem.ncbi.nlm.nih.gov/")
            else:
                st.success("✅ Ligand properties retrieved successfully!")
                
                st.markdown("---")
                st.subheader("📊 Ligand Properties")
                prop_col1, prop_col2, prop_col3, prop_col4 = st.columns(4)
                prop_col1.metric("Molecular Weight", f"{properties['MW']:.2f} g/mol")
                prop_col2.metric("LogP", f"{properties['LogP']:.2f}")
                prop_col3.metric("H-Bond Donors", int(properties['HBD']))
                prop_col4.metric("H-Bond Acceptors", int(properties['HBA']))

                with st.spinner("Predicting binding affinity..."):
                    delta_g = predict_affinity(properties, model, scaler)
                
                st.markdown("---")
                st.subheader("🎯 Prediction Result")
                
                if delta_g < -9:
                    color = "green"
                    strength = "Strong Binding"
                elif delta_g < -7:
                    color = "orange"
                    strength = "Moderate Binding"
                else:
                    color = "red"
                    strength = "Weak Binding"
                
                st.markdown(f"""
                <div style="padding: 20px; border-radius: 10px; background-color: {color}; color: white; text-align: center;">
                    <h2>Predicted ΔG: {delta_g:.3f} kcal/mol</h2>
                    <h3>{strength}</h3>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("---")
                st.subheader("💊 Drug-Likeness Assessment (Lipinski's Rule of Five)")
                
                violations = 0
                rules_status = []
                rules_status.append("✅ Molecular Weight ≤ 500 Da" if properties['MW'] <= 500 else "❌ Molecular Weight > 500 Da")
                violations += 1 if properties['MW'] > 500 else 0
                
                rules_status.append("✅ LogP ≤ 5" if properties['LogP'] <= 5 else "❌ LogP > 5")
                violations += 1 if properties['LogP'] > 5 else 0
                
                rules_status.append("✅ Hydrogen Bond Donors ≤ 5" if properties['HBD'] <= 5 else "❌ Hydrogen Bond Donors > 5")
                violations += 1 if properties['HBD'] > 5 else 0
                
                rules_status.append("✅ Hydrogen Bond Acceptors ≤ 10" if properties['HBA'] <= 10 else "❌ Hydrogen Bond Acceptors > 10")
                violations += 1 if properties['HBA'] > 10 else 0
                
                rule_col1, rule_col2 = st.columns(2)
                with rule_col1:
                    st.write(rules_status[0])
                    st.write(rules_status[1])
                with rule_col2:
                    st.write(rules_status[2])
                    st.write(rules_status[3])
                
                is_drug_like = violations <= 1
                if is_drug_like:
                    st.success(f"✅ **Drug-like** ({violations} violation{'s' if violations != 1 else ''})")
                    st.info("This compound has favorable properties for oral bioavailability.")
                else:
                    st.warning(f"⚠️ **Not drug-like** ({violations} violations)")
                    st.info("This compound may have poor oral bioavailability. Consider structural modifications.")
                
                st.subheader("🏆 Overall Drug Candidate Assessment")
                if delta_g < -9 and is_drug_like:
                    st.success("⭐ **Excellent Drug Candidate** - Strong binding AND drug-like properties!")
                    st.balloons()
                elif delta_g < -9 and not is_drug_like:
                    st.warning("⚠️ **Promising but needs optimization** - Strong binding but poor drug-likeness.")
                elif delta_g < -7 and is_drug_like:
                    st.info("✓ **Moderate Candidate** - Acceptable binding with good drug-like properties.")
                else:
                    st.error("❌ **Poor Candidate** - Weak binding and/or poor drug-likeness.")
                
                st.markdown("---")
                st.markdown(f"🔗 [View compound on PubChem](https://pubchem.ncbi.nlm.nih.gov/compound/{cid_input})")
    
    st.markdown("---")
    st.markdown("""                
            **Scale:**
            - **ΔG < -9**: Strong Binding
            - **ΔG < -7**: Moderate Binding
            - **ΔG > -7**: Weak Binding
                
            **More negative ΔG values indicate stronger binding affinities.**
    """)   
    st.markdown("""
    **Model Performance:**
    - Algorithm: Random Forest Regressor
    - Test R²: 0.866
    - Test RMSE: 0.892 kcal/mol
    - Test MAE: 0.721 kcal/mol
    """)
    
    st.markdown("""
    <div style="text-align: center; color: gray;">
        <p>🧬 AI-Powered Drug Discovery Tool</p>
        <p>Developed as part of bioinformatics research in drug design</p>
        <p>Model trained on 50 ligands</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
