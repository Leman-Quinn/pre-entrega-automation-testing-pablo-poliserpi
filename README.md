# TalentoTech_QA_Automation

## Autor: Pablo Poliserpi

Repositorio de las dos entregas pertinentes al proyecto final de QA Automation, Talento Tech

### Tecnologias y Proposito:

El proyecto utiliza Python 3.14, Pytest y Selenium con el objetivo de realizar una serie de pruebas de calidad en la página demo objetivo (https://saucedemo.com) que incluyen pruebas de login, de inventario, de UI y funcionalidad de carrito de compra.

### Dependencias

Dentro del archivo ```requirement.txt``` se puede encontrar la lista de dependecias requeridas para ejecutar las pruebas automatizadas.

Ejecutar el siguiente comando para su instalación:

```
pip install -r requirements.txt
```

### Ejecución de Pruebas

Comandos de ejecución:

- Todas las pruebas con reporte automático.
  
``` python
py -m pytest -v --html=reporte.html --self-contained-html --log-cli-level=INFO
```

- Prueba de Login con reporte automático.

``` python
py -m pytest -v --html=reporte.html --self-contained-html --log-cli-level=INFO tests/test_login.py
```

- Prueba de Inventario con reporte automático.

``` python
py -m pytest -v --html=reporte.html --self-contained-html --log-cli-level=INFO tests/test_inventory.py
```

- Prueba de Carrito con reporte automático.

``` python
py -m pytest -v --html=reporte.html --self-contained-html --log-cli-level=INFO tests/test_cart
```
