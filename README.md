# 🐉 LonghunFont · 龍魂中文字体

**DNA追溯码**: `#龍芯⚡️2026-06-22-LONGHUN-FONT-v0013`  
**归属**: 龍魂系统 × UID9622 原创  
**定位**: CNSH 中文原生字体 · 文化主权 · 稳定全场景  
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
| 字元库版本 | `v0013-稳定版` |
| 总字符数 | **3592** 个 |
| 汉字 | **2731** 个 |
| 拉丁/数字/符号 | **114** 个 |
| 易经八卦 | **75** 个（64 卦 + 8 卦 + 太极 + 两仪） |
| 五行/河图/洛书/太极八卦 | **8** 个 PUA |
| 甲骨文 | **150** 个 PUA |
| 中国风文化图标 | **29** 个 PUA |
| 二十四节气图标 | **24** 个 PUA |
| 十二生肖图标 | **12** 个 PUA |
| 天干地支 | **22** 个 PUA |
| 二十八宿 | **28** 个 PUA |
| 传统节日 | **15** 个 PUA |
| 苏州码子 | **10** 个 PUA |
| 传统纹样 | **15** 个 PUA |
| 文化主权图标 | **20** 个 PUA |
| 实用符号（标点/数学/箭头/制表符/货币/几何） | **151** 个 |
| 国际符号（拼音调号/希腊字母/天气/音乐/象棋/扑克/星座/上下标等） | **188** 个 |
| 字体文件 | `output/LonghunFont-Regular.otf`（OpenType/CFF，357 KB） |
| 字元库文件 | `glyphs/龍魂字元库_v0013_稳定版.json` |
| SVG 样张 | `output/sample_v0013.html` |
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
│   ├── 龍魂字元库_v0008_文化版.json  # 1366 字
│   ├── 龍魂字元库_v0009_农历版.json  # 1447 字
│   ├── 龍魂字元库_v0010_主权完整版.json  # 1607 字
│   ├── 龍魂字元库_v0011_两千中文字.json  # 2657 字
│   ├── 龍魂字元库_v0011_实用符号版.json  # 2808 字
│   ├── 龍魂字元库_v0012_国际符号版.json  # 2996 字
│   └── 龍魂字元库_v0013_稳定版.json  # 3592 字 ✅
├── output/               # 输出目录
│   ├── LonghunFont-Regular.otf       # OTF 字体文件
│   ├── sample_v0013.html             # 在线样张
│   ├── demo.html                     # Web 演示页
│   └── all_glyphs_v0013/             # 3592 个 SVG
├── css/                  # Web 字体 CSS
│   └── LonghunFont.css               # @font-face 与辅助类
├── scripts/              # 构建脚本
│   ├── build_font.py                 # OTF 导出（含字面外框/安全框）
│   ├── batch_render.py               # 批量 SVG 渲染
│   ├── expand_to_1000.py             # 千字符扩展
│   ├── expand_latin_symbols.py       # 拉丁/符号扩展
│   ├── expand_yijing_symbols.py      # 易经八卦扩展
│   ├── expand_wuxing_hetu_luoshu.py  # 五行/河图/洛书扩展
│   ├── expand_oracle_bone.py         # 甲骨文扩展
│   ├── expand_chinese_culture.py     # 中国风文化图标扩展
│   ├── expand_lunar_sovereignty.py   # 甲骨文/节气/生肖扩展
│   ├── expand_tiangan_dizhi.py       # 天干地支扩展
│   ├── expand_ershiba_xiu.py         # 二十八宿扩展
│   ├── expand_chuan_tong_jieri.py    # 传统节日扩展
│   ├── expand_suzhou_motifs.py       # 苏州码子/传统纹样扩展
│   ├── expand_extra_sovereignty.py   # 北斗/四象/福禄寿喜财/文房/乐器扩展
│   ├── expand_chinese_2000.py        # 中文字符扩至 2000+
│   ├── expand_practical_symbols.py   # 标点/数学/箭头/制表符/货币扩展
│   ├── expand_international_symbols.py # 拼音调号/希腊字母/天气/音乐/象棋/扑克/星座/上下标
│   ├── expand_chinese_2600.py        # 中文字符扩至 2600+
│   ├── glyph_generator.py            # 骨架生成器
│   ├── refine_core_glyphs.py         # 核心字形精修
│   ├── check_font.py                 # 字元库校验/审计脚本
│   └── release.sh                    # 一键构建/标签/双仓发布脚本
├── docs/                 # 文档
│   ├── 字体主权战略.md                # 战略文档
│   └── PUA编码表.md                   # PUA 编码对照
├── editor.py             # LonghunFont 编辑器 CLI
├── push_both.sh          # 双仓同步脚本
├── install_macos.sh      # macOS 字体安装脚本
├── CHANGELOG.md          # 版本变更日志
├── LICENSE               # SIL OFL 1.1
├── 操作清单.md            # 傻瓜式操作清单
└── README.md             # 本文件
```

---

## 🚀 快速开始

### 1. 构建 OTF 字体
```bash
python3 scripts/build_font.py \
    glyphs/龍魂字元库_v0013_稳定版.json \
    output/LonghunFont-Regular.otf
