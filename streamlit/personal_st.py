import streamlit as st
import numpy as np
import pandas as pd
import datetime
import joblib
from sklearn.preprocessing import MinMaxScaler
import pickle
date_time = datetime.datetime.now()

loaded_model = joblib.load('modelo_arbol_decision.joblib')



with open('scaler.pkl', 'rb') as file:
    scaler_loaded = pickle.load(file)

import streamlit as st

# Ruta a tu archivo de imagen
ruta_imagen = "./Imagen1.jpg"  # Cambia esto a la ruta correcta de tu imagen

# Mostrar la imagen
st.image(ruta_imagen, use_column_width=True)

def main(): 

   
    st.markdown("##### Evaluación de solicitudes de crédito")
    
    st.write('')
    st.write('')

    p1 = st.number_input('¿Cuantas personas tiene a su cargo?',0,25)
    
    p2 = st.number_input('¿Cuales son sus ingresos anuales?',0.0,50000000000.0)

    p3= st.number_input('¿Cuanto dinero necesita?',0.0,50000000000.0)

    p4 = st.number_input('Plazo del prestamo en años',0,50000000000)

    p5 = st.number_input('¿Cual es su CIBIL score?',300,900)

    p6 = st.number_input('¿Valor de sus bienes residenciales?',0.0,50000000000.0)

    p7 = st.number_input('¿Valor de sus bienes de lujo? (Vehiculos, joyas, arte)',0.0,50000000000.0)

    

    

    data_new = pd.DataFrame({
    ' no_of_dependents':[p1],
    ' income_annum':[p2],
    ' loan_amount':[p3],
    ' loan_term':[p4],
    ' cibil_score':[p5],
    ' residential_assets_value':[p6],
    ' luxury_assets_value':[p7]

},index=[0])
    try: 
        if st.button('¿Te podemos ofrecer el credito solicitado?'):
            
            X_scaled = scaler_loaded.transform(data_new)
            prediction = loaded_model.predict(X_scaled)

            if prediction==0:                
                st.warning('Lo sentimos, parece que no cumples nuestros requisitos para el prestamo solicitado. \n Si crees que hay algún error ponte en contacto y estudiaremos tu caso.')
            elif prediction==1:
                st.success("Fantástico, podemos ofrecerte el crédito solicitado. \n Envía un email con la captura de esta pagina y nos pondremos en contacto.")
    except:
        st.warning("Opps!! Something went wrong\nTry again")

if __name__ == '__main__':
    main()