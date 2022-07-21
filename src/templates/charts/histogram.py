def histogram_chart(df, param):
    import plotly.express as px
    

    if param == "state":
        field = "Estado"
    elif param == "product":
        field = "Produto"

    unit = df["unit"].iloc[0]

    chart = px.histogram(
        df,
        x="year",
        y="volume",
        color=param,
        barmode="group",
    )

    chart.update_layout(
        xaxis=dict(title="Ano"),
        yaxis=dict(title=f"Volume [{unit}]"),
        legend=dict(title=field),
        font=dict(family="Segoe UI", size=15),
    )

    return chart
