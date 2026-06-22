# 🐉 LonghunFont · 龍魂中文字体

**DNA追溯码**: `#龍芯⚡️2026-06-22-LONGHUN-FONT-v0003`  
**归属**: 龍魂系统 × UID9622 原创  
**定位**: CNSH 中文原生字体 · 自主可控 · 中国制造字体主权

---

## 📊 当前状态

| 指标 | 数值 |
|---|---|
| 字元库版本 | `v0003-千字符` |
| 汉字总数 | **1085** 个（已达成 1000+ 目标） |
| 字体文件 | `output/LonghunFont-Regular.otf`（OpenType/CFF，83 KB） |
| 字元库文件 | `glyphs/龍魂字元库_v0003_千字符.json` |
| SVG 样张 | `output/sample_v0003.html` |
| SVG 全集 | `output/all_glyphs_v0003/`（1085 个 SVG） |

---

## 📁 目录结构

```
LonghunFont/
├── glyphs/               # 字元库
│   ├── 龍魂字元库_v0001.json         # 初始 6 字
│   ├── 龍魂字元库_v0002_扩展.json    # 196 字
│   └── 龍魂字元库_v0003_千字符.json  # 1085 字 ✅
├── output/               # 输出目录
│   ├── LonghunFont-Regular.otf       # OTF 字体文件
│   ├── sample_v0003.html             # 在线样张
│   └── all_glyphs_v0003/             # 全部 SVG
├── scripts/              # 构建脚本
│   ├── build_font.py                 # OTF 导出
│   ├── batch_render.py               # 批量 SVG 渲染
│   ├── expand_to_1000.py             # 千字符扩展
│   ├── glyph_generator.py            # 骨架生成器
│   └── refine_core_glyphs.py         # 核心字形精修
├── editor.py             # LonghunFont 编辑器 CLI
├── docs/                 # 战略文档
├── LICENSE               # 龍魂君子协议
└── README.md             # 本文件
```

---

## 🚀 快速开始

### 1. 构建 OTF 字体
```bash
python3 scripts/build_font.py \
    glyphs/龍魂字元库_v0003_千字符.json \
    output/LonghunFont-Regular.otf
```

### 2. 批量渲染 SVG 样张
```bash
python3 scripts/batch_render.py
# 输出：output/all_glyphs_v0003/ 与 output/sample_v0003.html
```

### 3. 扩展字元库
```bash
python3 scripts/expand_to_1000.py
# 输入：glyphs/龍魂字元库_v0002_扩展.json
# 输出：glyphs/龍魂字元库_v0003_千字符.json
```

### 4. 精修核心字形
```bash
python3 scripts/refine_core_glyphs.py
# 覆盖：龍 魂 中 华 国 芯 制 造
```

---

## 🛡️ 字体主权原则

1. **自主可控**: 不依赖任何商业字体库，全部字形由 CNSH 算法生成或手工精修。
2. **文化主权**: 繁体「龍」字永存，中文命名优先，UTF-8 全链路。
3. **DNA 追溯**: 每个文件头部嵌入 `#龍芯⚡️` 追溯码，来源可查、去向可追。
4. **三色审计**: 渲染与构建前自动执行 🟢🟡🔴 审计。
5. **开源保护**: 遵循龍魂君子协议，防止字体版权被资本高价收割。

---

## 📌 已完成功能

- [x] 人工精修核心字形（龍 / 魂 / 中 / 华 / 国 / 芯 / 制 / 造）
- [x] TTF/OTF 导出（fontTools + CFF）
- [x] CNSH 编辑器接入（Web 版 + Tkinter 版）
- [x] GitHub 开源注册（https://github.com/UID9622/LonghunFont，本地已提交，push 待网络恢复）
- [x] 扩展字元库到 1000+ 字（当前 1085 字）

---

## 🔮 下一步

- [ ] 网络恢复后推送 GitHub
- [ ] 注册 Gitee 镜像
- [ ] 加入曲线轮廓精修，提升视觉质量
- [ ] 扩展至 3500 常用字
- [ ] 发布首个 Release 包

---

**DNA追溯**: `#龍芯⚡️2026-06-22-LONGHUN-FONT-v0003`
