# Page configurations
import streamlit as st

st.set_page_config(page_title="ML-DT KentKatigbak", layout="wide", initial_sidebar_state="expanded")

hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown("""
        <style>
            .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
            .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)

#App

#Import Libraries
import streamlit as st
import pandas as pd

#File upload
st.title("DATA CLEANING AND MANIPULATION WEB APP")
st.write("_____________________________________")
st.subheader("INPUT CSV")
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("_____________________________________")
    
    #Display upladed CSV
    st.subheader("UPLOADED DATAFRAME")
    st.write(df)
    st.write("DataFrame shape: ", df.shape)
    st.write("_____________________________________")
    
    #Select index and drop unnecessary columns
    st.subheader("DROP UNNECESSARY COLUMNS AND SELECT INDEX COLUMN")
    #Print columns
    #st.subheader("List of Columns")
    columns = df.columns
    # st.write(columns.tolist())
    columns_to_drop = st.multiselect("Select the columns you want to drop", columns)
    df2 = df.drop(columns_to_drop, axis=1)
    #Select index column
    columns2 = df2.columns
    index_column = st.selectbox("Select an index column", columns2)
    df3 = df2.set_index(index_column)
    st.write("_____________________________________")
    
    #Print new DataFrame
    st.subheader("DataFrame 2 (Dropped columns and new index)")
    st.write(df3)
    st.write("DataFrame shape: ", df3.shape)
    st.write("_____________________________________")
    
    #Remove null values
    st.subheader("REMOVE NULL VALUES")
    columns3 = df3.columns
    nulls_to_remove = st.selectbox("Choose columns where you want to remove null values", columns3)
    df4 = df3.dropna(subset=nulls_to_remove)
    st.write("_____________________________________")
    
    #Print new DataFrame
    st.subheader("DataFrame 3 (Dropped rows with null values in the selected columns)")
    st.write(df4)
    st.write("DataFrame shape: ", df4.shape)
    st.write("_____________________________________")
    
    #Replace null values
    st.subheader("REPLACE OTHER NULL VALUES")
    null_replacement = st.selectbox("Choose value to replace null values",
                                    ('Column Mean', 'Column Median', 'Column Mode', 'Custom Value'))
    if null_replacement == 'Column Mean':
        df5 = df4.fillna(df4.mean())
    elif null_replacement == 'Column Median':
        df5 = df4.fillna(df4.median())
    elif null_replacement == 'Column Mode':
        df5 = df4.fillna(df4.mode())
    else:
        custom_value = st.number_input("Input custom value")
        df5 = df4.fillna(custom_value)
    st.write("_____________________________________")
    
    #Print new DataFrame
    st.subheader("DataFrame 4 (Replaced null values)")
    st.write(df5)
    st.write("DataFrame shape: ", df5.shape)
    st.write("_____________________________________")
    
    #Remove duplicate values
    st.subheader("REMOVE DUPLICATE VALUES")
    columns4 = df5.columns
    duplicates_to_remove = st.multiselect("Choose columns to remove duplicates", columns4)
    df6 = df5.drop_duplicates(subset=duplicates_to_remove, keep=False)
    st.write("_____________________________________")
    
    #Print new DataFrame
    st.subheader("DataFrame 5 (Dropped duplicates in selected columns)")
    st.write(df6)
    st.write("DataFrame shape: ", df6.shape)
    st.write("_____________________________________")
    
    #Final DataFrame
    st.subheader("FINAL DATAFRAME")
    st.write(df6)
    st.write("DataFrame shape: ", df6.shape)
    
    #Download CSV option
    @st.cache
    def convert_df_to_csv(dfFinal):
        return dfFinal.to_csv().encode('utf-8')
    
    st.download_button(
        label="Download Final DataFrame as CSV",
        data=convert_df_to_csv(df6),
        file_name="Final_DataFrame",
        mime='text/csv',
    )
    st.write("_____________________________________")
    
    #Descriptive Statistics
    st.subheader("DESCRIPTIVE STATISTICS")
    st.write(df6.describe())
    st.write("_____________________________________")
    
    #-------------------------------------------------
    #PyGWalker
    import pygwalker as pg
    st.title("DATA VISUALIZATION")
    tableau = pg.walk(df6, env="Streamlit")
    st.write(tableau, unsafe_allow_html=True)
    #-------------------------------------------------
    
    
#     #DATA VISUALIZATION
#     st.title("DATA VISUALIZATION")
    
#     #Chart Selection
#     vis_chart = st.selectbox("Select a visualization chart",
#                             ("Line Chart", "Area Chart", "Bar Chart"))
    
#     #Final Columns
#     finalColumns = df6.columns
#     x_val = st.selectbox("Choose x-axis", finalColumns)
#     y_val = st.selectbox("Choose y-axis", finalColumns)
#     st.write("_____________________________________")
    
#     #Chart Creation
#     #Line Chart
#     if vis_chart == "Line Chart":
#         st.write(x_val, " and ", y_val, "Chart")
#         st.line_chart(data=df6, x=x_val, y=y_val)
    
#     #Area Chart
#     elif vis_chart == "Area Chart":
#         st.write(x_val, " and ", y_val, "Chart")
#         st.area_chart(data=df6, x=x_val, y=y_val)
    
#     #Bar Chart
#     else:
#         st.write(x_val, " and ", y_val, "Chart")
#         st.bar_chart(data=df6, x=x_val, y=y_val)
        
# else:
#     st.info("The app accepts CSV files only!")
    
#Developer
with st.sidebar:
    st.image("/Users/macbookair/Documents/VS Code/Web Apps/IE App/logo_kent.png")
    st.markdown("""
                <h1 class = title1>
                    Kent Jym B. Katigbak
                </h1>
                <h4 class = subtitle1>
                    Industrial Engineer, CLSSYB, SO2, PMFC, CIFC, DSFC, Data Analyst, Python Programmer
                </h4>
                <style>
                    .title1 {
                    padding-bottom: 0rem;
                }
                    .subtitle1 {
                    padding-top: 1rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                }
        </style>
        """, unsafe_allow_html=True)