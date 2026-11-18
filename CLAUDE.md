# simracerap-web

## Contexto de trabajo persistente — LÉELO PRIMERO

Este proyecto guarda su contexto en archivos, no en la sesión de chat. **Al empezar CUALQUIER sesión,
antes de tocar nada:** cambia a la rama `dev`, haz pull y lee `docs/dev/STATE.md` (dónde se quedó el
trabajo y cuál es el siguiente paso); después, `docs/dev/USER_ACTIONS.md`, la última entrada de
`docs/dev/LOG.md` y la fase activa de `docs/dev/PLAN.md`. Las reglas completas están en
`docs/dev/PROTOCOL.md` y son obligatorias. **Al cerrar la sesión o al llegar a un hito:** actualiza
`STATE.md`, añade una entrada a `LOG.md`, marca lo hecho en `PLAN.md`, ejecuta el control de cierre
(`python scripts/close_check.py --context-dir docs/dev`), haz commit y push a `dev`.

**Hilos sin sesión (una rutina en la nube, un CI, `claude -p`, un subagente):** se trabaja en `dev`
(o en la rama `factory/<id>` del trabajo de la fábrica, con su rastro en `.factory/jobs/<id>/`), nunca
en otra salvo que se diga; antes de cambiar nada, lee `docs/dev/STATE.md` y, del tema que vas a tocar,
`docs/dev/DECISIONS.md` y `docs/dev/ARCHITECTURE.md`; el comando de verificación se declara en
`factory.json` (hoy no hay ninguno: P1, la puerta de la fábrica falla cerrada); un cambio en un `.html`
o un `.css` va siempre por la fábrica, que solo hace merge a `dev` y con el «sí» del usuario.
**`main` es lo que publica GitHub Pages:** nunca hagas push ni merge a `main` sin el «sí» explícito del
usuario, y nunca reescribas la historia de los archivos de contexto.

## Qué es este repositorio

La web pública de **SimRacerAP** (canal de YouTube de simracing en Live for Speed), hecha junto al
proyecto hermano `streamer-project`: portada (`index.html`), política de privacidad
(`privacidad.html`), condiciones de uso (`condiciones.html`) y la hoja de estilos (`style.css`).
HTML y CSS estáticos, sin compilación. Se publica en https://adrianpascarella.github.io/simracerap/.
**El repositorio es público:** no escribas nada privado (ni IP, ni tokens, ni datos personales).
Todo (chat, documentación y commits) va en castellano.
