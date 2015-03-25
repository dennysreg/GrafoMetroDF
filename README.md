# GrafoMetroDF
Demo
https://metrocdmx.herokuapp.com/static/index.html

Visualización Interactiva del Metro de la Ciudad de México

Representación de la red del metro con D3, que permite mostrar la ruta más corta entre dos estaciones.

Basta con dar un click en la estación origen y otro click en la destino para generar una animación que describe la ruta más corta.

Se uso el algoritmo de Floyd-Warshall para calcular la matriz de distancias mínimas y las rutas. Se uso el número de estaciones como unidad de peso.

Para verlo funcionando es necesario levantar un servidor web, si tienen instalado python, solo hay que correr
python -m SimpleHTTPServer en el directorio /GrafoMetroDF que se genera al descomprimir el .zip
