
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

st.title("El Escuchadero🦻")
st.subheader("¿Cómo te sientes hoy?")

modo = st.radio("Es una difícil decisión, lo sé.", ("Feliz", "Triste", "Enojado", "Preocupado", "Asustado"))
if modo == "Feliz":
    st.write("¡Que bien!😊")
    image = Image.open("feliz.png")
if modo == "Triste":
    st.write("Lo lamento mucho 😔.")
    image2 = Image.open("triste.png")
if modo == "Enojado":
    st.write("Lo lamento mucho 😔.")
    image3 = Image.open("enojado.png")
if modo == "Preocupado":
    st.write("Lo lamento mucho 😔.")
    image4 = Image.open("preocupado.png")
if modo == "Asustado":
    st.write("Lo lamento mucho 😔.")
    image5 = Image.open("asustado.png")

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






