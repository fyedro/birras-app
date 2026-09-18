import os

import streamlit as st
import streamlit.components.v1 as components

from auth import require_login


def _read_html():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'BIRRAS.html')
    with open(path, encoding='utf-8') as f:
        return f.read()


def _render(html):
    if hasattr(st, 'iframe'):
        st.iframe(html, width='stretch', height=1200)
    else:
        components.html(html, height=1200, scrolling=True)


st.set_page_config(
    page_title='BIRRAS',
    page_icon='🍺',
    layout='wide',
    initial_sidebar_state='collapsed',
)

require_login()

html = _read_html()

_render(html)