# CSGO_Tiempo
Programa que implementa el cálculo de tiempo de espera en CSGO y otros juegos donde uno puede seleccionar más de un modo de juego para jugar.

## Forma de uso
Inserte en los mapas el tiempo de espera y seleccionelo para jugar. El programa calculará el tiempo general estimado.
De esta forma, podrá evaluar si es conveniente seleccionar más opciones de mapa para ahorrar tiempo de espera, o seleccionar solamente sus mapas favoritos.

## Opciones
En la pestaña de **Opciones** encontrará la opción de Agregar mapas y otra de Desconectar. Con Desconectar se desconectará de la base de datos. Es recomendable hacerlo antes de cerrar el programa para evitar que incluso después de cerrado el programa siga consumiendo recursos.

## Cómo calcula el tiempo?
Calcula el tiempo de espera total estimado en base a los tiempos individuales. Funciona como las resistencias de un circuito en paralelo, siendo las resistencias el tiempo de espera individual.

## Extensibilidad
El programa contiene algunos de los mapas de competitivo de CSGO cargados. Usted puede cargar los mapas que quiera. Incluso pueden ser modos de juego  o mapas de otros juegos. La forma de cálculo es siempre la misma.
Para borrar todos los mapas solo borre la base de datos **db**. Abra el programa y empiece a cargar sus propias opciones!

