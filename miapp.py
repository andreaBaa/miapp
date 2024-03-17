
import os
import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
from PIL import Image
import time
import glob

from gtts import gTTS
from googletrans import Translator

spoken_text = None


# Cargar las imágenes
image_feliz = Image.open("feliz.png")
image_triste = Image.open("triste.png")
image_enojado = Image.open("enojado.png")
image_preocupado = Image.open("preocupado.png")
image_asustado = Image.open("asustado.png")

# Cambiar el tamaño de las imágenes
width, height = 200, 200  # Tamaño deseado de las imágenes

image_feliz_resized = image_feliz.resize((width, height))
image_triste_resized = image_triste.resize((width, height))
image_enojado_resized = image_enojado.resize((width, height))
image_preocupado_resized = image_preocupado.resize((width, height))
image_asustado_resized = image_asustado.resize((width, height))


st.title("El Escuchadero🦻")
st.subheader("¿Cómo te sientes hoy?")

width, height = 200, 200

modo = st.radio("Es una difícil decisión, lo sé.", ("Feliz", "Triste", "Enojado", "Preocupado", "Asustado"))
if modo == "Feliz":
    st.write("¡Que bien!😊")
    st.image(image_feliz_resized)
if modo == "Triste":
    st.write("Lo lamento mucho 😔.")
    st.image(image_triste_resized)
if modo == "Enojado":
    st.write("Lo lamento mucho 😔.")
    st.image(image_enojado_resized)
if modo == "Preocupado":
    st.write("Lo lamento mucho 😔.")
    st.image(image_preocupado_resized)
if modo == "Asustado":
    st.write("Lo lamento mucho 😔.")
    st.image(image_asustado_resized)

# AUDIO A TEXTO
stt_button = Button(label=" COMENZAR ", width=200)

st.subheader("Cuéntame más sobre cómo te sientes")
st.write("Apenas hundas sobre el botón, comienza a hablar:")

stt_button.js_on_event("button_click", CustomJS(code="""
    var recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
 
    recognition.onresult = function (e) {
        var value = "";
        for (var i = e.resultIndex; i < e.results.length; ++i) {
            if (e.results[i].isFinal) {
                value += e.results[i][0].transcript;
            }
        }
        if ( value != "") {
            document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: value}));
        }
    }
    recognition.start();
    """))

result = streamlit_bokeh_events(
    stt_button,
    events="GET_TEXT",
    key="listen",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0)

if result:
    if "GET_TEXT" in result:
        spoken_text = result.get("GET_TEXT")
        st.write(f"Esto es lo que me dijiste que sientes: {spoken_text}")



#RECONOCIMIENTO DE EMOCIONES
from textblob import TextBlob
import streamlit as st

st.subheader("**Este es el sentimiento que percibo de tus palabras:**")

if spoken_text:
    blob = TextBlob(spoken_text)
    st.write('Polarity: ', round(blob.sentiment.polarity,2))
    st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
    x = round(blob.sentiment.polarity,2)
    if x >= 0.5:
        st.write( 'Es un sentimiento Positivo 😊')
    elif x <= -0.5:
        st.write( 'Es un sentimiento Negativo 😔')
    else:
        st.write( 'Es un sentimiento Neutral 😐')


#RECOMENDACIÓN
st.subheader("La recomendación que te doy es: ")
if modo == "Feliz":
    image6 = Image.open("feliz.jpg")
    st.image(image6)
if modo == "Triste":
    image7 = Image.open("triste.jpg")
    st.image(image7)
if modo == "Enojado":
    image8 = Image.open("enojo.jpg")
    st.image(image8)
if modo == "Preocupado":
    image9 = Image.open("preocupado.jpg")
    st.image(image9)
if modo == "Asustado":
    image10 = Image.open("miedo.jpg")
    st.image(image10)







