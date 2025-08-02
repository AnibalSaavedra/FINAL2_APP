
# -*- coding: utf-8 -*-
# SISTEMA UNIFICADO: MBI 360° - RITUAL (app.py)
# Autor: Aníbal Saavedra

import streamlit as st

# ---- MODULO: Disociación o Trauma ----
def ejecutar_test_disociacion():
    st.title("🌀 MBI 360° – Módulo 1: Test de Disociación o Trauma")
    st.markdown("Evalúa tu nivel de desconexión emocional y fragmentación del yo. Responde con sinceridad.")

    preguntas = [
        "Siento que a veces observo mi vida como si fuera una película.",
        "Pierdo la noción del tiempo con frecuencia.",
        "Me cuesta recordar etapas de mi infancia o adolescencia.",
        "Siento que una parte de mí se ha apagado emocionalmente.",
        "Tengo conductas que no logro controlar y no sé por qué las hago."
    ]

    respuestas = []
    for i, pregunta in enumerate(preguntas):
        col1, col2 = st.columns([4, 1])
        with col1:
            r = st.radio(pregunta, ["Nunca", "A veces", "Frecuentemente", "Casi siempre"], key=f"dis_{i}")
        with col2:
            with st.expander("❓"):
                st.caption("Esta afirmación evalúa la percepción de separación entre tu conciencia y tus acciones o emociones.")
        respuestas.append(r)

    if st.button("✅ Finalizar evaluación de disociación"):
        st.success("Gracias por completar este módulo. Tus respuestas han sido registradas.")

# ---- MODULO: Epigenético Emocional ----
def ejecutar_test_epigenetico():
    st.title("🧬 MBI 360° – Módulo 2: Estado Epigenético Emocional")
    st.markdown("Explora las huellas emocionales heredadas de tu linaje materno y paterno.")

    lineas = {
        "Línea Materna": [
            ("Siento que debo cuidar o proteger a todos.", "Puede provenir de mujeres cuidadoras o sacrificadas en tu linaje."),
            ("Me cuesta poner límites, incluso si me hacen daño.", "Podría reflejar patrones de sumisión heredados."),
            ("Siento culpa al priorizarme.", "La autoexigencia puede estar epigenéticamente reforzada.")
        ],
        "Línea Paterna": [
            ("Siento que debo ser fuerte y no mostrar emociones.", "Puede ser eco de hombres fríos o ausentes en tu historia."),
            ("Tengo miedo al fracaso o a decepcionar.", "La presión por el logro puede venir de exigencias masculinas anteriores."),
            ("Me cuesta confiar o mostrar vulnerabilidad.", "El rechazo a la emocionalidad puede ser aprendido desde generaciones pasadas.")
        ]
    }

    for linea, items in lineas.items():
        st.subheader(f"🔹 {linea}")
        for idx, (texto, explicacion) in enumerate(items):
            col1, col2 = st.columns([4, 1])
            with col1:
                st.slider(texto, 1, 3, key=f"{linea}_{idx}")
            with col2:
                with st.expander("❓"):
                    st.caption(explicacion)

    if st.button("✅ Finalizar evaluación epigenética"):
        st.success("Tus respuestas han sido registradas.")

