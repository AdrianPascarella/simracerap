# 🩺 Diagnóstico — simracerap-web
> Revisión inicial: 2026-11-18 (S1). Se actualiza cuando se encuentra algo nuevo.

## Veredicto
Una web pequeña y sana: cuatro archivos estáticos, bien formados a simple vista, con modo oscuro y
diseño adaptable. La deuda está toda en que **nada la comprueba**: ni un test, ni un control de
enlaces, ni la confirmación de que la web publicada es la última.

## ✅ Sano (no tocar sin motivo)
- Las tres páginas comparten estructura y hoja de estilos; enlaces internos relativos.
- `style.css` con variables de color en `:root` y versión oscura; columna de 720 px con margen de 16 px.
- El texto legal escrito a mano (D6).

## 🔴 Gravedad alta
### P1 — No hay verificación   [ABIERTO]
- **Evidencia:** el repositorio solo tiene `index.html`, `privacidad.html`, `condiciones.html` y
  `style.css` (commit `6f28a48`): sin tests, sin scripts de comprobación, sin CI. `factory.json` no
  declara `verify` (D8).
- **Impacto:** la puerta de la fábrica falla cerrada, así que ningún trabajo puede pasar solo por
  ella; y un enlace roto, una etiqueta mal cerrada o un metadato que falta llegarían a la web sin que
  nada lo avise. Hasta que exista un comando que pueda fallar, las reglas de la red de seguridad (§5)
  no se pueden hacer cumplir y cada cambio es una afirmación, no un resultado.
- **Acción:** W1 de `PLAN.md`: un script de Python solo con la biblioteca estándar
  (`scripts/verify.py`) que falle con HTML mal formado, enlaces internos o anclas que no existen,
  páginas sin `lang`, `charset`, `viewport` o `<title>`, y archivos de trabajo que `_config.yml` no
  excluye; demostrado en rojo y declarado en `factory.json` con el «sí» del usuario.

## 🟠 Gravedad media
### P2 — Nada confirma que la web publicada es la última   [ABIERTO]
- **Evidencia:** Pages publica `main` sin aviso visible desde aquí; no hay CI ni comprobación tras el
  merge. Es el punto ciego que el usuario declaró en S1.
- **Impacto:** un merge a `main` puede no llegar a publicarse (Pages en error o en caché) y nadie se
  entera hasta que alguien mira la web.
- **Acción:** de momento, una tarjeta de validar para el usuario después de cada merge a `main`; más
  adelante (idea en `PLAN.md`), un script que compare la web publicada con `main`.

## 🟡 Gravedad baja
### P3 — `_config.yml` aún no está en `main`   [ABIERTO]
- **Evidencia:** `_config.yml` se creó en `dev` en S1; `main` (lo publicado) sigue en `6f28a48`, sin él.
- **Impacto:** hoy no pasa nada (`main` no tiene `docs/` ni archivos de trabajo). Pero el primer merge
  de `dev` a `main` llevará a la vez los documentos y `_config.yml`, y con él Pages empezará a
  procesar la web con Jekyll; si el `exclude` fallara, los documentos de trabajo saldrían en la web.
- **Acción:** en el primer merge a `main` (con el «sí» del usuario), comprobar después que
  `https://adrianpascarella.github.io/simracerap/docs/dev/STATE.md` y `.../factory.json` dan 404 y que
  las tres páginas se ven igual.
