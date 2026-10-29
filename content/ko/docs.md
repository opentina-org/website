---
title: 소개
description: OpenTina가 무엇이며 프로젝트가 어떻게 구성되어 있는지 소개합니다.
---

OpenTina는 **올위너(Allwinner) A733** 칩 플랫폼을 위한 저수준 시스템 소프트웨어와 멀티 OS 배포 지원을 제공하는 오픈 소스 커뮤니티입니다.

이 프로젝트는 올위너 A733 기반 하드웨어를 위한 견고하고 프로덕션급 소프트웨어 생태계를 구축합니다: 최신 보드 지원, 메인라인 커널 통합, 임베디드 Linux·라우터 플랫폼·주요 데스크톱 배포판을 아우르는 시스템 빌드 파이프라인입니다.

## 저장소 지도

모든 개발은 GitHub의 [opentina-org](https://github.com/opentina-org) 조직에서 진행됩니다.

### 저수준 및 핵심 BSP

| 저장소 | 설명 |
| :--- | :--- |
| [build](https://github.com/opentina-org/build) | 최상위 오케스트레이션 도구, 빌드 스크립트 및 설정 — 원클릭 빌드 진입점 |
| [trusted-firmware-a](https://github.com/opentina-org/trusted-firmware-a) | 올위너 A733용 ARM Trusted Firmware(ATF) 포트 — PSCI / 시큐어 월드 |
| [optee_os](https://github.com/opentina-org/optee_os) | 올위너 A733용 TEE(OP-TEE)의 신뢰 측 구현 |
| [u-boot](https://github.com/opentina-org/u-boot) | 올위너 A733 플랫폼에 맞춘 U-Boot 부트로더 — SPL, Fastboot, 부트 플로우 |
| [linux](https://github.com/opentina-org/linux) | 올위너 A733 임베디드 DTS를 포함한 Linux 커널 트리 — **Linux 6.18 LTS** 브랜치 |
| [awbin](https://github.com/opentina-org/awbin) | 올위너 A733 관련 바이너리 blob 및 펌웨어 |
| [xfel](https://github.com/opentina-org/xfel) | 올위너 SoC를 위한 초경량 FEL 도구 — USB를 통한 FEL 모드 통신 |

### 빌드 시스템 및 OS 배포판

| 저장소 | 설명 |
| :--- | :--- |
| [buildroot](https://github.com/opentina-org/buildroot) | 올위너 A733용으로 사전 구성된 Buildroot — 미니멀하고 빠르게 부팅되는 rootfs |
| [openwrt](https://github.com/opentina-org/openwrt) | 올위너 A733용 OpenWrt 타깃 정의 및 네트워크 스택 — 라우터 / 게이트웨이 솔루션 |
| [meta-opentina](https://github.com/opentina-org/meta-opentina) | Yocto Project BSP 레이어 — 산업용 / 엔터프라이즈 Linux |
| [debian](https://github.com/opentina-org/debian) | Debian rootfs 생성 스크립트 및 이미지 빌더 |
| [ubuntu](https://github.com/opentina-org/ubuntu) | Ubuntu rootfs 생성 스크립트 및 보드 지원 |

### 기타 리소스

| 리소스 | 설명 |
| :--- | :--- |
| [docs](https://github.com/opentina-org/docs) | 심층 가이드와 기술 문서 |
| [opentina](https://github.com/opentina-org/opentina) | 커뮤니티 메타 저장소 — 프로젝트의 [이슈 트래커](https://github.com/opentina-org/opentina/issues) |
| [.github](https://github.com/opentina-org/.github) | 조직 프로필 및 커뮤니티 건강 파일 |

## 빠른 시작

최상위 오케스트레이션 저장소를 클론합니다:

```bash
git clone https://github.com/opentina-org/build.git
cd build
```

**1. 초기화 및 소스 트리 가져오기** — 기본 매니페스트를 통해 필요한 모든 저장소를 다운로드합니다:

```bash
./build.sh init
```

**2. 지원되는 보드와 rootfs 유형 목록:**

```bash
./build.sh targets
```

**3. 이미지 빌드 시작** — `<BOARD_NAME>`을 이전 단계에 표시된 보드로 바꿉니다:

```bash
./build.sh <BOARD_NAME> build
```

자세한 사용법, 빌드 옵션 및 고급 구성은 [build 저장소 README](https://github.com/opentina-org/build/blob/tina-dev/README.md)를 참조하세요.

## 도움받기

사용 중 문제가 발생하면 [이슈를 등록](https://github.com/opentina-org/opentina/issues)해 주세요. 버그 보고, 질문, Pull Request 모두 환영합니다.
