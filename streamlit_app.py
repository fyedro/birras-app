import os

import streamlit as st


def _read_html():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'BIRRAS.html')
    with open(path, encoding='utf-8') as f:
        return f.read()


st.set_page_config(
    page_title='BIRRAS',
    page_icon='🍺',
    layout='wide',
    initial_sidebar_state='collapsed',
)

html = _read_html()

st.components.v1.html(html, height=1200, scrolling=True)