#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 CollegeFiles 里的讲义 / 复习 / 练习搬进 docs/。

只做三件事：
1. 复制 markdown 正文（不改内容，只换文件名）；
2. 复制四份答题卡，并在 </body> 前追加一个「查看解析」悬浮按钮；
3. 生成练习页（iframe 嵌入答题卡 + 工具栏）。

用法：python tools/sync_content.py
"""
from pathlib import Path
import sys

SRC = Path(r"C:\Users\81578\iCloudDrive\CollegeFiles")
ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

# ---------- 讲义与练习：源文件 -> 目标路径 ----------
NOTES = [
    # 微积分
    ("MTH026-Calculus/calculus-lecture1-notes-v2.md", "mth026/lecture01.md"),
    ("MTH026-Calculus/calculus-lecture2-notes-v2.md", "mth026/lecture02.md"),
    ("MTH026-Calculus/calculus-lecture3-notes-v2.md", "mth026/lecture03.md"),
    ("MTH026-Calculus/calculus-lecture4-notes.md", "mth026/lecture04.md"),
    ("MTH026-Calculus/calculus-lecture5-notes.md", "mth026/lecture05.md"),
    ("MTH026-Calculus/calculus-lecture6-notes.md", "mth026/lecture06.md"),
    ("MTH026-Calculus/calculus-lecture7-notes.md", "mth026/lecture07.md"),
    ("MTH026-Calculus/calculus-lecture8-notes.md", "mth026/lecture08.md"),
    ("MTH026-Calculus/calculus-lecture9-notes.md", "mth026/lecture09.md"),
    ("MTH026-Calculus/calculus-lecture10-notes.md", "mth026/lecture10.md"),
    ("MTH026-Calculus/calculus-lecture11-notes.md", "mth026/lecture11.md"),
    ("MTH026-Calculus/midterm-review-notes.md", "mth026/midterm-review.md"),
    ("MTH026-Calculus/核心概念解析：从“直观极限”到“严谨定义”的逻辑跨越.md", "mth026/concept-limits.md"),
    ("MTH026-Calculus/mth026-week1-6-practice-questions.md", "mth026/practice-basic-questions.md"),
    ("MTH026-Calculus/mth026-week1-6-practice-solutions.md", "mth026/practice-basic-solutions.md"),
    ("MTH026-Calculus/mth026-week1-6-advanced-questions.md", "mth026/practice-advanced-questions.md"),
    ("MTH026-Calculus/mth026-week1-6-advanced-solutions.md", "mth026/practice-advanced-solutions.md"),
    # 线性代数
    ("MTH028-LinearAlgebra/mth028-lecture1-notes-v2.md", "mth028/lecture01.md"),
    ("MTH028-LinearAlgebra/mth028-lecture2-notes-v2.md", "mth028/lecture02.md"),
    ("MTH028-LinearAlgebra/mth028-lecture3-notes-v2.md", "mth028/lecture03.md"),
    ("MTH028-LinearAlgebra/mth028-lecture4-notes.md", "mth028/lecture04.md"),
    ("MTH028-LinearAlgebra/mth028-lecture5-notes.md", "mth028/lecture05.md"),
    ("MTH028-LinearAlgebra/mth028-lecture6-notes.md", "mth028/lecture06.md"),
    ("MTH028-LinearAlgebra/mth028-lecture7-notes.md", "mth028/lecture07.md"),
    ("MTH028-LinearAlgebra/mth028-lecture8-notes.md", "mth028/lecture08.md"),
    ("MTH028-LinearAlgebra/mth028-lecture9-notes.md", "mth028/lecture09.md"),
    ("MTH028-LinearAlgebra/mth028-lecture10-notes-v2.md", "mth028/lecture10.md"),
    ("MTH028-LinearAlgebra/mth028-lecture11-notes.md", "mth028/lecture11.md"),
    ("MTH028-LinearAlgebra/mth028-midterm-review-notes.md", "mth028/midterm-review.md"),
    ("MTH028-LinearAlgebra/mth028-week1-8-practice-questions.md", "mth028/practice-basic-questions.md"),
    ("MTH028-LinearAlgebra/mth028-week1-8-practice-solutions.md", "mth028/practice-basic-solutions.md"),
    ("MTH028-LinearAlgebra/mth028-week1-8-advanced-questions.md", "mth028/practice-advanced-questions.md"),
    ("MTH028-LinearAlgebra/mth028-week1-8-advanced-solutions.md", "mth028/practice-advanced-solutions.md"),
]

# ---------- 站内没有的目标：把死链降级成纯文本 ----------
# 笔记里的「来源」会指向课件 PDF 和作业解析，这两类不上站，留着只会 404。
# 新增一条就加一行 (原样, 替换成)。
LINK_FIXES = [
    ("[Lecture 10 – Section 3.1](<Lecture 10 - Section 3.1.pdf>)", "Lecture 10 – Section 3.1"),
    ("[Weekly Assignment 9 解析 v2](mth028-assignment9-answer-v2.md)", "Weekly Assignment 9 解析 v2"),
    ("[Lecture 11 with solutions](<Lecture 11 with solutions.pdf>)", "Lecture 11 with solutions"),
    ("[Assignment 11 解析](calculus-assignment11-answer.md)", "Assignment 11 解析"),
    ("[第 11 课课件](<Lecture 11 - Section 3.2.pdf>)", "第 11 课课件"),
    ("[Weekly Assignment 10 解析](mth028-assignment10-answer.md)", "Weekly Assignment 10 解析"),
    # 站内已有的笔记：换成能点的站内链接
    ("[余子式展开](mth028-lecture10-notes-v2.md)", "[余子式展开](../lecture10/)"),
]

# ---------- 答题卡：源文件 -> (目标路径, 解析页相对地址) ----------
CARDS = [
    ("MTH026-Calculus/mth026-week1-6-answer-card.html", "cards/mth026-basic.html", "../mth026/practice-basic-solutions/"),
    ("MTH026-Calculus/mth026-week1-6-advanced-answer-card.html", "cards/mth026-advanced.html", "../mth026/practice-advanced-solutions/"),
    ("MTH028-LinearAlgebra/mth028-week1-8-answer-card.html", "cards/mth028-basic.html", "../mth028/practice-basic-solutions/"),
    ("MTH028-LinearAlgebra/mth028-week1-8-advanced-answer-card.html", "cards/mth028-advanced.html", "../mth028/practice-advanced-solutions/"),
]

# ---------- 练习页 ----------
PRACTICE = [
    dict(course="mth026", slug="practice-basic", title="基础卷 · Week 1–6 答题卡",
         desc="Week 1–6 综合练习：极限、导数与导数应用。作答进度存在浏览器本地，随时可以关掉再回来。",
         card="mth026-basic.html", stem="practice-basic-questions.md", sol="practice-basic-solutions.md"),
    dict(course="mth026", slug="practice-advanced", title="进阶卷 · Week 1–6 综合提高",
         desc="综合提高卷：跨章综合题与更难的变形，适合复习后期限时训练。",
         card="mth026-advanced.html", stem="practice-advanced-questions.md", sol="practice-advanced-solutions.md"),
    dict(course="mth028", slug="practice-basic", title="基础卷 · Week 1–8 答题卡",
         desc="Week 1–8 综合练习：方程组、矩阵运算与可逆性。作答进度存在浏览器本地。",
         card="mth028-basic.html", stem="practice-basic-questions.md", sol="practice-basic-solutions.md"),
    dict(course="mth028", slug="practice-advanced", title="进阶卷 · Week 1–8 综合提高",
         desc="综合提高卷：子空间、维数与秩相关的综合题。",
         card="mth028-advanced.html", stem="practice-advanced-questions.md", sol="practice-advanced-solutions.md"),
]

TOOLBAR_CSS = """
<style id="mthnotes-toolbar">
#mn-sol{position:fixed;left:16px;bottom:16px;z-index:2147483000;
  font:600 13px/1 -apple-system,BlinkMacSystemFont,"Segoe UI","Microsoft YaHei",sans-serif}
