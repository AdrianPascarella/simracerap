# 📓 Diario — simracerap-web
<!-- Solo de añadir, lo más nuevo arriba. Una entrada por sesión. -->

## S1 — 2026-11-18 — Instalación del protocolo de trabajo y de la fábrica
**Hecho:** instalación FRESH del protocolo de trabajo (agentic-protocol 4.4.0, plantilla 4) y de la
fábrica (0.23.0), hecha por un subagente con las respuestas del usuario a la entrevista. Rama `dev`
creada desde `main` (`6f28a48`). Escritos: `docs/dev/` (INDEX, STATE, USER_ACTIONS, LOG, PLAN,
DIAGNOSIS, DECISIONS, ARCHITECTURE, PROTOCOL), `CLAUDE.md` con el gancho de inicio, `factory.json`
(idioma, autonomía `review`, publicación git, rutas protegidas, `route_paths`, hermanos; sin
`verify`), `_config.yml` (lo que Pages no publica), `.gitignore`, `.claude/settings.json` (plugins,
actualización automática del marketplace, variables de entorno) y los scripts de inicio y cierre en
`scripts/`. Los hermanos se añadieron a `.claude/settings.local.json` con `siblings.py allow --local`
(no se sube). Sin tocar la web.
**Diagnóstico:** sin verificación (P1, alta); nada confirma que la web publicada es la última (P2,
media); `_config.yml` aún no está en `main` (P3, baja).
**Decisiones:** D1 (castellano), D2 (`dev` trabaja, `main` publica), D3 (los documentos no se publican
y no llevan nada privado), D4 (web estática), D5 (fábrica con revisión, hasta `dev`), D6 (texto legal
intocable salvo petición), D7 (hermanos), D8 (sin verificación inventada).
**Verificación:** no hay comando de verificación (P1). `setup_check.py check` y `close_check.py`, en
el informe de la instalación.
**Commits:** el de la instalación, en `dev`.
