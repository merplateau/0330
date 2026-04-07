# 《新大学法语》教材讲解项目

`prompt/` 下的是提示词。其中 `prompt_all.md` 是完整提示词，`prompt.json` 是提示词初稿；

`newlayout/` 下的是初版 $\TeX$ 模板，使用 `XeLaTeX` 编译。其目前处于归档状态，供设计参考，不要改动；

`newlayout-lua/` 下的是现役的 $\TeX$ 模板，使用 `LuaLaTeX` 编译。其目前处于活跃状态，用法：

（在 newlayout/ 路径下）：

1. 将 `whichJson.tex` 中的路径改为待渲染的 .json 文件路径；
1. `lualatex main.tex`；
1. `mv main.pdf ../output/b2u1a.pdf` 或手动操作。

