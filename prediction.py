import streamlit as st
import pandas as pd
import joblib

# Import Model
with open('model_scaler.pkl', 'rb') as file_1:
    model_scaler = joblib.load(file_1)
with open('model_rf.pkl', 'rb') as file_2:
    model_rf = joblib.load(file_2)
# with open('num_columns.txt', 'r') as file_3:
#     num_columns = json.load(file_3)
    
def run():
    st.title('Prediction')
    with st.form(key='Parameter'):
        # name = st.text_input('Name', value ='')
        CRIM =st.number_input('CRIM', min_value = 0, max_value= 1, value = 0, step=0, 
                              help='per capita crime rate by town')
        ZN = st.number_input('ZN', min_value = 0, max_value= 100, value = 0, step=1,  
                              help='proportion of residential land zoned for lots over 25.000 sq.ft')
        INDUS = st.number_input('INDUS', min_value = 0, max_value= 28, value = 0, step=0,  
                              help='proportion of non-retail business acres per town')
        CHAS = st.number_input('CHAS', min_value = 0, max_value= 1, value = 0, step=1,  
                              help='1 if Tract bounds river, 0 if otherwise')
        RM = st.number_input('RM', min_value = 0, max_value= 10, value = 4, step=1,
                             help='average number of rooms per dwelling.')
        AGE = st.number_input('AGE', min_value = 2, max_value= 100, value = 20, step=1,
                              help='proportion of owner-occupied units built prior to 1940')
        DIS = st.number_input('DIS', min_value = 1, max_value= 15, value = 5, step=1,
                              help='weighted distances to five Boston employment centres')
        PTRATIO = st.number_input('PTRATIO', min_value = 1, max_value= 25, value = 15, step=1,
                                  help='pupil-teacher ratio by town')
        B = st.number_input('B', min_value = 1, max_value= 400, value = 10, step=1,
                            help='1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town.')
        LSTAT = st.number_input('LSTAT', min_value = 1, max_value= 40, value = 10, step=1,
                                help='% lower status of the population')
        
        st.markdown('----')
        
        submitted= st.form_submit_button('Predict Price')
    
    data_inf={
        # 'Name' : name,
        'CRIM':CRIM,
        'ZN' : ZN,
        'INDUS': INDUS,
        'CHAS' : CHAS,
        'RM' : RM,
        'AGE': AGE,
        'DIS' : DIS, 
        'PTRATIO': PTRATIO,
        'B' : B,
        'LSTAT': LSTAT
    }
    
    data_inf= pd.DataFrame([data_inf])
    st.dataframe(data_inf)
    
    if submitted:
        data_inf_num_scaled = model_scaler.transform(data_inf)
        
        y_pred_inf = model_rf.predict(data_inf_num_scaled)
        
        st.write('# Predict Price: ', '<span style="color: red;">{:.2f} USD</span>'.format(float(y_pred_inf)), unsafe_allow_html=True)


if __name__ == '__Home__':
    run()
        