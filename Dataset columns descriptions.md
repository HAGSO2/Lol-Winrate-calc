| Columna            | Descripción                                                                   |

| ------------------ | ----------------------------------------------------------------------------- |

| `gameid`           | Identificador único de la partida.                                            |

| `datacompleteness` | Nivel de completitud de los datos (`complete`, `partial`, etc.).              |

| `url`              | URL de referencia de donde se extrajeron los datos de la partida.             |

| `league`           | Liga o competición donde se disputó la partida (LCK, LPL, LEC, Worlds, etc.). |

| `year`             | Año correspondiente a la temporada competitiva.                               |

| `split`            | División de la temporada (Spring, Summer, Winter, etc.).                      |

| `playoffs`         | Indica si la partida pertenece a playoffs (1) o fase regular (0).             |

| `date`             | Fecha y hora de la partida.                                                   |

| `game`             | Número del mapa dentro de una serie (Bo3, Bo5, etc.).                         |

| `patch`            | Versión del juego utilizada en la partida.                                    |

Información del participante

| Columna         | Descripción                                                               |

| --------------- | ------------------------------------------------------------------------- |

| `participantid` | Identificador del participante dentro de la partida.                      |

| `side`          | Lado del mapa (`Blue` o `Red`).                                           |

| `position`      | Rol del jugador (`top`, `jng`, `mid`, `bot`, `sup`).                      |

| `playername`    | Nombre del jugador profesional.                                           |

| `playerid`      | Identificador único del jugador en Oracle's Elixir.                       |

| `teamname`      | Nombre del equipo.                                                        |

| `teamid`        | Identificador único del equipo.                                           |

| `firstPick`     | Indica si el equipo tuvo la primera selección del draft (1 = sí, 0 = no). |

Draft

| Columna         | Descripción                                                          |

| --------------- | -------------------------------------------------------------------- |

| `champion`      | Campeón seleccionado por el jugador.                                 |

| `ban1`-`ban5`   | Campeones baneados por el equipo durante el draft.                   |

| `pick1`-`pick5` | Orden de selección de campeones del equipo (cuando está disponible). |

Resultado general

| Columna      | Descripción                                          |

| ------------ | ---------------------------------------------------- |

| `gamelength` | Duración de la partida en segundos.                  |

| `result`     | Resultado de la partida (1 = victoria, 0 = derrota). |

Estadísticas de combate

| Columna       | Descripción                      |

| ------------- | -------------------------------- |

| `kills`       | Asesinatos realizados.           |

| `deaths`      | Muertes sufridas.                |

| `assists`     | Asistencias.                     |

| `teamkills`   | Total de asesinatos del equipo.  |

| `teamdeaths`  | Total de muertes del equipo.     |

| `doublekills` | Número de dobles asesinatos.     |

| `triplekills` | Número de triples asesinatos.    |

| `quadrakills` | Número de cuádruples asesinatos. |

| `pentakills`  | Número de pentakills.            |

Primera sangre

| Columna            | Descripción                          |

| ------------------ | ------------------------------------ |

| `firstblood`       | Participó en la primera sangre.      |

| `firstbloodkill`   | Consiguió la primera sangre.         |

| `firstbloodassist` | Dio asistencia en la primera sangre. |

| `firstbloodvictim` | Fue la víctima de la primera sangre. |

Ritmo de asesinatos

| Columna    | Descripción                                        |

| ---------- | -------------------------------------------------- |

| `team kpm` | Asesinatos del equipo por minuto.                  |

| `ckpm`     | Asesinatos combinados de ambos equipos por minuto. |

Objetivos neutrales

| Columna                  | Descripción                                                        |

| ------------------------ | ------------------------------------------------------------------ |

| `firstdragon`            | El equipo obtuvo el primer dragón.                                 |

| `dragons`                | Dragones conseguidos por el equipo.                                |

| `opp\_dragons`            | Dragones obtenidos por el rival.                                   |

| `elementaldrakes`        | Dragones elementales obtenidos.                                    |

| `opp\_elementaldrakes`    | Dragones elementales del rival.                                    |

| `infernals`              | Dragones infernales obtenidos.                                     |

| `mountains`              | Dragones de montaña obtenidos.                                     |

| `clouds`                 | Dragones de viento obtenidos.                                      |

| `oceans`                 | Dragones oceánicos obtenidos.                                      |

| `chemtechs`              | Dragones Chemtech obtenidos.                                       |

| `hextechs`               | Dragones Hextech obtenidos.                                        |

| `dragons (type unknown)` | Dragones cuyo tipo no pudo determinarse.                           |

