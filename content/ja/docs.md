---
title: はじめに
description: OpenTina とは何か、そしてプロジェクトの構成について。
---

OpenTina は、**オールウィナー（Allwinner）A733** チッププラットフォーム向けの低レベル・システムソフトウェアとマルチ OS ディストリビューション対応を提供するオープンソースコミュニティです。

このプロジェクトは、オールウィナー A733 ベースのハードウェアのために堅牢で本番品質のソフトウェアエコシステムを構築します：最新のボードサポート、メインラインカーネルの統合、組み込み Linux・ルータープラットフォーム・主要デスクトップディストリビューションにわたるシステムビルドパイプラインです。

## リポジトリマップ

すべての開発は GitHub の [opentina-org](https://github.com/opentina-org) 組織で行われています。

### 低レベル・コア BSP

| リポジトリ | 説明 |
| :--- | :--- |
| [build](https://github.com/opentina-org/build) | トップレベルのオーケストレーションツール、ビルドスクリプト、設定 —— ワンクリックのビルドエントリポイント |
| [trusted-firmware-a](https://github.com/opentina-org/trusted-firmware-a) | オールウィナー A733 向け ARM Trusted Firmware（ATF）ポート —— PSCI / Secure World |
| [optee_os](https://github.com/opentina-org/optee_os) | オールウィナー A733 における TEE（OP-TEE）のトラステッドサイド実装 |
| [u-boot](https://github.com/opentina-org/u-boot) | オールウィナー A733 プラットフォーム向け U-Boot —— SPL、Fastboot、ブートフロー |
| [linux](https://github.com/opentina-org/linux) | オールウィナー A733 の組み込み DTS を含む Linux カーネルツリー —— **Linux 6.18 LTS** ブランチ |
| [awbin](https://github.com/opentina-org/awbin) | オールウィナー A733 関連のバイナリ blob とファームウェア |
| [xfel](https://github.com/opentina-org/xfel) | オールウィナー SoC 向けの小型 FEL ツール —— USB 経由の FEL モード通信 |

### ビルドシステムと OS ディストリビューション

| リポジトリ | 説明 |
| :--- | :--- |
| [buildroot](https://github.com/opentina-org/buildroot) | オールウィナー A733 向けに事前設定された Buildroot —— ミニマルで高速起動の rootfs |
| [openwrt](https://github.com/opentina-org/openwrt) | オールウィナー A733 向け OpenWrt ターゲット定義とネットワークスタック —— ルーター / ゲートウェイソリューション |
| [meta-opentina](https://github.com/opentina-org/meta-opentina) | Yocto Project BSP レイヤー —— エンタープライズ向け Linux |
| [debian](https://github.com/opentina-org/debian) | Debian ルートファイルシステム作成スクリプトとイメージビルダー |
| [ubuntu](https://github.com/opentina-org/ubuntu) | Ubuntu ルートファイルシステム生成スクリプトとボード有効化 |

### その他のリソース

| リソース | 説明 |
| :--- | :--- |
| [docs](https://github.com/opentina-org/docs) | 詳細なガイドと技術ドキュメント |
| [opentina](https://github.com/opentina-org/opentina) | コミュニティメタリポジトリ —— プロジェクトの [issue トラッカー](https://github.com/opentina-org/opentina/issues) |
| [.github](https://github.com/opentina-org/.github) | 組織プロファイルとコミュニティヘルスファイル |

## クイックスタート

トップレベルのオーケストレーションリポジトリをクローンします：

```bash
git clone https://github.com/opentina-org/build.git
cd build
```

**1. 初期化とソースツリーの取得** —— デフォルトマニフェストを使用して必要なすべてのリポジトリをダウンロードします：

```bash
./build.sh init
```

**2. 対応ボードと rootfs タイプの一覧表示：**

```bash
./build.sh targets
```

**3. イメージのビルド** —— `<BOARD_NAME>` を前のステップで表示されたボードに置き換えます：

```bash
./build.sh <BOARD_NAME> build
```

詳細な手順、ビルドオプション、高度な設定については、[build リポジトリの README](https://github.com/opentina-org/build/blob/tina-dev/README.md) を参照してください。

## ヘルプを得る

使用中に問題が発生した場合は、[イシューを開いてください](https://github.com/opentina-org/opentina/issues)。バグレポート、質問、Pull Request を歓迎します。
