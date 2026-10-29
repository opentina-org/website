---
title: Introduction
description: What OpenTina is, and how the project is organized.
---

OpenTina is an open-source community dedicated to providing low-level system software and multi-OS distribution support for the **Allwinner A733** chip platform.

The project aims to build a robust, production-grade software ecosystem for Allwinner A733-based hardware: up-to-date board support, mainline kernel integration, and system build pipelines across embedded Linux, router platforms, and mainstream desktop distributions.

## Repository map

All development happens on GitHub under the [opentina-org](https://github.com/opentina-org) organization.

### Low-level & core BSP

| Repository | Description |
| :--- | :--- |
| [build](https://github.com/opentina-org/build) | Orchestration tools, top-level build scripts & configs — the one-click build entrypoint |
| [trusted-firmware-a](https://github.com/opentina-org/trusted-firmware-a) | ARM Trusted Firmware (ATF) port for Allwinner A733 — PSCI / Secure World |
| [optee_os](https://github.com/opentina-org/optee_os) | Trusted side of the TEE (OP-TEE) for Allwinner A733 |
| [u-boot](https://github.com/opentina-org/u-boot) | U-Boot bootloader tailored for Allwinner A733 — SPL, Fastboot, bootflow |
| [linux](https://github.com/opentina-org/linux) | Linux kernel tree with embedded DTS for Allwinner A733 — **Linux 6.18 LTS** branch |
| [awbin](https://github.com/opentina-org/awbin) | Allwinner A733 related binary blobs and firmware |
| [xfel](https://github.com/opentina-org/xfel) | Tiny FEL tools for Allwinner SoCs — communicate over USB in FEL mode |

### Build systems & OS distributions

| Repository | Description |
| :--- | :--- |
| [buildroot](https://github.com/opentina-org/buildroot) | Buildroot tree pre-configured for Allwinner A733 — minimal, fast-booting rootfs |
| [openwrt](https://github.com/opentina-org/openwrt) | OpenWrt target definitions & network stack — router / gateway solutions |
| [meta-opentina](https://github.com/opentina-org/meta-opentina) | Yocto Project BSP layer — industrial / enterprise Linux |
| [debian](https://github.com/opentina-org/debian) | Debian rootfs creation scripts & image builder |
| [ubuntu](https://github.com/opentina-org/ubuntu) | Ubuntu rootfs generation scripts & board enablement |

### Other resources

| Resource | Description |
| :--- | :--- |
| [docs](https://github.com/opentina-org/docs) | In-depth guides and technical documentation |
| [opentina](https://github.com/opentina-org/opentina) | Community meta-repo — [issue tracker](https://github.com/opentina-org/opentina/issues) for the project |
| [.github](https://github.com/opentina-org/.github) | Organization profile and community health files |

## Quick start

Clone the top-level orchestration repository:

```bash
git clone https://github.com/opentina-org/build.git
cd build
```

**1. Initialize and fetch source trees** — downloads all required repositories via the default manifest:

```bash
./build.sh init
```

**2. List supported target boards and rootfs types:**

```bash
./build.sh targets
```

**3. Trigger image build** — replace `<BOARD_NAME>` with a board from the previous step:

```bash
./build.sh <BOARD_NAME> build
```

For detailed instructions, build options, and advanced configuration, see the [build repository README](https://github.com/opentina-org/build/blob/tina-dev/README.md).

## Getting help

If you encounter any issues while using the system, [submit an issue](https://github.com/opentina-org/opentina/issues). Bug reports, questions and pull requests are all welcome.
