# MTH-Notes

**在线访问：<https://rainyboat1029.github.io/mth-notes/>**

MTH026 微积分 / MTH028 线性代数的个人笔记站，MkDocs Material 构建，挂 GitHub Pages 发布。

## 结构

```
mkdocs.yml               站点配置（导航、主题、pymdownx.arithmatex + KaTeX）
tools/sync_content.py     从 CollegeFiles 同步讲义到 docs/（不改正文，只改名 + 给答题卡加悬浮按钮）
docs/                    站点内容
  index.md               首页
  mth026/ mth028/        课程页、讲义、期中复习、练习题与解析
  cards/                 四份答题卡（自包含 HTML，内联 KaTeX 字体）
  javascripts/katex/     本地 KaTeX 0.16.9（离线可用，596 KB）
  stylesheets/extra.css  主题样式
```

## 更新流程

笔记源文件在 `C:\Users\81578\Documents\CollegeFiles`，站点内容是从那里拷过来的。

```bash
python tools/sync_content.py    # 从 CollegeFiles 同步到 docs/
python -m mkdocs gh-deploy      # 构建并推送到 gh-pages，1 分钟左右上线
```

新增一节课要改三处：`tools/sync_content.py` 的 `NOTES` 列表、`mkdocs.yml` 的 `nav`、`docs/mth02X/index.md` 的卡片列表。

> **注意**：`docs/` 下由 sync 生成的文件是覆盖式写入，手改会在下次同步时丢失。要改内容改 `CollegeFiles` 里的源文件。

## 本地预览

```bash
python -m pip install -r requirements.txt
python tools/sync_content.py
python -m mkdocs serve         # http://127.0.0.1:8000
```

## 发布

- 仓库：<https://github.com/Rainyboat1029/mth-notes>（public）
- `main` = 源码，`gh-pages` = 构建产物，Pages 源指向 `gh-pages` 分支根目录
- `site_url` 已写在 `mkdocs.yml`，子路径 `/mth-notes/` 下的资源与链接已校验
- Pages 软限制：站点 1 GB、月流量 100 GB、每小时 10 次构建，按当前体量（首访约 200 KB）不构成约束

## 收录范围

只收自己整理的讲义笔记、期中复习、自编练习卷与解析、答题卡。
不含课程作业、作业解答、课程原始 PDF（版权原因）。
