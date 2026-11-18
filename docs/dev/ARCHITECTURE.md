# 🗺️ Arquitectura — simracerap-web
> Lo que es verdad hoy: qué existe, dónde vive, cómo se verifica y qué decisión explica cada límite.
> Se reescribe en su sitio en el cierre que lo cambia (PROTOCOL §4); nunca es un diario. Basado en la
> estructura y las convenciones, nunca en números de línea. Tope ~200 líneas.

## Componentes
- **Portada** — presenta el canal SimRacerAP y cómo se hace el contenido; enlaza al canal de YouTube
  y a las dos páginas legales · `index.html` · D4
- **Política de privacidad** — qué datos de Google usa la aplicación «streamer-project», dónde se
  guardan y cómo retirar el acceso · `privacidad.html` · texto escrito a mano: D6
- **Condiciones de uso** — uso de «streamer-project», YouTube, privacidad y cambios · `condiciones.html` · D6
- **Estilos** — una sola hoja para las tres páginas; colores como variables en `:root`, con su
  versión oscura en `prefers-color-scheme: dark`; columna de 720 px con 16 px de margen · `style.css` · D4
- **Configuración de Pages** — qué no se publica · `_config.yml` · D3
- **Herramientas del protocolo** — controles de inicio y cierre de sesión (copiados del plugin
  `agentic-protocol`) · `scripts/` · no forman parte de la web (D3)
- **Contexto de trabajo** — `docs/dev/` (este archivo y sus hermanos), `CLAUDE.md`, `factory.json` · D3

## Límites (lo que deliberadamente no se hace, y dónde está la línea)
- Sin generador, sin framework, sin JavaScript, sin dependencias — D4
- Pages solo sirve las páginas y el CSS; nada de `docs/`, `scripts/`, `factory.json`, `CLAUDE.md`,
  `.claude/`, `.factory/` — D3
- Nada privado en el repositorio (es público) — D3
- `main` solo con el «sí» del usuario; la fábrica llega hasta `dev` — D2, D5
- El texto legal no se toca sin petición del usuario — D6

## Convenciones
- Textos y documentación en castellano; clases y variables CSS en inglés — D1
- Cada página: `<!doctype html>`, `lang="es"`, `charset` utf-8, `viewport`, `<title>`, enlace a
  `style.css` y un `<footer>` que enlaza a las otras dos páginas con rutas relativas.
- Las páginas legales llevan en su `.lead` la fecha de «Última actualización»; si cambia su texto,
  cambia esa fecha.

## Cómo se publica
- GitHub Pages sirve la rama `main`, carpeta `/`, en https://adrianpascarella.github.io/simracerap/.
  Se trabaja en `dev`; pasar a `main` lo pide el usuario — D2.

## Cómo se verifica
- **No hay comando de verificación** (P1, D8): `factory.json` no declara `verify` y la puerta de la
  fábrica falla cerrada. W1 lo establece.
- Lo que valida el usuario (punto ciego, PROTOCOL Configuración): cómo se ve en un móvil y en un
  navegador de escritorio, y que la web publicada se actualizó tras un merge a `main`.

## Dónde vive el estado
- El contexto, en `docs/dev/`; la declaración para las herramientas, en `factory.json`; el rastro de
  cada trabajo de la fábrica, en `.factory/jobs/<id>/` en su rama `factory/<id>`.
- Lo hecho a mano que nunca se pierde: el texto de `privacidad.html` y `condiciones.html` — D6.