```

### 2. 批量渲染 SVG 样张
```bash
python3 scripts/batch_render.py glyphs/龍魂字元库_v0013_稳定版.json output/all_glyphs_v0013
# 输出：output/all_glyphs_v0013/ 与 output/sample_v0013.html
```

### 3. 字元库校验
```bash
python3 scripts/check_font.py glyphs/龍魂字元库_v0013_稳定版.json
```

### 4. 一键发布（校验 + 构建 + 渲染 + 提交 + 标签 + 双仓推送）
```bash
./scripts/release.sh v0013
```

### 5. macOS 安装字体
```bash
./install_macos.sh
```

### 6. Web 演示
用浏览器打开 `output/demo.html`，或把 `css/LonghunFont.css` 引入你的网页：
```html
<link rel="stylesheet" href="css/LonghunFont.css">
<div class="longhun-font">龍魂字体演示</div>
```

### 7. 双仓同步
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

- [x] 2731 个汉字 + 114 个拉丁/数字/符号
- [x] 151 个实用符号（标点/数学/箭头/制表符/货币/几何）
- [x] 188 个国际符号（拼音调号/希腊字母/天气/音乐/象棋/扑克/星座/上下标等）
- [x] 75 个易经/八卦/太极/两仪符号
- [x] 8 个五行/河图/洛书/太极八卦 PUA 图标
- [x] 150 个甲骨文字符（四季、时序、天象、祭祀、权力、农牧工商、器物等）
- [x] 29 个中国风文化图标（龙纹、凤纹、祥云、灯笼、红包、饺子等）
- [x] 24 个二十四节气 PUA 图标
- [x] 12 个十二生肖 PUA 图标
- [x] 22 个天干地支 PUA 图标
- [x] 28 个二十八宿 PUA 图标
- [x] 15 个传统节日 PUA 图标
- [x] 10 个苏州码子 PUA 符号
- [x] 15 个传统纹样 PUA 图标
- [x] 20 个文化主权图标（北斗/四象/福禄寿喜财/文房/乐器/麒麟）
- [x] OTF 导出，含真实字面外框与安全框
- [x] 字元库校验脚本（完整性/唯一性/编码一致性/分类统计）
- [x] 一键发布脚本（校验 → 构建 → 渲染 → 提交 → 标签 → 双仓推送）
- [x] CHANGELOG 版本变更日志
- [x] macOS 安装脚本
- [x] Web 字体 CSS + 演示页
- [x] CNSH 编辑器接入（Web + Tkinter）
- [x] Gitee 主仓 + GitHub 镜像双同步
- [x] SIL Open Font License 1.1

---

**DNA追溯**: `#龍芯⚡️2026-06-22-LONGHUN-FONT-v0013`
