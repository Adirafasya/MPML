import streamlit as st
import joblib
import numpy as np

# Memuat model dari file model.pkl
model = joblib.load('model2.pkl')

# Judul aplikasi
st.title("Aplikasi Prediksi Tarif Uber")

# Deskripsi aplikasi
st.write("""
    Aplikasi ini menggunakan model Random Forest untuk mengklasifikasikan tarif Uber menjadi 'high' atau 'low'.
    Masukkan detail perjalanan untuk mendapatkan hasil prediksi.
""")

# Membuat input untuk pengguna
pickup_longitude = st.number_input("Pickup Longitude:", format="%f")
pickup_latitude = st.number_input("Pickup Latitude:", format="%f")
dropoff_longitude = st.number_input("Dropoff Longitude:", format="%f")
dropoff_latitude = st.number_input("Dropoff Latitude:", format="%f")

# Tombol untuk melakukan prediksi
if st.button("Prediksi"):
    # Membuat array input dari data yang diberikan pengguna
    input_data = np.array([[pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude]])
    
    # Melakukan prediksi menggunakan model
    prediction = model.predict(input_data)

    # Menampilkan hasil prediksi
    st.write(f"Hasil prediksi: {prediction[0]} (high: tarif tinggi, low: tarif rendah)")
