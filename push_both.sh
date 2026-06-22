#!/bin/bash
# 龍魂·双仓推送脚本
# DNA追溯码:#龍芯⚡️2026-06-22-LONGHUN-FONT-PUSH-BOTH-v1.0
# 用法：./push_both.sh

set -e

echo "🚀 推送到 Gitee（主仓）..."
git push origin main

echo "🚀 推送到 GitHub（镜像）..."
git push github main

echo "✅ 双仓同步完成"
