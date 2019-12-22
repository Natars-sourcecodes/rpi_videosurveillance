-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Client :  localhost:3306
-- Généré le :  Ven 20 Décembre 2019 à 16:36
-- Version du serveur :  10.3.17-MariaDB-0+deb10u1
-- Version de PHP :  7.3.11-1~deb10u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `videosurveillance`
--

-- --------------------------------------------------------

--
-- Structure de la table `choixMenuDeroulant`
--

CREATE TABLE `choixMenuDeroulant` (
  `id` tinyint(4) NOT NULL,
  `menu` varchar(255) NOT NULL COMMENT 'Nom du menu concerné',
  `choix` varchar(255) NOT NULL COMMENT 'Choix disponibles',
  `nomChoix` varchar(255) NOT NULL COMMENT 'Nom affiché dans le menu'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Liste des choix disponibles par menu';

--
-- Contenu de la table `choixMenuDeroulant`
--

INSERT INTO `choixMenuDeroulant` (`id`, `menu`, `choix`, `nomChoix`) VALUES
(1, 'intervalle', '-1', '------'),
(2, 'intervalle', '24', '1 jour'),
(3, 'intervalle', '12', '12 heures'),
(4, 'intervalle', '4', '4 heures'),
(5, 'intervalle', '2', '2 heures'),
(6, 'intervalle', '1', '1 heure'),
(7, 'intervalle', '0.5', '30 minutes'),
(8, 'intervalle', '0.25', '15 minutes'),
(9, 'parametreCameraEffet', 'none', '------'),
(10, 'parametreCameraEffet', 'solarise', 'Solarisé'),
(11, 'parametreCameraEffet', 'posterise', 'Postérisé'),
(12, 'parametreCameraEffet', 'whiteboard', 'Tableau blanc'),
(13, 'parametreCameraEffet', 'blackboard', 'Tableau noir'),
(14, 'parametreCameraEffet', 'sketch', 'Esquisse'),
(15, 'parametreCameraEffet', 'denoise', 'Débruité'),
(16, 'parametreCameraEffet', 'emboss', 'Relief'),
(17, 'parametreCameraEffet', 'oilpaint', 'Peinture à l\'huile'),
(18, 'parametreCameraEffet', 'hatch', 'Esquisse hachurée'),
(19, 'parametreCameraEffet', 'gpen', 'Graphite'),
(20, 'parametreCameraEffet', 'pastel', 'Pastel'),
(21, 'parametreCameraEffet', 'watercolour', 'Aquarelle'),
(22, 'parametreCameraEffet', 'film', 'Effet de grain'),
(23, 'parametreCameraEffet', 'blur', 'Brouillé'),
(24, 'parametreCameraEffet', 'saturation', 'Saturé'),
(25, 'parametreCameraExposition', 'auto', 'Automatique'),
(26, 'parametreCameraExposition', 'night', 'Nuit'),
(27, 'parametreCameraExposition', 'nightpreview', 'Prévisualisation de nuit'),
(28, 'parametreCameraExposition', 'blacklight', 'Lumière noire'),
(29, 'parametreCameraExposition', 'spotlight', 'Projecteur'),
(30, 'parametreCameraExposition', 'sports', 'Sport'),
(31, 'parametreCameraExposition', 'snow', 'Neige'),
(32, 'parametreCameraExposition', 'beach', 'Plage'),
(33, 'parametreCameraExposition', 'fixedfps', 'FPS à valeur fixe'),
(34, 'parametreCameraExposition', 'antishake', 'Stabilisation'),
(35, 'parametreCameraExposition', 'firework', 'Feux d\'artifices'),
(36, 'parametreCameraBalanceBlanc', 'off', 'Désactivé'),
(37, 'parametreCameraBalanceBlanc', 'auto', 'Automatique'),
(38, 'parametreCameraBalanceBlanc', 'sun', 'Ensoleillé'),
(39, 'parametreCameraBalanceBlanc', 'cloud', 'Nuageux'),
(40, 'parametreCameraBalanceBlanc', 'shade', 'Ombré'),
(41, 'parametreCameraBalanceBlanc', 'tungsten', 'Tungstène'),
(42, 'parametreCameraBalanceBlanc', 'fluorescent', 'Fluorescent'),
(43, 'parametreCameraBalanceBlanc', 'incandescent', 'Incandescent'),
(44, 'parametreCameraBalanceBlanc', 'flash', 'Flash'),
(45, 'parametreCameraBalanceBlanc', 'horizon', 'Horizon'),
(46, 'parametreCameraBalanceBlanc', 'greyword', 'Correcteur caméra IR');

--
-- Index pour les tables exportées
--

--
-- Index pour la table `choixMenuDeroulant`
--
ALTER TABLE `choixMenuDeroulant`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `choixMenuDeroulant`
--
ALTER TABLE `choixMenuDeroulant`
  MODIFY `id` tinyint(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
