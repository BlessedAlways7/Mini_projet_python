-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 09, 2024 at 07:46 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gestion`
--

-- --------------------------------------------------------

--
-- Table structure for table `fileattente`
--

CREATE TABLE `fileattente` (
  `nom` varchar(20) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `prenom` varchar(20) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `prioritaire` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `fileattente`
--

INSERT INTO `fileattente` (`nom`, `prenom`, `prioritaire`) VALUES
('Bonnette', 'Murielle', 0),
('Castanou', 'Albert', 0),
('Luamba', 'Julianna', 1),
('Wora', 'Esther', 1);

-- --------------------------------------------------------

--
-- Table structure for table `personnes`
--

CREATE TABLE `personnes` (
  `nom` varchar(20) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `prenom` varchar(20) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `genre` varchar(15) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `age` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `personnes`
--

INSERT INTO `personnes` (`nom`, `prenom`, `genre`, `age`) VALUES
('Lachance', 'Elizabeth', 'feminin', 20),
('Lambert', 'Joe', 'masculin', 38),
('Legrand', 'Sandra', 'feminin', 15),
('St-Denis', 'Samuel', 'masculin', 21),
('Standfield', 'Samuella', 'feminin', 29),
('Sung', 'Liam', 'masculin', 25);

-- --------------------------------------------------------

--
-- Table structure for table `reservations`
--

CREATE TABLE `reservations` (
  `nom` varchar(20) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `prenom` varchar(20) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `place` int(200) NOT NULL,
  `place_speciale` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reservations`
--

INSERT INTO `reservations` (`nom`, `prenom`, `place`, `place_speciale`) VALUES
('Bermington', 'Dan', 0, 2),
('Lafrance', 'Francois', 6, 0),
('Lapierre ', 'Bernard', 0, 2),
('Laroche', 'Eloic', 2, 0),
('Masson', 'Milan', 6, 0),
('Rousseau', 'Ella', 3, 0),
('Lacouche', 'Pierre', 7, 0),
('St-Henrie', 'Louiji', 2, 0),
('Lechanceux', 'Samuel', 1, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `fileattente`
--
ALTER TABLE `fileattente`
  ADD PRIMARY KEY (`nom`);

--
-- Indexes for table `personnes`
--
ALTER TABLE `personnes`
  ADD PRIMARY KEY (`nom`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
