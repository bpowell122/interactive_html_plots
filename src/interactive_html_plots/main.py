import os
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


def render_figure_1(output_dir=''):
    # example taken from: https://kanishkegb.github.io/plotly-with-markdown/

    df = px.data.gapminder()
    fig = px.scatter(
            df.query("year==2007"),
            x="gdpPercap", y="lifeExp",
            size="pop", color="continent",
            hover_name="country", log_x=True, size_max=60
        )
    # fig.show()
    out_path = f'{output_dir}/figure_1.html'
    fig.write_html(out_path, full_html=False, include_plotlyjs='cdn')


def render_figure_2(output_dir=''):
    # example taken from: https://plotly.com/python/dropdowns/#update-dropdown

    # Load dataset
    df = pd.read_csv(
        "https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")
    df.columns = [col.replace("AAPL.", "") for col in df.columns]

    # Initialize figure
    fig = go.Figure()

    # Add Traces

    fig.add_trace(
        go.Scatter(x=list(df.Date),
                   y=list(df.High),
                   name="High",
                   line=dict(color="#33CFA5")))

    fig.add_trace(
        go.Scatter(x=list(df.Date),
                   y=[df.High.mean()] * len(df.index),
                   name="High Average",
                   visible=False,
                   line=dict(color="#33CFA5", dash="dash")))

    fig.add_trace(
        go.Scatter(x=list(df.Date),
                   y=list(df.Low),
                   name="Low",
                   line=dict(color="#F06A6A")))

    fig.add_trace(
        go.Scatter(x=list(df.Date),
                   y=[df.Low.mean()] * len(df.index),
                   name="Low Average",
                   visible=False,
                   line=dict(color="#F06A6A", dash="dash")))

    # Add Annotations and Buttons
    high_annotations = [dict(x="2016-03-01",
                             y=df.High.mean(),
                             xref="x", yref="y",
                             text="High Average:<br> %.3f" % df.High.mean(),
                             ax=0, ay=-40),
                        dict(x=df.Date[df.High.idxmax()],
                             y=df.High.max(),
                             xref="x", yref="y",
                             text="High Max:<br> %.3f" % df.High.max(),
                             ax=-40, ay=-40)]
    low_annotations = [dict(x="2015-05-01",
                            y=df.Low.mean(),
                            xref="x", yref="y",
                            text="Low Average:<br> %.3f" % df.Low.mean(),
                            ax=0, ay=40),
                       dict(x=df.Date[df.High.idxmin()],
                            y=df.Low.min(),
                            xref="x", yref="y",
                            text="Low Min:<br> %.3f" % df.Low.min(),
                            ax=0, ay=40)]

    fig.update_layout(
        updatemenus=[
            dict(
                active=0,
                buttons=list([
                    dict(label="None",
                         method="update",
                         args=[{"visible": [True, False, True, False]},
                               {"title": "Yahoo",
                                "annotations": []}]),
                    dict(label="High",
                         method="update",
                         args=[{"visible": [True, True, False, False]},
                               {"title": "Yahoo High",
                                "annotations": high_annotations}]),
                    dict(label="Low",
                         method="update",
                         args=[{"visible": [False, False, True, True]},
                               {"title": "Yahoo Low",
                                "annotations": low_annotations}]),
                    dict(label="Both",
                         method="update",
                         args=[{"visible": [True, True, True, True]},
                               {"title": "Yahoo",
                                "annotations": high_annotations + low_annotations}]),
                ]),
            )
        ])

    # Set title
    fig.update_layout(title_text="Yahoo")

    out_path = f'{output_dir}/figure_2.html'
    fig.write_html(out_path, full_html=False, include_plotlyjs='cdn')


if __name__ == "__main__":
    figure_dir = 'docs/_source/prerendered_figures'
    os.makedirs(figure_dir, exist_ok=True)
    render_figure_1(figure_dir)
    render_figure_2(figure_dir)
