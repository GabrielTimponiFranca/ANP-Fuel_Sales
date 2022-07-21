def pie_chart(df, param):
    import plotly.express as px

    if param == "state":
        field = "Estado"
    elif param == "product":
        field = "Produto"

    unit = df["unit"].iloc[0]

    chart = px.pie(df, values="volume", names=param)

    chart.update_layout(
        font=dict(family="Segoe UI", size=15),
        legend=dict(title=field),
    )

    return chart
