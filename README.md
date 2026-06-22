# 🐉 LonghunFont · 龍魂中文字体

**DNA追溯码**: `#龍芯⚡️2026-06-22-LONGHUN-FONT-v0008`  
**归属**: 龍魂系统 × UID9622 原创  
**定位**: CNSH 中文原生字体 · 文化主权 · 办公/PDF 中英文混排  
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
| 字元库版本 | `v0008-文化版` |
| 总字符数 | **1366** 个 |
| 汉字 | **1085** 个 |
| 拉丁/数字/符号 | **114** 个 |
| 易经八卦 | **75** 个（64 卦 + 8 卦 + 太极 + 两仪） |
| 五行/河图/洛书/太极八卦 | **8** 个 PUA |
| 甲骨文 | **55** 个 PUA |
| 中国风文化图标 | **29** 个 PUA |
| 字体文件 | `output/LonghunFont-Regular.otf`（OpenType/CFF，123 KB） |
| 字元库文件 | `glyphs/龍魂字元库_v0008_文化版.json` |
| SVG 样张 | `output/sample_v0008.html` |
| PUA 编码表 | `docs/PUA编码表.md` |
| 许可证 | `LICENSE`（SIL OFL 1.1） |

---

## 📁 目录结构

```
longhun-font/
├── glyphs/               # 字元库
│   ├── 龍魂字元库_v0001.json         # 初始 6 字
│   ├── 龍魂字元库_v0002_扩展.json    # 196 字
│   ├── 龍魂字元库_v0003_千字符.json  # 1085 字
│   ├── 龍魂字元库_v0004_办公版.json  # 1199 字
│   ├── 龍魂字元库_v0005_易经版.json  # 1274 字
│   ├── 龍魂字元库_v0006_五行版.json  # 1282 字
│   ├── 龍魂字元库_v0007_甲骨文版.json # 1337 字
│   └── 龍魂字元库_v0008_文化版.json  # 1366 字 ✅
├── output/               # 输出目录
│   ├── LonghunFont-Regular.otf       # OTF 字体文件
│   ├── sample_v0008.html             # 在线样张
│   └── all_glyphs_v0008/             # 1366 个 SVG
├── scripts/              # 构建脚本
│   ├── build_font.py                 # OTF 导出（含字面外框/安全框）
│   ├── batch_render.py               # 批量 SVG 渲染
│   ├── expand_to_1000.py             # 千字符扩展
│   ├── expand_latin_symbols.py       # 拉丁/符号扩展
│   ├── expand_yijing_symbols.py      # 易经八卦扩展
│   ├── expand_wuxing_hetu_luoshu.py  # 五行/河图/洛书扩展
│   ├── expand_oracle_bone.py         # 甲骨文扩展
│   ├── expand_chinese_culture.py     # 中国风文化图标扩展
│   ├── glyph_generator.py            # 骨架生成器
│   └── refine_core_glyphs.py         # 核心字形精修
├── docs/                 # 文档
│   ├── 字体主权战略.md                # 战略文档
│   └── PUA编码表.md                   # PUA 编码对照
├── editor.py             # LonghunFont 编辑器 CLI
├── push_both.sh          # 双仓同步脚本
├── LICENSE               # SIL OFL 1.1
├── 操作清单.md            # 傻瓜式操作清单
└── README.md             # 本文件
```

---

## 🚀 快速开始

### 1. 构建 OTF 字体
```bash
python3 scripts/build_font.py \
    glyphs/龍魂字元库_v0008_文化版.json \
    output/LonghunFont-Regular.otf
```

### 2. 批量渲染 SVG 样张
```bash
python3 scripts/batch_render.py
# 输出：output/all_glyphs_v0008/ 与 output/sample_v0008.html
```

### 3. 双仓同步
```bash
./push_both.sh
```

---

## 🛡️ 字体主权原则

1. **自主可控**: 不依赖商业字体，全部字形由 CNSH 算法生成或手工精修。
2. **文化主权**: 繁体「龍」字永存，中文命名优先，UTF-8 全链路。
3. **易经五行**: 64 卦、八卦、太极、五行、河图、洛书、甲骨文全部纳入。
4. **DNA 追溯**: 每个文件头部嵌入 `#龍芯⚡️` 追溯码。
5. **开源保护**: SIL OFL 1.1，防止字体版权被资本收割。
6. **办公就绪**: 支持中英文混排、PDF 嵌入、Office 排版。

---

## 📌 已完成功能

- [x] 1085 个汉字 + 114 个拉丁/数字/符号
- [x] 75 个易经/八卦/太极/两仪符号
- [x] 8 个五行/河图/洛书/太极八卦 PUA 图标
- [x] 55 个甲骨文字符
- [x] 29 个中国风文化图标（龙纹、凤纹、祥云、灯笼、红包、饺子等）
- [x] OTF 导出，含真实字面外框与安全框
- [x] CNSH 编辑器接入（Web + Tkinter）
- [x] Gitee 主仓 + GitHub 镜像双同步
- [x] SIL Open Font License 1.1

---

**DNA追溯**: `#龍芯⚡️2026-06-22-LONGHUN-FONT-v0008`
