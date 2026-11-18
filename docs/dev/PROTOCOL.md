# 📜 Protocolo de trabajo — simracerap-web

<!-- protocol-template-version: 4 -->

## Configuración

**Idiomas.** El chat, los mensajes de commit y la documentación de trabajo (`docs/dev`) van en
**castellano**. Los textos de la web también (las páginas son `lang="es"`). En el código se sigue lo
que ya hay: nombres de clases y variables CSS en inglés (`lead`, `button`, `--accent`), comentarios en
castellano. *Por qué: decisión del usuario en S1 (D1).*

**Qué es el proyecto.** La web pública de **SimRacerAP**, el canal de YouTube de simracing en Live for
Speed, hecha junto al proyecto hermano `streamer-project` (que detecta los momentos de las carreras y
los publica en el canal). Cuatro archivos estáticos en la raíz: `index.html` (portada),
`privacidad.html` y `condiciones.html` (las páginas legales de la aplicación «streamer-project») y
`style.css`. Sin compilación, sin dependencias, sin JavaScript (D4). El mapa, en `ARCHITECTURE.md`.

**El repositorio es PÚBLICO** (`AdrianPascarella/simracerap` en GitHub). **Regla: en este repositorio
no se escribe nada privado**: ni IP, ni puertos de servidores, ni tokens, contraseñas o claves, ni
rutas o datos personales más allá del nombre y el correo públicos que ya llevan los commits. Vale
para la web, para `docs/dev`, para `factory.json`, para los mensajes de commit y para el rastro de la
fábrica (`.factory/`). Lo privado de los hermanos se queda en los hermanos. *Por qué: todo lo que
entra en un repositorio público es público para siempre, aunque luego se borre (D3).*

