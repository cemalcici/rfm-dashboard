import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd


# Veri Setinin Alınması
rfm_table = pd.read_pickle("rfm_table.pkl")
rfm_statistics = pd.read_pickle("rfm_statistics.pkl")

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# Sidebar Yapısının Oluşturulması. Fixed kullanarak sabitledik.
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# Sağ tarafta kalan alan yeniden düzenlendi
CONTENT_STYLE = {
    "margin-left": "22rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

SEGMENT_LIST = list(rfm_table["Segment"].unique())

sidebar = html.Div(
    [
        html.A([html.H2("RFM Dashboard", className="display-5")], href="/", className="text-decoration-none"),
        html.Hr(),
        html.P(
            "Aşağıda bulunan her bir sekmede segmentlere ait RFM değerleri ve istatistikleri bulunmaktadır.", className="lead"
        ),
        dbc.Nav(
            children=[dbc.NavLink(segment, href="/"+segment.lower(), active="exact") for segment in rfm_table["Segment"].unique()],
            vertical=True,
            pills=True)
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.Div([
            html.Div([
                html.H1("Hoş Geldin!", className="display-4"),
                html.P("RFM Analizi sonucunda herbir segmente ait istatistikleri görmek için basit bir dahsboard yapısı oluşturduk. Solda bulunan herhangi bir segmentin üzerinde tıkladığında söz konusu segmentlere ait istatistikleri görebileceksin."),
                html.Hr(),
                html.P("Analiz tarihi 11.12.2011 olarak belirlendi."),
                html.P("RFM tablosu oluşturulurken kullanılan R-F-M skorları aşağıda anlatılan şekilde belirlendi."),
                html.Ul([
                    html.Li("R: Müşterinin bügünden son temas ettiği gün arasındaki fark. (En son kaç gün önce alışveriş yaptı?)"),
                    html.Li(
                        "F: Müşteri başına alınan ürün sayısı (Müşteri bugüne kadar toplamda kaç ürün aldı?)"),
                    html.Li(
                        "M: Müşterinin bıraktığı toplam para (Müşteri bugüne kadar toplamda ne kadar para bıraktı?)"),
                ])
            ]),
            html.Div([
                html.H2("İncelenen RFM Tablosu", className="display-5"),
                dbc.Table.from_dataframe(rfm_table.head(), striped=True, bordered=True, hover=True)
            ]),
            html.Div([
                html.H2("İncelenen RFM İstatistikleri", className="display-5"),
                dbc.Table.from_dataframe(rfm_statistics.head(), striped=True, bordered=True, hover=True)
            ])
        ])
    elif pathname == "/"+SEGMENT_LIST[0].lower():
        showing_table = rfm_table[rfm_table["Segment"] == SEGMENT_LIST[0]]
        showing_statistics = rfm_statistics[rfm_statistics["Segment"] == SEGMENT_LIST[0]]
        showing_ids = list(rfm_table.loc[rfm_table["Segment"] == SEGMENT_LIST[0],"Customer ID"].unique())
        return html.Div([
            html.H2(f"{SEGMENT_LIST[0]} Segmentine Ait Sonuçlar", className="display-5"),
            html.Hr(),
            html.H3("Her Bir Müşterinin RFM Değerleri", className="display-5"),
            dbc.Table.from_dataframe(showing_table, striped=True, bordered=True, hover=True),
            html.Hr(),
            html.H3(f"{SEGMENT_LIST[0]} Segmentine Ait Sonuçlar", className="display-5"),
            dbc.Table.from_dataframe(showing_statistics, striped=True, bordered=True, hover=True),
            html.Hr(),
            html.P("Bu segmente ait müşteri numaraları"),
            html.P(f"{showing_ids}")
        ])
    elif pathname == "/" + SEGMENT_LIST[1].lower():
        showing_table = rfm_table[rfm_table["Segment"] == SEGMENT_LIST[1]]
        showing_statistics = rfm_statistics[rfm_statistics["Segment"] == SEGMENT_LIST[1]]
        showing_ids = list(rfm_table.loc[rfm_table["Segment"] == SEGMENT_LIST[1], "Customer ID"].unique())
        return html.Div([
            html.H2(f"{SEGMENT_LIST[1]} Segmentine Ait Sonuçlar", className="display-5"),
            html.Hr(),
            html.H3("Her Bir Müşterinin RFM Değerleri", className="display-5"),
            dbc.Table.from_dataframe(showing_table, striped=True, bordered=True, hover=True),
            html.Hr(),
            html.H3(f"{SEGMENT_LIST[1]} Segmentine Ait Sonuçlar", className="display-5"),
            dbc.Table.from_dataframe(showing_statistics, striped=True, bordered=True, hover=True),
            html.Hr(),
            html.P("Bu segmente ait müşteri numaraları"),
            html.P(f"{showing_ids}")
        ])
    elif pathname == "/" + SEGMENT_LIST[2].lower():
        showing_table = rfm_table[rfm_table["Segment"] == SEGMENT_LIST[2]]
        showing_statistics = rfm_statistics[rfm_statistics["Segment"] == SEGMENT_LIST[2]]
        showing_ids = list(rfm_table.loc[rfm_table["Segment"] == SEGMENT_LIST[2], "Customer ID"].unique())
        return html.Div([
            html.H2(f"{SEGMENT_LIST[2]} Segmentine Ait Sonuçlar", className="display-5"),
            html.Hr(),
            html.H3("Her Bir Müşterinin RFM Değerleri", className="display-5"),
            dbc.Table.from_dataframe(showing_table, striped=True, bordered=True, hover=True),
            html.Hr(),
            html.H3(f"{SEGMENT_LIST[2]} Segmentine Ait Sonuçlar", className="display-5"),
            dbc.Table.from_dataframe(showing_statistics, striped=True, bordered=True, hover=True),
            html.Hr(),
            html.P("Bu segmente ait müşteri numaraları"),
            html.P(f"{showing_ids}")
        ])
    elif pathname == "/" + SEGMENT_LIST[3].lower():
        showing_table = rfm_table[rfm_table["Segment"] == SEGMENT_LIST[3]]
        showing_statistics = rfm_statistics[rfm_statistics["Segment"] == SEGMENT_LIST[3]]
        showing_ids = list(rfm_table.loc[rfm_table["Segment"] == SEGMENT_LIST[3], "Customer ID"].unique())
        return html.Div([
            html.H2(f"{SEGMENT_LIST[3]} Segmentine Ait Sonuçlar", className="display-5"),
            html.Hr(),
            html.H3("Her Bir Müşterinin RFM Değerleri", className="display-5"),
            dbc.Table.from_dataframe(showing_table, striped=True, bordered=True, hover=True),
            html.Hr(),
            html.H3(f"{SEGMENT_LIST[3]} Segmentine Ait Sonuçlar", className="display-5"),
            dbc.Table.from_dataframe(showing_statistics, striped=True, bordered=True, hover=True),
            html.Hr(),
            html.P("Bu segmente ait müşteri numaraları"),
            html.P(f"{showing_ids}")
        ])
    elif pathname == "/" + SEGMENT_LIST[4].lower():
        showing_table = rfm_table[rfm_table["Segment"] == SEGMENT_LIST[4]]
        showing_statistics = rfm_statistics[rfm_statistics["Segment"] == SEGMENT_LIST[4]]
        showing_ids = list(rfm_table.loc[rfm_table["Segment"] == SEGMENT_LIST[4], "Customer ID"].unique())
        return html.Div([
            html.H2(f"{SEGMENT_LIST[4]} Segmentine Ait Sonuçlar", className="display-5"),
            html.Hr(),
            html.H3("Her Bir Müşterinin RFM Değerleri", className="display-5"),
            dbc.Table.from_dataframe(showing_table, striped=True, bordered=True, hover=True),
            html.Hr(),
            html.H3(f"{SEGMENT_LIST[4]} Segmentine Ait Sonuçlar", className="display-5"),
            dbc.Table.from_dataframe(showing_statistics, striped=True, bordered=True, hover=True),
            html.Hr(),
            html.P("Bu segmente ait müşteri numaraları"),
            html.P(f"{showing_ids}")
        ])
    elif pathname == "/" + SEGMENT_LIST[5].lower():
        showing_table = rfm_table[rfm_table["Segment"] == SEGMENT_LIST[5]]
        showing_statistics = rfm_statistics[rfm_statistics["Segment"] == SEGMENT_LIST[5]]
        showing_ids = list(rfm_table.loc[rfm_table["Segment"] == SEGMENT_LIST[5], "Customer ID"].unique())
        return html.Div([
            html.H2(f"{SEGMENT_LIST[5]} Segmentine Ait Sonuçlar", className="display-5"),
            html.Hr(),
            html.H3("Her Bir Müşterinin RFM Değerleri", className="display-5"),
            dbc.Table.from_dataframe(showing_table, striped=True, bordered=True, hover=True),
            html.Hr(),
            html.H3(f"{SEGMENT_LIST[5]} Segmentine Ait Sonuçlar", className="display-5"),
            dbc.Table.from_dataframe(showing_statistics, striped=True, bordered=True, hover=True),
            html.Hr(),
            html.P("Bu segmente ait müşteri numaraları"),
            html.P(f"{showing_ids}")
        ])
    elif pathname == "/" + SEGMENT_LIST[6].lower():
        showing_table = rfm_table[rfm_table["Segment"] == SEGMENT_LIST[6]]
        showing_statistics = rfm_statistics[rfm_statistics["Segment"] == SEGMENT_LIST[6]]
        showing_ids = list(rfm_table.loc[rfm_table["Segment"] == SEGMENT_LIST[6], "Customer ID"].unique())
        return html.Div([
            html.H2(f"{SEGMENT_LIST[6]} Segmentine Ait Sonuçlar", className="display-5"),
            html.Hr(),
            html.H3("Her Bir Müşterinin RFM Değerleri", className="display-5"),
            dbc.Table.from_dataframe(showing_table, striped=True, bordered=True, hover=True),
            html.Hr(),
            html.H3(f"{SEGMENT_LIST[6]} Segmentine Ait Sonuçlar", className="display-5"),
            dbc.Table.from_dataframe(showing_statistics, striped=True, bordered=True, hover=True),
            html.Hr(),
            html.P("Bu segmente ait müşteri numaraları"),
            html.P(f"{showing_ids}")
        ])
    elif pathname == "/" + SEGMENT_LIST[7].lower():
        showing_table = rfm_table[rfm_table["Segment"] == SEGMENT_LIST[7]]
        showing_statistics = rfm_statistics[rfm_statistics["Segment"] == SEGMENT_LIST[7]]
        showing_ids = list(rfm_table.loc[rfm_table["Segment"] == SEGMENT_LIST[7], "Customer ID"].unique())
        return html.Div([
            html.H2(f"{SEGMENT_LIST[7]} Segmentine Ait Sonuçlar", className="display-5"),
            html.Hr(),
            html.H3("Her Bir Müşterinin RFM Değerleri", className="display-5"),
            dbc.Table.from_dataframe(showing_table, striped=True, bordered=True, hover=True),
            html.Hr(),
            html.H3(f"{SEGMENT_LIST[7]} Segmentine Ait Sonuçlar", className="display-5"),
            dbc.Table.from_dataframe(showing_statistics, striped=True, bordered=True, hover=True),
            html.Hr(),
            html.P("Bu segmente ait müşteri numaraları"),
            html.P(f"{showing_ids}")
        ])
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(port=8888)
