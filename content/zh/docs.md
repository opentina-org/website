---
title: 简介
description: OpenTina 是什么，以及项目如何组织。
---

OpenTina 是一个开源社区，致力于为 **全志（Allwinner）A733** 芯片平台提供底层系统软件和多操作系统发行版支持。

项目旨在为基于全志 A733 的硬件打造稳健、生产级的软件生态：及时维护的板级支持、主线内核集成，以及覆盖嵌入式 Linux、路由平台和主流桌面发行版的系统构建流水线。

## 仓库地图

所有开发都在 GitHub 的 [opentina-org](https://github.com/opentina-org) 组织下进行。

### 底层与核心 BSP

| 仓库 | 说明 |
| :--- | :--- |
| [build](https://github.com/opentina-org/build) | 顶层编排工具、构建脚本与配置 —— 一键构建入口 |
| [trusted-firmware-a](https://github.com/opentina-org/trusted-firmware-a) | 全志 A733 的 ARM 可信固件（ATF）移植 —— PSCI / 安全世界 |
| [optee_os](https://github.com/opentina-org/optee_os) | 全志 A733 上 TEE（OP-TEE）的可信侧实现 |
| [u-boot](https://github.com/opentina-org/u-boot) | 面向全志 A733 平台定制的 U-Boot —— SPL、Fastboot、启动流程 |
| [linux](https://github.com/opentina-org/linux) | 包含全志 A733 嵌入式设备树的 Linux 内核源码树 —— **Linux 6.18 LTS** 分支 |
| [awbin](https://github.com/opentina-org/awbin) | 全志 A733 相关的二进制 blob 与固件 |
| [xfel](https://github.com/opentina-org/xfel) | 全志 SoC 的轻量 FEL 工具 —— 通过 USB FEL 模式通信 |

### 构建系统与操作系统发行版

| 仓库 | 说明 |
| :--- | :--- |
| [buildroot](https://github.com/opentina-org/buildroot) | 为全志 A733 预配置的 Buildroot 源码树 —— 极简、快速启动的根文件系统 |
| [openwrt](https://github.com/opentina-org/openwrt) | 全志 A733 的 OpenWrt 目标定义与网络协议栈 —— 路由器 / 网关方案 |
| [meta-opentina](https://github.com/opentina-org/meta-opentina) | Yocto Project BSP 层 —— 工业级 / 企业级 Linux |
| [debian](https://github.com/opentina-org/debian) | Debian 根文件系统创建脚本与镜像构建器 |
| [ubuntu](https://github.com/opentina-org/ubuntu) | Ubuntu 根文件系统生成脚本与板级支持 |

### 其他资源

| 资源 | 说明 |
| :--- | :--- |
| [docs](https://github.com/opentina-org/docs) | 深入的指南与技术文档 |
| [opentina](https://github.com/opentina-org/opentina) | 社区元仓库 —— 项目的 [issue 跟踪](https://github.com/opentina-org/opentina/issues) |
| [.github](https://github.com/opentina-org/.github) | 组织主页与社区健康文件 |

## 快速上手

克隆顶层编排仓库：

```bash
git clone https://github.com/opentina-org/build.git
cd build
```

**1. 初始化并拉取源码树** —— 通过默认 manifest 下载所有需要的仓库：

```bash
./build.sh init
```

**2. 查看支持的目标开发板与根文件系统类型：**

```bash
./build.sh targets
```

**3. 触发镜像构建** —— 将 `<BOARD_NAME>` 替换为上一步列出的开发板：

```bash
./build.sh <BOARD_NAME> build
```

详细的使用说明、构建选项与高级配置，请参阅 [build 仓库 README](https://github.com/opentina-org/build/blob/tina-dev/README.md)。

## 获取帮助

使用过程中遇到任何问题，欢迎[提交 issue](https://github.com/opentina-org/opentina/issues)。缺陷报告、问题和 Pull Request 均受欢迎。
