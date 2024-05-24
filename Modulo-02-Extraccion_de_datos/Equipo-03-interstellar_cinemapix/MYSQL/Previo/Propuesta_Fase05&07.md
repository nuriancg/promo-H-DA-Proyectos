# Consultas SQL para Base de Datos de Películas

Este repositorio contiene las consultas SQL necesarias para obtener información de una base de datos de películas, incluyendo detalles sobre géneros, valoraciones y premios Óscar. Las tablas ya están creadas en la base de datos según las estructuras proporcionadas.

## Tablas

### Tabla `generos`
| Column        | Type               |
|---------------|--------------------|
| genero_id     | SMALLINT AI PK     |
| nombre_genero | VARCHAR(30)        |

### Tabla `peliculas_generos`
| Column     | Type           |
|------------|----------------|
| pelicula_id| INT            |
| genero_id  | SMALLINT       |

### Tabla `detalles_peliculas`
| Column            | Type          |
|-------------------|---------------|
| ID_IMDB           | VARCHAR(50) PK|
| Nombre            | VARCHAR(100)  |
| Director          | VARCHAR(255)  |
| Guionista         | VARCHAR(250)  |
| Argumento         | TEXT          |
| Duracion          | VARCHAR(30)   |
| Puntuacion_IMDb   | VARCHAR(30)   |
| Puntuacion_Rotten | VARCHAR(30)   |

### Tabla `peliculas`
| Column     | Type           |
|------------|----------------|
| Tipo       | VARCHAR(30)    |
| Genero     | VARCHAR(30)    |
| Titulo     | VARCHAR(255)   |
| Mes        | SMALLINT       |
| Anio       | INT            |
| ID_IMDB    | VARCHAR(255)   |
| pelicula_id| INT AI PK      |

### Tabla `premios_oscar`
| Column          | Type           |
|-----------------|----------------|
| oscar_id        | SMALLINT AI PK |
| fecha_ceremonia | YEAR           |
| mejor_pelicula  | VARCHAR(100)   |
| mejor_director  | VARCHAR(50)    |
| mejor_actor     | VARCHAR(50)    |
| mejor_actriz    | VARCHAR(50)    |

## Consultas SQL

### ¿Qué géneros han recibido más premios Óscar?

```sql
SELECT g.nombre_genero, COUNT(*) AS total_premios
FROM premios_oscar po
JOIN peliculas p ON po.mejor_pelicula = p.Titulo
JOIN peliculas_generos pg ON p.pelicula_id = pg.pelicula_id
JOIN generos g ON pg.genero_id = g.genero_id
GROUP BY g.nombre_genero
ORDER BY total_premios DESC;
```

### ¿Qué género es el mejor valorado en IMDB?

```sql
SELECT g.nombre_genero, AVG(CAST(dp.Puntuacion_IMDb AS DECIMAL(3, 1))) AS promedio_puntuacion
FROM detalles_peliculas dp
JOIN peliculas p ON dp.ID_IMDB = p.ID_IMDB
JOIN peliculas_generos pg ON p.pelicula_id = pg.pelicula_id
JOIN generos g ON pg.genero_id = g.genero_id
GROUP BY g.nombre_genero
ORDER BY promedio_puntuacion DESC
LIMIT 1;
```

### ¿En qué año se estrenaron más películas?

```sql
SELECT Anio, COUNT(*) AS total_peliculas
FROM peliculas
WHERE Tipo = 'Película'
GROUP BY Anio
ORDER BY total_peliculas DESC
LIMIT 1;
```

### ¿En qué año se estrenaron más cortos?

```sql
SELECT Anio, COUNT(*) AS total_cortos
FROM peliculas
WHERE Tipo = 'Corto'
GROUP BY Anio
ORDER BY total_cortos DESC
LIMIT 1;
```

### ¿Cuál es la mejor serie valorada en IMDB?

```sql
SELECT p.Titulo, dp.Puntuacion_IMDb
FROM detalles_peliculas dp
JOIN peliculas p ON dp.ID_IMDB = p.ID_IMDB
WHERE p.Tipo = 'Serie'
ORDER BY CAST(dp.Puntuacion_IMDb AS DECIMAL(3, 1)) DESC
LIMIT 1;
```

### ¿Cuál es la película mejor valorada en IMDB?

```sql
SELECT p.Titulo, dp.Puntuacion_IMDb
FROM detalles_peliculas dp
JOIN peliculas p ON dp.ID_IMDB = p.ID_IMDB
WHERE p.Tipo = 'Película'
ORDER BY CAST(dp.Puntuacion_IMDb AS DECIMAL(3, 1)) DESC
LIMIT 1;
```

### ¿Qué actor/actriz ha recibido más premios?

```sql
-- Subconsulta para obtener el número máximo de premios recibidos
WITH max_premios AS (
    SELECT 
        MAX(total_premios) AS max_total_premios
    FROM (
        SELECT 
            nombre_actor, 
            COUNT(*) AS total_premios
        FROM (
            SELECT mejor_actor AS nombre_actor FROM proyecto_peliculas.premios_oscar
            UNION ALL
            SELECT mejor_actriz FROM proyecto_peliculas.premios_oscar
        ) AS actores_premiados
        GROUP BY nombre_actor
    ) AS premios_contados
)

-- Consulta principal para obtener los actores o actrices con el número máximo de premios
SELECT 
    nombre_actor, 
    total_premios
FROM (
    SELECT 
        nombre_actor, 
        COUNT(*) AS total_premios
    FROM (
        SELECT mejor_actor AS nombre_actor FROM proyecto_peliculas.premios_oscar
        UNION ALL
        SELECT mejor_actriz FROM proyecto_peliculas.premios_oscar
    ) AS actores_premiados
    GROUP BY nombre_actor
) AS premios_contados
WHERE total_premios = (SELECT max_total_premios FROM max_premios);
```

### ¿Hay algún actor/actriz que haya recibido más de un premio Óscar?

```sql
SELECT ganador, COUNT(*) AS total_premios
FROM (
    SELECT mejor_actor AS ganador FROM premios_oscar
    UNION ALL
    SELECT mejor_actriz AS ganador FROM premios_oscar
) AS premios
GROUP BY ganador
HAVING total_premios > 1;
```



