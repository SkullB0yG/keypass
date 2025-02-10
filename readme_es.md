# KeyPass

KeyPass es un proyecto diseñado para gestionar y almacenar tus contraseñas de manera segura. Este README te guiará a través de la instalación, configuración y uso del proyecto.

## Instalación

1. Clona el repositorio en tu máquina local:
    ```sh
    git clone https://github.com/tu-usuario/keypass.git
    cd keypass
    ```

2. Asegúrate de tener Python instalado. Puedes verificarlo con:
    ```sh
    python --version
    ```

3. Instala las dependencias necesarias:
    ```sh
    pip install -r requirements.txt
    ```

## Configuración

Para integrar KeyPass con tu shell, necesitas agregar algunas líneas a tu archivo de configuración `.zshrc` o `.bashrc`.

### Zsh

1. Abre tu archivo `.zshrc`:
    ```sh
    nano ~/.zshrc
    ```

2. Agrega la siguiente línea al final del archivo:
    ```sh
    source /ruta/a/keypass/keypass.zsh
    ```

3. Guarda y cierra el archivo, luego recarga la configuración:
    ```sh
    source ~/.zshrc
    ```

### Bash

1. Abre tu archivo `.bashrc`:
    ```sh
    nano ~/.bashrc
    ```

2. Agrega la siguiente línea al final del archivo:
    ```sh
    source /ruta/a/keypass/keypass.bash
    ```

3. Guarda y cierra el archivo, luego recarga la configuración:
    ```sh
    source ~/.bashrc
    ```

## Uso

Una vez que hayas configurado KeyPass, puedes usarlo directamente desde tu terminal.

### Comandos Básicos

- **Agregar una contraseña**:
    ```sh
    keypass add <nombre> <contraseña>
    ```

- **Obtener una contraseña**:
    ```sh
    keypass get <nombre>
    ```

- **Eliminar una contraseña**:
    ```sh
    keypass delete <nombre>
    ```

## Contribuir

Si deseas contribuir al proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Contacto

Para cualquier duda o sugerencia, por favor abre un issue en el repositorio o contacta al mantenedor del proyecto.
