# Space Game

Este proyecto es un juego 2D desarrollado en Python usando la biblioteca Pygame. El juego está inspirado en el estilo de Metal Slug y se ambienta en el espacio con diferentes enemigos y jefes finales.

## Requisitos

- Python 3.x
- Pygame (instalar con `pip install pygame`)

## Estructura del Proyecto

El proyecto se organiza en varios archivos y carpetas:

- **`main.py`**: Archivo principal que inicia el juego.
- **`game.py`**: Contiene la clase principal `Game` que gestiona el flujo del juego, incluyendo menús, lógica del juego y eventos.
- **`player.py`**: Define la clase `Player` que representa al jugador y maneja su movimiento y disparos.
- **`enemies.py`**: Contiene las clases `Enemy`, `Boss`, y `NPC` para los enemigos y personajes no jugables.
- **`projectiles.py`**: Define las clases `Projectile` y `EnemyProjectile` para los disparos de los jugadores y enemigos.
- **`settings.py`**: Archivo de configuración que contiene ajustes globales del juego como la resolución y la velocidad de fotogramas.

## Cómo Jugar

1. **Iniciar el Juego**:
    - Ejecuta `main.py` para iniciar el juego.

2. **Menú Principal**:
    - Al iniciar el juego, verás el menú principal con las opciones de "Start" y "Quit".
    - Usa el ratón para seleccionar una opción:
        - **Start**: Comienza el juego.
        - **Quit**: Sal del juego.

3. **En el Juego**:
    - **Movimiento**: Usa las teclas de flechas para mover la nave del jugador.
    - **Disparar**: Presiona la barra espaciadora para disparar proyectiles desde la nave del jugador.
    - **Interacción**: Presiona la tecla `E` para interactuar con los NPCs (personajes no jugables).

4. **Menú de Pausa**:
    - Presiona `ESC` para pausar el juego y abrir el menú de pausa.
    - Desde el menú de pausa puedes reanudar el juego o volver al menú principal.

## Lógica del Juego

- **Jugador**:
    - La nave del jugador puede moverse en todas las direcciones y disparar proyectiles.
    - Puede adquirir habilidades especiales al derrotar jefes.

- **Enemigos**:
    - **Enemies**: Enemigos básicos que se mueven aleatoriamente y disparan proyectiles.
    - **Bosses**: Jefes finales con habilidades especiales que atacan al jugador y tienen habilidades únicas.

- **Proyectiles**:
    - Los proyectiles disparados por el jugador y los enemigos se mueven en la pantalla y pueden causar daño.

## Archivos y Clases

### `game.py`
- **`Game`**: La clase principal que gestiona la lógica del juego, menús y actualizaciones de sprites.

### `player.py`
- **`Player`**: Representa al jugador, maneja el movimiento, disparos y adquisición de habilidades.

### `enemies.py`
- **`Enemy`**: Define el comportamiento de los enemigos básicos.
- **`Boss`**: Define el comportamiento de los jefes finales y sus habilidades especiales.
- **`NPC`**: Define los personajes no jugables con los que el jugador puede interactuar.

### `proyectiles.py`
- **`Projectile`**: Proyectiles disparados por el jugador.
- **`EnemyProjectile`**: Proyectiles disparados por los enemigos.

## Problemas Conocidos

- Asegúrate de tener las imágenes en la carpeta correcta (`CrazySpace/npc/recursos/images/`) para evitar errores.
- La lógica de algunas habilidades especiales de los jefes aún no está completamente implementada.

