---
title: Introducción
description: Qué es OpenTina y cómo está organizado el proyecto.
---

OpenTina es una comunidad de código abierto dedicada a proporcionar software de sistema de bajo nivel y soporte de distribuciones multi-SO para la plataforma de chips **Allwinner A733**.

El proyecto tiene como objetivo crear un ecosistema de software sólido y de calidad industrial para hardware basado en Allwinner A733: soporte de placas actualizado, integración con el kernel mainline y pipelines de construcción del sistema para Linux empotrado, plataformas de enrutamiento y distribuciones de escritorio principales.

## Mapa de repositorios

Todo el desarrollo se realiza en GitHub bajo la organización [opentina-org](https://github.com/opentina-org).

### Nivel bajo y BSP principal

| Repositorio | Descripción |
| :--- | :--- |
| [build](https://github.com/opentina-org/build) | Herramientas de orquestación, scripts y configuraciones de compilación — el punto de entrada único |
| [trusted-firmware-a](https://github.com/opentina-org/trusted-firmware-a) | Port de ARM Trusted Firmware (ATF) para Allwinner A733 — PSCI / Secure World |
| [optee_os](https://github.com/opentina-org/optee_os) | Lado de confianza del TEE (OP-TEE) para Allwinner A733 |
| [u-boot](https://github.com/opentina-org/u-boot) | Cargador de arranque U-Boot adaptado a Allwinner A733 — SPL, Fastboot, bootflow |
| [linux](https://github.com/opentina-org/linux) | Árbol del kernel Linux con DTS integrados para Allwinner A733 — rama **Linux 6.18 LTS** |
| [awbin](https://github.com/opentina-org/awbin) | Blobs binarios y firmware para Allwinner A733 |
| [xfel](https://github.com/opentina-org/xfel) | Herramientas FEL diminutas para SoC Allwinner — comunicación USB en modo FEL |

### Sistemas de compilación y distribuciones de SO

| Repositorio | Descripción |
| :--- | :--- |
| [buildroot](https://github.com/opentina-org/buildroot) | Árbol Buildroot preconfigurado para Allwinner A733 — rootfs mínimo y de arranque rápido |
| [openwrt](https://github.com/opentina-org/openwrt) | Definiciones de destino y pila de red de OpenWrt — soluciones de router y pasarela |
| [meta-opentina](https://github.com/opentina-org/meta-opentina) | Capa BSP del Yocto Project — Linux industrial y empresarial |
| [debian](https://github.com/opentina-org/debian) | Scripts de creación de rootfs y constructor de imágenes de Debian |
| [ubuntu](https://github.com/opentina-org/ubuntu) | Scripts de generación de rootfs y habilitación de placas de Ubuntu |

### Otros recursos

| Recurso | Descripción |
| :--- | :--- |
| [docs](https://github.com/opentina-org/docs) | Guías detallados y documentación técnica |
| [opentina](https://github.com/opentina-org/opentina) | Repositorio meta de la comunidad — [gestión de incidencias](https://github.com/opentina-org/opentina/issues) del proyecto |
| [.github](https://github.com/opentina-org/.github) | Perfil de la organización y archivos de salud de la comunidad |

## Inicio rápido

Clone el repositorio de orquestación de nivel superior:

```bash
git clone https://github.com/opentina-org/build.git
cd build
```

**1. Inicializar y obtener el código fuente** — descarga todos los repositorios necesarios mediante el manifiesto predeterminado:

```bash
./build.sh init
```

**2. Listar las placas compatibles y los tipos de rootfs:**

```bash
./build.sh targets
```

**3. Iniciar la compilación de una imagen** — reemplace `<BOARD_NAME>` con una placa del paso anterior:

```bash
./build.sh <BOARD_NAME> build
```

Para instrucciones detalladas, opciones de compilación y configuración avanzada, consulte el [README del repositorio build](https://github.com/opentina-org/build/blob/tina-dev/README.md).

## Obtener ayuda

Si encuentra algún problema durante el uso, [abra una incidencia](https://github.com/opentina-org/opentina/issues). Se aceptan informes de errores, preguntas y pull requests.
