#Library
import streamlit as st

#dictionary
dictPh = {
    'Merah': 'Asam Kuat',
    'Jingga': 'Asam Lemah',
    'Kuning': 'Asam Sangat Lemah',
    'Hijau': 'Netral',
    'Biru': 'Basa Sangat Lemah',
    'Ungu': 'Basa Lemah',
    'Violet': 'Basa Kuat'
}

# input dari user
pH = st.number_input("Masukkan nilai pH nya: ")
st.write('pH nya adalah ', pH)

#hasil
def output():

    if pH < 1 or pH > 14:
        st.write("Nilai Ph tidak valid, silahkan masukkan angka mulai dari 1-14")

    elif pH >= 1 and pH <= 3:
        st.write("Nilai Ph memiliki sifat" + dictPh["Merah"], 'dengan warna Merah')

    elif pH >= 3 and pH <= 5:
        st.write("Nilai Ph memiliki sifat " + dictPh["Jingga"], 'dengan warna Jingga')

    elif pH >= 5 and pH <= 6:
        st.write("Nilai Ph memiliki sifat " + dictPh["Kuning"], 'dengan warna Kuning')
    
    elif pH >= 6 and pH <= 7:
        st.write("Nilai Ph memiliki sifat " + dictPh["Hijau"], 'dengan warna Hijau')
    
    elif pH >= 7 and pH <= 8:
        st.write("Nilai Ph memiliki sifat " + dictPh["Biru"], 'dengan warna Biru')
    
    elif pH >= 8 and pH <= 10:
        st.write("Nilai Ph memiliki sifat " + dictPh["Ungu"], 'dengan warna Ungu')
    
    elif pH >= 10 and pH <= 14:
        st.write("Nilai Ph memiliki sifat " + dictPh["Violet"], 'dengan warna Violet')

#output
output()

#kalkulator pH
