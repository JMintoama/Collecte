#
# Structure de la table `admin`
#

CREATE TABLE admin (²
  id tinyint(3) unsigned NOT NULL auto_increment,
  nom varchar(50) NOT NULL default '',
  email varchar(75) NOT NULL default '',
  login varchar(20) NOT NULL default '',
  pass varchar(32) NOT NULL default '',
  destination varchar(30) NOT NULL default '',
  PRIMARY KEY  (id)
) TYPE=MyISAM;

#
# Contenu de la table `admin`
#

INSERT INTO admin VALUES (1, 'btissam', 'mbtissam@hotmail.com', 'btissam', '91adce762775004125bf88212bf4df90', 'indexation');
INSERT INTO admin VALUES (5, '', '', 'latifa', 'e69248dcdc9ccb1121d7aec4afbb2aa7', 'suivi');

#
# Structure de la table `collecteur`
#

CREATE TABLE collecteur (
  nomrc varchar(100) NOT NULL default '',
  PRIMARY KEY  (nomrc)
) TYPE=MyISAM;

#
# Contenu de la table `collecteur`
#

# --------------------------------------------------------

#
# Structure de la table `control`
#

CREATE TABLE control (
  nomc varchar(100) NOT NULL default '',
  dat_ctrl date NOT NULL default '0000-00-00',
  observation varchar(200) default NULL,
  retourne char(3) NOT NULL default '',
  dat_retour date default NULL,
  dat_valid date NOT NULL default '0000-00-00',
  visa varchar(50) NOT NULL default '',
  n_enregistrement smallint(5) NOT NULL default '0',
  dat_recepc date NOT NULL default '0000-00-00',
  PRIMARY KEY  (nomc,n_enregistrement)
) TYPE=MyISAM;

#
# Contenu de la table `control`
#

INSERT INTO control VALUES ('Rabia AMJOUD', '0000-00-00', '', '', '0000-00-00', '2006-03-15', '', 3185, '0000-00-00');
INSERT INTO control VALUES ('Rabia AMJOUD', '0000-00-00', '', '', '0000-00-00', '2006-03-15', '', 3186, '0000-00-00');
INSERT INTO control VALUES ('Rabia AMJOUD', '0000-00-00', '', '', '0000-00-00', '2006-03-15', '', 3187, '0000-00-00');

# --------------------------------------------------------

#
# Structure de la table `controleur`
#

CREATE TABLE controleur (
  nomc varchar(100) NOT NULL default '',
  PRIMARY KEY  (nomc)
) TYPE=MyISAM;

#
# Contenu de la table `controleur`
#

# --------------------------------------------------------

#
# Structure de la table `controleurpv`
#

CREATE TABLE controleurpv (
  controleur varchar(100) NOT NULL default '',
  PRIMARY KEY  (controleur)
) TYPE=MyISAM;

#
# Contenu de la table `controleurpv`
#

# --------------------------------------------------------

#
# Structure de la table `depot`
#

CREATE TABLE depot (
  type varchar(30) NOT NULL default '',
  PRIMARY KEY  (type),
  KEY type (type)
) TYPE=MyISAM;

#
# Contenu de la table `depot`
#

INSERT INTO depot VALUES ('Achat');
INSERT INTO depot VALUES ('Dep�t Obligatoire');
INSERT INTO depot VALUES ('Don');
INSERT INTO depot VALUES ('Pr�t');
# --------------------------------------------------------

#
# Structure de la table `doc`
#

CREATE TABLE doc (
  n_enregistrement bigint(5) unsigned NOT NULL default '0',
  titre varchar(200) NOT NULL default '',
  titre_article varchar(200) default NULL,
  pages varchar(30) default '0',
  domaine varchar(80) NOT NULL default '',
  type varchar(100) NOT NULL default '',
  periodicite char(3) default '0',
  vol varchar(25) NOT NULL default '',
  tom varchar(25) NOT NULL default '',
  num varchar(25) NOT NULL default '',
  statut varchar(10) NOT NULL default '0',
  n_periodique smallint(5) default NULL,
  lang char(2) NOT NULL default '',
  PRIMARY KEY  (n_enregistrement),
  KEY titre (titre)
) TYPE=MyISAM;

#
# Contenu de la table `doc`
#

INSERT INTO doc VALUES (12, '������� � ����� ������� ������� �������', '', '407', 'Individu - Culture - Soci�t�', '', 'np', '', '', '', 'fini', 0, 'Ar');


# --------------------------------------------------------

#
# Structure de la table `domaine`
#

CREATE TABLE domaine (
  domaine varchar(100) NOT NULL default '',
  PRIMARY KEY  (domaine)
) TYPE=MyISAM;

#
# Contenu de la table `domaine`
#

INSERT INTO domaine VALUES ('Activit�s Economiques');

# --------------------------------------------------------

#
# Structure de la table `ecriture`
#

CREATE TABLE ecriture (
  auteur varchar(255) NOT NULL default '0',
  n_enregistrement smallint(5) NOT NULL default '0',
  PRIMARY KEY  (auteur,n_enregistrement)
) TYPE=MyISAM;

#
# Contenu de la table `ecriture`
#

INSERT INTO ecriture VALUES ('', 0);