#mn-sol a{display:inline-block;padding:10px 14px;border-radius:999px;
  background:rgba(30,34,42,.92);color:#fff;text-decoration:none;
  box-shadow:0 8px 22px rgba(0,0,0,.3);backdrop-filter:blur(6px);transition:background .15s}
#mn-sol a:hover{background:#3b5bdb}
@media print{#mn-sol{display:none}}
</style>
<div id="mn-sol"><a href="__SOL__" target="_parent">查看解析 →</a></div>
"""

PAGE = """# {title}

{desc}

<div class="quiz-bar" markdown="1">

[新标签页打开答题卡](../../cards/{card}){{ .qp-btn target="_blank" }}
[查看解析]({sol}){{ .qp-btn .qp-ghost }}
[打印版题干]({stem}){{ .qp-btn .qp-ghost }}

</div>

<iframe class="quiz-frame" src="../../cards/{card}" title="{title}" loading="eager"></iframe>
"""


def copy_notes() -> int:
    n = 0
    for src, dst in NOTES:
        s = SRC / src
        if not s.is_file():
            sys.exit(f"缺少源文件: {s}")
        d = DOCS / dst
        d.parent.mkdir(parents=True, exist_ok=True)
        text = s.read_text(encoding="utf-8")
        for old, new in LINK_FIXES:
            text = text.replace(old, new)
        if not text.endswith("\n"):
            text += "\n"
        d.write_text(text, encoding="utf-8")
        n += 1
    return n


def copy_cards() -> int:
    n = 0
    for src, dst, sol in CARDS:
        s = SRC / src
        if not s.is_file():
            sys.exit(f"缺少源文件: {s}")
        html = s.read_text(encoding="utf-8")
        inject = TOOLBAR_CSS.replace("__SOL__", sol)
        if "</body>" in html:
            html = html.replace("</body>", inject + "\n</body>", 1)
        else:
            html += inject
        d = DOCS / dst
        d.parent.mkdir(parents=True, exist_ok=True)
        d.write_text(html, encoding="utf-8")
        n += 1
    return n


def write_practice() -> int:
    for p in PRACTICE:
        d = DOCS / p["course"] / (p["slug"] + ".md")
        d.parent.mkdir(parents=True, exist_ok=True)
        d.write_text(PAGE.format(**p), encoding="utf-8")
    return len(PRACTICE)


def main() -> None:
    docs = copy_notes()
    cards = copy_cards()
    pages = write_practice()
    print(f"讲义/练习 {docs} 篇, 答题卡 {cards} 份, 练习页 {pages} 个 -> {DOCS}")


if __name__ == "__main__":
    main()
