# 龍魂·六层来源链 / LongHun Six-Layer Source Chain
# DNA追溯码:#龍芯⚡️2026-06-22-LONGHUN-FONT-MAKEFILE-v1.0

GLYPHS = glyphs/龍魂字元库_v0014_龍纹版.json
OTF = output/LonghunFont-Regular.otf
SVG_DIR = output/all_glyphs_v0014
SAMPLE = output/sample_v0014.html

.PHONY: all build render check release install demo clean

all: build render check

build:
	python3 scripts/build_font.py $(GLYPHS) $(OTF)

render:
	python3 scripts/batch_render.py $(GLYPHS) $(SVG_DIR) $(SAMPLE)

check:
	python3 scripts/check_font.py $(GLYPHS)

release:
	./scripts/release.sh

install:
	./install_macos.sh

demo:
	@echo "用浏览器打开 output/demo.html"

clean:
	rm -rf output/all_glyphs_v0013
	rm -f output/sample_v0013.html
	rm -f $(OTF)
