import streamlit as st
from st_aggrid import AgGrid
from glob import glob
from scripts.data.read import read_data
from services.path.check_path import _get_resource_path
from templates import show

st.set_page_config(
    page_title="Desafio Raízen",
    page_icon="https://www.raizen.com.br/img/favicon.ico",
    layout="wide",
)


def start(path=None):
    st.title("Bem vindo!")

    if path is None:
        path = glob(_get_resource_path("data/parquet/*.parquet"))[-1]

    KEYS = {"dataset", "state", "year", "month", "product"}

    if not KEYS.issubset(set(st.session_state.keys())):
        st.session_state["dataset"] = read_data(path)
        st.session_state["state"] = (
            st.session_state["dataset"]["state"].unique().tolist()
        )
        st.session_state["product"] = (
            st.session_state["dataset"]["product"].unique().tolist()
        )
        st.session_state["year"] = st.session_state["dataset"]["year"].unique().tolist()
        st.session_state["month"] = (
            st.session_state["dataset"]["month"].unique().tolist()
        )

    show()


if __name__ == "__main__":
    start()
