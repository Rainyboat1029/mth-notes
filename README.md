# MTH-Notes

MTH026 微积分 / MTH028 线性代数的个人笔记站，MkDocs Material 构建，可直接挂 GitHub Pages。

## 结构

```
mkdocs.yml              站点配置（导航、主题、MathJax 替代方案 KaTeX）
tools/sync_content.py    从 CollegeFiles 同步讲义到 docs/（不改正文，只改名+加导航按钮）
docs/                   站点内容
  index.md              首页
  mth026/ mth028/       课程页、讲义、复习、练习题与解析
  cards/                四份答题卡（自包含 HTML，含 KaTeX）
  javascripts/katex/    本地 KaTeX 0.16.9（离线可用）
  stylesheets/extra.css 主题样式
```

## 本地预览

```bash
python -m pip install -r requirements.txt
python tools/sync_content.py
mkdocs serve        # http://127.0.0.1:8000
```

## 发布

```bash
mkdocs build        # 产物在 site/
```
把仓库推到 GitHub，在 Actions 里用 `mkdocs gh-deploy --force` 推到 gh-pages 分支即可。

## 收录范围

只收自己整理的讲义笔记、期中复习、自编练习卷与解析、答题卡。
不含课程作业、作业解答、课程原始 PDF（版权原因）。
