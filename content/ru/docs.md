---
title: Введение
description: Что такое OpenTina и как устроен проект.
---

OpenTina — это открытое сообщество, предоставляющее низкоуровневое системное ПО и поддержку мульти-ОС дистрибутивов для чип-платформы **Allwinner A733**.

Проект создаёт надёжную программную экосистему промышленного уровня для аппаратных платформ на базе Allwinner A733: актуальную поддержку платформ, интеграцию с mainline-ядром и конвейеры сборки для встраиваемого Linux, роутерных платформ и основных настольных дистрибутивов.

## Карта репозиториев

Вся разработка ведётся на GitHub в организации [opentina-org](https://github.com/opentina-org).

### Низкоуровневый стек и BSP

| Репозиторий | Описание |
| :--- | :--- |
| [build](https://github.com/opentina-org/build) | Инструменты оркестрации, скрипты и конфигурации сборки — единая точка входа |
| [trusted-firmware-a](https://github.com/opentina-org/trusted-firmware-a) | Порт ARM Trusted Firmware (ATF) для Allwinner A733 — PSCI / Secure World |
| [optee_os](https://github.com/opentina-org/optee_os) | Доверенная часть TEE (OP-TEE) для Allwinner A733 |
| [u-boot](https://github.com/opentina-org/u-boot) | Загрузчик U-Boot для платформ Allwinner A733 — SPL, Fastboot, процесс загрузки |
| [linux](https://github.com/opentina-org/linux) | Дерево ядра Linux с встроенными DTS для Allwinner A733 — ветка **Linux 6.18 LTS** |
| [awbin](https://github.com/opentina-org/awbin) | Бинарные компоненты и прошивки для Allwinner A733 |
| [xfel](https://github.com/opentina-org/xfel) | Компактные FEL-инструменты для SoC Allwinner — связь по USB в режиме FEL |

### Системы сборки и дистрибутивы ОС

| Репозиторий | Описание |
| :--- | :--- |
| [buildroot](https://github.com/opentina-org/buildroot) | Преднастроенное для Allwinner A733 дерево Buildroot — минимальная rootfs с быстрой загрузкой |
| [openwrt](https://github.com/opentina-org/openwrt) | Определения целей и сетевой стек OpenWrt — решения для роутеров и шлюзов |
| [meta-opentina](https://github.com/opentina-org/meta-opentina) | Слой BSP Yocto Project — промышленный и корпоративный Linux |
| [debian](https://github.com/opentina-org/debian) | Скрипты создания rootfs и сборщик образов Debian |
| [ubuntu](https://github.com/opentina-org/ubuntu) | Скрипты генерации rootfs и поддержка плат на Ubuntu |

### Другие ресурсы

| Ресурс | Описание |
| :--- | :--- |
| [docs](https://github.com/opentina-org/docs) | Подробные руководства и техническая документация |
| [opentina](https://github.com/opentina-org/opentina) | Мета-репозиторий сообщества — [трекер проблем](https://github.com/opentina-org/opentina/issues) проекта |
| [.github](https://github.com/opentina-org/.github) | Профиль организации и файлы здоровья сообщества |

## Быстрый старт

Клонируйте верхнеуровневый репозиторий оркестрации:

```bash
git clone https://github.com/opentina-org/build.git
cd build
```

**1. Инициализация и загрузка деревьев исходников** — загружает все необходимые репозитории по манифесту по умолчанию:

```bash
./build.sh init
```

**2. Список поддерживаемых платформ и типов rootfs:**

```bash
./build.sh targets
```

**3. Запуск сборки образа** — замените `<BOARD_NAME>` на платформу из предыдущего шага:

```bash
./build.sh <BOARD_NAME> build
```

Подробные инструкции, параметры сборки и расширенная конфигурация — в [README репозитория build](https://github.com/opentina-org/build/blob/tina-dev/README.md).

## Получение помощи

Если во время работы возникли проблемы, [создайте issue](https://github.com/opentina-org/opentina/issues). Сообщения об ошибках, вопросы и pull request приветствуются.
