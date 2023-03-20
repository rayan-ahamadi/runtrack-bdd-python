CREATE TABLE etage (
    id int PRIMARY KEY auto_increment,
    nom varchar(255),
    numero int,
    superficie int
);

CREATE TABLE salles (
    id int PRIMARY KEY auto_increment,
    nom varchar(255),
    id_etage int,
    capacite int
);