**Ramas.** Se trabaja en **`dev`**. **`main` es lo que publica GitHub Pages** (rama `main`, carpeta
`/`, en https://adrianpascarella.github.io/simracerap/): **nunca se hace push ni merge a `main` sin el
«sí» explícito del usuario**, ni siquiera la fábrica. `_config.yml` (en la raíz) impide que Pages
sirva `docs/`, `scripts/`, `factory.json`, `CLAUDE.md`, `.claude/` y `.factory/`; si se añade otra
carpeta de trabajo, se añade también ahí (D2, D3). La protección de `main` se apoya en este protocolo,
no en GitHub.

**La fábrica** (plugin `factory`, D5): cada trabajo va en su rama `factory/<id>`, que sale de `dev`,
con su rastro en `.factory/jobs/<id>/`. Se publica con git (`"publish": "git"`: merge local y push;
GitHub es solo el remoto, sin pull requests ni `gh`). Autonomía **`review`**: el merge a `dev` lo hace
la fábrica solo cuando el usuario dice «merge» en el chat. **Qué va por la fábrica:** todo cambio en un
`.html` o un `.css` (`route_paths`); el contexto, los scripts y la configuración se cambian en `dev`.
Pasar `dev` a `main` (publicar la web) no es nunca un trabajo de la fábrica: lo pide el usuario.
Ninguna herramienta automática puede tocar `docs/dev/PROTOCOL.md`, `factory.json`, `.github/**` ni
`_config.yml` (`protected_paths`).

**Hermanos** (§17, declarados en `factory.json` como `siblings`; todos trabajan con LFS y se declaran
para compartir los descubrimientos): `ai-control` (`../lfs-ai-control`), `setups`
(`../lfs-setup-optimizer`), `streamer` (`../streamer-project`), `insim` (`../AP_LFS_InSim`) y `camera`
(`../lfs-free-camera`). Viven en la misma carpeta padre en los dos equipos. Sus rutas absolutas van en
`.claude/settings.local.json` (no se sube: `.gitignore`), con `siblings.py allow --root . --local`.

**Equipos.** Dos ordenadores con Windows; se hace pull y push en cada sesión. En los dos, el
repositorio vive en la carpeta de proyectos del usuario, junto a sus hermanos (las rutas absolutas no
se escriben aquí: el repositorio es público).
- **Principal:** Python 3.14. La cuenta activa global de `gh` es otra (a propósito) y **no se
  cambia**: el repositorio tiene su ayudante de credenciales local, que pide el token de la cuenta
  `AdrianPascarella` (§13).
- **Segundo:** el repositorio aún no está clonado ahí. Por lo que consta en el hermano
  `lfs-ai-control`: Python 3.14 y 3.12, y `git push` funciona con el ayudante global. Lo que difiera
  para esta web, se apunta aquí cuando se vea.

**Verificación.** **Hoy no hay ninguna** (P1): no hay tests ni un comando que pueda fallar, y
`factory.json` no declara `verify`, así que la puerta de la fábrica falla cerrada y todo cambio en la
web es una afirmación, no un resultado. Establecerla es la fase W1 de `PLAN.md` (por ejemplo, un
script de Python solo con la biblioteca estándar que detecte HTML mal formado, enlaces internos rotos
y metadatos que faltan). Cuando exista, se declara **como dato** en `factory.json` y aquí se describe
por lo que detecta. Sin lint ni prueba de humo.

**Punto ciego (lo que el agente no puede comprobar).** Queda para el usuario, y nunca se da por hecho:
- **Cómo se ve la web en un móvil real y en un navegador de escritorio** (claro y oscuro).
- **Que la web publicada se actualizó de verdad** después de un merge a `main` (que GitHub Pages
  terminó de publicar y sirve la versión nueva, y que no sirve los archivos de trabajo).

**Lo que nunca se pierde.** **El texto de las páginas legales, `privacidad.html` y `condiciones.html`**:
está escrito a mano y es el que respalda el uso de las API de YouTube por «streamer-project». Ningún
agente lo reescribe por iniciativa propia; solo cambia cuando el usuario lo pide, y el cambio se le
enseña palabra por palabra antes del commit. Antes de cualquier pull, checkout o stash, si tienen
cambios sin commit: copia, commit y push (D6).

**Permisos.** Sin preguntar: commit y push a `dev`. **Siempre con permiso:** cualquier cosa en `main`
(publica la web), borrar (archivos, ramas), y todo lo que se vea desde fuera (ajustes de GitHub,
Pages, issues, el canal).

**Identidad.** Los commits llevan **`AdrianPascarella <pascarellaadrian@gmail.com>`** (configurada
en local en el repositorio). La cuenta de GitHub es `AdrianPascarella`; no se usa `gh` para publicar
(publish git) y la cuenta activa global de `gh` no se toca. Si `git push` falla por autenticación, se
pone el ayudante de credenciales local igual que en `lfs-ai-control` (§13).

**Versión de la plantilla del protocolo absorbida:** 4 (`protocol-template-version: 4`, S1).

---

## §0 — Directiva principal

El contexto vive en archivos, no en la sesión de chat. Nunca des por hecho que recordarás algo de una
sesión a otra: si importa, va a `docs/dev`.
*Por qué: sin esto se empieza de cero cada sesión y el usuario reexplica el proyecto para siempre. Los
archivos en git sobreviven al modelo, a la herramienta y al equipo.*

## §1 — Los archivos son tuyos

Eres su único escritor. Que los lea una persona que no los escribió: castellano, prosa, sin
abreviaturas privadas. El usuario los lee para auditarte; nunca los edita.
*Por qué: un solo escritor evita formatos que derivan, IDs duplicados y versiones contradictorias.*

**Edítalos con bisturí, nunca «limpiando» un bloque.** Para añadir, sustituye solo la línea o el
encabezado donde va; nunca reescribas una sección entera. Lo tachado o lo que parece viejo no se poda
por iniciativa propia. Después de editar, mira `git diff` y confirma que no borraste nada que no
querías.
*Por qué: una reescritura en bloque es igual que una limpieza hasta que se come una línea que nadie
pidió quitar. Ni los tests ni `close_check.py` lo detectan.*

## §2 — Los archivos de contexto

| Archivo | Qué es | Tamaño |
|---|---|---|
| `STATE.md` | El relevo: dónde estamos, **el siguiente paso**, el puntero a las acciones del usuario | **Tope ~120 líneas.** |
| `USER_ACTIONS.md` | Todo lo que necesita al usuario: probar, hacer, decidir o aportar | Tarjetas pendientes + cerradas, **una línea cada una**. |
| `LOG.md` | Diario solo de añadir, una entrada por sesión | Sin límite. Al empezar solo se lee la última. |
| `PLAN.md` | Fases con listas y criterios de aceptación | Sin límite. Al empezar solo se lee la fase activa. |
| `DIAGNOSIS.md` | Problemas conocidos, con ID estable y estado | Referencia, bajo demanda. |
| `DECISIONS.md` | **El cerebro (1):** las decisiones vigentes, `D<n>`, con su porqué y lo descartado | Referencia, solo de añadir. Se lee **por tema antes de especificar, construir o revisar**. |
| `ARCHITECTURE.md` | **El cerebro (2):** el mapa de lo que es verdad hoy | Se reescribe en su sitio. Por tema. **Tope ~200 líneas.** |
| `PROTOCOL.md` | Estas reglas | **Se lee entero en cada sesión.** |
| `INDEX.md` | Punto de entrada | Mínimo. |

**El tope de `STATE.md` es una regla.** Si se desborda, lo más viejo pasa a `LOG.md`.
*Por qué: es el archivo que se lee en todas las sesiones; sin tope se vuelve un segundo diario.*

**Lo mismo para la cabecera y los cerrados de `USER_ACTIONS.md`:** la cabecera dice los contadores de
hoy y se **reescribe** cada sesión; una tarjeta cerrada queda en **una línea con fecha** y el veredicto
en pocas palabras; la cita entera va a `LOG.md`.

**IDs estables.** Problemas `P<n>` (`DIAGNOSIS.md`), fases `W<n>` y tareas `W<n>.<m>` (`PLAN.md`),
sesiones `S<n>` (`LOG.md`), acciones del usuario `U<n>` (`USER_ACTIONS.md`), decisiones `D<n>`. Un ID
nunca cambia de significado ni se reutiliza. El número de sesión lo pones tú al cerrar: la última de
`LOG.md` más uno.

**Una tarea hecha de `PLAN.md`** se marca y lleva `hecha en S<n> → LOG.md S<n>`, nada más.

**`DIAGNOSIS.md` sigue la disciplina contraria, a propósito:** al resolver un problema se **añade**
una línea `Resuelto (S<n>): <cómo y qué lo demostró>`; nunca se acortan la evidencia, el impacto ni la
acción. *Por qué: cada entrada se lee sola, por ID, sin abrir `LOG.md`.*

**La regla de fondo:** `LOG.md` es el diario del proceso (cuándo pasó); lo que tiene ID por tema
(`P<n>`, `D<n>`) es referencia (qué es verdad hoy). Cada hecho vive en uno de los dos, nunca en ambos.

**El cerebro (`DECISIONS.md` + `ARCHITECTURE.md`).** Una decisión va a `DECISIONS.md` cuando un agente
futuro podría deshacerla sin darse cuenta de que estaba decidida. Una entrada por decisión, con lo
decidido, el porqué, las alternativas descartadas con su porqué, la sesión y lo que toca. **Solo de
añadir:** la que deja de valer gana `SUSTITUIDA (S<n>) por D<m>`. `ARCHITECTURE.md` es el mapa que
señala cada `D<n>`, se reescribe en el cierre que cambia la realidad. **Nadie los lee al empezar**;
quien va a especificar, construir o revisar un cambio lee antes las entradas de **su tema**.
*Por qué: una decisión que solo vive en el diario se vuelve a tomar, a menudo al revés.*

**Presupuesto de lectura al empezar.**

| Entero | En parte | NO al empezar |
|---|---|---|
| `STATE.md` · `USER_ACTIONS.md` · este archivo | la **última entrada** de `LOG.md` · la **fase activa** de `PLAN.md` | el resto de `LOG.md` y `PLAN.md` · `DIAGNOSIS.md` (por ID) · `DECISIONS.md` y `ARCHITECTURE.md` (por tema) |

*Por qué: `LOG.md` crece sin límite; leerlo entero quema la ventana en historia que no se usa. Si un
archivo que se lee entero ya no cabe, el defecto está en el archivo.*

**Lo mismo para las secciones de este archivo:** la regla y un porqué corto; la historia que la
justificó, en `LOG.md`, citada por sesión. Un procedimiento detallado y poco frecuente puede salir a
una skill del proyecto (`.claude/skills/<nombre>/SKILL.md`), pero nunca un aviso que haya que leer
antes de que pase lo que avisa; y solo después de comprobar que el entorno la anuncia solo.

## §3 — INICIO de sesión

1. Estar en `dev`.
2. **Confirmar la identidad antes de nada con git:** la efectiva (`git config user.name` /
   `user.email`) debe ser `AdrianPascarella <pascarellaadrian@gmail.com>`. Nunca mirar el autor del
   último commit. Si no coincide, arreglarlo en local (nunca `--global`). Sin preguntar. La cuenta
   activa de `gh` no se cambia (ver Configuración).
3. **Proteger `privacidad.html` y `condiciones.html` antes de cualquier pull, checkout o stash:** si
   tienen cambios sin commit, copia, commit y push. Sin preguntar.
4. `git pull` (se trabaja en dos equipos).
5. Leer `STATE.md`.
6. Leer `USER_ACTIONS.md`: cuántas pendientes y cuál bloquea (§7).
7. Leer la última entrada de `LOG.md` y la fase activa de `PLAN.md`.
8. Contrastar con la realidad (`git status`, `git log --oneline -5`). Si no cuadran, gana la realidad.
9. La comparación de versión de la plantilla del protocolo la hace el hook de inicio del plugin
   `agentic-protocol`; si dice que este archivo va por detrás, ofrecer el modo UPGRADE.
10. Resumir en 2–3 líneas dónde estamos y qué propones, **cuántas acciones esperan al usuario y cuál
    bloquea**. Después, actuar.

Los pasos 2, 4 y 8 se hacen de una vez con:
`python scripts/session_start_check.py --git-identity "AdrianPascarella <pascarellaadrian@gmail.com>" --branch dev`
y el 7 con `python scripts/ctx_log_last.py` y `python scripts/ctx_plan_active.py`. Si faltan los
scripts, cada paso se hace a mano: la prosa es el contrato.

**Un hilo sin sesión** (rutina en la nube, CI, `claude -p`, subagente) solo lee `CLAUDE.md`, y por eso
su gancho lleva este apartado comprimido: la rama, qué leer antes de cambiar nada, dónde está la
verificación y lo que nunca hace (merge a `main`, reescribir la historia del contexto).

*Por qué: una identidad equivocada se publica en silencio y es permanente; el texto legal hecho a mano
es lo único que el repositorio no puede regenerar; una deuda con el usuario que no se enumera no se
paga; una sesión que acabó mal deja documentos que mienten.*

## §4 — CIERRE de sesión (y en cada hito)

1. Actualizar `STATE.md`: estado, siguiente paso concreto, lo que quedó a medias, el puntero a las
   acciones pendientes. Respetar el tope.
2. **Todo lo pedido al usuario en la sesión existe como tarjeta `U<n>`** antes de cerrar, con los
   contadores de la cabecera al día.
3. Añadir una entrada a `LOG.md`: lo hecho, decisiones con su porqué, verificación, commits y los
   veredictos del usuario. Una decisión que seguirá valiendo el mes que viene gana su `D<n>`.
4. Marcar lo hecho en `PLAN.md`; añadir las tareas descubiertas. Un defecto encontrado va a
   `DIAGNOSIS.md` con un `P<n>` nuevo. Si el cierre cambió cómo está hecho el proyecto, reescribir lo
   afectado de `ARCHITECTURE.md`; si cierra una fase que cambia lo que el proyecto es (cómo se publica,
   cómo se verifica), actualizar la Configuración de este archivo en el mismo cierre.
5. Ejecutar `python scripts/close_check.py --context-dir docs/dev` y **pegar su salida**. Si falla, se
   arregla antes de dar el cierre por hecho; un `WARN` de algo que no se comprobó se dice.
6. Commit y push a `dev` (nunca acabar con trabajo sin subir).
7. **Terminar el informe con lo que le toca al usuario**: las tarjetas pendientes, en el orden
   recomendado.

Con `"orchestrator": true` en `factory.json` (apagado; es del usuario), un subagente hace los pasos
1–6 y el control con `--delegated`; el hilo principal pega su salida y hace el 7.

**Cerrar barato:** recortar borrando bloques enteros que ya están en `LOG.md`, nunca reescribiendo
prosa; el control, una vez al final; un solo commit con su push.

## §5 — Tocar lo frágil: la red de seguridad

- Mirar `DIAGNOSIS.md` antes de tocar un archivo frágil.
- **Tests de caracterización primero** sobre lo que se va a cambiar; refactorizar solo con la red puesta.
- **Ver la red en ROJO** contra el código viejo. *Por qué: un test que nunca falló es decoración.*
- Nunca cambiar comportamiento y estructura en el mismo paso.
- Mejor extraer con seguridad que reescribir, y **demostrar** el movimiento.
- **Nunca debilitar ni borrar un test para que pase.** Solo se cambia un test que se demuestra
  equivocado, y se dice en el informe y en `LOG.md`.

Mientras no haya verificación (P1), esta red no se puede hacer cumplir: cada cambio se describe como
lo que es, una afirmación pendiente de que el usuario la vea.

## §6 — Definición de hecho

1. El comando de verificación de `factory.json` pasa, y se pega su salida real (hoy no existe: P1).
2. Se dice si cambió algo que se ve desde fuera (textos, enlaces, direcciones).
3. Si toca el punto ciego (§7), **no** está hecho: queda pendiente de validar.

Informar con honestidad: si algo falla, con la salida real; si se saltó un paso, se dice.

**Cuando ningún comando puede verificar el entregable** (un documento, un plan, este protocolo):
recorrer su ciclo de vida entero en lugar de releerlo; buscar un lector que no sepa lo que se quiso
decir; y si el mismo contenido vive en dos sitios, derivar uno del otro o comprobarlos con un comando.
*Por qué: lo que fallan estos artefactos son ausencias, y una ausencia no se ve al releer.*

## §7 — Lo que solo puede hacer el usuario: el punto ciego y la cola de acciones

El punto ciego (Configuración) es lo que el agente **no puede comprobar**. Además, el usuario hace lo
que el agente no puede, decide lo que solo él decide y aporta lo que el agente no tiene. **Todo vive en
`USER_ACTIONS.md`; nada pedido al usuario existe solo en el chat.**

Una tarjeta por acción, con ID estable `U<n>`:

```markdown
### U3 — <título>          ⏳ · bloquea: <nada | W1.2 | el merge a main> · abierta en S<n>
**Tipo:** validar | hacer | decidir | aportar          **Tiempo:** ~5 min
**Por qué:** <qué depende de esto>
**Pasos:**
  1. <concretos y copiables>
**Resultado esperado:** <qué pasa si funciona>
**Señales de fallo:** <cómo se ve cuando no>
**Si falla, dime:** <qué necesitas oír para actuar>
```

- Un campo que no se sabe se declara («Resultado esperado: no lo sé; dime qué ves»), nunca se omite.
- La cabecera del archivo dice en una línea cuántas hay, cuál bloquea (🚧) y el orden recomendado.
- `STATE.md` lleva un puntero a este archivo, nunca una copia.
- **El agente nunca cierra una tarjeta; la cierra el usuario** con su veredicto, que va a `LOG.md`; la
  tarjeta queda en una línea en «Cerradas».
- **No se abre una tarjeta de validar antes de que lo validado esté en manos del usuario.** Para esta
  web: la tarjeta de «cómo se ve en la web publicada» espera al merge a `main` y a que Pages termine.
  Antes de aceptar un veredicto, comprobar que lo que vio lleva el cambio (el commit que sirve Pages).

**Bloquear es blando: parar y preguntar, nunca negarse.** El bloqueo se declara en la tarjeta. Una
tarea que toca lo mismo que una tarjeta pendiente de validar queda bloqueada por defecto. Al topar con
un bloqueo, parar antes de escribir nada, nombrar la tarjeta y recomendar el orden. El usuario siempre
puede saltárselo: se apunta en la tarjeta y en `LOG.md`, y no se vuelve a sacar.

**Recordarlo en cuatro momentos:** al empezar, al chocar una tarea con una tarjeta, cuando la cola pasa
de ~4 y al cerrar.

## §8 — Diagnosticar antes de arreglar

Reproducir o medir primero; enunciar la hipótesis e intentar matarla; contar las hipótesis refutadas;
nombrar la causa raíz; buscar la regla que ya existe en el código antes de inventar otra.

## §9 — Riesgo y reversibilidad

- Un cambio arriesgado va en su propio commit, para poder revertirlo solo.
- Nunca destruir el texto de las páginas legales.
- Antes de algo destructivo o difícil de deshacer (borrar, forzar un push, tocar `main`, cualquier
  cosa que se vea desde fuera), confirmar con el usuario. Un permiso dado en un contexto no vale para
  el siguiente.
- Antes de matar procesos «huérfanos», mirar qué son.

## §10 — Decisiones

Cada decisión relevante, con su porqué y lo descartado; la que seguirá valiendo va a `DECISIONS.md`
como `D<n>` y `LOG.md` la cita. Al presentar opciones, marcar la recomendada y justificarla. Con
información suficiente, actuar; no preguntar lo que se puede averiguar.

## §11 — Comunicación

Hablar en castellano. El usuario es el autor del proyecto: ir al grano, empezar por el resultado. Al
acabar una tarea, recomendar si seguir en esta sesión o abrir otra; si otra, comprobar sin que lo pida
que puede empezar limpia (control de cierre en verde, `STATE.md` con el siguiente paso).

## §12 — Alcance

Hacer solo lo pedido; las ideas, a «Ideas» en `PLAN.md`. Si el alcance crece, parar y decirlo con una
recomendación. Una petición fuera del plan es legítima: se aparca la fase en `STATE.md` y se apunta en
`LOG.md`.

## §13 — Cicatrices

Las formas en que este equipo o estas herramientas ya han dañado el trabajo. Respetarlas; **la que
causes tú, añádela**.

- **Dos cuentas de GitHub en el equipo principal.** La cuenta activa global de `gh` es otra, a
  propósito, y no se cambia. Este repositorio lleva en su `.git/config` un ayudante de credenciales
  local para `https://github.com` que responde con el usuario `AdrianPascarella` y la contraseña de
  `gh auth token --user AdrianPascarella`, el mismo que tiene `lfs-ai-control` (se ve con
  `git -C ../lfs-ai-control config --local --get-regexp credential`). Si en un clon nuevo `git push`
  falla por autenticación, se copia ese ayudante en local (nunca `--global`).

## §14 — Guías

Cuando una tarea recurrente cueste mucho de orientar, escribir una guía basada en estructura y
convenciones, nunca en números de línea, fuera del archivo que se carga siempre.

## §15 — Instrucciones permanentes (esta sección crece)

Las reglas que el usuario da para todas las sesiones futuras («siempre X», «nunca Y», «a partir de
ahora Z», o una corrección que no debe repetirse) **son configuración, no chat**. Al recibir una:
escribirla aquí con fecha y, en lo posible, con sus palabras; decirle que se escribió y dónde;
aplicarla desde ese momento. Si no se sabe si es permanente, preguntar.

| Lo que llega | Dónde va |
|---|---|
| Una regla de cómo trabajar, para siempre | Aquí (§15) |
| Un daño de este equipo o de las herramientas | §13 |
| Algo que el usuario debe probar, hacer, decidir o aportar | `USER_ACTIONS.md`, `U<n>` |
| Un veredicto | Cerrar la `U<n>` y apuntarlo en `LOG.md` |
| Una decisión de diseño y sus razones | `DECISIONS.md`, `D<n>` |
| Cómo está hecho el proyecto | `ARCHITECTURE.md` |
| Dónde está el trabajo | `STATE.md` |
| Una tarea o una idea | `PLAN.md` |
| Un defecto | `DIAGNOSIS.md`, `P<n>` |

*(Ninguna todavía.)*

## §16 — Mantener vivo el sistema

El sistema lo mantiene el agente. Si cambia la realidad (una verificación nueva, una trampa, una rama,
otro punto ciego), se actualiza este archivo y se dice. Si una regla resulta equivocada para este
proyecto, se propone cambiarla con su razón; nunca se deja de cumplir en silencio. El usuario solo
tiene que hablar con el agente.

## §17 — Repositorios hermanos

Los hermanos están en `factory.json` (`siblings`); la línea de inicio de sesión los nombra y da la
ruta de `siblings.py` (viene en el plugin `agentic-protocol`). Cuando una tarea necesita un cambio en
un hermano, se hace, no se deja una nota:

1. `siblings.py enter <nombre>`: comprueba que el árbol está limpio y sin sesión viva, cambia a la rama
   de trabajo de ese repositorio, hace pull e imprime su `STATE.md` y su verificación.
2. Se trabaja allí **con su protocolo** (sus reglas, su rama, su verificación; si tiene la fábrica y la
   ruta va por ella, como trabajo de su fábrica), con su entrada en su `LOG.md` diciendo de dónde se
   viene; commit y push a su rama de trabajo.
3. **Nunca push ni merge a una rama que publica, ni una versión, sin el «sí» del usuario.**
4. `siblings.py leave <nombre>` pasa su control de cierre; el `LOG.md` de aquí dice qué se hizo allí,
   por commit.

Si `enter` se niega, se escribe en el `SIDECAR.md` del hermano.
**Ojo, este repositorio es público y los hermanos no siempre:** lo que se traiga de un hermano a esta
web o a estos documentos pasa antes por la regla de «nada privado» de la Configuración.