# ---- MODULO: Condiciones Clínicas ----
def ejecutar_test_condiciones_clinicas():
    st.title("🧬 MBI 360° – Módulo 3: Condiciones Clínicas Opcionales")
    st.markdown("Evalúa tu estado físico a través de síntomas relacionados con metabolismo, digestión, inflamación, hormonas, inmunidad y salud neuropsicológica.")
    st.markdown("Responde cada afirmación del 1 (nada) al 3 (mucho). Puedes presionar ❓ para entender mejor cada afirmación.")

    afirmaciones = {
        "Metabolismo": [
            ("Siento cansancio excesivo incluso después de dormir.", "Podrías tener un metabolismo lento o desequilibrio energético celular."),
            ("Mi peso varía fácilmente sin causa aparente.", "El metabolismo alterado influye en la regulación de peso corporal."),
            ("Me cuesta mantenerme activo o motivado físicamente.", "Una baja eficiencia metabólica puede reducir tu energía.")
        ],
        "Digestión": [
            ("Frecuentemente tengo hinchazón o gases después de comer.", "Puede deberse a una mala digestión o disbiosis intestinal."),
            ("Sufro de estreñimiento o diarrea de forma regular.", "Puede ser por estrés o alimentos inflamatorios."),
            ("Siento pesadez o lentitud mental luego de las comidas.", "Tu cuerpo puede estar sobrecargado procesando alimentos.")
        ],
        "Inflamación": [
            ("Siento dolor muscular o articular sin haberme exigido físicamente.", "Puede indicar inflamación crónica en tejidos blandos."),
            ("Mi piel suele enrojecerse, picar o tener brotes.", "Las inflamaciones internas a menudo se manifiestan en la piel."),
            ("Retengo líquidos o me hincho con facilidad.", "Un sistema inflamado tiende a acumular líquidos.")
        ],
        "Salud Hormonal": [
            ("Mis cambios de humor son intensos o impredecibles.", "Las hormonas influyen directamente en el equilibrio emocional."),
            ("Siento disminución del deseo sexual sin causa aparente.", "Puede estar relacionado con un desequilibrio hormonal."),
            ("Mis ciclos menstruales o patrones hormonales son irregulares.", "Puede ser señal de desregulación endocrina.")
        ],
        "Inmunidad": [
            ("Me enfermo con frecuencia (resfríos, virus, etc.).", "Tu sistema inmune podría estar debilitado."),
            ("Tardo más tiempo del habitual en recuperarme de enfermedades.", "Una inmunidad baja puede dificultar la recuperación."),
            ("Siento fatiga inmune (como si estuviera siempre en modo alerta).", "Tu sistema inmune puede estar hiperactivo.")
        ],
        "Neuropsicológicos": [
            ("Tengo problemas de memoria o concentración frecuentes.", "Tu sistema nervioso puede estar afectado por estrés o inflamación."),
            ("Siento ansiedad o nerviosismo constante.", "Refleja desregulación del sistema nervioso autónomo."),
            ("Me cuesta mantener el ánimo estable durante el día.", "Puede haber desequilibrio entre neurotransmisores y hormonas.")
        ]
    }

    for categoria, items in afirmaciones.items():
        st.subheader(f"🔹 {categoria}")
        for idx, (texto, explicacion) in enumerate(items):
            col1, col2 = st.columns([4, 1])
            with col1:
                st.radio(texto, [1, 2, 3], key=f"{categoria}_{idx}")
            with col2:
                with st.expander("❓"):
                    st.caption(explicacion)

    if st.button("✅ Finalizar evaluación"):
        st.success("Tus respuestas han sido registradas.")

# ---- APP PRINCIPAL ----
st.set_page_config(page_title="MBI 360°", page_icon="🌀", layout="centered")

st.title("🌀 MBI 360° – Evaluación Integral del Ser")

st.markdown("""
Bienvenido al sistema **MBI 360°**, una herramienta única para conocer en profundidad tu estado emocional, epigenético, físico y energético.

**Marca:** RITUAL  
**Creador:** Aníbal Saavedra – Biotecnólogo MIB
""")

st.markdown("### Selecciona uno o varios módulos que deseas realizar:")

modulos = [
    "Test de disociación o trauma",
    "Estado epigenético emocional (líneas materna/paterna)",
    "Condiciones clínicas opcionales"
]

modulos_seleccionados = st.multiselect("", modulos)

if not modulos_seleccionados:
    st.warning("Selecciona al menos un módulo para continuar.")
else:
    if "Test de disociación o trauma" in modulos_seleccionados:
        ejecutar_test_disociacion()
    if "Estado epigenético emocional (líneas materna/paterna)" in modulos_seleccionados:
        ejecutar_test_epigenetico()
    if "Condiciones clínicas opcionales" in modulos_seleccionados:
        ejecutar_test_condiciones_clinicas()

st.markdown("---")
st.markdown("📲 ¿Necesitas ayuda o una consulta personalizada? [Contáctame por WhatsApp](https://wa.me/56967010107)")