| `elders`                 | Dragones ancianos obtenidos.                                       |

| `opp\_elders`             | Dragones ancianos del rival.                                       |

| `firstherald`            | El equipo consiguió el primer Heraldo.                             |

| `heralds`                | Heraldos obtenidos.                                                |

| `opp\_heralds`            | Heraldos del rival.                                                |

| `void\_grubs`             | Void Grubs obtenidos.                                              |

| `opp\_void\_grubs`         | Void Grubs del rival.                                              |

| `firstbaron`             | El equipo consiguió el primer Barón Nashor.                        |

| `barons`                 | Barones obtenidos.                                                 |

| `opp\_barons`             | Barones obtenidos por el rival.                                    |

| `atakhans`               | Atakhans obtenidos (objetivo introducido en temporadas recientes). |

| `opp\_atakhans`           | Atakhans obtenidos por el rival.                                   |

Torres y estructuras

| Columna              | Descripción                                       |

| -------------------- | ------------------------------------------------- |

| `firsttower`         | El equipo destruyó la primera torre.              |

| `towers`             | Torres destruidas.                                |

| `opp\_towers`         | Torres destruidas por el rival.                   |

| `firstmidtower`      | El equipo destruyó primero la torre central.      |

| `firsttothreetowers` | El equipo fue el primero en destruir tres torres. |

| `turretplates`       | Placas de torre obtenidas.                        |

| `opp\_turretplates`   | Placas obtenidas por el rival.                    |

| `inhibitors`         | Inhibidores destruidos.                           |

| `opp\_inhibitors`     | Inhibidores destruidos por el rival.              |

Daño

| Columna                    | Descripción                                                   |

| -------------------------- | ------------------------------------------------------------- |

| `damagetochampions`        | Daño total infligido a campeones enemigos.                    |

| `dpm`                      | Daño por minuto.                                              |

| `damageshare`              | Proporción del daño del jugador respecto al total del equipo. |

| `damagetakenperminute`     | Daño recibido por minuto.                                     |

| `damagemitigatedperminute` | Daño mitigado por minuto.                                     |

| `damagetotowers`           | Daño realizado a torres.                                      |



Visión

| Columna              | Descripción                       |

| -------------------- | --------------------------------- |

| `wardsplaced`        | Guardianes colocados.             |

| `wpm`                | Guardianes colocados por minuto.  |

| `wardskilled`        | Guardianes enemigos destruidos.   |

| `wcpm`               | Guardianes destruidos por minuto. |

| `controlwardsbought` | Guardianes de control comprados.  |

| `visionscore`        | Puntuación de visión.             |

| `vspm`               | Puntuación de visión por minuto.  |

Oro

| Columna           | Descripción                                            |

| ----------------- | ------------------------------------------------------ |

| `totalgold`       | Oro total acumulado.                                   |

| `earnedgold`      | Oro ganado durante la partida.                         |

| `earned gpm`      | Oro ganado por minuto.                                 |

| `earnedgoldshare` | Porcentaje del oro del equipo generado por el jugador. |

| `goldspent`       | Oro gastado.                                           |

| `gspd`            | Diferencia porcentual de oro respecto al rival.        |

| `gpr`             | Ratio de generación de oro.                            |

Farm (CS)

| Columna                   | Descripción                                |

| ------------------------- | ------------------------------------------ |

| `total cs`                | Súbditos y monstruos eliminados.           |

| `minionkills`             | Súbditos eliminados.                       |

| `monsterkills`            | Monstruos neutrales eliminados.            |

| `monsterkillsownjungle`   | Monstruos eliminados en la propia jungla.  |

| `monsterkillsenemyjungle` | Monstruos eliminados en la jungla enemiga. |

| `cspm`                    | CS por minuto.                             |

Ventajas temporales



A partir de aquí aparecen las mismas métricas para distintos momentos de la partida (10, 15, 20 y 25 minutos):



* goldat10, goldat15, goldat20, goldat25: oro del jugador.
* xpat10, xpat15, xpat20, xpat25: experiencia acumulada.
* csat10, csat15, csat20, csat25: CS acumulado.
* opp\_goldatXX, opp\_xpatXX, opp\_csatXX: estadísticas del rival directo.
* golddiffatXX: diferencia de oro frente al rival de línea.
* xpdiffatXX: diferencia de experiencia.
* csdiffatXX: diferencia de CS.
* killsatXX, assistsatXX, deathsatXX: K/D/A del jugador hasta ese minuto.
* opp\_killsatXX, opp\_assistsatXX, opp\_deathsatXX: K/D/A del oponente hasta ese momento.

