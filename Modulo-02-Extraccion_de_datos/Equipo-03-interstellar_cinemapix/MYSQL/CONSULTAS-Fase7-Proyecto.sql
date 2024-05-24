USE proyecto_peliculas; 


-- 1. **¿Qué géneros han recibido más premios Óscar?**

-- Paso 1: Obtener todas las películas premiadas y contarlas
WITH peliculas_premiadas AS (
    SELECT mejor_pelicula AS titulo
    FROM proyecto_peliculas.premios_oscar
    UNION ALL
    SELECT mejor_director AS titulo
    FROM proyecto_peliculas.premios_oscar
    UNION ALL
    SELECT mejor_actor AS titulo
    FROM proyecto_peliculas.premios_oscar
    UNION ALL
    SELECT mejor_actriz AS titulo
    FROM proyecto_peliculas.premios_oscar
),

-- Paso 2: Contar los premios por película
premios_por_pelicula AS (
    SELECT 
        titulo,
        COUNT(*) AS total_premios
    FROM 
        peliculas_premiadas
    GROUP BY 
        titulo
)

-- Paso 3: Seleccionar las películas más premiadas
SELECT 
    titulo,
    total_premios
FROM 
    premios_por_pelicula
ORDER BY 
    total_premios DESC;
    
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 -- De las consultas anterior sacamos la tupla con la que saber qué películas han sido premiadas y a qué género pertenecen 

SELECT Titulo, Genero
FROM proyecto_peliculas.peliculas
WHERE Titulo IN (
    'A. Cuarón',
    'A. Lee',
    'S. Penn',
    'D. Day-Lewis',
    'H. Swank',
    'E. Stone',
    'F. McDormand',
    'Million Dollar Baby',
    'Crash',
    'The Departed',
    'No Country for Old Men',
    'Slumdog Millionaire',
    'The Hurt Locker',
    'The King''s Speech',
    'The Artist',
    'Argo',
    '12 Years a Slave',
    'Birdman or',
    'Spotlight',
    'Moonlight',
    'The Shape of Water',
    'Green Book',
    'Parasite',
    'Nomadland',
    'CODA',
    'Everything Everywhere All at Once',
    'Oppenheimer',
    'S. Mendes',
    'S. Soderbergh',
    'R. Howard',
    'R. Polanski',
    'P. Jackson',
    'C. Eastwood',
    'M. Scorsese',
    'J. Coen E. Coen',
    'D. Boyle',
    'K. Bigelow',
    'T. Hooper',
    'M. Hazanavicius',
    'A. G. Iñárritu',
    'D. Chazelle',
    'G. del Toro',
    'Bong J.',
    'C. Zhao',
    'J. Campion',
    'D. Kwan D. Scheinert',
    'C. Nolan',
    'K. Spacey',
    'R. Crowe',
    'D. Washington',
    'A. Brody',
    'American Beauty',
    'J. Foxx',
    'P. S. Hoffman',
    'F. Whitaker',
    'Gladiator',
    'J. Bridges',
    'C. Firth',
    'J. Dujardin',
    'M. McConaughey',
    'E. Redmayne',
    'L. DiCaprio',
    'C. Affleck',
    'G. Oldman',
    'R. Malek',
    'J. Phoenix',
    'A. Hopkins',
    'W. Smith',
    'B. Fraser',
    'C. Murphy',
    'A Beautiful Mind',
    'J. Roberts',
    'H. Berry',
    'N. Kidman',
    'C. Theron',
    'R. Witherspoon',
    'H. Mirren',
    'M. Cotillard',
    'K. Winslet',
    'S. Bullock',
    'N. Portman',
    'M. Streep',
    'J. Lawrence',
    'C. Blanchett',
    'J. Moore',
    'B. Larson',
    'Chicago',
    'The Lord of the Rings: The Return of the King',
    'O. Colman',
    'R. Zellweger',
    'J. Chastain',
    'M. Yeoh'
);
 

-- otra prueba 
SELECT g.nombre_genero, COUNT(*) AS total_premios
FROM premios_oscar po
JOIN peliculas p ON po.mejor_pelicula = p.Titulo
JOIN peliculas_generos pg ON p.pelicula_id = pg.pelicula_id
JOIN generos g ON pg.genero_id = g.genero_id
GROUP BY g.nombre_genero
ORDER BY total_premios DESC;



-- 2. **¿Qué género es el mejor valorado en IMDB?**

SELECT g.nombre_genero, AVG(dp.puntuacion_IMDB) AS promedio_puntuacion
FROM detalles_peliculas dp
JOIN peliculas p ON dp.ID_IMDB = p.ID_IMDB
JOIN peliculas_generos pg ON p.pelicula_id = pg.pelicula_id
JOIN generos g ON pg.genero_id = g.genero_id
GROUP BY g.nombre_genero
ORDER BY promedio_puntuacion DESC
LIMIT 1; 



-- 3. **¿En qué año se estrenaron más películas?**

SELECT Anio, COUNT(*) AS total_peliculas
FROM peliculas
WHERE Tipo = 'Película'
GROUP BY Anio
ORDER BY total_peliculas DESC
LIMIT 1; 


-- 4. ### ¿En qué año se estrenaron más cortos?

SELECT Anio, COUNT(*) AS total_cortos
FROM peliculas
WHERE Tipo = 'Corto'
GROUP BY Anio
ORDER BY total_cortos DESC
LIMIT 1;


-- 5. ### ¿Cuál es la mejor serie valorada en IMDB?

SELECT p.Titulo, dp.Puntuacion_IMDb
FROM detalles_peliculas dp
JOIN peliculas p ON dp.ID_IMDB = p.ID_IMDB
WHERE p.Tipo = 'Serie'
ORDER BY CAST(dp.Puntuacion_IMDb AS DECIMAL(3, 1)) DESC
LIMIT 1;

-- 6. ### ¿Cuál es la película mejor valorada en IMDB?

SELECT Nombre, MAX( round( puntuacion_IMDB))
FROM detalles_peliculas AS DP
INNER JOIN peliculas AS P
ON P.ID_IMDB = DP.ID_IMDB
WHERE puntuacion_IMDB not like 'No encontrado'
GROUP BY P.TIPO = 'MOVIE' 
ORDER BY puntuacion_IMDB DESC
LIMIT 1;

-- 7- ### ¿Qué actor/actriz ha recibido más premios?

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



-- 8- ### ¿Hay algún actor/actriz que haya recibido más de un premio Óscar?

SELECT ganador, COUNT(*) AS total_premios
FROM (
    SELECT mejor_actor AS ganador FROM premios_oscar
    UNION ALL
    SELECT mejor_actriz AS ganador FROM premios_oscar
) AS premios
GROUP BY ganador
HAVING total_premios > 1;
