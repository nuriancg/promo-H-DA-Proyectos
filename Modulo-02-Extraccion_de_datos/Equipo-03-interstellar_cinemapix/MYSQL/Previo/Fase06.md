# IMPORTAR DATOS CSV A TABLAS EN MYSQL

### Paso 1: Crear la tabla en MySQL
Primero, asegúrate de que la tabla en la que quieres importar los datos esté creada y tenga una estructura compatible con los datos del CSV. Por ejemplo, si tienes un CSV con las columnas `id`, `name`, y `age`, la tabla en MySQL podría ser algo así:

```sql
CREATE TABLE my_table (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);
```

### Paso 2: Cargar el archivo CSV en MySQL

Puedes usar el comando `LOAD DATA INFILE` para cargar los datos del CSV en la tabla. Aquí hay un ejemplo de cómo hacerlo:

```sql
LOAD DATA INFILE '/path/to/yourfile.csv'
INTO TABLE my_table
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, name, age);
```

### Detalles del comando `LOAD DATA INFILE`

- `/path/to/yourfile.csv`: Ruta completa al archivo CSV en el servidor MySQL.
- `INTO TABLE my_table`: Especifica la tabla en la que se van a importar los datos.
- `FIELDS TERMINATED BY ','`: Define el delimitador de campos, en este caso una coma.
- `ENCLOSED BY '"'`: Define el carácter que encierra los valores de los campos, en este caso comillas dobles.
- `LINES TERMINATED BY '\n'`: Define el delimitador de líneas, en este caso un salto de línea.
- `IGNORE 1 LINES`: Ignora la primera línea del CSV (generalmente es el encabezado).
- `(id, name, age)`: Lista de columnas en la tabla que corresponde a las columnas del archivo CSV.

### Nota Importante

Para que `LOAD DATA INFILE` funcione, el archivo CSV debe estar accesible desde el servidor MySQL. Si estás ejecutando MySQL en una máquina local, puedes colocar el archivo en una ruta accesible. Si estás trabajando con un servidor remoto, es posible que necesites subir el archivo al servidor.

### Uso de `LOAD DATA LOCAL INFILE`

Si el archivo CSV está en tu máquina local y no en el servidor, puedes usar `LOAD DATA LOCAL INFILE` en su lugar:

```sql
LOAD DATA LOCAL INFILE '/path/to/yourfile.csv'
INTO TABLE my_table
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, name, age);
```

### Permisos y Configuraciones

Asegúrate de que el servidor MySQL tiene los permisos necesarios para leer archivos y que las configuraciones del servidor permiten la carga de datos desde archivos locales. A veces, necesitas ajustar el parámetro `secure_file_priv` en el archivo de configuración de MySQL (`my.cnf` o `my.ini`).

### Ejemplo Completo

Aquí tienes un ejemplo completo:

1. Crea la tabla en MySQL:

    ```sql
    CREATE TABLE my_table (
        id INT PRIMARY KEY,
        name VARCHAR(100),
        age INT
    );
    ```

2. Coloca tu archivo CSV en `/var/lib/mysql-files/myfile.csv` (o una ruta accesible para MySQL).

3. Ejecuta el comando `LOAD DATA INFILE`:

    ```sql
    LOAD DATA INFILE '/var/lib/mysql-files/myfile.csv'
    INTO TABLE my_table
    FIELDS TERMINATED BY ',' 
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    (id, name, age);
    ```
```
