---
title: Einführung
description: Was OpenTina ist und wie das Projekt organisiert ist.
---

OpenTina ist eine Open-Source-Community, die Low-Level-Systemsoftware und Multi-OS-Distributionsunterstützung für die **Allwinner-A733**-Chipplattform bereitstellt.

Das Projekt baut ein robustes, produktionsreifes Software-Ökosystem für Hardware auf Basis des Allwinner A733: aktuelle Board-Unterstützung, Mainline-Kernel-Integration und System-Build-Pipelines für Embedded Linux, Router-Plattformen und gängige Desktop-Distributionen.

## Karte der Repositorien

Die gesamte Entwicklung erfolgt auf GitHub unter der Organisation [opentina-org](https://github.com/opentina-org).

### Low-Level & Kern-BSP

| Repository | Beschreibung |
| :--- | :--- |
| [build](https://github.com/opentina-org/build) | Orchestrierungswerkzeuge, Build-Skripte und Konfigurationen — der Einstiegspunkt für den Build |
| [trusted-firmware-a](https://github.com/opentina-org/trusted-firmware-a) | ARM-Trusted-Firmware-(ATF-)Port für Allwinner A733 — PSCI / Secure World |
| [optee_os](https://github.com/opentina-org/optee_os) | Vertrauenswürdige Seite der TEE (OP-TEE) für Allwinner A733 |
| [u-boot](https://github.com/opentina-org/u-boot) | Für Allwinner-A733-Plattformen angepasster U-Boot-Bootloader — SPL, Fastboot, Bootflow |
| [linux](https://github.com/opentina-org/linux) | Linux-Kernelbaum mit eingebetteten DTS für Allwinner A733 — **Linux 6.18 LTS**-Branch |
| [awbin](https://github.com/opentina-org/awbin) | Binäre Blobs und Firmware für Allwinner A733 |
| [xfel](https://github.com/opentina-org/xfel) | Kleine FEL-Werkzeuge für Allwinner-SoCs — Kommunikation per USB im FEL-Modus |

### Build-Systeme & OS-Distributionen

| Repository | Beschreibung |
| :--- | :--- |
| [buildroot](https://github.com/opentina-org/buildroot) | Für Allwinner A733 vorkonfigurierter Buildroot — minimales, schnell startendes Rootfs |
| [openwrt](https://github.com/opentina-org/openwrt) | OpenWrt-Target-Definitionen und Netzwerk-Stack — Router- und Gateway-Lösungen |
| [meta-opentina](https://github.com/opentina-org/meta-opentina) | Yocto-Project-BSP-Layer — Industrie- und Enterprise-Linux |
| [debian](https://github.com/opentina-org/debian) | Debian-Rootfs-Erstellungsskripte und Image-Builder |
| [ubuntu](https://github.com/opentina-org/ubuntu) | Ubuntu-Rootfs-Erstellungsskripte und Board-Enablement |

### Weitere Ressourcen

| Ressource | Beschreibung |
| :--- | :--- |
| [docs](https://github.com/opentina-org/docs) | Tiefgehende Anleitungen und technische Dokumentation |
| [opentina](https://github.com/opentina-org/opentina) | Meta-Repositorium der Community — [Issue-Tracker](https://github.com/opentina-org/opentina/issues) des Projekts |
| [.github](https://github.com/opentina-org/.github) | Organisationsprofil und Community-Health-Dateien |

## Erste Schritte

Klonen Sie das übergeordnete Orchestrierungsrepositorium:

```bash
git clone https://github.com/opentina-org/build.git
cd build
```

**1. Initialisieren und Quellen laden** — lädt alle benötigten Repositorien über das Standard-Manifest herunter:

```bash
./build.sh init
```

**2. Unterstützte Boards und Rootfs-Typen auflisten:**

```bash
./build.sh targets
```

**3. Image-Build starten** — ersetzen Sie `<BOARD_NAME>` durch ein Board aus dem vorherigen Schritt:

```bash
./build.sh <BOARD_NAME> build
```

Detaillierte Anleitungen, Build-Optionen und erweiterte Konfiguration finden Sie im [README des build-Repositoriums](https://github.com/opentina-org/build/blob/tina-dev/README.md).

## Hilfe erhalten

Wenn Ihnen beim Nutzung Probleme auffallen, [öffnen Sie ein Issue](https://github.com/opentina-org/opentina/issues). Fehlerberichte, Fragen und Pull Requests sind willkommen.
