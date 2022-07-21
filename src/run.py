import streamlit as st
from st_aggrid import AgGrid
from scripts.data.read import read_data
from services.path.check_path import _get_resource_path
from templates import show

st.set_page_config(
    page_title="Desafio Raízen",
    page_icon="https://www.raizen.com.br/img/favicon.ico",
    layout="wide",
)

st.title("Bem vindo!")

path = _get_resource_path("data/parquet/raw_data_20220715.parquet")

KEYS = {"dataset", "state", "year", "month", "product"}

if not KEYS.issubset(set(st.session_state.keys())):
    st.session_state["dataset"] = read_data(path)
    st.session_state["state"] = st.session_state["dataset"]["state"].unique().tolist()
    st.session_state["product"] = (
        st.session_state["dataset"]["product"].unique().tolist()
    )
    st.session_state["year"] = st.session_state["dataset"]["year"].unique().tolist()
    st.session_state["month"] = st.session_state["dataset"]["month"].unique().tolist()


def start():
    show()


if __name__ == "__main__":
    start()
