-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 17, 2026 at 04:40 PM
-- Server version: 8.4.3
-- PHP Version: 8.3.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ico801`
--

-- --------------------------------------------------------

--
-- Table structure for table `alumnos`
--

CREATE TABLE `alumnos` (
  `id` int NOT NULL,
  `nombre` varchar(250) NOT NULL,
  `apaterno` varchar(50) NOT NULL,
  `amaterno` varchar(150) NOT NULL,
  `edad` int NOT NULL,
  `correo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `alumnos`
--

INSERT INTO `alumnos` (`id`, `nombre`, `apaterno`, `amaterno`, `edad`, `correo`) VALUES
(1, 'emmanuel', 'moreno', 'c', 25, 'emmanuel@gmail.com'),
(2, 'alejandro', 'castillo', 'm', 25, 'alejandro@gmail.com'),
(3, 'jose', 'jose', 'r', 34, 'jose@gmail.com'),
(5, 'shidarta', 'gautama', 'buda', 1000, 'buda@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `cursos`
--

CREATE TABLE `cursos` (
  `id` int NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `descripcion` text,
  `maestro_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `cursos`
--

INSERT INTO `cursos` (`id`, `nombre`, `descripcion`, `maestro_id`) VALUES
(1, 'filosofia', 'filosofia existencialista', 2),
(2, 'tecnolgia', 'tec', 3),
(3, 'redes', 'ciber seguridad', 3),
(4, 'fisica', 'ggggg', 2),
(5, 'electromagnetismo', 'basico', NULL),
(6, 'canto', 'canto basico', 2);

-- --------------------------------------------------------

--
-- Table structure for table `inscripciones`
--

CREATE TABLE `inscripciones` (
  `id` int NOT NULL,
  `alumno_id` int NOT NULL,
  `curso_id` int NOT NULL,
  `fecha_inscripcion` datetime DEFAULT (now())
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `inscripciones`
--

INSERT INTO `inscripciones` (`id`, `alumno_id`, `curso_id`, `fecha_inscripcion`) VALUES
(2, 2, 1, '2026-04-16 08:15:20'),
(8, 1, 1, '2026-04-16 12:30:42'),
(9, 3, 1, '2026-04-16 12:30:47'),
(10, 1, 2, '2026-04-16 12:30:52'),
(11, 1, 3, '2026-04-16 12:30:56'),
(12, 1, 4, '2026-04-16 12:30:59'),
(15, 2, 2, '2026-04-17 07:22:57'),
(16, 1, 5, '2026-04-17 07:46:45'),
(17, 2, 5, '2026-04-17 07:46:53'),
(18, 3, 5, '2026-04-17 07:47:02'),
(19, 5, 5, '2026-04-17 07:47:08'),
(20, 1, 6, '2026-04-17 09:17:37'),
(21, 3, 6, '2026-04-17 09:17:45'),
(22, 5, 6, '2026-04-17 09:17:59');

-- --------------------------------------------------------

--
-- Table structure for table `maestros`
--

CREATE TABLE `maestros` (
  `matricula` int NOT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `apellidos` varchar(50) DEFAULT NULL,
  `especialidad` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `maestros`
--

INSERT INTO `maestros` (`matricula`, `nombre`, `apellidos`, `especialidad`, `email`) VALUES
(2, 'platon', 'rmirez', 'filosofia', 'platon@gmail.com'),
(3, 'alejandro', 'magno', 'historia', 'magno@gmail.com'),
(1902, 'nappoleon', 'bonaparte', 'estrategia avanzada', 'elbona@gmail.com'),
(1903, 'jesus', 'de nazaret', 'resucitacion rcp', 'yisus@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alumnos`
--
ALTER TABLE `alumnos`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cursos`
--
ALTER TABLE `cursos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `maestro_id` (`maestro_id`);

--
-- Indexes for table `inscripciones`
--
ALTER TABLE `inscripciones`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uq_alumno_curso` (`alumno_id`,`curso_id`),
  ADD KEY `curso_id` (`curso_id`);

--
-- Indexes for table `maestros`
--
ALTER TABLE `maestros`
  ADD PRIMARY KEY (`matricula`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `alumnos`
--
ALTER TABLE `alumnos`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `cursos`
--
ALTER TABLE `cursos`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `inscripciones`
--
ALTER TABLE `inscripciones`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `maestros`
--
ALTER TABLE `maestros`
  MODIFY `matricula` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2657;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `cursos`
--
ALTER TABLE `cursos`
  ADD CONSTRAINT `cursos_ibfk_1` FOREIGN KEY (`maestro_id`) REFERENCES `maestros` (`matricula`);

--
-- Constraints for table `inscripciones`
--
ALTER TABLE `inscripciones`
  ADD CONSTRAINT `inscripciones_ibfk_1` FOREIGN KEY (`alumno_id`) REFERENCES `alumnos` (`id`),
  ADD CONSTRAINT `inscripciones_ibfk_2` FOREIGN KEY (`curso_id`) REFERENCES `cursos` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
