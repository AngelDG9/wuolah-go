wuolah-go
=========

Script que canjea tickets de sorteos en Wuolah de forma automática, evitando clics repetitivos manuales.

El Problema
-----------

Wuolah te permite usar múltiples tickets en un mismo sorteo para aumentar tus probabilidades de ganar. Sin embargo, la plataforma obliga a canjearlos **de uno en uno manualmente**, lo que convierte una tarea sencilla en un proceso tedioso, lento y muy repetitivo si tienes cientos de tickets.

La Solución
-----------

**wuolah-go** automatiza por completo esta tarea. El script simula los clics del ratón y la pulsación de teclas de forma continua. Solo tienes que colocar el cursor sobre el botón de participar y dejar que el programa canjee todos los tickets por ti.

🚀 Características
------------------

*   **Automatización Total**: Simula el flujo completo de participación (clic + enter) de forma indefinida.
    
*   **Comportamiento Humano**: Utiliza pausas aleatorias entre acciones para evitar patrones robóticos.
    
*   **Control Sencillo**: El script se detiene de forma instantánea y segura con solo presionar la letra "q".
    
*   **Fácil de Usar**: No requiere ninguna configuración. ¡Ejecutar y listo!
    

⚙️ Requisitos Previos
---------------------

Necesitas tener **Python 3** instalado. Después, abre una terminal o consola y ejecuta el siguiente comando para instalar las librerías necesarias:

`   pip install pyautogui keyboard   `

**Nota:** En algunos sistemas operativos (especialmente Linux), pyautogui puede requerir la instalación de dependencias adicionales. Si tienes problemas, consulta su documentación oficial.

📋 Instrucciones de Uso
-----------------------

1.  Descarga el script main.py.
    
2.  Abre la página del sorteo en Wuolah donde quieras participar.
    
3.  python main.py
    
4.  **¡Rápido! Tienes 10 segundos** para mover el cursor y **posicionarlo sobre el botón "Participar"** del sorteo.
    
5.  Una vez pasen los 10 segundos, el script comenzará a hacer clics automáticamente.
    
6.  Para detener el programa en cualquier momento, simplemente **presiona** la **tecla q**.
    

⚠️ Descargo de Responsabilidad (Disclaimer)
-------------------------

Este script se ha creado con fines puramente educativos y de demostración. El autor **no se hace responsable** del uso indebido de este programa ni de las posibles consecuencias que puedan derivarse de su utilización, incluyendo, entre otras, la suspensión o el bloqueo de la cuenta de Wuolah.

El uso de esta herramienta es bajo la **entera y exclusiva responsabilidad del usuario final**.
    

📄 Licencia
-----------

Este proyecto se distribuye bajo la Licencia MIT.
