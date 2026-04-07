# 《新大学法语》教材讲解项目

`prompt/` 下的是提示词。其中 `prompt_all.md` 是完整提示词，`prompt.json` 是提示词初稿；

`newlayout/` 下的是初版 $\TeX$ 模板，使用 `XeLaTeX` 编译。其目前处于归档状态，供设计参考，不要改动；

`newlayout-lua/` 下的是现役的 $\TeX$ 模板，使用 `LuaLaTeX` 编译。其目前处于活跃状态，并且使用 GitHub Actions 自动渲染 PDF。


# 生产和渲染流程：

1. 在 `output/` 下新建.json，并 add/commit/push；
1. push 后 GitHub 会在云端自动渲染 PDF, 运行时间长短不一，5分钟及以上；
1. 新开一个终端，输出 `gh run whatch` 可以监测进程；

如果不想要通过 GitHub 自动渲染，可以不放在 `output/`，而放在 `output-manual/`，就和老流程一样手动渲染。