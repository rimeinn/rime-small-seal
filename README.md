# Rime 小篆 / rime-small-seal

℞ rimeinn/rime-small-seal

該倉提供 Unicode 18 小篆碼位與對應現代 CJK 形式的 OpenCC 映射表。所有
數據和代碼均釋入公共域。

This repo hosts the OpenCC definitions for the Small Seal script
introduced in Unicode 18.  All of the data is released into the Public
Domain.

## 使用方法 / Usage

將 `opencc/small_seal.json` 與 `opencc/small_seal.txt` 放入用戶目錄的
`opencc` 目錄，然後給所用方案增加一個 simplifier 引用該數據。

## 數據 / Data

數據從 https://www.unicode.org/Public/UCD/latest/ucd/SealSources.txt
生成。

The table is programmatically generated from
https://www.unicode.org/Public/UCD/latest/ucd/SealSources.txt .

## 開發 / Development

```bash
make
```
