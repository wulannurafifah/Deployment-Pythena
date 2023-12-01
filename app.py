import streamlit as st
from PIL import Image
import os
import cv2
import shutil
from roboflow import Roboflow

# Streamlit app
st.title("Health and Safety PPE Detection app by Pythena")

st.markdown(
    """
    <style>
        .sidebar-button {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar
if st.sidebar.button("Nama Anggota",key="button1", on_click=None, args=None):
    st.write("Kelompok Kami Beranggotakan:")
    st.markdown(
    '''
    1. Priskila Dwi Nilam Sari
    2. Wulan Nur Afifah
    3. Qatrunnada Salsabila
    4. Khofifah Hidayatullah
    5. Ratu Nur Rozi Sekar Wungu
    6. Evan Hendy Aripranaja
    '''
    )

if st.sidebar.button("Tujuan", key="button2", on_click=None, args=None):
    st.write("Tujuan :")
    st.markdown(
    '''
    1. Memastikan bahwa pekerja menggunakan peralatan perlindungan diri (PPE) dengan benar 
       untuk mengurangi risiko cedera dan kecelakaan kerja.
    2. Memberikan kemampuan untuk mendeteksi keberadaan atau ketidakberadaan PPE secara cepat
       dan akurat melalui analisis gambar.
    3. Memungkinkan perusahaan atau individu untuk melakukan inspeksi mandiri terhadap penggunaan 
       PPE tanpa memerlukan kehadiran petugas keamanan secara fisik.
    4. Mengurangi waktu dan upaya yang diperlukan untuk inspeksi manual PPE dengan memberikan solusi 
       otomatis melalui teknologi deteksi gambar.
    '''
    )

if st.sidebar.button("Contoh Gambar", key="button3", on_click=None, args=None):
    st.write("Berikut adalah contoh gambar sebelum dan sesudah dideteksi")
    # Ganti dengan URL gambar yang telah Anda dapatkan dari Google Drive
    image_url_before1 = "https://drive.google.com/uc?id=1qBgwvF2-80OCaoYLaxDqwyh0HvY_-gqG"
    image_url_before2 = "https://drive.google.com/uc?id=1oljv9N-jk6MLpgyRCPIzcpsWVwTBl0jF"
    image_url_before3 = "https://drive.google.com/uc?id=1Mdq0_7TJ118z1nD_VSmgReMD5yC_WNdH"
    image_url_before4 = "https://drive.google.com/uc?id=1ZosVJfwaa1IybVFGcckHk40sbP3tjxp3"
    image_url_after1 = "https://drive.google.com/uc?id=1Z5Kynjcm3906REltlyW7O5lVSjOWzUYq"
    image_url_after2 = "https://drive.google.com/uc?id=1JD92viuadu_LElttGC1gZd-CtEx7qjDw"
    image_url_after3 = "https://drive.google.com/uc?id=124Jex8J-a1a6RsYzyr-ncdQOhsvhGzPp"
    image_url_after4 = "https://drive.google.com/uc?id=178xQq_WUV4-EdfFdT6zJzrW5Urk-T1lP"

    # Menampilkan gambar dalam format 4 kolom dan 2 baris
    col1, col2, col3, col4 = st.columns(4)

    # Baris pertama (sebelum diprediksi)
    with col1:
        st.image(image_url_before1, caption='Gambar 1 Sebelum dideteksi', use_column_width=True)

    # Baris kedua (sebelum diprediksi)
    with col2:
        st.image(image_url_before2, caption='Gambar 2 Sebelum dideteksi', use_column_width=True)
    
    # Baris ketiga (sebelum diprediksi)
    with col3:
        st.image(image_url_before3, caption='Gambar 3 Sebelum dideteksi', use_column_width=True)

    # Baris keempat (sebelum diprediksi)
    with col4:
        st.image(image_url_before4, caption='Gambar 4 Sebelum dideteksi', use_column_width=True)

    # Baris pertama (setelah diprediksi)
    with col1:
        st.image(image_url_after1, caption='Gambar 1 Setelah dideteksi', use_column_width=True)

    # Baris kedua (setelah diprediksi)
    with col2:
        st.image(image_url_after2, caption='Gambar 2 Setelah dideteksi', use_column_width=True)
    
    # Baris ketiga (setelah diprediksi)
    with col3:
        st.image(image_url_after3, caption='Gambar 3 Setelah dideteksi', use_column_width=True)
    
    # Baris keempat (setelah diprediksi)
    with col4:
        st.image(image_url_after4, caption='Gambar 4 Setelah dideteksi', use_column_width=True)


if st.sidebar.button("Latar Belakang", key="button4", on_click=None, args=None):
    st.write("Latar Belakang dari Aplikasi ini adalah sebagai berikut")
    st.markdown(
    """
    Dalam perusahaan konstruksi dengan ratusan pekerja, masalah ketidakpatuhan PPE terus berlanjut, 
    mengancam keselamatan dan kesejahteraan karyawan. Meskipun ada kebijakan yang jelas, tantangan 
    dalam memastikan kepatuhan penuh di antara pekerja berpotensi menimbulkan kecelakaan, cedera, 
    denda, masalah hukum, dan kerusakan reputasi perusahaan. Jika sebuah industri mengalami kerugian 
    ditiap bulannya, yaitu setiap per bulan ada sekitar 4 pekerja yang mengalami cidera karena tidak 
    mematuhi PPE atau prosedure kerja yang diberikan, dan dalam contruction tersebut ada 500 pekerja 
    yang berkerja di masing-masing bidangnya. 
    Solusi yang kami usulkan adalah mengembangkan atau mengimplementasikan sebuah sistem perangkat lunak 
    yang memiliki kemampuan untuk secara akurat melacak penggunaan Personal Protective Equipment (PPE) 
    oleh seluruh pekerja dalam suatu lingkungan kerja. Pendekatan yang akan kami gunakan dalam pengembangan 
    sistem ini adalah dengan memanfaatkan teknologi computer vision, yang merupakan cabang dari kecerdasan 
    buatan yang memungkinkan komputer untuk mengenali dan menganalisis objek dalam gambar
    """
    )
# Set up Roboflow API key
roboflow_api_key = "clQem65ckvHSrRU3g25x"
rf = Roboflow(api_key=roboflow_api_key)

# Set up Roboflow project
project_name = "pythenaai5g-project"
project = rf.workspace().project(project_name)

# Set up Roboflow model
model_version = 1
model = project.version(model_version).model

st.markdown(""" Masukkan gambar yang ingin dideteksi!""")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Function to perform prediction
def predict_image(image):
    # Simpan gambar yang diunggah secara lokal
    image_path = "uploaded_image.jpg"
    image.save(image_path)

    # Lakukan prediksi menggunakan model Roboflow
    prediction_response = model.predict(image_path).json()

    # Simpan gambar prediksi
    prediction_image_path = "prediction.jpg"
    model.predict(image_path).save(prediction_image_path)

    # Tampilkan gambar prediksi
    st.image(prediction_image_path, caption='Gambar Setelah Dideteksi', use_column_width=True)

# Make prediction if file is uploaded
if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Gambar sebelum Dideteksi.', use_column_width=True)

    # Perform prediction
    predict_image(image)