import streamlit as st
import joblib
import numpy as np

# Memuat model dari file model2.pkl
try:
    model = joblib.load('model2.pkl')
    st.write("Model berhasil dimuat!")
except FileNotFoundError:
    st.error("File model 'model2.pkl' tidak ditemukan. Pastikan file tersebut ada di direktori yang benar.")
    model = None
except Exception as e:
    st.error(f"Terjadi kesalahan saat memuat model: {e}")
    model = None

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
    if model is not None:
        # Membuat array input dari data yang diberikan pengguna
        input_data = np.array([[pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude]])
        
        # Melakukan prediksi menggunakan model
        try:
            prediction = model.predict(input_data)
            # Menampilkan hasil prediksi
            st.write(f"Hasil prediksi: {prediction[0]} (high: tarif tinggi, low: tarif rendah)")
        except Exception as e:
            st.error(f"Terjadi kesalahan saat melakukan prediksi: {e}")
    else:
        st.error("Model tidak tersedia. Tidak bisa melakukan prediksi.")