# --------------------------------------------------------

#
# Structure de la table `editeur`
#

CREATE TABLE editeur (
  editeur varchar(200) NOT NULL default '',
  PRIMARY KEY  (editeur)
) TYPE=MyISAM;

#
# Contenu de la table `editeur`
#

# --------------------------------------------------------

#
# Structure de la table `edition`
#

CREATE TABLE edition (
  editeur varchar(255) NOT NULL default '0',
  n_enregistrement smallint(5) NOT NULL default '0',
  date_edition date NOT NULL default '0000-00-00',
  ville_edition varchar(60) default NULL,
  PRIMARY KEY  (editeur,n_enregistrement)
) TYPE=MyISAM;

#
# Contenu de la table `edition`
#

INSERT INTO edition VALUES ('��� ����', 12, '1998-00-00', '');

# --------------------------------------------------------

#
# Structure de la table `fournit`
#

CREATE TABLE fournit (
  source varchar(255) NOT NULL default '0',
  n_enregistrement smallint(5) NOT NULL default '0',
  date_reception date NOT NULL default '0000-00-00',
  obligation varchar(30) NOT NULL default '',
  PRIMARY KEY  (source,n_enregistrement)
) TYPE=MyISAM;

#
# Contenu de la table `fournit`
#

INSERT INTO fournit VALUES ('Acquisition du Centre National de Documentation', 12, '2003-04-14', 'Achat');

# --------------------------------------------------------

#
# Structure de la table `indexation`
#

CREATE TABLE indexation (
  nomi varchar(100) NOT NULL default '',
  n_enregistrement smallint(5) NOT NULL default '0',
  dat_reception date NOT NULL default '0000-00-00',
  dat_indexation date NOT NULL default '0000-00-00',
  dat_saisi date NOT NULL default '0000-00-00',
  dat_envoi date NOT NULL default '0000-00-00',
  PRIMARY KEY  (nomi,n_enregistrement)
) TYPE=MyISAM;

#
# Contenu de la table `indexation`
#

INSERT INTO indexation VALUES ('Ilham NAHAS', 819, '2004-01-26', '2004-01-27', '2004-03-17', '2004-03-30');

# --------------------------------------------------------

#
# Structure de la table `indexeur`
#

CREATE TABLE indexeur (
  nomi varchar(100) NOT NULL default '',
  PRIMARY KEY  (nomi)
) TYPE=MyISAM;

#
# Contenu de la table `indexeur`
#

# --------------------------------------------------------

#
# Structure de la table `source`
#

CREATE TABLE source (
  source varchar(200) NOT NULL default '',
  PRIMARY KEY  (source)
) TYPE=MyISAM;

#
# Contenu de la table `source`
#

INSERT INTO source VALUES ('');


# --------------------------------------------------------

#
# Structure de la table `suiveur`
#
# --------------------------------------------------------

#
# Structure de la table `indexeur`
#

CREATE TABLE indexeur (
  nomi varchar(100) NOT NULL default '',
  PRIMARY KEY  (nomi)
) TYPE=MyISAM;

#
# Contenu de la table `indexeur`
#

# --------------------------------------------------------

#
# Structure de la table `source`
#

CREATE TABLE source (
  source varchar(200) NOT NULL default '',
  PRIMARY KEY  (source)
) TYPE=MyISAM;

#
# Contenu de la table `source`
#

INSERT INTO source VALUES ('');

CREATE TABLE suiveur (
  noms varchar(100) NOT NULL default '',
  PRIMARY KEY  (noms)
) TYPE=MyISAM;

#
# Contenu de la table `suiveur`
#

# --------------------------------------------------------

#
# Structure de la table `suivi`
#

CREATE TABLE suivi (
  noms varchar(100) NOT NULL default '',
  n_enregistrement smallint(5) NOT NULL default '0',
  datenvoi_t date NOT NULL default '0000-00-00',
  dat_rsuivi date NOT NULL default '0000-00-00',
  datsaisi_ic date NOT NULL default '0000-00-00',
  datenvoi_sir date NOT NULL default '0000-00-00',
  dat_pv date NOT NULL default '0000-00-00',
  dat_mont date NOT NULL default '0000-00-00',
  dat_rrsuivi date NOT NULL default '0000-00-00',
  datsaisi_pv date NOT NULL default '0000-00-00'
) TYPE=MyISAM;

#
# Contenu de la table `suivi`
#

INSERT INTO suivi VALUES ('', 12, '2004-02-10', '0000-00-00', '0000-00-00', '0000-00-00', '0000-00-00', '0000-00-00', '0000-00-00', '0000-00-00');


# --------------------------------------------------------

#
# Structure de la table `vue`
#

CREATE TABLE vue (
  controleur varchar(100) NOT NULL default '',
  n_enregistrement smallint(5) NOT NULL default '0',
  dat_ctrl date NOT NULL default '0000-00-00',
  visa varchar(50) NOT NULL default '',
  dat_recepv date NOT NULL default '0000-00-00',
  PRIMARY KEY  (controleur,n_enregistrement)
) TYPE=MyISAM;

#
# Contenu de la table `vue`
#

INSERT INTO vue VALUES ('', 12, '0000-00-00', '', '0000-00-00');



