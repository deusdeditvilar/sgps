--CREATE SCHEMA sgps;
--SET search_path TO sgps;
--ALTER ROLE root SET search_path TO sgps;

CREATE TYPE TURNO AS ENUM ('MATUTINO', 'VESPERTINO', 'NOTURNO', 'INTEGRAL');
CREATE TYPE TIPOPESSOA AS ENUM ('CRIANCA', 'JOVEM', 'IDOSO');

CREATE TABLE PESSOA (
    ID INTEGER PRIMARY KEY,
    NOME VARCHAR(80) NOT NULL,
    TIPO_PESSOA TIPOPESSOA NOT NULL,
    NOME_DA_MAE VARCHAR(80),
    NOME_DO_PAI VARCHAR(80),
    ESTADO_CIVIL VARCHAR(15),
    CPF VARCHAR(11) UNIQUE NOT NULL,
    SITUACAO_MORADIA VARCHAR(20),
    DATA_NASCIMENTO timestamp without time zone NOT NULL,
    ESCOLA VARCHAR(30),
    ANO_ESCOLAR VARCHAR(15),
    TURNO_ESCOLAR TURNO,
    ESCOLARIDADE VARCHAR(30),
    BOLSA_FAMILIA BOOLEAN NOT NULL
);

CREATE TABLE FUNCIONARIO (
    ID INTEGER PRIMARY KEY,
    NOME VARCHAR(80) NOT NULL,
    TIPO_PESSOA TIPOPESSOA NOT NULL,
    NOME_DA_MAE VARCHAR(80),
    NOME_DO_PAI VARCHAR(80),
    ESTADO_CIVIL VARCHAR(15),
    CPF VARCHAR(11) UNIQUE NOT NULL,
    SITUACAO_MORADIA VARCHAR(20),
    DATA_NASCIMENTO timestamp without time zone NOT NULL,
    ESCOLA VARCHAR(30),
    ANO_ESCOLAR VARCHAR(15),
    TURNO_ESCOLAR TURNO,
    ESCOLARIDADE VARCHAR(30),
    BOLSA_FAMILIA BOOLEAN NOT NULL
);

CREATE TABLE USUARIO (
    ID INTEGER PRIMARY KEY,
    PESSOA_ID REFERENCES PESSOA
    NOME VARCHAR(80) NOT NULL,
    NOME_USUARIO VARCHAR(20) NOT NULL,
    SENHA VARCHAR(20) NOT NULL,
    CPF VARCHAR(11) UNIQUE NOT NULL,
    CARGO VARCHAR(11) NOT NULL,
    NIVEL_PERMISSAO INTEGER,
);