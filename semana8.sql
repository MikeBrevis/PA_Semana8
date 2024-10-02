USE semana8;
CREATE TABLE FaunaFlora (
    ID INT PRIMARY KEY,
    NombreCientifico VARCHAR(100),
    Habitat VARCHAR(50),
    EstadoConservacion VARCHAR(20),
    RegionGeografica VARCHAR(50)
);

SELECT * FROM FaunaFlora;
SHOW tables;
SELECT * FROM FaunaFlora;

-- Insertar registros
INSERT INTO FaunaFlora (ID, NombreCientifico, Habitat, EstadoConservacion, RegionGeografica) VALUES 
(1,'Panthera leo', 'Sabana', 'Vulnerable', 'África'), 
(2,'Quercus robur', 'Bosque Templado', 'Preocupación Menor', 'Europa'), 
(3,'Phalaenopsis amabilis', 'Selva Tropical', 'En Peligro', 'Sudeste Asiático');

SHOW tables;
SELECT * FROM FaunaFlora;



