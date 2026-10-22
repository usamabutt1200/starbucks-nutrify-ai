import streamlit as st
import joblib
import pandas as pd

# Load the multi-output nutrition regressor model
model = joblib.load('starbucks_nutrify_model.pkl')

st.title("☕ Starbucks Nutrify AI — Macro Predictor")
st.write("Input the baseline content of your beverage to evaluate exact structural macros:")

# UI Input Fields for User (Features)
total_fat = st.slider("Total Fat (grams)", 0, 30, 8)
trans_fat = st.slider("Trans Fat (grams)", 0.0, 5.0, 0.2)
cholesterol = st.number_input("Cholesterol Level (mg)", 0, 150, 25)
sodium = st.number_input("Sodium Content (mg)", 0, 500, 95)
protein = st.slider("Protein Content (grams)", 0, 30, 5)

# Formatting data variables correctly
input_data = pd.DataFrame([{
    'total_fat_g': total_fat,
    'trans_fat_g': trans_fat,
    'cholesterol_mg': cholesterol,
    'sodium_mg': sodium,
    'protein_g': protein
}])

# Diagnosis Button with Pure English Outputs
if st.button("Calculate Beverage Macros"):
    prediction = model.predict(input_data)
    
    # Extracting values from the multi-output prediction list
    pred_calories = prediction[0][0]
    pred_sugars = prediction[0][1]
    pred_carbs = prediction[0][2]
    
    st.markdown("### 📊 Predicted Nutritional Values:")
    st.info(f"🔥 **Calories:** {pred_calories:.1f} kcal")
    st.success(f"🍬 **Sugars:** {pred_sugars:.1f} grams")
    st.warning(f"🍞 **Total Carbohydrates:** {pred_carbs:.1f} grams")
