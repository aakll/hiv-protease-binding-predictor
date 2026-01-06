import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests

# Page configuration
st.set_page_config(
    page_title="HIV Protease Binding Predictor",
    page_icon="🧬",
    layout="wide"
)

# Load model and scaler
@st.cache_resource
def load_model():
    with open('rf_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    return model, scaler

# Fetch ligand properties from PubChem
def get_ligand_properties(cid):
    """
    Fetch ligand properties from PubChem given a CID.
    Returns: MW, LogP, HBD, HBA
    """
    try:
        url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/MolecularWeight,XLogP,HBondDonorCount,HBondAcceptorCount/JSON"
        
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        props = data['PropertyTable']['Properties'][0]
        
        return {
            'MW': props.get('MolecularWeight'),
            'LogP': props.get('XLogP'),
            'HBD': props.get('HBondDonorCount'),
            'HBA': props.get('HBondAcceptorCount'),
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
    # Create feature array in correct order
    features = np.array([[
        properties['MW'],
        properties['LogP'],
        properties['HBD'],
        properties['HBA']
    ]])
    
    # Scale features
    features_scaled = scaler.transform(features)
    
    # Predict
    prediction = model.predict(features_scaled)[0]
    
    return prediction

# Main app
def main():
    st.title("🧬 HIV-1 Protease Binding Affinity Predictor")
    st.markdown("---")
    
    # Description
    st.markdown("""
    ### About This Tool
    This machine learning model predicts the binding affinity (ΔG) of ligands to **HIV-1 protease (1HVR)** 
    based solely on molecular properties, eliminating the need for computationally expensive molecular docking simulations.
    
    **Model Performance:**
    - Algorithm: Random Forest Regressor
    - Test R²: 0.866
    - Test RMSE: 0.892 kcal/mol
    - Test MAE: 0.721 kcal/mol
    
    **How to use:** Enter a PubChem Compound ID (CID) below to predict binding affinity.
    """)
    
    st.markdown("---")
    
    # Load model
    try:
        model, scaler = load_model()
    except FileNotFoundError:
        st.error("⚠️ Model files not found. Please ensure rf_model.pkl and scaler.pkl are in the same directory.")
        return
    
    # Input section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📥 Input")
        cid_input = st.text_input(
            "Enter PubChem Compound ID (CID):",
            placeholder="e.g., 92727, 5362440, 64143",
            help="Find CIDs at https://pubchem.ncbi.nlm.nih.gov/"
        )
        
        predict_button = st.button("🔍 Predict Binding Affinity", type="primary")
    
    with col2:
        st.subheader("ℹ️ Example CIDs")
        st.markdown("""
        - **92727** (Ritonavir)
        - **5362440** (Darunavir)
        - **64143** (Saquinavir)
        - **392622** (Indinavir)
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
                # Display properties
                st.success("✅ Ligand properties retrieved successfully!")
                
                st.markdown("---")
                st.subheader("📊 Ligand Properties")
                
                prop_col1, prop_col2, prop_col3, prop_col4 = st.columns(4)
                
                with prop_col1:
                    st.metric("Molecular Weight", f"{properties['MW']:.2f} g/mol")
                
                with prop_col2:
                    st.metric("LogP", f"{properties['LogP']:.2f}")
                
                with prop_col3:
                    st.metric("H-Bond Donors", int(properties['HBD']))
                
                with prop_col4:
                    st.metric("H-Bond Acceptors", int(properties['HBA']))
                
                # Make prediction
                with st.spinner("Predicting binding affinity..."):
                    delta_g = predict_affinity(properties, model, scaler)
                
                st.markdown("---")
                st.subheader("🎯 Prediction Result")
                
                # Display prediction with color coding
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
                st.markdown("""
                **Interpretation:**
                - **ΔG < -9 kcal/mol**: Strong binding (high affinity)
                - **-9 < ΔG < -7 kcal/mol**: Moderate binding
                - **ΔG > -7 kcal/mol**: Weak binding (low affinity)
                
                *Note: More negative ΔG values indicate stronger binding.*
                """)
                
                # Show PubChem link
                st.markdown(f"🔗 [View compound on PubChem](https://pubchem.ncbi.nlm.nih.gov/compound/{cid_input})")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: gray;">
        <p>Developed as part of a bioinformatics research project</p>
        <p>Model trained on 50 ligands docked to HIV-1 protease (1HVR)</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
