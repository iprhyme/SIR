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


df= pd.read_excel("Book1.xlsx")


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

    text = plot.mark_text(align='center', color="#29b5e8", font="Lato", fontSize=24, fontWeight=700, fontStyle="italic").encode(
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

def assign_color(resistance_rate):
    if resistance_rate >= 77:  
        return 'green'
    elif 50 <= resistance_rate < 77:  
        return 'orange'
    else:  
        return 'red'



# Radio button for user choice
choice= st.radio(label="Choose a Bacteria", options=["A. baumannii", "E. coli", "K. pneumoniae"])

# Custom CSS for styling
st.markdown(
    """
    <style>
    .card {
        background-color: #2e2e2e;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        color: white;
        text-align: center;
        width: 220px;
        height: 150px;
        display: inline-block;
        margin-right: 15px;
    }

    .title {
        font-size: 18px;
        font-weight: bold;
    }

    .value {
        font-size: 28px;
        font-weight: bold;
    }

    .delta-positive {
        color: #27AE60;
        font-size: 16px;
    }

    .delta-negative {
        color: #E74C3C;
        font-size: 16px;
    }

    </style>
    """, unsafe_allow_html=True
)



# Filter the DataFrame based on the user's choice
selected_df = df[df['Bacteria '] == choice]

# Calculate the average resistance rate for the selected choice
selected_avg = selected_df['Resistance Rate'].mean()

# Get the choices for the other two groups
other_choices = df['Bacteria '].unique().tolist()
other_choices.remove(choice)

# Calculate the average resistance rates for the other two groups
other_avg_1 = df[df['Bacteria '] == other_choices[0]]['Resistance Rate'].mean()
other_avg_2 = df[df['Bacteria '] == other_choices[1]]['Resistance Rate'].mean()

# Create 2 columns to display the two comparison cards
col1, col2 = st.columns(2)

# First card comparing selected group with the first other group
with col1:
    delta_1 = selected_avg - other_avg_1 if selected_avg > other_avg_1 else other_avg_1 - selected_avg
    is_positive_1 = selected_avg > other_avg_1
    delta_class_1 = "delta-positive" if is_positive_1 else "delta-negative"
    delta_symbol_1 = "⬆" if is_positive_1 else "⬇"
    
    st.markdown(
        f"""
        <div class="card">
            <div class="title">{choice} vs {other_choices[0]}</div>
            <div class="value">{selected_avg:.2f}%</div>
            <div class="{delta_class_1}">{delta_symbol_1} {delta_1:.2f}%</div>
        </div>
        """, unsafe_allow_html=True
    )

# Second card comparing selected group with the second other group
with col2:
    delta_2 = selected_avg - other_avg_2 if selected_avg > other_avg_2 else other_avg_2 - selected_avg
    is_positive_2 = selected_avg > other_avg_2
    delta_class_2 = "delta-positive" if is_positive_2 else "delta-negative"
    delta_symbol_2 = "⬆" if is_positive_2 else "⬇"
    
    st.markdown(
        f"""
        <div class="card">
            <div class="title">{choice} vs {other_choices[1]}</div>
            <div class="value">{selected_avg:.2f}%</div>
            <div class="{delta_class_2}">{delta_symbol_2} {delta_2:.2f}%</div>
        </div>
        """, unsafe_allow_html=True
    )


filtered_df = df[df["Bacteria "] == choice.strip()]

# Sort the filtered DataFrame by Resistance Rate and get the top 3
top_3 = filtered_df.nlargest(3, 'Resistance Rate')




# Create 3 columns to display the charts side by side
cols = st.columns(3)


# Generate donut charts for each row in the top 3
for idx, (index, row) in enumerate(top_3.iterrows()):
    with cols[idx]:
        # Assign colors based on the ranking
        color = assign_color(row['Resistance Rate'])
        donut_chart = make_donut(input_response=row['Resistance Rate'], 
                                 input_text=row['Abx'], 
                                 input_color=color)
        st.write(f"{row['Abx']}")
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

