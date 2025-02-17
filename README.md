# RetoCaptaci-n
 Miembros del equipo:
 
  - Manel Díaz

  - Ruben Alsasua

  - Eneko Saez

 Enlace a github: https://github.com/ManelDiaz/RetoCaptaci-n

 Descripción del proyecto:

    El proyecto hace uso de un pipeline de datos usando Mage y PostgreSQL. Utilizando estos contenedores, es posible:
    
      - Extraer datos de una base de datos PostgreSQL
      
      - Transformarlos mediante un script de Python en Mage 
      
      - Guardar los cambios en una tabla nueva

 Pasos seguidos:

    Para poder desarrollar el proyecto se han seguido los siguientes pasos: 

      1. Para empezar, se configuraron PostgreSQL y Mage en dos contenedores Docker. 
         Para ello se creó el archivo docker-compose.yml donde se realizaron las configuraciones necesarias para ambos servicios. 
         Además la tabla de datos inicial en PostgreSQL.
         
      2. Se estableció una conexión a Postgre desde Mage.

      3. Se creó el pipeline de Mage.

      4. Se desarrolló el bloque de extracción de datos de la tabla. En este proceso se recopilan todos los datos relevantes.

      5. Se creó el bloque de transformación de datos, en el cual se editaban los datos recibidos del bloque anterior. 
         En este caso, se transformó el siguiente dato de la tabla: se suman dos años a la edad de cada persona. 
         
      6. Se creo el bloque de almacenamiento de datos trasnformados, para ello se creo una tabla adicional en PostgreSQL. 

 Instrucciones de uso:

    Para poder ejecutar el proyecto sería necesario clonar el repositorio mediante el comando 'git clone'. Después, es necesario levantar los contenedores 
    ejecutando el comando 'docker-compose up -d' en la terminal de WSL. 
    
    Al generar los contenedores será necesario crear en PostgresSQL las tablas de datos que se van a utilizar, para ello usar el siguiente código:

      #docker exec -it postgres psql -U username -d postgres
      para acceder a postgres, y una vez dentro:

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

    Con pgAdmin, se pueden visualizar las dos tablas.
    
 Posibles vías de mejora:

    - En el bloque de transformación de datos, se podría haber separado la lógica, de la función transformar con la propia transformación, por 
      si en un futuro se quisiera ampliar el proyecto con más transformaciones. Se podría haber hecho un #def incrementar_edad(...) , por ejemplo.

    - Se podría haber programado la función con una variable de incremento, en vez de con un 2 estático, y así el usuario podría decidir cuánto incrementar.

 Problemas y retos encontrados:
 
  En cuanto a los problmas encontrados durante la creación del proyecto, se pueden destacar los siguientes:
  
    - Problemas a la hora de acceder correctamente a PostgreSQL, ya que por todas las descargas desde git, puede no crearse 
      correctamente el usuario definido en el docker-compose. Para  solucionarlo, se tienen que reiniciar del todo los contenedores 
      con #docker-compose down -v, y de nuevo #docker-compose up -d.

    - Problemas a la hora de conectar Mage con PostgreSQL. Debido a que creamos ambos contenedores en una misma carpeta.
      no utilizamos un entorno virtual de Python (venv). Se acabó solucionando cambiando algunas configuraciones del host
      y del archivo io_config.yaml.

    - Problemas con el bloque de recopilación de datos de Mage. Debido a que cambiamos las columnas de la tabla de PostgreSQL, 
      aparecia un error de que las columnas no coincidian. Cambiando de nuevo las columnas se pudo arreglar el problema. 

    - Es necesario crear las tablas de datos cada vez que se quiere descarga por primera vez el proyecto, estaría muy bien 
      conseguir poder pasar las tablas creadas con los pulls y push de github.

 Alternativas posibles:

    Hemos visto que, en vez de Mage, se podría haber utilizado Prefect, que en una interfaz web parecida, pero con un archivo único de Python, 
    se podría haber gestionado el flujo de recibir datos de postgres, modificarlos, y volverlos a enviar a una nueva tabla. Esta alternativa parece que es,
    para un proyecto como este, la menos compleja de utilizar.


