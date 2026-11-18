# 🧠 Decisiones — simracerap-web
> Las decisiones vigentes, una entrada cada una, la más nueva al final. Solo de añadir: una decisión
> que deja de valer nunca se borra; gana una línea SUSTITUIDA y la entrada nueva dice qué cambió. Se
> leen por tema (buscando la línea «Toca» desde las rutas que vas a cambiar), nunca enteras.

### D1 — Todo en castellano   [VIGENTE]
- **Decisión:** el chat, la documentación de trabajo, los commits y los textos de la web van en
  castellano. En el código se sigue lo que ya hay: clases y variables CSS en inglés, comentarios en
  castellano.
- **Por qué:** el canal y su público son hispanohablantes; el usuario trabaja en castellano.
- **Descartado:** documentación en inglés — nadie la lee aquí, y la web ya es en castellano · renombrar
  las clases CSS al castellano — cambia código por gusto, sin ganar nada.
- **Tomada:** S1 (2026-11-18; el usuario).
- **Toca:** `docs/dev/`, mensajes de commit, `index.html`, `privacidad.html`, `condiciones.html`, `style.css`.

### D2 — `dev` para trabajar, `main` publica   [VIGENTE]
- **Decisión:** se trabaja en `dev`. `main` es la rama que sirve GitHub Pages (carpeta `/`): nunca se
  hace push ni merge a `main` sin el «sí» explícito del usuario, tampoco la fábrica.
- **Por qué:** cada cambio en `main` se publica al momento en una web pública; el usuario quiere ver
  qué sale antes de que salga. Elegido por el usuario: «dev + main publica, sin docs en la web».
- **Descartado:** trabajar directamente en `main` — cada commit de documentación o a medias saldría a
  la web · publicar Pages desde otra rama o desde `/docs` — obliga a reconfigurar Pages y mezcla la
  carpeta de documentación de trabajo con la web.
- **Tomada:** S1 (2026-11-18; el usuario).
- **Toca:** ramas, `git push`, la publicación en GitHub Pages, la fábrica (base `dev`).

### D3 — La documentación de trabajo no se publica y no lleva nada privado   [VIGENTE]
- **Decisión:** `_config.yml` (en `dev`, y en `main` cuando el usuario publique) excluye de Pages
  `docs/`, `scripts/`, `factory.json`, `CLAUDE.md`, `.claude/` y `.factory/`. Como el repositorio es
  público, en él no se escribe nada privado: ni IP, ni tokens, ni rutas o datos personales más allá
  del nombre y el correo públicos de los commits.
- **Por qué:** la web solo son las páginas; los documentos de trabajo no deben aparecer en la
  dirección pública. Y aunque Pages no los sirva, cualquiera puede leer el repositorio en GitHub.
- **Descartado:** un repositorio privado aparte para los documentos — dos repositorios para cuatro
  archivos, y el contexto lejos del código · confiar solo en que Jekyll ignora lo que empieza por
  punto — no cubre `docs/`, `scripts/`, `factory.json` ni `CLAUDE.md`.
- **Tomada:** S1 (2026-11-18; el usuario).
- **Toca:** `_config.yml`, `docs/dev/`, `factory.json`, `CLAUDE.md`, todo lo que se escribe en el repositorio.

### D4 — Web estática, sin compilación ni dependencias   [VIGENTE]
- **Decisión:** la web son HTML y CSS escritos a mano en la raíz, sin generador, sin framework, sin
  JavaScript y sin dependencias; GitHub Pages los sirve tal cual.
- **Por qué:** son cuatro páginas que cambian poco; cualquier herramienta añadiría algo que mantener
  sin aportar nada.
- **Descartado:** un generador de sitios (Jekyll con plantillas, Hugo, un framework) — más piezas que
  páginas · copiar la cabecera y el pie con JavaScript — rompe sin JavaScript y no ahorra casi nada.
- **Tomada:** S1 (2026-11-18; constatado en la auditoría, confirmado por el usuario).
- **Toca:** `index.html`, `privacidad.html`, `condiciones.html`, `style.css`, `_config.yml`.

### D5 — La fábrica, con revisión del usuario y solo hasta `dev`   [VIGENTE]
- **Decisión:** la fábrica (`factory.json`) trabaja en castellano, con autonomía `review` (el merge
  lo hace la fábrica solo cuando el usuario dice «merge» en el chat), publica con git (merge local y
  push, sin pull requests), su base es `dev`, y todo cambio en un `.html` o un `.css` va por ella
  (`route_paths`). No puede tocar `docs/dev/PROTOCOL.md`, `factory.json`, `.github/**` ni
  `_config.yml`. Pasar `dev` a `main` nunca es un trabajo de la fábrica.
- **Por qué:** lo que se cambia en la web acaba siendo público; el usuario quiere decidir cada merge,
  y `main` solo lo toca él.
- **Descartado:** autonomía `merge` — la fábrica uniría sin que el usuario lo vea, y la web es pública ·
  publicar como pull request — nadie más revisa en GitHub; git basta · que la fábrica una a `main` —
  publicaría sin el «sí» del usuario.
- **Tomada:** S1 (2026-11-18; el usuario).
- **Toca:** `factory.json`, `.factory/`, ramas `factory/<id>`, `*.html`, `*.css`.

### D6 — El texto legal es intocable salvo petición del usuario   [VIGENTE]
- **Decisión:** el texto de `privacidad.html` y `condiciones.html` está escrito a mano y es lo que
  nunca se pierde. Ningún agente lo reescribe, resume ni «mejora» por iniciativa propia; solo cambia
  cuando el usuario lo pide, y el texto nuevo se le enseña entero antes del commit. Antes de un pull,
  checkout o stash, si tiene cambios sin commit, se guarda y se sube.
- **Por qué:** es el texto que respalda el uso de las API de YouTube por «streamer-project»; un
  cambio de palabras puede cambiar lo que promete.
- **Descartado:** meterlos en `protected_paths` — impediría también a la fábrica aplicar un cambio
  que el usuario sí pide; la protección va en el protocolo y en la revisión.
- **Tomada:** S1 (2026-11-18; el usuario).
- **Toca:** `privacidad.html`, `condiciones.html`.

### D7 — Hermanos declarados para compartir lo descubierto   [VIGENTE]
- **Decisión:** `factory.json` declara como hermanos `ai-control`, `setups`, `streamer`, `insim` y
  `camera`, con rutas relativas en la misma carpeta padre en los dos equipos.
- **Por qué:** todos trabajan con LFS; si un descubrimiento aquí afecta a otro, se va a cambiarlo allí
  con su protocolo (PROTOCOL §17) en lugar de dejar una nota.
- **Descartado:** solo `streamer-project` — el usuario quiere los cinco.
- **Tomada:** S1 (2026-11-18; el usuario).
- **Toca:** `factory.json` (`siblings`), `.claude/settings.local.json`.

### D8 — Sin verificación inventada   [VIGENTE]
- **Decisión:** mientras no haya un comando que pueda fallar, `factory.json` no declara `verify`; la
  puerta de la fábrica falla cerrada. Establecerla es la primera fase (W1, P1).
- **Por qué:** un `verify` falso haría pasar cualquier cosa y escondería que nada se comprueba.
- **Descartado:** declarar algo que siempre pasa (`echo ok`) — mentiría a la puerta · instalar un
  validador externo ya — el usuario no pidió instalar nada; primero se propone en W1.
- **Tomada:** S1 (2026-11-18; el usuario).
- **Toca:** `factory.json`, `scripts/`.
