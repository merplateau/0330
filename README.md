# 《新大学法语》教材讲解项目

`prompt/` 下的是提示词。其中 `prompt_all.md` 是完整提示词，`prompt.json` 是提示词初稿；

`newlayout/` 下的是初版 $\TeX$ 模板，使用 `XeLaTeX` 编译。其目前处于归档状态，供设计参考，不要改动；

`newlayout-lua/` 下的是现役的 $\TeX$ 模板，使用 `LuaLaTeX` 编译。其目前处于活跃状态，用法：

本地手工生成 PDF：

1. 在仓库根目录执行：`./scripts/render-json-to-pdf.sh output/b2u1a.json`
1. 脚本会自动生成 `newlayout-lua/whichJson.tex`
1. 脚本会在 `newlayout-lua/` 下运行 `lualatex main.tex`
1. 生成的 PDF 会自动放回 `output/b2u1a.pdf`

如果仍然想手工编译，可以参考 `newlayout-lua/whichJsonExample.tex`。

GitHub Actions 已支持自动处理新 JSON：

1. 当 push 中有新增的 `output/*.json` 文件时，会触发 workflow
1. workflow 会为每个新增 JSON 渲染对应 PDF
1. 生成的 PDF 会提交回同一分支的 `output/` 目录
