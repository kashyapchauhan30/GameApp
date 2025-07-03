# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 2025
@author: 
"""

import streamlit as st
import numpy as np
import pickle

# Load the trained model (update path as needed)
model_path = r"D:\GameApp\gaming_model.sav"
loaded_model = pickle.load(open(model_path, 'rb'))

# Prediction function
def engagement_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data).reshape(1, -1)
    prediction = loaded_model.predict(input_data_as_numpy_array)
    
    return {0: "🟢 Low Engagement", 1: "🟡 Medium Engagement", 2: "🔴 High Engagement"}.get(prediction[0], "Unknown")

# Main Streamlit app
def main():
    st.set_page_config(page_title="🎮 Gaming Engagement Predictor", page_icon="🎮")
    st.title("🎮 Gaming Engagement Predictor")
    st.markdown("##### Enter player details to predict their expected engagement level.")

    col1, col2 = st.columns(2)

    with col1:
        PlayerID  = st.number_input("🆔 Player ID", min_value=9000, step=1)
        age = st.number_input("🎂 Age", min_value=10, max_value=100, step=1)
        gender = st.selectbox("🧑 Gender", ['Male', 'Female'])
        location = st.selectbox("🌍 Location", ['USA', 'Europe', 'Other'])
        game_genre = st.selectbox("🎮 Game Genre", ['Action', 'Strategy', 'Sports'])
        play_time = st.slider("⏱️ Play Time (Hours per week)", 0.0, 100.0, 10.0)

    with col2:
        in_game_purchases = st.selectbox("🛒 In-Game Purchases", ['No', 'Yes'])
        game_difficulty = st.selectbox("🎯 Game Difficulty", ['Easy', 'Medium', 'Hard'])
        sessions_per_week = st.slider("📆 Sessions Per Week", 1, 50, 7)
        avg_session_duration = st.slider("🕒 Avg. Session Duration (min)", 5, 300, 60)
        player_level = st.slider("📈 Player Level", 1, 100, 20)
        achievements_unlocked = st.slider("🏆 Achievements Unlocked", 0, 1000, 50)

    result = ''
    if st.button("🔍 Predict Engagement"):
        try:
            # Encode categorical fields
            gender_encoded = {'Male': 0, 'Female': 1}[gender]
            location_encoded = {'USA': 0, 'Europe': 1, 'Other': 2}[location]
            genre_encoded = {'Action': 0, 'Strategy': 1, 'Sports': 2}[game_genre]
            purchases_encoded = {'No': 0, 'Yes': 1}[in_game_purchases]
            difficulty_encoded = {'Easy': 0, 'Medium': 1, 'Hard': 2}[game_difficulty]

            # Prepare input list
            input_list = [PlayerID,
                age,
                gender_encoded,
                location_encoded,
                genre_encoded,
                play_time,
                purchases_encoded,
                difficulty_encoded,
                sessions_per_week,
                avg_session_duration,
                player_level,
                achievements_unlocked
            ]

            # Predict
            result = engagement_prediction(input_list)

        except Exception as e:
            result = f"⚠️ Error: {str(e)}"

    st.success(f"**{result}**")


if __name__ == '__main__':
    main()
