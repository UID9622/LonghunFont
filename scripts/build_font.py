#!/usr/bin/env python3
# 龍魂·六层来源链 / LongHun Six-Layer Source Chain
# DNA追溯码:#龍芯⚡️2026-06-22-LONGHUN-FONT-BUILD-v1.0

"""
LonghunFont 字体构建器 v1.0
使用 fontTools 将字元库导出为 OTF 字体文件。
当前为骨架版本，字形由笔画路径加粗生成。
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime

from fontTools.fontBuilder import FontBuilder
from fontTools.pens.t2CharStringPen import T2CharStringPen
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Identity

DNA = "#龍芯⚡️2026-06-22-LONGHUN-FONT-BUILD-v1.0"

# 字框参数
UNITS_PER_EM = 1000
VIEWBOX = 600
STROKE_WIDTH = 24


def stroke_line_to_polygon(p1, p2, width=STROKE_WIDTH):
    """将线段加粗为四边形轮廓 (返回逆时针点列表)"""
    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1
    length = (dx ** 2 + dy ** 2) ** 0.5
    if length < 1e-6:
        return []
    # 单位法向量
    ux = -dy / length
    uy = dx / length
    hw = width / 2
    return [
        (x1 + ux * hw, y1 + uy * hw),
        (x2 + ux * hw, y2 + uy * hw),
        (x2 - ux * hw, y2 - uy * hw),
        (x1 - ux * hw, y1 - uy * hw),
    ]


def path_to_contours(strokes):
    """将笔画路径列表转换为字体轮廓列表"""
    contours = []
    current_point = None

    for stroke in strokes:
        t = stroke["类型"]
        if t == "移动到":
            current_point = tuple(stroke["坐标"])
        elif t == "直线段":
            end = tuple(stroke["终点"])
            if current_point is None:
                continue
            poly = stroke_line_to_polygon(current_point, end)
            if poly:
                contours.append(poly)
            current_point = end
        elif t == "三次曲线":
            # 简化为从 current_point 到 P3 的直线段加粗
            # 真实三次曲线转轮廓较复杂，骨架版用弦近似
            P1, P2, P3 = [tuple(p) for p in stroke["控制点"]]
            if current_point is None:
                continue
            poly = stroke_line_to_polygon(current_point, P3)
            if poly:
                contours.append(poly)
            current_point = P3

    return contours


def scale_contour(contour, scale):
    """缩放到字体单位"""
    return [(x * scale, y * scale) for x, y in contour]


def build_otf(glyph_path: str, output_path: str):
    """构建 OTF 字体"""
    with open(glyph_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    chars = data["字符集_cnsh9622"]
    scale = UNITS_PER_EM / VIEWBOX

    # 字符到字形名称映射
    cmap = {}
    glyph_order = [".notdef"]
    charstrings = {}

    # .notdef 字形：简单方块
    pen = T2CharStringPen(UNITS_PER_EM, None)
    pen.moveTo((100, 100))
    pen.lineTo((900, 100))
    pen.lineTo((900, 900))
    pen.lineTo((100, 900))
    pen.closePath()
    charstrings[".notdef"] = pen.getCharString()

    for char in sorted(chars.keys()):
        glyph_name = f"uni{ord(char):04X}"
        cmap[ord(char)] = glyph_name
        glyph_order.append(glyph_name)

        strokes = chars[char]["笔画路径_cnsh9622"]
        contours = path_to_contours(strokes)

        pen = T2CharStringPen(UNITS_PER_EM, None)
        if not contours:
            # 空字形画一个占位框
            pen.moveTo((100, 100))
            pen.lineTo((900, 100))
            pen.lineTo((900, 900))
            pen.lineTo((100, 900))
            pen.closePath()
        else:
            for contour in contours:
                sc = scale_contour(contour, scale)
                if not sc:
                    continue
                pen.moveTo(sc[0])
                for pt in sc[1:]:
                    pen.lineTo(pt)
                pen.closePath()

        charstrings[glyph_name] = pen.getCharString()

    # 计算每个字形的边界框
    glyph_bboxes = {}
    for name, cs in charstrings.items():
        # 简单 bbox：从 charstring 提取大致范围
        # 这里用字体单位全框作为近似
        glyph_bboxes[name] = (0, 0, UNITS_PER_EM, UNITS_PER_EM)

    fb = FontBuilder(UNITS_PER_EM, isTTF=False)
    fb.setupGlyphOrder(glyph_order)
    fb.setupCFF(
        psName="LonghunFont-Regular",
        fontInfo={
            "version": "1.000",
            "FullName": "LonghunFont Regular",
            "FamilyName": "LonghunFont",
            "Weight": "Regular",
            "isFixedPitch": False,
            "ItalicAngle": 0,
            "UnderlinePosition": -100,
            "UnderlineThickness": 50,
        },
        charStringsDict=charstrings,
        privateDict={"defaultWidthX": 600, "nominalWidthX": 600},
    )
    fb.setupCharacterMap(cmap)
    fb.setupHorizontalMetrics({name: (600, 0) for name in glyph_order})
    fb.setupOS2(
        sTypoAscender=800,
        sTypoDescender=-200,
        sTypoLineGap=200,
        usWinAscent=1000,
        usWinDescent=200,
    )
    fb.setupPost()
    fb.setupNameTable({
        "copyright": "LonghunFont by UID9622 · DNA追溯 #龍芯⚡️",
        "familyName": "LonghunFont",
        "styleName": "Regular",
        "uniqueFontIdentifier": "LonghunFont-Regular-1.000",
        "fullName": "LonghunFont Regular",
        "version": "Version 1.000",
        "psName": "LonghunFont-Regular",
        "manufacturer": "龍魂系统 · UID9622",
    })

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fb.save(output_path)
    print(f"✅ OTF 字体已生成: {output_path}")
    print(f"   包含字形: {len(cmap)} 个")
    return output_path


if __name__ == "__main__":
    base_dir = Path(__file__).parent.parent
    glyph_path = base_dir / "glyphs" / "龍魂字元库_v0002_扩展.json"
    output_path = base_dir / "output" / "LonghunFont-Regular.otf"
    build_otf(str(glyph_path), str(output_path))
