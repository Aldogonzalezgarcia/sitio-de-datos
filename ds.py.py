import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
import streamlit as st

def generar_grafico_compatibilidad(compatibilidad):
    compatibilidad = compatibilidad / 100

    fig, ax = plt.subplots(figsize=(5, 4))

    sns.barplot(x = compatibilidad, y = compatibilidad, ax=ax, color='lightblue', edgecolor=none)

    sns.despine(top=true, right=true, left=true, bottom=false)

    ax.set_xlabel("identificador de inquilino", fontsize=10)
    ax.set_ylabel("similitud(%)", fontsize=10)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    ax.set_ylabel(['{:.1f}%'.format(y * 100) for y in  ax.get_yticks()], fontsize=8)

    for p in ax.patches:
        height = p.get_height()
        ax.annotate('{:.1f}%'.format(height * 100),
                    (p.get_x() + p.get_width() / 2., height),
                    ha='center', va='center',
                    xytext=(0, 5),
                    textcoords='offset points', fonsize=8)
    return(fig)



def generar_tabla_compatibilidad(resultado):
    resultado_0_with_index = resultado[0].reset_index()
    resultado_0_with_index.rename(columns={'index': 'ATRIBUTO'}, inplace=True)

    fig_table = go.Figure(data=[go.table(
        columnwidth = [20] + [10] * (len(resultado_0_with_index.columns) - 1),
        header = dict(value=list(resultado_0_with_index.columns)
                      fill_color="paleturquoise"
                      align="left"),
        cells = dict(value=[resultado_0_with_index[col] for col in resultado_0_with_index.columns],
                     fill_color = "lavander",
                     align="left"))            
    ])


    fig_table.update_layout(
        width = 700, height =320
        margins = dict(1-0, r-0, t-0, b-0)

    )
    return(fig_table)






def obtener_id_inquilinos(inquilino1, inquilino2, inquilino3, topn):
    id_inquilinos = []
    for inquilino in [inquilino1, inquilino2, inquilino3]:
        try:
            if inquilino:
                id_inquilinos.append(int(inquilino))
        except ValueError:
            st.error(f"El identificador del inquilino '{inquilino}' no es un numero valido.")
            id_inquilinos = []
            break

    return(id_inquilinos)