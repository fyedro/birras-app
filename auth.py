"""Autenticación simple por contraseña compartida (misma mecánica que dotaciones).

La contraseña se lee del secret/enviroment ``BIRRAS_PASSWORD`` (secrets de
Community Cloud). Si no está configurada, el acceso es abierto (útil en
desarrollo local). Al autenticarse se guarda la sesión en ``st.session_state``.
"""
import hmac
import os
import streamlit as st


def _password() -> str:
    if "BIRRAS_PASSWORD" in os.environ:
        return os.environ.get("BIRRAS_PASSWORD", "") or ""
    try:
        return str(st.secrets["BIRRAS_PASSWORD"] or "") if st.secrets else ""
    except Exception:
        return ""


def _es_correcta(clave: str) -> bool:
    esperada = _password()
    if not esperada:
        return True
    return bool(clave) and hmac.compare_digest(clave, esperada)


def require_login():
    """Muestra el formulario de acceso y detiene la app si no hay sesión."""
    if st.session_state.get("birras_autenticado"):
        return
    if not _password():
        st.error(
            "Configuración incompleta: falta definir BIRRAS_PASSWORD en el "
            "secret. La app queda bloqueada por seguridad hasta que se configure.",
            icon="🔒",
        )
        st.stop()

    st.markdown(
        """
        <style>
        .login-wrap { max-width: 380px; margin: 12vh auto 0 auto; padding: 24px;
                      border: 1px solid #e0e0e0; border-radius: 12px;
                      box-shadow: 0 4px 16px rgba(0,0,0,.06); }
        .login-wrap .logo { font-size: 18px; font-weight: 700; color: #1e3a5f;
                            text-align: center; margin-bottom: 4px; }
        .login-wrap .sub { font-size: 13px; color: #777; text-align: center;
                           margin-bottom: 18px; }
        </style>
        <div class="login-wrap">
          <div class="logo">BIRRAS — Consulta de bolsas</div>
          <div class="sub">Acceso restringido al personal del centro</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    clave = st.text_input("Contraseña", type="password", placeholder="Introduce la contraseña", key="birras_clave")
    if st.button("Entrar", type="primary", use_container_width=True):
        if _es_correcta(clave):
            st.session_state["birras_autenticado"] = True
            st.rerun()
        else:
            st.error("Contraseña incorrecta.")
    st.stop()