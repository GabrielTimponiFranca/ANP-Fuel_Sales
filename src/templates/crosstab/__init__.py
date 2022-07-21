def crosstab_table(df):
    from pandas import crosstab

    return (
        crosstab(
            [df["month_n"], df["month"]],
            [df["year"]],
            values=df["volume"],
            aggfunc="sum",
        )
        .rename_axis(None, axis=1)
        .reset_index()
        .drop(columns=["month_n"])
        .rename(columns={"month": "Mês"})
    )
