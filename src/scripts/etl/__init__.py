import os
from .initialize_excel import _initialize_excel


LOGIN = os.getlogin()

MONTHS = {
    "Janeiro": 1,
    "Fevereiro": 2,
    "Março": 3,
    "Abril": 4,
    "Maio": 5,
    "Junho": 6,
    "Julho": 7,
    "Agosto": 8,
    "Setembro": 9,
    "Outubro": 10,
    "Novembro": 11,
    "Dezembro": 12,
}


def get_data(file, table_number):
    import numpy as np
    from pandas import DataFrame
    

    fields = {"n_product": 1, "n_state": 4}

    data = {
        "state": [],
        "product": [],
        "year": [],
        "month": [],
        "month_n": [],
        "year_month": [],
        "volume": [],
        "unit": [],
    }

    with _initialize_excel(file) as wb:
        ws = wb.Sheets("Plan1")

        length = {
            key: len(
                ws.PivotTables(f"Tabela dinâmica{table_number}")
                .PivotFields(idx)
                .PivotItems()
            )
            + 1
            for key, idx in fields.items()
        }

        unit = str(
            ws.PivotTables(f"Tabela dinâmica{table_number}")
            .PivotFields(5)
            .PivotItems(1)
        )

        for idx_state in range(1, length["n_state"]):
            state = str(
                ws.PivotTables(f"Tabela dinâmica{table_number}")
                .PivotFields(fields["n_state"])
                .PivotItems(idx_state)
            )

            ws.PivotTables(f"Tabela dinâmica{table_number}").PivotFields(
                "UN. DA FEDERAÇÃO"
            ).CurrentPage = state

            for idx_product in range(1, length["n_product"]):
                product = str(
                    ws.PivotTables(f"Tabela dinâmica{table_number}")
                    .PivotFields(fields["n_product"])
                    .PivotItems(idx_product)
                )

                ws.PivotTables(f"Tabela dinâmica{table_number}").PivotFields(
                    "PRODUTO"
                ).CurrentPage = product

                n_month = len(
                    ws.PivotTables(f"Tabela dinâmica{table_number}").GetDataFields()
                )

                n_year = (
                    len(
                        ws.PivotTables(f"Tabela dinâmica{table_number}")
                        .PivotFields(2)
                        .PivotItems()
                    )
                    + 1
                )

                for idx_year, idx_month in itertools.product(
                    range(1, n_year), range(1, n_month)
                ):

                    year = int(
                        ws.PivotTables(f"Tabela dinâmica{table_number}")
                        .PivotFields(2)
                        .PivotItems(idx_year)
                    )

                    month = str(
                        ws.PivotTables(f"Tabela dinâmica{table_number}").GetDataFields(
                            idx_month
                        )
                    )

                    month_n = MONTHS[month]

                    volume = (
                        ws.PivotTables(f"Tabela dinâmica{table_number}")
                        .PivotValueCell(idx_month, idx_year)
                        .__call__()
                    )

                    if (
                        volume == 0
                        or volume == "-"
                        or volume == np.nan
                        or volume is None
                    ):
                        continue

                    volume = float(str(volume).replace(",", "."))

                    data["state"].append(state)
                    data["product"].append(product)
                    data["year"].append(year)
                    data["month"].append(month)
                    data["month_n"].append(month_n)
                    data["year_month"].append(f"{year}_{month_n}")
                    data["volume"].append(volume)
                    data["unit"].append(unit)

    return DataFrame.from_dict(data)


def _read_raw_data(file):
    from pandas import concat

    df = concat([get_data(file, 1), get_data(file, 3)], ignore_index=True)