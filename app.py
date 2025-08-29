import streamlit as st

st.title("🧮 Aplikasi Serbaguna dengan Streamlit")

menu = st.sidebar.selectbox(
    "Pilih Fitur:",
    ["Kalkulator", "Konversi Suhu", "Baris Fibonacci"]
)

# --- FITUR 1: Kalkulator ---
if menu == "Kalkulator":
    st.header("🔢 Kalkulator Sederhana")
    num1 = st.number_input("Masukkan angka pertama:", value=0.0)
    num2 = st.number_input("Masukkan angka kedua:", value=0.0)
    operator = st.selectbox("Pilih operator:", ["+", "-", "×", "÷"])
    hasil = None
    if st.button("Hitung"):
        if operator == "+": hasil = num1 + num2
        elif operator == "-": hasil = num1 - num2
        elif operator == "×": hasil = num1 * num2
        elif operator == "÷":
            hasil = num1 / num2 if num2 != 0 else "Error: Tidak bisa dibagi 0"
        st.success(f"Hasil: {hasil}")

# --- FITUR 2: Konversi Suhu ---
elif menu == "Konversi Suhu":
    st.header("🌡️ Konversi Suhu")
    satuan_awal = st.selectbox("Pilih satuan asal:", ["Celcius", "Reamur", "Fahrenheit"])
    nilai = st.number_input(f"Masukkan nilai suhu ({satuan_awal}):", value=0.0)
    if st.button("Konversi"):
        if satuan_awal == "Celcius":
            st.write(f"Reamur: {(4/5)*nilai:.2f} °R")
            st.write(f"Fahrenheit: {(9/5)*nilai+32:.2f} °F")
        elif satuan_awal == "Reamur":
            st.write(f"Celcius: {(5/4)*nilai:.2f} °C")
            st.write(f"Fahrenheit: {(9/4)*nilai+32:.2f} °F")
        elif satuan_awal == "Fahrenheit":
            st.write(f"Celcius: {(5/9)*(nilai-32):.2f} °C")
            st.write(f"Reamur: {(4/9)*(nilai-32):.2f} °R")

# --- FITUR 3: Baris Fibonacci ---
elif menu == "Baris Fibonacci":
    st.header("🔗 Deret Fibonacci")
    n = st.number_input("Masukkan jumlah bilangan (n):", min_value=1, step=1, value=5)
    if st.button("Generate"):
        fib = [0, 1]
        for i in range(2, int(n)):
            fib.append(fib[-1] + fib[-2])
        st.success(f"Deret Fibonacci hingga {n} angka:")
        st.write(fib[:int(n)])
