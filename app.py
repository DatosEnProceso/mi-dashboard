import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(
    page_title = "Dashboard visualización de datos",
    layout = "wide"
)
st.title('📊Dashboard visualización de datos')
st.markdown("### Mortalidad hospitalaria")

with st.expander("📝Ver introducción y variables", expanded = True):
    st.markdown("""
    **Objetivo:**

    Desarrollo de un dashboard interactivo para la visualización de los datos para facilitar la identificación de patrones y tendencias. Esto permitirá tomar decisiones informadas para mejorar la gestión hospitalaria y asignación de recursos.
    
    **Introducción:**

    En este proyecto, se busca desarrollar una solución de visualización interactiva para los datos de mortalidad hospitalaria, con el fin de facilitar la toma de decisiones en el hospital. A través de un dashboard, se podrán analizar datos clave que permitirán identificar patrones y tendencias en las causas de mortalidad y la cantidad de pacientes afectados, mejorando así la gestión hospitalaria.

    **Variables:**

    1. **AÑO**: Año en que se registra la mortalidad.
    2. **C.I.E.10**: Clasificación de enfermedades según la décima versión de la CIE.
    3. **MORTALIDAD**: Causa o lesión que causó la muerte.
    4. **NUMERO DE PACIENTES**: Número de pacientes afectados por la causa de mortalidad registrada.
    """)

    try:
        df = pd.read_excel("Datos_Mortalidad.xlsx")
        st.success("Datos cargados correctamente")

    except Exception as e:
        st.error(f"Error al cargar los datos: {str(e)}")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título
st.header("Visualizaciones con Matplotlib, Seaborn y Plotly")

# Comparar mortalidad antes y después de la pandemia
df['AÑO'] = df['AÑO'].astype(int)

# Filtrar los datos antes y después de la pandemia
before_pandemic = df[df['AÑO'] < 2020]
after_pandemic = df[df['AÑO'] >= 2020]

# Agrupar por año y sumar el número de pacientes
mortalidad_anual_before = before_pandemic.groupby('AÑO')['NUMERO DE PACIENTES'].sum()
mortalidad_anual_after = after_pandemic.groupby('AÑO')['NUMERO DE PACIENTES'].sum()

# Crear una nueva columna de comparación antes y después de la pandemia
df_comparacion = pd.DataFrame({
    'Antes de la Pandemia': mortalidad_anual_before,
    'Después de la Pandemia': mortalidad_anual_after
}).fillna(0)

# Graficar la comparación con un gráfico de barras horizontales más gruesas
st.subheader("Gráfica de Barras Horizontales")
fig, ax = plt.subplots(figsize=(14, 8))
df_comparacion.plot(kind='barh', ax=ax, color=['#2E8B57', '#1E90FF'], width=0.7)  # Aumentando el grosor de las barras
ax.set_title('Comparación de Mortalidad: Antes y Después de la Pandemia')
ax.set_xlabel('Número de Pacientes')
ax.set_ylabel('Año')
ax.set_yticklabels(df_comparacion.index, rotation=0)
st.pyplot(fig)

# Descripción de la gráfica
with st.expander("📝Descripción de la Gráfica", expanded=True):
    st.markdown("""
    Esta gráfica muestra la comparación del número de pacientes afectados por mortalidad antes y después de la pandemia. 
    Las barras verdes representan los años previos a 2020, mientras que las barras azules reflejan los años posteriores. 
    Permite observar cómo ha variado la mortalidad a lo largo de los años, destacando posibles cambios post-pandemia.
    """)


# Agrupar por 'AÑO' y 'MORTALIDAD', y sumar el número de pacientes
top_enfermedades = df.groupby(['AÑO', 'MORTALIDAD'])['NUMERO DE PACIENTES'].sum().reset_index()

# Ordenamos los valores por 'AÑO' y 'NUMERO DE PACIENTES'
top_enfermedades = top_enfermedades.sort_values(['AÑO', 'NUMERO DE PACIENTES'], ascending=[True, False])

# Seleccionamos las 3 enfermedades más mortales por año
top_3_enfermedades = top_enfermedades.groupby('AÑO').head(3)

# Crear dos columnas para mostrar los gráficos
col1, col2 = st.columns(2)

# Columna 1: Gráfico de dispersión
with col1:
    st.subheader("Gráfico de Dispersión")
    fig1, ax1 = plt.subplots(figsize=(14, 8))
    sns.scatterplot(data=top_3_enfermedades, x='AÑO', y='NUMERO DE PACIENTES', hue='MORTALIDAD', ax=ax1)
    ax1.set_title("Número de Pacientes por Año y Enfermedad Mortal")
    ax1.set_xlabel("Año")
    ax1.set_ylabel("Número de Pacientes")
    st.pyplot(fig1)

# Columna 2: Gráfico de barras
with col2:
    st.subheader("Gráfico de Barras")
    fig2, ax2 = plt.subplots(figsize=(14, 8))
    sns.barplot(data=top_3_enfermedades, x='AÑO', y='NUMERO DE PACIENTES', hue='MORTALIDAD', ax=ax2)
    ax2.set_title("Tres Enfermedades Más Mortales por Año")
    ax2.set_xlabel("Año")
    ax2.set_ylabel("Número de Pacientes")
    st.pyplot(fig2)
    
# Descripción de las gráficas
with st.expander("📝Descripción de las Gráficas", expanded = True):
    st.markdown("""
    Ambas gráficas muestran la evolución de las tres enfermedades más mortales por año. 
    El gráfico de dispersión destaca la relación entre el número de pacientes y el año, 
    mientras que el gráfico de barras compara la cantidad de pacientes afectados por cada enfermedad 
    a lo largo del tiempo, facilitando la identificación de tendencias y patrones en las causas de mortalidad.
    """)

with st.expander("📝Conclusión", expanded = True):
    st.markdown("""
    A través del dashboard, se ha logrado identificar y visualizar las tres enfermedades con más mortalidad por año, 
    destacando cómo la mortalidad ha cambiado a lo largo del tiempo, especialmente antes y después de la pandemia. 
    Las gráficas interactivas proporcionan una visión clara de los patrones de mortalidad y las enfermedades más 
    afectadas, permitiendo tomar decisiones basadas en datos. De esta forma se puede optimizar la asignación de recursos
    y mejorando las estrategias de salud pública.
    """)
