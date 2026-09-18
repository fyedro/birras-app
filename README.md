# 🍺 BIRRAS

BIRRAS — Base de Interinos y Registro de Relevos, Asignaciones y Sustituciones.

Versión de consulta pública de BIRRAS desplegada en Streamlit Community Cloud
(todos los datos son públicos: PADI, Comunidad de Madrid, datos abiertos).

## Estructura

- `streamlit_app.py` — app Streamlit que muestra el dashboard en un iframe.
- `BIRRAS.html` — dashboard standalone (interfaz + lógica, sin datos).
- `data/cloud/part_*.js` — datos troceados por sentencias JS (< 80 MB por archivo,
  límite GitHub de 100 MB), que el navegador carga secuencialmente vía
  `raw.githubusercontent.com`.

## Regenerar el bundle

Los datos viven en el proyecto local `Docencia/BIRRAS`. Tras refrescar
sustituciones/listas, regenerar con:

```bash
cd Docencia/BIRRAS
python3 build_cloud_data.py
```

Esto reescribe `../birras-app/BIRRAS.html` y `../birras-app/data/cloud/`.
Después `git add` + `git push` en el repo `fyedro/birras-app` para actualizar
la app desplegada.

## Despliegue

App pública: `https://birras-app.streamlit.app` (Streamlit Community Cloud).
Cualquier push a `main` dispara el rebuild automático (1-3 min).

> Nota: es una vista de consulta. El botón "Actualizar sustituciones" queda
> deshabilitado en la nube (el refresco requiere el backend local).