# 🗺️ Plan — simracerap-web
> Fases con criterios de aceptación. `[x]` = hecho. `P<n>` remite a DIAGNOSIS.md. Cada tarea lleva su
> ID estable `W<n>.<m>`, asignado una vez, en orden, nunca reutilizado ni renumerado.

## W1 — Establecer un comando de verificación   ⏳ ACTIVA
**Objetivo:** que exista un comando que pueda fallar y que la fábrica lo use como puerta (P1, D8).

- [ ] **W1.1** — Proponer al usuario qué comprueba el script (HTML bien formado, enlaces internos y anclas, `lang`/`charset`/`viewport`/`<title>`, `_config.yml` excluye lo de trabajo) y que sea Python con la biblioteca estándar, sin instalar nada          bloqueado por: nada
- [ ] **W1.2** — Escribir `scripts/verify.py` con sus pruebas y verlo en ROJO con un enlace roto y una etiqueta sin cerrar puestos a propósito (en una copia, nunca en las páginas)          bloqueado por: W1.1
- [ ] **W1.3** — Declararlo como `verify` en `factory.json` (ruta protegida: con el «sí» del usuario) y describirlo por lo que detecta en PROTOCOL Configuración y en `ARCHITECTURE.md`          bloqueado por: W1.2
- [ ] **W1.4** — Pasar la puerta de la fábrica contra `dev` (`gate.py --base dev`) y que salga en verde          bloqueado por: W1.3

**Criterios de aceptación:** `factory.json` declara `verify`; el comando pasa sobre la web de hoy, se
ha visto fallar con un fallo puesto a propósito, y la puerta de la fábrica sale en verde contra `dev`.

## W2 — Primera publicación con la configuración nueva   ⏸ EN ESPERA
**Objetivo:** que `main` lleve `_config.yml` y la web publicada siga igual, sin documentos de trabajo (P3).

- [ ] **W2.1** — Cuando el usuario lo pida, merge de `dev` a `main` y push          bloqueado por: el «sí» del usuario
- [ ] **W2.2** — Tarjeta de validar: la web publicada se ve igual y no sirve `docs/` ni `factory.json`          bloqueado por: W2.1

**Criterios de aceptación:** el usuario confirma que las tres páginas se ven igual y que las rutas de
trabajo dan 404 en la web publicada.

## Ideas (aparcadas, sin compromiso)
- Un script que compare lo que sirve la web publicada con `main` tras un merge (P2) — antes, W1.
- Comprobar también los enlaces externos (YouTube, Google) — necesita red; la verificación de W1 debe
  funcionar sin ella.
