# RetoCaptaci-n
 Miembros del equipo:
 
  - Manel Díaz

  - Ruben Alsasua

  - Eneko Saez

 Descripción del proyecto:
    El proyecto hace uso de un pipeline de datos usando Mage y PostgreSQL. Utilizando estos contenedores, es posible:
    
      - Extraer datos de una base de datos PostgreSQL
      
      - Transformarlos mediante un script de Python en Mage 
      
      - Guardar los cambios en una tabla nueva

 Pasos seguidos:
    Para poder desrrollar el proyecto se han seguido los siguientes pasos: 

      1. Para empezar se configuraron PostgreSQL y Mage en dos contenedores Docker. 
         Para ello se creó el archivo docker-compose.yml donde se realizaron las configuraciones necesarias para ambos servicios. 
         Además la tabla de datos inicial en PostgreSQL.
         
      2. Se estableció una conexión a Postgre desde Mage.

      3. Se creó el pipeline de Mage.

      4. Se desarrolló el bloque de estración de datos de la tabla. En este proceso se recopilan todos los datos relevantes.

      5. Se creó el bloque de extracción de datos, en el cual se editaban los datos recibidos del bloque anterior. 
         En este caso, se transformaron los siguientes datos: apellido se convierte a mayusculas, el salario pasa a ser un numero entero, 
         ...
      6. Se creo el bloque de almacenamiento de datos trasnformados, para ello se creo una tabla adicional en PostgreSQL. 

 Instrucciones de uso:
    Para poder ejecutar el proyecto sería necesario clonar el repositorio mediante el comando 'git clone'. Después, es necesario levantar los contenedores 
    ejecutando el comando 'docker-compose up -d' en la terminal de WSL. Al tener los contendores ejecutando, es posible acceder a la interfaz de Mage buscando 
    en el navegador 'http://localhost:6789'. Una vez dentro, se selecciona el pipeline a ejecutar y se puede comprobar el correcto funcionamiento. 
    
 Posibles vías de mejora:

 Problemas y retos encontrados:

 Alternativas posibles:
