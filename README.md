# 🐉 LonghunFont · 龍魂中文字体

**DNA追溯码**: `#龍芯⚡️2026-06-22-LONGHUN-FONT-v0004`  
**归属**: 龍魂系统 × UID9622 原创  
**定位**: CNSH 中文原生字体 · 自主可控 · 办公/PDF 中英文混排  
**许可证**: SIL Open Font License 1.1

---

## 🌐 仓库地址

| 角色 | 平台 | 地址 |
|---|---|---|
| 主仓（中国） | Gitee | https://gitee.com/uid9622_admin/LonghunFont |
| 镜像（国际） | GitHub | https://github.com/UID9622/LonghunFont |

> 主仓在国内 Gitee，镜像在国外 GitHub。双仓同步，世界可见。

---

## 📊 当前状态

| 指标 | 数值 |
|---|---|
| 字元库版本 | `v0004-办公版` |
| 总字符数 | **1199** 个 |
| 汉字 | **1085** 个 |
| 拉丁字母 / 数字 / 符号 | **114** 个 |
| 字体文件 | `output/LonghunFont-Regular.otf`（OpenType/CFF，93 KB） |
| 字元库文件 | `glyphs/龍魂字元库_v0004_办公版.json` |
| SVG 样张 | `output/sample_v0004.html` |
| 许可证 | `LICENSE`（SIL OFL 1.1） |

---

## 📁 目录结构

```
longhun-font/
├── glyphs/               # 字元库
│   ├── 龍魂字元库_v0001.json         # 初始 6 字
│   ├── 龍魂字元库_v0002_扩展.json    # 196 字
│   ├── 龍魂字元库_v0003_千字符.json  # 1085 字
│   └── 龍魂字元库_v0004_办公版.json  # 1199 字（含拉丁/符号）✅
├── output/               # 输出目录
│   ├── LonghunFont-Regular.otf       # OTF 字体文件
│   ├── sample_v0004.html             # 在线样张
│   └── all_glyphs_v0004/             # 1199 个 SVG
├── scripts/              # 构建脚本
│   ├── build_font.py                 # OTF 导出（含字面外框/安全框）
│   ├── batch_render.py               # 批量 SVG 渲染
│   ├── expand_to_1000.py             # 千字符扩展
│   ├── expand_latin_symbols.py       # 拉丁/符号扩展
│   ├── glyph_generator.py            # 骨架生成器
│   └── refine_core_glyphs.py         # 核心字形精修
├── editor.py             # LonghunFont 编辑器 CLI
├── docs/                 # 战略文档
├── LICENSE               # SIL OFL 1.1
└── README.md             # 本文件
```

---

## 🚀 快速开始

### 1. 构建 OTF 字体
```bash
python3 scripts/build_font.py \
    glyphs/龍魂字元库_v0004_办公版.json \
    output/LonghunFont-Regular.otf
```

### 2. 批量渲染 SVG 样张
```bash
python3 scripts/batch_render.py
# 输出：output/all_glyphs_v0004/ 与 output/sample_v0004.html
```

### 3. 扩展拉丁/符号
```bash
python3 scripts/expand_latin_symbols.py
# 输入：glyphs/龍魂字元库_v0003_千字符.json
# 输出：glyphs/龍魂字元库_v0004_办公版.json
```

---

## 🛡️ 字体主权原则

1. **自主可控**: 不依赖商业字体，全部字形由 CNSH 算法生成或手工精修。
2. **文化主权**: 繁体「龍」字永存，中文命名优先，UTF-8 全链路。
3. **DNA 追溯**: 每个文件头部嵌入 `#龍芯⚡️` 追溯码。
4. **开源保护**: SIL OFL 1.1，防止字体版权被资本收割。
5. **办公就绪**: 支持中英文混排、PDF 嵌入、Office 排版。

---

## 📌 已完成功能

- [x] 1085 个汉字 + 114 个拉丁/数字/符号
- [x] OTF 导出，含真实字面外框与安全框
- [x] CNSH 编辑器接入（Web + Tkinter）
- [x] GitHub 开源：https://github.com/UID9622/LonghunFont
- [x] SIL Open Font License 1.1

---

**DNA追溯**: `#龍芯⚡️2026-06-22-LONGHUN-FONT-v0004`
