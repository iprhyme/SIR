import streamlit as st
import pandas as pd
import plotly.express as px 
import altair as alt


st.set_option("deprecation.showPyplotGlobalUse", False)
st.set_page_config(
    page_title="SIR",
    page_icon="https://cdn-icons-png.flaticon.com/512/11469/11469451.png",
    layout="wide",
    initial_sidebar_state="expanded",
)
with st.sidebar:
    
   
    st.sidebar.write("Developed by SIR's Team")
st.title("Dashboard!")
st.logo("b019d1f9-fe62-4653-bbc3-6f5093c68a28.jpg")
if st.session_state.logged_in:

    df= pd.read_excel("Book1.xlsx")

    col= st.columns((10, 5, 5), gap='medium')
    def make_donut(input_response, input_text, input_color):
        if input_color == 'blue':
            chart_color = ['#29b5e8', '#155F7A']
        if input_color == 'green':
            chart_color = ['#27AE60', '#12783D']
        if input_color == 'orange':
            chart_color = ['#F39C12', '#875A12']
        if input_color == 'red':
            chart_color = ['#E74C3C', '#781F16']

        source = pd.DataFrame({
            "Topic": ['', input_text],
            "% value": [100-input_response, input_response]
        })
        source_bg = pd.DataFrame({
            "Topic": ['', input_text],
            "% value": [100, 0]
        })

        plot = alt.Chart(source).mark_arc(innerRadius=45, cornerRadius=25).encode(
            theta="% value",
            color= alt.Color("Topic:N",
                            scale=alt.Scale(
                                domain=[input_text, ''],
                                range=chart_color),
                            legend=None),
        ).properties(width=130, height=130)

        text = plot.mark_text(align='center', color="#29b5e8", font="Lato", fontSize=32, fontWeight=700, fontStyle="italic").encode(
            text=alt.value(f'{input_response} %')
        )
        
        plot_bg = alt.Chart(source_bg).mark_arc(innerRadius=45, cornerRadius=20).encode(
            theta="% value",
            color= alt.Color("Topic:N",
                            scale=alt.Scale(
                                domain=[input_text, ''],
                                range=chart_color),
                            legend=None),
        ).properties(width=130, height=130)
        
        return plot_bg + plot + text

    donut_chart= make_donut(input_response=75, input_text="Antibiotic A", input_color="green")
    st.altair_chart(donut_chart)

    abx_resistance = df.groupby('Abx').sum().reset_index()
    figure = px.pie(abx_resistance, values='Resistance Rate', names='Abx', 
    title='Chart of Resistance Rates by Antibiotic',
    hole=0.4)  # Makes it a donut
    st.plotly_chart(figure)
    figure2 = px.pie(df, values='Resistance Rate', names='Abx', facet_col='Bacteria ', 
                title='Pie Chart of Resistance Rates by Bacteria and Antibiotics', hole=0.4)
    for annotation in figure2.layout.annotations:
        if 'Bacteria =' in annotation.text:
            annotation.text = annotation.text.replace('Bacteria =', '')
    st.plotly_chart(figure2)
    fig = px.bar(df, 
                x='Bacteria ', 
                y='Resistance Rate', 
                color='Bacteria ', 
                facet_col='Abx', 
                title='Antibiotic Resistance Rates Across Bacterias',
                text_auto=True,)




    for annotation in fig.layout.annotations:
        if 'Abx=' in annotation.text:
            annotation.text = annotation.text.replace('Abx=', '')
    fig.update_xaxes(title_text='')

    fig.update_layout(
        font=dict(size=11.2),   
    )





    st.plotly_chart(fig)
    
else:
    st.subheader("Please Log in, to get access to this page ")
        