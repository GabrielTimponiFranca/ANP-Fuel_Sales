import streamlit as st


def filter_dataframe(df, state, product, year, month):
    if state:
        df = df[df["state"].isin(state)]

    if product:
        df = df[df["product"].isin(product)]

    if year:
        df = df[df["year"].isin(year)]

    if month:
        df = df[df["month"].isin(month)]

    return df


def show():
    from .charts.histogram import histogram_chart
    from .charts.pie import pie_chart
    from .crosstab import crosstab_table

    with st.sidebar:
        state = st.multiselect("Estado: ", st.session_state["state"])
        product = st.multiselect("Produto: ", st.session_state["product"])
        year = st.multiselect("Ano: ", st.session_state["year"])
        month = st.multiselect("Mês: ", st.session_state["month"])

    with st.spinner("Carregando base de dados..."):
        df = st.session_state["dataset"]

        df = filter_dataframe(df, state, product, year, month)

        st.header("Consumo de combustível, por produto.")

        col1, col2 = st.columns(2)

        chart = histogram_chart(df, "product")

        col1.plotly_chart(chart, True)

        chart = pie_chart(df, "product")

        col2.plotly_chart(chart, True)

        st.header("Consumo de combustível, por estado.")

        col1, col2 = st.columns(2)

        chart = histogram_chart(df, "state")

        col1.plotly_chart(chart, True)

        chart = pie_chart(df, "state")

        col2.plotly_chart(chart, True)

        crosstab = crosstab_table(df)

        st.table(crosstab)
