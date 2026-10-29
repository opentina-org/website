---
title: 簡介
description: OpenTina 是什麼，以及專案如何組織。
---

OpenTina 是一個開源社群，致力於為**全志（Allwinner）A733** 晶片平台提供底層系統軟體與多作業系統發行版支援。

專案旨在為基於全志 A733 的硬體打造穩健、生產等級的軟體生態：及時維護的板級支援、主線核心整合，以及涵蓋嵌入式 Linux、路由平台與主流桌面發行版的系統建置管線。

## 倉庫地圖

所有開發都在 GitHub 的 [opentina-org](https://github.com/opentina-org) 組織下進行。

### 底層與核心 BSP

| 倉庫 | 說明 |
| :--- | :--- |
| [build](https://github.com/opentina-org/build) | 頂層編排工具、建置腳本與設定 —— 一鍵建置入口 |
| [trusted-firmware-a](https://github.com/opentina-org/trusted-firmware-a) | 全志 A733 的 ARM 可信固體（ATF）移植 —— PSCI / 安全世界 |
| [optee_os](https://github.com/opentina-org/optee_os) | 全志 A733 上 TEE（OP-TEE）的可信側實作 |
| [u-boot](https://github.com/opentina-org/u-boot) | 面向全志 A733 平台客製的 U-Boot —— SPL、Fastboot、開機流程 |
| [linux](https://github.com/opentina-org/linux) | 包含全志 A733 嵌入式裝置樹的 Linux 核心原始碼樹 —— **Linux 6.18 LTS** 分支 |
| [awbin](https://github.com/opentina-org/awbin) | 全志 A733 相關的二進位 blob 與韌體 |
| [xfel](https://github.com/opentina-org/xfel) | 全志 SoC 的輕量 FEL 工具 —— 透過 USB FEL 模式通訊 |

### 建置系統與作業系統發行版

| 倉庫 | 說明 |
| :--- | :--- |
| [buildroot](https://github.com/opentina-org/buildroot) | 為全志 A733 預先配置的 Buildroot 原始碼樹 —— 極簡、快速開機的根檔案系統 |
| [openwrt](https://github.com/opentina-org/openwrt) | 全志 A733 的 OpenWrt 目標定義與網路協定堆疊 —— 路由器 / 閘道器方案 |
| [meta-opentina](https://github.com/opentina-org/meta-opentina) | Yocto Project BSP 層 —— 工業級 / 企業級 Linux |
| [debian](https://github.com/opentina-org/debian) | Debian 根檔案系統建立腳本與映像建置器 |
| [ubuntu](https://github.com/opentina-org/ubuntu) | Ubuntu 根檔案系統產生腳本與板級支援 |

### 其他資源

| 資源 | 說明 |
| :--- | :--- |
| [docs](https://github.com/opentina-org/docs) | 深入的指南與技術文件 |
| [opentina](https://github.com/opentina-org/opentina) | 社群元倉庫 —— 專案的 [issue 跟蹤](https://github.com/opentina-org/opentina/issues) |
| [.github](https://github.com/opentina-org/.github) | 組織首頁與社群健全檔案 |

## 快速入門

複製頂層編排倉庫：

```bash
git clone https://github.com/opentina-org/build.git
cd build
```

**1. 初始化並取得原始碼樹** —— 透過預設 manifest 下載所有需要的倉庫：

```bash
./build.sh init
```

**2. 檢視支援的開發板與根檔案系統類型：**

```bash
./build.sh targets
```

**3. 觸發映像建置** —— 將 `<BOARD_NAME>` 替換為上一步列出的開發板：

```bash
./build.sh <BOARD_NAME> build
```

詳細的使用說明、建置選項與進階設定，請參閱 [build 倉庫 README](https://github.com/opentina-org/build/blob/tina-dev/README.md)。

## 取得協助

使用過程中遇到任何問題，歡迎[提交 issue](https://github.com/opentina-org/opentina/issues)。錯誤報告、問題與 Pull Request 均受到歡迎。
