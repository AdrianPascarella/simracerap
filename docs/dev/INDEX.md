# 🧭 Sistema de contexto — simracerap-web

> El contexto no vive en la sesión de chat. Vive aquí. Cada sesión **empieza leyendo estos archivos**
> y **termina actualizándolos**, para que la siguiente siga justo donde se quedó la anterior sin que
> tengas que repetir nada.

## 🚀 Frase de inicio (dila al empezar cada sesión)

> **«Empieza la sesión siguiendo tu protocolo.»**

Para cerrar: **«Cierra la sesión siguiendo el protocolo»**. El agente también cierra por su cuenta en
cada hito.

## Orden de lectura
1. **STATE.md** — dónde nos quedamos y cuál es el siguiente paso. Siempre se empieza aquí.
2. **USER_ACTIONS.md** — lo que te espera: qué probar, hacer, decidir o aportar.
3. **LOG.md** — la última entrada, para el contexto reciente.
4. **PLAN.md** — la fase activa y su lista.
5. **PROTOCOL.md** — las reglas (obligatorias).
6. **DIAGNOSIS.md** — problemas conocidos. Bajo demanda.
7. **DECISIONS.md** y **ARCHITECTURE.md** — el cerebro: qué se decidió y por qué, y el mapa de lo que
   existe. Por tema, antes de especificar, construir o revisar un cambio. Nunca al empezar.

## Los archivos
| Archivo | Qué es | Cuándo se actualiza |
|---|---|---|
| STATE.md | El relevo entre sesiones | Al final de cada sesión y en cada hito |
| USER_ACTIONS.md | Lo que necesita tus manos o tu criterio | Cuando el agente te necesita y cuando das un veredicto |
| LOG.md | Diario, solo de añadir | Al final de cada sesión |
| PLAN.md | Fases, listas y criterios de aceptación | Cuando se acaban tareas o cambia el plan |
| DIAGNOSIS.md | Problemas conocidos, con ID estable | Cuando se encuentra algo nuevo |
| DECISIONS.md | Decisiones vigentes, con lo descartado | Cuando se toma o se sustituye una decisión |
| ARCHITECTURE.md | El mapa de lo que existe y cómo se verifica | En el cierre que cambia cómo está hecho |
| PROTOCOL.md | Las reglas de trabajo | Cuando cambian las reglas |
| ../../factory.json | La verificación y las rutas protegidas, como datos | Cuando cambia la verificación |

> Estos archivos los escribe el agente, nunca a mano. Si algo está mal, díselo y lo arregla.
> **El repositorio es público:** nada de lo que se escriba aquí puede ser privado.
