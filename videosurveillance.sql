-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost:3306
-- Généré le :  mar. 24 déc. 2019 à 15:17
-- Version du serveur :  10.3.17-MariaDB-0+deb10u1
-- Version de PHP :  7.3.11-1~deb10u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
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
-- Structure de la table `champFormulaire`
--

CREATE TABLE `champFormulaire` (
  `id` tinyint(4) NOT NULL,
  `typeDeChamp` tinyint(4) NOT NULL DEFAULT 0 COMMENT 'Type de champ',
  `formulaire` varchar(255) NOT NULL COMMENT 'Nom du menu concerné',
  `nomChamp` varchar(255) NOT NULL,
  `titreChamp` varchar(255) NOT NULL COMMENT 'Nom affiché dans le menu',
  `minimum` smallint(6) DEFAULT NULL,
  `maximum` smallint(6) DEFAULT NULL,
  `pas` tinyint(4) DEFAULT NULL,
  `valeur` varchar(255) DEFAULT NULL COMMENT 'Choix disponibles',
  `valeurParDefaut` smallint(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Liste des choix disponibles par menu';

--
-- Déchargement des données de la table `champFormulaire`
--

INSERT INTO `champFormulaire` (`id`, `typeDeChamp`, `formulaire`, `nomChamp`, `titreChamp`, `minimum`, `maximum`, `pas`, `valeur`, `valeurParDefaut`) VALUES
(1, 1, 'filtreAgeEnregistrement', 'intervalle', 'Aucun', NULL, NULL, NULL, '-1', NULL),
(2, 1, 'filtreAgeEnregistrement', 'intervalle', '1 jour', NULL, NULL, NULL, '86400', NULL),
(3, 1, 'filtreAgeEnregistrement', 'intervalle', '12 heures', NULL, NULL, NULL, '43200', NULL),
(4, 1, 'filtreAgeEnregistrement', 'intervalle', '4 heures', NULL, NULL, NULL, '14400', NULL),
(5, 1, 'filtreAgeEnregistrement', 'intervalle', '2 heures', NULL, NULL, NULL, '7200', NULL),
(6, 1, 'filtreAgeEnregistrement', 'intervalle', '1 heure', NULL, NULL, NULL, '3600', NULL),
(7, 1, 'filtreAgeEnregistrement', 'intervalle', '30 minutes', NULL, NULL, NULL, '1800', NULL),
(8, 1, 'filtreAgeEnregistrement', 'intervalle', '15 minutes', NULL, NULL, NULL, '900', NULL),
(9, 1, 'parametreCamera', 'effet', 'Aucun', NULL, NULL, NULL, 'none', NULL),
(10, 1, 'parametreCamera', 'effet', 'Solarisé', NULL, NULL, NULL, 'solarise', NULL),
(11, 1, 'parametreCamera', 'effet', 'Postérisé', NULL, NULL, NULL, 'posterise', NULL),
(12, 1, 'parametreCamera', 'effet', 'Tableau blanc', NULL, NULL, NULL, 'whiteboard', NULL),
(13, 1, 'parametreCamera', 'effet', 'Tableau noir', NULL, NULL, NULL, 'blackboard', NULL),
(14, 1, 'parametreCamera', 'effet', 'Esquisse', NULL, NULL, NULL, 'sketch', NULL),
(15, 1, 'parametreCamera', 'effet', 'Débruité', NULL, NULL, NULL, 'denoise', NULL),
(16, 1, 'parametreCamera', 'effet', 'Relief', NULL, NULL, NULL, 'emboss', NULL),
(17, 1, 'parametreCamera', 'effet', 'Peinture à l\'huile', NULL, NULL, NULL, 'oilpaint', NULL),
(18, 1, 'parametreCamera', 'effet', 'Esquisse hachurée', NULL, NULL, NULL, 'hatch', NULL),
(19, 1, 'parametreCamera', 'effet', 'Graphite', NULL, NULL, NULL, 'gpen', NULL),
(20, 1, 'parametreCamera', 'effet', 'Pastel', NULL, NULL, NULL, 'pastel', NULL),
(21, 1, 'parametreCamera', 'effet', 'Aquarelle', NULL, NULL, NULL, 'watercolour', NULL),
(22, 1, 'parametreCamera', 'effet', 'Effet de grain', NULL, NULL, NULL, 'film', NULL),
(23, 1, 'parametreCamera', 'effet', 'Brouillé', NULL, NULL, NULL, 'blur', NULL),
(24, 1, 'parametreCamera', 'effet', 'Saturé', NULL, NULL, NULL, 'saturation', NULL),
(25, 1, 'parametreCamera', 'exposition', 'Automatique', NULL, NULL, NULL, 'auto', NULL),
(26, 1, 'parametreCamera', 'exposition', 'Nuit', NULL, NULL, NULL, 'night', NULL),
(27, 1, 'parametreCamera', 'exposition', 'Prévisualisation de nuit', NULL, NULL, NULL, 'nightpreview', NULL),
(28, 1, 'parametreCamera', 'exposition', 'Lumière noire', NULL, NULL, NULL, 'blacklight', NULL),
(29, 1, 'parametreCamera', 'exposition', 'Projecteur', NULL, NULL, NULL, 'spotlight', NULL),
(30, 1, 'parametreCamera', 'exposition', 'Sport', NULL, NULL, NULL, 'sports', NULL),
(31, 1, 'parametreCamera', 'exposition', 'Neige', NULL, NULL, NULL, 'snow', NULL),
(32, 1, 'parametreCamera', 'exposition', 'Plage', NULL, NULL, NULL, 'beach', NULL),
(33, 1, 'parametreCamera', 'exposition', 'FPS à valeur fixe', NULL, NULL, NULL, 'fixedfps', NULL),
(34, 1, 'parametreCamera', 'exposition', 'Stabilisation', NULL, NULL, NULL, 'antishake', NULL),
(35, 1, 'parametreCamera', 'exposition', 'Feux d\'artifices', NULL, NULL, NULL, 'firework', NULL),
(36, 1, 'parametreCamera', 'balanceBlanc', 'Désactivé', NULL, NULL, NULL, 'off', NULL),
(37, 1, 'parametreCamera', 'balanceBlanc', 'Automatique', NULL, NULL, NULL, 'auto', NULL),
(38, 1, 'parametreCamera', 'balanceBlanc', 'Ensoleillé', NULL, NULL, NULL, 'sun', NULL),
(39, 1, 'parametreCamera', 'balanceBlanc', 'Nuageux', NULL, NULL, NULL, 'cloud', NULL),
(40, 1, 'parametreCamera', 'balanceBlanc', 'Ombré', NULL, NULL, NULL, 'shade', NULL),
(41, 1, 'parametreCamera', 'balanceBlanc', 'Tungstène', NULL, NULL, NULL, 'tungsten', NULL),
(42, 1, 'parametreCamera', 'balanceBlanc', 'Fluorescent', NULL, NULL, NULL, 'fluorescent', NULL),
(43, 1, 'parametreCamera', 'balanceBlanc', 'Incandescent', NULL, NULL, NULL, 'incandescent', NULL),
(44, 1, 'parametreCamera', 'balanceBlanc', 'Flash', NULL, NULL, NULL, 'flash', NULL),
(45, 1, 'parametreCamera', 'balanceBlanc', 'Horizon', NULL, NULL, NULL, 'horizon', NULL),
(46, 1, 'parametreCamera', 'balanceBlanc', 'Correcteur caméra IR', NULL, NULL, NULL, 'greyword', NULL),
(47, 2, 'parametreCamera', 'finesse', 'Finesse de l\'image', -100, 100, 1, NULL, 0),
(48, 2, 'parametreCamera', 'contraste', 'Contraste', -100, 100, 1, NULL, 0),
(49, 2, 'parametreCamera', 'luminosite', 'Luminosité', 0, 100, 1, NULL, 50),
(50, 2, 'parametreCamera', 'saturation', 'Saturation', -100, 100, 1, NULL, 0),
(51, 2, 'parametreCamera', 'iso', 'ISO', 100, 800, 1, NULL, 450),
(52, 2, 'parametreCamera', 'compensationLuminosite', 'Compensation de la luminosité', -10, 10, 1, NULL, 0),
(53, 2, 'parametreCamera', 'sharpness', 'Rotation', -100, 100, 1, NULL, 0),
(54, 3, 'parametreCamera', 'retourneHorizontal', 'Retournement horizontal', NULL, NULL, NULL, NULL, 1),
(55, 3, 'parametreCamera', 'retourneVertical', 'Retournement vertical', NULL, NULL, NULL, NULL, 0);

-- --------------------------------------------------------

--
-- Structure de la table `typeChampFormulaire`
--

CREATE TABLE `typeChampFormulaire` (
  `id` tinyint(11) NOT NULL,
  `champ` varchar(255) NOT NULL COMMENT 'Type de champ'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `typeChampFormulaire`
--

INSERT INTO `typeChampFormulaire` (`id`, `champ`) VALUES
(1, 'menuDeroulant'),
(2, 'curseur'),
(3, 'caseACocher');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `champFormulaire`
--
ALTER TABLE `champFormulaire`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Type de champ formulaire` (`typeDeChamp`);

--
-- Index pour la table `typeChampFormulaire`
--
ALTER TABLE `typeChampFormulaire`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `champFormulaire`
--
ALTER TABLE `champFormulaire`
  MODIFY `id` tinyint(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT pour la table `typeChampFormulaire`
--
ALTER TABLE `typeChampFormulaire`
  MODIFY `id` tinyint(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `champFormulaire`
--
ALTER TABLE `champFormulaire`
  ADD CONSTRAINT `Type de champ formulaire` FOREIGN KEY (`typeDeChamp`) REFERENCES `typeChampFormulaire` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
