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
    ejecutando el comando 'docker-compose up -d' en la terminal de WSL. 
    
    AL generar los contenedores será necesario crear en PostgresSQL las tablas de datos que se van a utilizar, para ello unar el siguiente código:

         CREATE TABLE usuarios_origen (
         id SERIAL PRIMARY KEY,
         nombre VARCHAR(100),
         edad INT,
         email VARCHAR(100)
         );

         CREATE TABLE usuarios_destino (
         id SERIAL PRIMARY KEY,
         nombre_completo VARCHAR(200),
         edad INT,
         email VARCHAR(100)
         );

         INSERT INTO usuarios_origen (nombre, edad, email) VALUES
         ('Juan Perez', 30, 'juan.perez@example.com'),
         ('Maria Lopez', 25, 'maria.lopez@example.com'),
         ('Carlos Sanchez', 40, 'carlos.sanchez@example.com');
    
    Al tener los contendores ejecutando y las tablas que se van a utilizar creadas, es posible acceder a la interfaz de Mage buscando 
    en el navegador 'http://localhost:6789'. 
    
    Una vez dentro, se selecciona el pipeline a ejecutar "pipeline_final", y se ejecutan los bloques.
    
 Posibles vías de mejora:

 Problemas y retos encontrados:
  En cuanto a los problmas encontrados durante la creación del proyecto, se pueden destacar los siguientes:
  
    - Problemas a la hora de conectar Mage con PostgreSQL. Debido a que creamos ambos contenedores en una misma carpeta.
      no utilizamos un entorno virtual de Python (venv). Se acabó solucionando cambiando algunas configuraciones del host
      y del archivo io_config.yaml.

    - Problemas con el bloque de recopilación de datos de Mage. Debido a que cambiamos las columnas de la tabla de PostgreSQL, 
      aparecia un error de que las columnas no coincidian. Cambiando de nuevo las columnas se pudo arreglar el problema. 

    - Es necesario crear las tablas de datos cada vez que se quiere descarga por primera vez el proyecto, estaría muy bien conseguir poder pasar las tablas creadas con los pulls y push de github.

 Alternativas posibles:

 (desarrollar alternmativas)


