# 🐉 LonghunFont 编辑器 v1.0

**DNA追溯码**: `#龍芯⚡️2026-06-22-LONGHUN-FONT-EDITOR-v1.0`  
**归属**: 龍魂系统 × UID9622 原创  
**定位**: CNSH 中文原生字体 · 字元编辑工作区

---

## 📁 目录结构

```
longhun-font/
├── engines/              # CNSH 字体引擎
│   ├── cnsh_font_engine_uid9622.py   # 基础三次贝塞尔渲染引擎
│   └── cnsh_font_engine.py           # CNSH 字体系统（含风格、DNA）
├── glyphs/               # 字元库
│   └── 龍魂字元库_v0001.json         # 初始字元库（龍/魂/中/华/民/芯）
├── output/               # SVG 输出目录
├── assets/               # 字体资源（图片、参考）
├── docs/                 # 文档
├── editor.py             # LonghunFont 编辑器 CLI
└── README.md             # 本文件
```

---

## 🚀 快速开始

### 1. 统计字元
```bash
python3 editor.py stats
```

### 2. 关键字搜索
```bash
# 按字元搜索
python3 editor.py search --keyword 龍

# 按 Unicode 前缀搜索
python3 editor.py search --unicode U+9F

# 按结构搜索
python3 editor.py search --structure 左右
```

### 3. 渲染字元/文本
```bash
# 渲染单字
python3 editor.py render 龍

# 渲染文本（每个字独立 SVG）
python3 editor.py render "中华龍魂"
```

### 4. 查看字元笔画
```bash
python3 editor.py list 龍
```

### 5. 编辑笔画

添加笔画：
```bash
python3 editor.py add-stroke 龍 移动到 '[100,100]'
python3 editor.py add-stroke 龍 直线段 '[500,100]'
python3 editor.py add-stroke 龍 三次曲线 '[[400,200],[400,400],[300,500]]'
```

更新笔画：
```bash
python3 editor.py update-stroke 龍 0 移动到 '[120,120]'
```

删除笔画：
```bash
python3 editor.py delete-stroke 龍 5
```

### 6. 保存与审计
```bash
python3 editor.py audit
python3 editor.py save
```

---

## 🎨 字元库格式

每个字元包含：
- `unicode`: Unicode 编码
- `笔画数`: 笔画计数
- `结构`: 单一 / 左右 / 上下 / 包围 等
- `笔画路径_cnsh9622`: 笔画路径数组

笔画类型：
- `移动到`: `{"坐标": [x, y]}`
- `直线段`: `{"终点": [x, y]}`
- `三次曲线`: `{"控制点": [[P1x,P1y], [P2x,P2y], [P3x,P3y]]}`

---

## 🛡️ 设计原则

1. **文化主权**: 全部使用 UTF-8，中文命名
2. **DNA 追溯**: 每个文件头部嵌入 `#龍芯⚡️` 追溯码
3. **三色审计**: 渲染前自动执行 🟢🟡🔴 审计
4. **开源保护**: 遵循龍魂君子协议，避免字体版权被高价收割

---

## 📌 下一步

- [ ] 用 editor.py 编辑 `龍` 字笔画，生成正式 LonghunFont 第一个字
- [ ] 扩展字元库到 100/1000/10000 字
- [ ] 接入 CNSH 编辑器作为显示字体
- [ ] 导出 TTF/OTF 字体文件

---

**DNA追溯**: `#龍芯⚡️2026-06-22-LONGHUN-FONT-EDITOR-v1.0`
