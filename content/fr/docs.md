---
title: Introduction
description: Ce qu'est OpenTina et comment le projet est organisé.
---

OpenTina est une communauté open source dédiée à la fourniture de logiciels système de bas niveau et d'une prise en charge multi-OS pour la plateforme de puces **Allwinner A733**.

Le projet vise à construire un écosystème logiciel robuste et de qualité production pour le matériel basé sur l'Allwinner A733 : support des cartes à jour, intégration au noyau mainline et pipelines de construction du système pour Linux embarqué, les plateformes de routage et les distributions de bureau principales.

## Carte des dépôts

Tout le développement se fait sur GitHub au sein de l'organisation [opentina-org](https://github.com/opentina-org).

### Niveau bas & BSP principal

| Dépôt | Description |
| :--- | :--- |
| [build](https://github.com/opentina-org/build) | Outils d'orchestration, scripts et configurations de build — le point d'entrée unique |
| [trusted-firmware-a](https://github.com/opentina-org/trusted-firmware-a) | Port ARM Trusted Firmware (ATF) pour Allwinner A733 — PSCI / Secure World |
| [optee_os](https://github.com/opentina-org/optee_os) | Part de confiance du TEE (OP-TEE) pour Allwinner A733 |
| [u-boot](https://github.com/opentina-org/u-boot) | Chargeur de démarrage U-Boot adapté aux plateformes Allwinner A733 — SPL, Fastboot, bootflow |
| [linux](https://github.com/opentina-org/linux) | Arbre du noyau Linux avec DTS embarqués pour Allwinner A733 — branche **Linux 6.18 LTS** |
| [awbin](https://github.com/opentina-org/awbin) | Blobs binaires et firmware pour Allwinner A733 |
| [xfel](https://github.com/opentina-org/xfel) | Outils FEL compacts pour les SoC Allwinner — communication USB en mode FEL |

### Systèmes de build & distributions OS

| Dépôt | Description |
| :--- | :--- |
| [buildroot](https://github.com/opentina-org/buildroot) | Arbre Buildroot préconfiguré pour Allwinner A733 — rootfs minimal et démarrage rapide |
| [openwrt](https://github.com/opentina-org/openwrt) | Définitions de cible et pile réseau OpenWrt — solutions routeur / passerelle |
| [meta-opentina](https://github.com/opentina-org/meta-opentina) | Couche BSP Yocto Project — Linux industriel et entreprise |
| [debian](https://github.com/opentina-org/debian) | Scripts de création du rootfs et constructeur d'images Debian |
| [ubuntu](https://github.com/opentina-org/ubuntu) | Scripts de génération du rootfs et support des cartes Ubuntu |

### Autres ressources

| Ressource | Description |
| :--- | :--- |
| [docs](https://github.com/opentina-org/docs) | Guides détaillés et documentation technique |
| [opentina](https://github.com/opentina-org/opentina) | Dépôt méta de la communauté — [suivi des issues](https://github.com/opentina-org/opentina/issues) du projet |
| [.github](https://github.com/opentina-org/.github) | Profil de l'organisation et fichiers de santé de la communauté |

## Démarrage rapide

Clonnez le dépôt d'orchestration de haut niveau :

```bash
git clone https://github.com/opentina-org/build.git
cd build
```

**1. Initialiser et récupérer les sources** — télécharge tous les dépôts requis via le manifeste par défaut :

```bash
./build.sh init
```

**2. Lister les cartes supportées et les types de rootfs :**

```bash
./build.sh targets
```

**3. Lancer la construction d'une image** — remplacez `<BOARD_NAME>` par une carte de l'étape précédente :

```bash
./build.sh <BOARD_NAME> build
```

Pour des instructions détaillées, des options de build et une configuration avancée, consultez le [README du dépôt build](https://github.com/opentina-org/build/blob/tina-dev/README.md).

## Obtenir de l'aide

Si vous rencontrez un problème pendant l'utilisation, [ouvrez un issue](https://github.com/opentina-org/opentina/issues). Rapports de bugs, questions et pull requests sont les bienvenus.
