# TalentoTech - QA Automation

## Autor: Pablo Poliserpi

Repositorio de las dos entregas pertinentes al proyecto final de QA Automation, Talento Tech

### Proposito

El objetivo del proyecto es realizar una serie de pruebas de calidad automatizadas en las páginas demo objetivo (```https://saucedemo.com/```, ```https://reqres.in/```, ```https://jsonplaceholder.typicode.com```).  
Estas incluyen pruebas de UI (login, inventory, cart) y pruebas de funcionamiento de API.

### Tecnologias

El proyecto utiliza Python, Pytest y Selenium, asi como librerias del entorno Python como PathLib para manejor de rutas, Pytest_html para reportes autocontenidos, Logging para creacion y manejo de logs, Request para conexiones HTTPS.  

### Features

El proyecto se centra en utilizar técnicas de QA donde prima la reutilización de recursos, buenas prácticas de código para minimizar la incidencia de errores en las pruebas, estrategias de programación para evitar hardlocks en pruebas y uso de decorators (fixtures, parametrizaciones, marks) para evitar duplicación de datos y hardcoding asi como extracción automática de datos en archivos externos con el fin de proveer escalabilidad a futuro.

### Dependencias

Dentro del archivo ```requirement.txt``` se puede encontrar la lista de dependecias requeridas para ejecutar las pruebas automatizadas.

Ejecutar el siguiente comando para su instalación:

``` python
pip install -r requirements.txt
```

### Reportes y Logs

El proyecto centraliza los resultados dentro de la carpeta ```reports/```, donde se pueden encontrar capturas de pantalla automáticas en casos donde las pruebas hayan fallado, tanto esperada como inesperadamente.  
Dentro de la carpeta ```logs/``` se encuentran los archivos ```.log``` con un desglose magnificado para casos de depuración.

### Ejecución de Pruebas

Comandos de ejecución:

- Todas las pruebas con reporte automático.
  
``` python
pytest
```

- Pruebas de Login.

``` python
pytest tests/test_login.py
```

- Pruebas de Inventory.

``` python
pytest tests/test_inventory.py
```

- Pruebas de Cart.

``` python
pytest tests/test_cart
```

- Pruebas de login en API.

``` python
pytest tests/test_api_login.py
```

- Pruebas de creacion de usuario en API.

``` python
pytest tests/test_create_user.py
```

- Pruebas de consistencia estructural en API.

``` python
pytest tests/test_user.py
```

- Prueba encadenada integral en API.

``` python
pytest tests/test_post_lifecycle.py
```
