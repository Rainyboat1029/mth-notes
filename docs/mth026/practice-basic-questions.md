# MTH026 Calculus I · Week 1–6 练习册 (Practice Workbook)

> **50 题 · 英文题干 · 五选一 · 按 Week 1–6 分节**
> 题目按 `026PracticeQuiz` 中 LM Core 小测与《MTH026 微积分分类复习题集》的题型原创改编（覆盖 Notes 1–6 全部考点）：每题给出中文考点标签和「做题技巧」提示，题干保留英文，选项为 A–E。
> 使用方法：先限时做完整节，再对照《解析册》核对；解析册开头有 50 题答案速查表。

**覆盖范围**

| 周次 | 对应讲义 | 内容 |
|---|---|---|
| Week 1 | Notes 1（§1.5–1.9） | 函数、定义域、复合、反函数、反三角 |
| Week 2 | Notes 2（§2.1, 2.3） | 极限直观、极限定理、0/0 型 |
| Week 3 | Notes 3（§2.4, 2.5） | 无穷远极限、无穷极限、渐近线、三角极限 |
| Week 4 | Notes 4（§2.6, 2.7） | 指数对数极限、连续、介值定理 |
| Week 5 | Notes 5（§3.1–3.6） | 导数定义、求导法则、链式法则、高阶导数 |
| Week 6 | Notes 6（§3.7–3.10） | 隐函数、对数求导、反三角、IFT、相关变化率 |

**作答格式**：每题在 `Answer / 作答：(　　　)` 中写选项字母；解析册按题号 W1-01 … W6-07 对应。

---

## Week 1 · Functions and Inverse Trigonometry（函数与反三角）

### W1-01 定义域

*做题技巧 · 对数的真数必须严格大于零；二次式先因式分解再画符号表。*

Find the natural domain of $f(x)=\log_{4}\left(x^{2}+3x-10\right)$.

**SELECT ONE**

- A. $(-5,\,2)$
- B. $[-5,\,2]$
- C. $(-\infty,\,-5)\cup(2,\,\infty)$
- D. $(-\infty,\,-5]\cup[2,\,\infty)$
- E. $(-2,\,5)$

Answer / 作答：(　　　)　·　解析见 W1-01

---

### W1-02 定义域

*做题技巧 · 多个限制条件取交集：偶次根号内 ≥ 0，对数真数 > 0，分母 ≠ 0。*

Find the natural domain of $f(x)=\dfrac{\sqrt{9-x^{2}}}{\ln(x+1)}$.

**SELECT ONE**

- A. $[-3,\,3]$
- B. $(-1,\,3]$
- C. $(0,\,3]$
- D. $(-1,\,0)\cup(0,\,3]$
- E. $[-3,\,0)\cup(0,\,3]$

Answer / 作答：(　　　)　·　解析见 W1-02

---

### W1-03 复合函数求值

*做题技巧 · 复合函数从里往外算：先算内层 $f(x_{0})$，再把结果代入外层 $g$。*

Let $f(x)=2x$ and $g(x)=\sin x$. If $x_{0}=\dfrac{5\pi}{6}$, find $(g\circ f)(x_{0})$.

**SELECT ONE**

- A. $\dfrac{\sqrt{3}}{2}$
- B. $-\dfrac{\sqrt{3}}{2}$
- C. $\dfrac{1}{2}$
- D. $-\dfrac{1}{2}$
- E. $\dfrac{5\pi}{3}$

Answer / 作答：(　　　)　·　解析见 W1-03

---

### W1-04 反函数

*做题技巧 · 求反函数三步：写 $y=f(x)$ → 解出 $x$ → 交换 $x,y$；反函数的定义域＝原函数的值域。*

Find the inverse function $f^{-1}(x)$ and its domain for
$$f(x)=\frac{2x-1}{x+3},\qquad x\neq -3.$$

**SELECT ONE**

- A. $f^{-1}(x)=\dfrac{3x+1}{2-x},\quad x\neq 2$
- B. $f^{-1}(x)=\dfrac{3x+1}{x-2},\quad x\neq 2$
- C. $f^{-1}(x)=\dfrac{2x+1}{3-x},\quad x\neq 3$
- D. $f^{-1}(x)=\dfrac{x+3}{2x-1},\quad x\neq \dfrac{1}{2}$
- E. $f^{-1}(x)=\dfrac{3x-1}{2-x},\quad x\neq 2$

Answer / 作答：(　　　)　·　解析见 W1-04

---

### W1-05 反三角主值

*做题技巧 · $\arccos(\cos\theta)$ 先判断 $\theta$ 是否落在 $[0,\pi]$；不在就用 $\cos(2\pi-\theta)=\cos\theta$ 把角拉回主值区间。*

Evaluate $\arccos\left(\cos\dfrac{10\pi}{7}\right)$.

**SELECT ONE**

- A. $\dfrac{10\pi}{7}$
- B. $\dfrac{4\pi}{7}$
- C. $\dfrac{3\pi}{7}$
- D. $-\dfrac{4\pi}{7}$
- E. $\dfrac{2\pi}{7}$

Answer / 作答：(　　　)　·　解析见 W1-05

---

### W1-06 反三角与三角复合

*做题技巧 · 设 $\theta=\arcsin u$，画直角三角形求 $\tan\theta$；注意 $\arcsin$ 的值域是 $[-\pi/2,\pi/2]$，符号跟着 $u$ 走。*

Evaluate $\tan\left(\arcsin\left(-\dfrac{3}{5}\right)\right)$ without a calculator.

**SELECT ONE**

- A. $\dfrac{3}{4}$
- B. $\dfrac{4}{3}$
- C. $-\dfrac{3}{4}$
- D. $-\dfrac{4}{3}$
- E. $-\dfrac{3}{5}$

Answer / 作答：(　　　)　·　解析见 W1-06

---

### W1-07 差商

*做题技巧 · 先把 $F(1+h)-F(1)$ 展开并化到含因子 $h$，再约去 $h$——这是第 3 章导数定义的雏形。*

Let $F(x)=x^{2}-3x$. Evaluate
$$\frac{F(1+h)-F(1)}{h}.$$

**SELECT ONE**

- A. $h+1$
- B. $2h-1$
- C. $h-3$
- D. $-1$
- E. $h-1$

Answer / 作答：(　　　)　·　解析见 W1-07

---

### W1-08 反三角主值

*做题技巧 · $\arcsin(\sin\theta)$ 的主值区间是 $[-\pi/2,\pi/2]$；$\theta\in(\pi,3\pi/2)$ 时先提负号再判断。*

Evaluate $\arcsin\left(\sin\dfrac{9\pi}{7}\right)$.

**SELECT ONE**

- A. $\dfrac{9\pi}{7}$
- B. $\dfrac{2\pi}{7}$
- C. $-\dfrac{2\pi}{7}$
- D. $\dfrac{\pi}{7}$
- E. $\dfrac{8\pi}{7}$

Answer / 作答：(　　　)　·　解析见 W1-08

---

## Week 2 · Limits and Limit Theorems（极限与极限定理）

### W2-01 0/0 型：因式分解

*做题技巧 · 代入得 $0/0$ 先因式分解，约去公因子再代入。*

Evaluate $\displaystyle\lim_{x\to 3}\frac{x^{2}-x-6}{x^{2}-9}$.

**SELECT ONE**

- A. $\dfrac{5}{6}$
- B. $1$
- C. $0$
- D. $\infty$
- E. $\dfrac{5}{3}$

Answer / 作答：(　　　)　·　解析见 W2-01

---

### W2-02 0/0 型：有理化

*做题技巧 · 含根号的差式，分子分母同乘共轭式 $\sqrt{2+x}+\sqrt{2-x}$。*

Evaluate $\displaystyle\lim_{x\to 0}\frac{\sqrt{2+x}-\sqrt{2-x}}{x}$.

**SELECT ONE**

- A. $\sqrt{2}$
- B. $\dfrac{1}{4}$
- C. $0$
- D. $\dfrac{\sqrt{2}}{2}$
- E. $1$

Answer / 作答：(　　　)　·　解析见 W2-02

---

### W2-03 取整函数与单侧极限

*做题技巧 · 分界点两侧取整值不同，必须用单侧极限；$x\to 2^{-}$ 时 $x\in(1,2)$，$\lfloor x\rfloor=1$。*

Evaluate $\displaystyle\lim_{x\to 2^{-}}\bigl(x-\lfloor x\rfloor\bigr)$.

**SELECT ONE**

- A. $0$
- B. $1$
- C. $2$
- D. $-1$
- E. Does not exist

Answer / 作答：(　　　)　·　解析见 W2-03

---

### W2-04 绝对值与单侧极限

*做题技巧 · 绝对值在分界点拆左右：$x>1$ 时 $|x-1|=x-1$；$x<1$ 时 $|x-1|=-(x-1)$。*

Evaluate $\displaystyle\lim_{x\to 1}\frac{|x-1|}{x-1}$.

**SELECT ONE**

- A. $1$
- B. $-1$
- C. $0$
- D. Does not exist
- E. $\dfrac{1}{2}$

Answer / 作答：(　　　)　·　解析见 W2-04

---

### W2-05 已知极限反求参数

*做题技巧 · 分母 → 0 而极限有限，分子在 $x=1$ 必须也为 0（否则发散）；由此得一个方程，约分后再用极限值。*

If $\displaystyle\lim_{x\to 1}\frac{x^{2}+ax+b}{x-1}=3$, find $a+b$.

**SELECT ONE**

- A. $-1$
- B. $1$
- C. $-3$
- D. $2$
- E. $0$

Answer / 作答：(　　　)　·　解析见 W2-05

---

### W2-06 极限运算法则

*做题技巧 · 分母极限不为 0 时直接用法则：和差积商、常数倍、幂次逐项代入。*

Given $\displaystyle\lim_{x\to c}f(x)=4$ and $\displaystyle\lim_{x\to c}g(x)=-2$, evaluate
$$\lim_{x\to c}\frac{f(x)^{3}+2g(x)}{f(x)+g(x)}.$$

**SELECT ONE**

- A. $34$
- B. $15$
- C. $30$
- D. $-30$
- E. Does not exist

Answer / 作答：(　　　)　·　解析见 W2-06

---

### W2-07 夹逼定理

*做题技巧 · $\sin(1/x)$ 有界（$|\sin|\le 1$），乘上趋于 0 的 $x^{2}$，整体被 $[-x^{2},x^{2}]$ 夹住。*

Evaluate $\displaystyle\lim_{x\to 0}x^{2}\sin\frac{1}{x}$.

**SELECT ONE**

- A. $1$
- B. Does not exist
- C. $\infty$
- D. $\dfrac{1}{2}$
- E. $0$

Answer / 作答：(　　　)　·　解析见 W2-07

---

### W2-08 导数定义型极限

*做题技巧 · 识别 $\dfrac{(3+h)^{3}-27}{h}=\dfrac{f(3+h)-f(3)}{h}$，其中 $f(x)=x^{3}$。*

Evaluate $\displaystyle\lim_{h\to 0}\frac{(3+h)^{3}-27}{h}$.

**SELECT ONE**

- A. $9$
- B. $27$
- C. $0$
- D. $54$
- E. $81$

Answer / 作答：(　　　)　·　解析见 W2-08

---

## Week 3 · Limits at Infinity, Infinite Limits and Trigonometric Limits（无穷远、无穷与三角极限）

### W3-01 有理式在无穷远

*做题技巧 · 分子分母同除以最高次幂 $x^{3}$；次数相同则极限为首项系数之比。*

Evaluate $\displaystyle\lim_{x\to\infty}\frac{3x^{3}-2x+1}{2x^{3}+x^{2}-5}$.

**SELECT ONE**

- A. $\dfrac{3}{2}$
- B. $\dfrac{2}{3}$
- C. $0$
- D. $\dfrac{1}{2}$
- E. $\infty$

Answer / 作答：(　　　)　·　解析见 W3-01

---

### W3-02 根式在负无穷

*做题技巧 · $x\to-\infty$ 时 $\sqrt{x^{2}+3x}=|x|\sqrt{1+3/x}=-x\sqrt{1+3/x}$，开方出来要变号。*

Evaluate $\displaystyle\lim_{x\to-\infty}\left(x+\sqrt{x^{2}+3x}\right)$.

**SELECT ONE**

- A. $\dfrac{3}{2}$
- B. $-\dfrac{3}{2}$
- C. $0$
- D. $-\infty$
- E. Does not exist

Answer / 作答：(　　　)　·　解析见 W3-02

---

### W3-03 根式差在正无穷

*做题技巧 · 根式差先乘共轭 $\dfrac{\sqrt{4x^{2}+3x}+2x}{\sqrt{4x^{2}+3x}+2x}$，再把分母除以 $x$。*

Evaluate $\displaystyle\lim_{x\to\infty}\left(\sqrt{4x^{2}+3x}-2x\right)$.

**SELECT ONE**

- A. $\dfrac{3}{2}$
- B. $0$
- C. $\dfrac{3}{4}$
- D. $\infty$
- E. $\dfrac{4}{3}$

Answer / 作答：(　　　)　·　解析见 W3-03

---

### W3-04 无穷极限（单侧）

*做题技巧 · 分母 → 0 时看两侧符号；$x\to2^{+}$ 时分母为正，分子 $\to 3>0$，故 $+\infty$。*

Evaluate $\displaystyle\lim_{x\to 2^{+}}\frac{x+1}{x-2}$.

**SELECT ONE**

- A. $+\infty$
- B. $-\infty$
- C. $3$
- D. $0$
- E. Does not exist

Answer / 作答：(　　　)　·　解析见 W3-04

---

### W3-05 渐近线

*做题技巧 · 水平渐近线看 $x\to\pm\infty$ 的极限；垂直渐近线找分母为 0 且分子不为 0 的点。*

Find all asymptotes of $f(x)=\dfrac{2x^{2}-3x+1}{x^{2}-4}$.

**SELECT ONE**

- A. Horizontal $y=2$; vertical $x=2$ only
- B. Horizontal $y=0$; vertical $x=\pm 2$
- C. Horizontal $y=2$; no vertical asymptote
- D. Horizontal $y=2$; vertical $x=\pm 2$
- E. Horizontal $y=2$; vertical $x=\pm 2$ and $x=1$

Answer / 作答：(　　　)　·　解析见 W3-05

---

### W3-06 三角极限（第一重要极限）

*做题技巧 · 把 $\tan 5x$ 拆成 $\dfrac{\tan 5x}{5x}\cdot 5x$，把 $\sin 3x$ 拆成 $\dfrac{\sin 3x}{3x}\cdot 3x$，再用 $\lim_{t\to0}\frac{\sin t}{t}=1$。*

Evaluate $\displaystyle\lim_{x\to 0}\frac{\tan 5x}{\sin 3x}$.

**SELECT ONE**

- A. $\dfrac{3}{5}$
- B. $\dfrac{5}{3}$
- C. $5$
- D. $3$
- E. $1$

Answer / 作答：(　　　)　·　解析见 W3-06

---

### W3-07 $1-\cos$ 型极限

*做题技巧 · 用半角公式 $1-\cos 4x=2\sin^{2}2x$，或记住 $\lim_{t\to0}\dfrac{1-\cos t}{t^{2}}=\dfrac{1}{2}$ 再配系数。*

Evaluate $\displaystyle\lim_{x\to 0}\frac{1-\cos 4x}{x^{2}}$.

**SELECT ONE**

- A. $4$
- B. $16$
- C. $8$
- D. $0$
- E. $\dfrac{1}{8}$

Answer / 作答：(　　　)　·　解析见 W3-07

---

### W3-08 有界振荡因子

*做题技巧 · $\cos(1/x)$ 有界，$x\to 0$ 时 $x\cos(1/x)$ 被 $[-|x|,|x|]$ 夹逼到 0。*

Evaluate $\displaystyle\lim_{x\to 0}x\cos\frac{1}{x}$.

**SELECT ONE**

- A. $0$
- B. $1$
- C. Does not exist
- D. $\infty$
- E. $-1$

Answer / 作答：(　　　)　·　解析见 W3-08

---

### W3-09 数列极限

*做题技巧 · 分子分母同除以 $n$；$\sqrt{n^{2}+n+1}=n\sqrt{1+1/n+1/n^{2}}$。*

Evaluate $\displaystyle\lim_{n\to\infty}\frac{n}{\sqrt{n^{2}+n+1}}$.

**SELECT ONE**

- A. $0$
- B. $\dfrac{1}{2}$
- C. $\infty$
- D. Does not exist
- E. $1$

Answer / 作答：(　　　)　·　解析见 W3-09

---

### W3-10 三角极限（乘积型）

*做题技巧 · 拆成 $\dfrac{\sin 3x}{3x}\cdot\dfrac{\sin 5x}{5x}\cdot 15$，两个因子都趋于 1。*

Evaluate $\displaystyle\lim_{x\to 0}\frac{\sin 3x\,\sin 5x}{x^{2}}$.

**SELECT ONE**

- A. $8$
- B. $0$
- C. $1$
- D. $15$
- E. $5$

Answer / 作答：(　　　)　·　解析见 W3-10

---

## Week 4 · Exponential/Logarithmic Limits, Continuity and IVT（指数对数极限、连续与介值定理）

### W4-01 指数增量极限

*做题技巧 · 凑标准形式 $\lim_{t\to0}\dfrac{e^{t}-1}{t}=1$：把 $3x$ 看成 $t$。*

Evaluate $\displaystyle\lim_{x\to 0}\frac{e^{3x}-1}{x}$.

**SELECT ONE**

- A. $3$
- B. $1$
- C. $e^{3}$
- D. $0$
- E. $\infty$

Answer / 作答：(　　　)　·　解析见 W4-01

---

### W4-02 对数增量极限

*做题技巧 · 凑 $\lim_{t\to0}\dfrac{\ln(1+t)}{t}=1$：分子写成 $\ln(1+5x)$，分母配 $5x$。*

Evaluate $\displaystyle\lim_{x\to 0}\frac{\ln(1+5x)}{x}$.

**SELECT ONE**

- A. $1$
- B. $0$
- C. $5$
- D. $e^{5}$
- E. $\infty$

Answer / 作答：(　　　)　·　解析见 W4-02

---

### W4-03 $1^{\infty}$ 型（有理式）

*做题技巧 · 写成 $\left(1+\dfrac{4}{2x+1}\right)^{x}$，指数极限 $\lim x\cdot\dfrac{4}{2x+1}=2$，故为 $e^{2}$。*

Evaluate $\displaystyle\lim_{x\to\infty}\left(\frac{2x+5}{2x+1}\right)^{x}$.

**SELECT ONE**

- A. $e^{4}$
- B. $e^{2}$
- C. $e$
- D. $1$
- E. $e^{1/2}$

Answer / 作答：(　　　)　·　解析见 W4-03

---

### W4-04 $1^{\infty}$ 型（$x\to 0$）

*做题技巧 · $(1+2x)^{3/x}=\left[(1+2x)^{1/(2x)}\right]^{6}\to e^{6}$。*

Evaluate $\displaystyle\lim_{x\to 0}(1+2x)^{3/x}$.

**SELECT ONE**

- A. $e^{3}$
- B. $e^{2}$
- C. $1$
- D. $\infty$
- E. $e^{6}$

Answer / 作答：(　　　)　·　解析见 W4-04

---

### W4-05 可去间断点

*做题技巧 · $(x^{2}-9)/(x-3)=x+3$（$x\neq3$）；补定义 $f(3)=\lim_{x\to3}f(x)$ 即可连续。*

The function $f(x)=\dfrac{x^{2}-9}{x-3}$ is undefined at $x=3$. Which value of $f(3)$ makes $f$ continuous at $x=3$?

**SELECT ONE**

- A. $3$
- B. $0$
- C. $9$
- D. $6$
- E. It cannot be made continuous

Answer / 作答：(　　　)　·　解析见 W4-05

---

### W4-06 间断点分类

*做题技巧 · 左右极限都存在但不等 → 跳跃间断点；先分别算两侧。*

Classify the discontinuity of
$$f(x)=\begin{cases}x+1,&x<2,\\[2pt] 4-x,&x\ge 2\end{cases}$$
at $x=2$.

**SELECT ONE**

- A. Jump discontinuity
- B. Removable discontinuity
- C. Infinite discontinuity
- D. Oscillating discontinuity
- E. $f$ is continuous at $x=2$

Answer / 作答：(　　　)　·　解析见 W4-06

---

### W4-07 分段函数求参数

*做题技巧 · 每个分界点列两个条件：左极限＝右极限（连续）；左导数＝右导数（可导，若题目要求）。本题只要求连续。*

Find $a,b$ so that
$$f(x)=\begin{cases}x+1,&x<1,\\[2pt] ax+b,&1\le x<2,\\[2pt] 3x-1,&x\ge 2\end{cases}$$
is continuous everywhere.

**SELECT ONE**

- A. $(a,b)=(-1,\,3)$
- B. $(a,b)=(2,\,0)$
- C. $(a,b)=(3,\,-1)$
- D. $(a,b)=(3,\,1)$
- E. $(a,b)=(1,\,2)$

Answer / 作答：(　　　)　·　解析见 W4-07

---

### W4-08 介值定理

*做题技巧 · 找使 $f$ 变号的整数端点：$f(0)<0<f(1)$，则在 $(0,1)$ 内有根。*

The equation $x^{3}+4x-2=0$ has a root in which interval?

**SELECT ONE**

- A. $(1,\,2)$
- B. $(0,\,1)$
- C. $(-1,\,0)$
- D. $(2,\,3)$
- E. The equation has no real root

Answer / 作答：(　　　)　·　解析见 W4-08

---

## Week 5 · Derivatives and Differentiation Rules（导数与求导法则）

### W5-01 导数定义

*做题技巧 · 多项式先用幂函数法则求 $f'(x)$，再代 $x=2$；也可用定义验证。*

If $f(x)=x^{2}+3x$, find $f'(2)$.

**SELECT ONE**

- A. $4$
- B. $3$
- C. $8$
- D. $7$
- E. $1$

Answer / 作答：(　　　)　·　解析见 W5-01

---

### W5-02 切线方程

*做题技巧 · 切线：$y-f(a)=f'(a)(x-a)$；先算点坐标，再算斜率。*

Find the tangent line to $y=xe^{x}$ at $x=0$.

**SELECT ONE**

- A. $y=x$
- B. $y=x+1$
- C. $y=ex$
- D. $y=2x-1$
- E. $y=x-1$

Answer / 作答：(　　　)　·　解析见 W5-02

---

### W5-03 分段函数可导性

*做题技巧 · 可导必连续：先用连续性定一个方程，再用左右导数相等定另一个。*

Let
$$f(x)=\begin{cases}x^{2},&x\le 1,\\[2pt] ax+b,&x>1.\end{cases}$$
If $f$ is differentiable at $x=1$, find $a-b$.

**SELECT ONE**

- A. $1$
- B. $-1$
- C. $2$
- D. $0$
- E. $3$

Answer / 作答：(　　　)　·　解析见 W5-03

---

### W5-04 乘积法则

*做题技巧 · $(uv)'=u'v+uv'$，两个因子分别求导再相加；不要漏第二项。*

If $f(x)=(x^{2}+1)(x^{3}-2)$, find $f'(1)$.

**SELECT ONE**

- A. $2$
- B. $4$
- C. $6$
- D. $0$
- E. $-2$

Answer / 作答：(　　　)　·　解析见 W5-04

---

### W5-05 链式法则

*做题技巧 · 外层幂函数、内层 $3x^{2}+5$：$4(3x^{2}+5)^{3}\cdot 6x$。*

Differentiate $y=(3x^{2}+5)^{4}$.

**SELECT ONE**

- A. $12x(3x^{2}+5)^{3}$
- B. $4(3x^{2}+5)^{3}$
- C. $24x(3x^{2}+5)^{3}$
- D. $24x(3x^{2}+5)^{4}$
- E. $8x(3x^{2}+5)^{3}$

Answer / 作答：(　　　)　·　解析见 W5-05

---

### W5-06 三角函数求导

*做题技巧 · $\sin^{2}x$ 是复合函数：$2\sin x\cos x=\sin 2x$；在 $\pi/4$ 处 $\sin(\pi/2)=1$。*

If $f(x)=\sin^{2}x$, find $f'\left(\dfrac{\pi}{4}\right)$.

**SELECT ONE**

- A. $1$
- B. $0$
- C. $\dfrac{\sqrt{2}}{2}$
- D. $2$
- E. $-1$

Answer / 作答：(　　　)　·　解析见 W5-06

---

### W5-07 高阶导数

*做题技巧 · 逐阶求导，每阶只保留还会继续产生非零项的部分；$x^{6}$ 的四阶导是 $6\cdot5\cdot4\cdot3x^{2}$。*

If $f(x)=x^{6}-2x^{4}+x$, find $f^{(4)}(1)$.

**SELECT ONE**

- A. $360$
- B. $240$
- C. $48$
- D. $312$
- E. $0$

Answer / 作答：(　　　)　·　解析见 W5-07

---

### W5-08 位置、速度与加速度

*做题技巧 · $v(t)=s'(t)$，$a(t)=v'(t)=s''(t)$；先由 $a=0$ 求时刻，再代回 $v$。*

A particle moves along a line with position $s(t)=t^{3}-6t^{2}+9t$. Find its velocity at the instant when its acceleration is zero.

**SELECT ONE**

- A. $0$
- B. $3$
- C. $9$
- D. $-9$
- E. $-3$

Answer / 作答：(　　　)　·　解析见 W5-08

---

### W5-09 水平切线

*做题技巧 · 水平切线 ⇔ $f'(x)=0$；解方程后要确认点在定义域内。*

At which points does $f(x)=x^{3}-3x$ have a horizontal tangent?

**SELECT ONE**

- A. $x=0$
- B. $x=\pm 1$
- C. $x=\pm\sqrt{3}$
- D. $x=1$ only
- E. $x=\pm 3$

Answer / 作答：(　　　)　·　解析见 W5-09

---

## Week 6 · Implicit Differentiation, Logarithmic Differentiation, IFT and Related Rates（隐函数、对数求导、IFT 与相关变化率）

### W6-01 对数函数求导

*做题技巧 · $\dfrac{d}{dx}\ln u=\dfrac{u'}{u}$，链式法则把内层导数放分子。*

Differentiate $y=\ln(x^{2}+1)$.

**SELECT ONE**

- A. $\dfrac{1}{x^{2}+1}$
- B. $2x\ln(x^{2}+1)$
- C. $\dfrac{2x}{x^{2}+1}$
- D. $\dfrac{x}{x^{2}+1}$
- E. $\dfrac{2x}{(x^{2}+1)^{2}}$

Answer / 作答：(　　　)　·　解析见 W6-01

---

### W6-02 指数函数求导

*做题技巧 · $\dfrac{d}{dx}e^{u}=e^{u}u'$；这里 $u=\sin x$，$u'=\cos x$。*

Differentiate $y=e^{\sin x}$.

**SELECT ONE**

- A. $\cos x\,e^{\sin x}$
- B. $e^{\sin x}$
- C. $\sin x\,e^{\cos x}$
- D. $\cos x\,e^{\cos x}$
- E. $-\cos x\,e^{\sin x}$

Answer / 作答：(　　　)　·　解析见 W6-02

---

### W6-03 反三角求导

*做题技巧 · $\dfrac{d}{dx}\arcsin\dfrac{x}{a}=\dfrac{1}{\sqrt{a^{2}-x^{2}}}$（$a>0$）；也可用链式法则 $\dfrac{1/2}{\sqrt{1-(x/2)^{2}}}$ 化简。*

Differentiate $y=\arcsin\dfrac{x}{2}$.

**SELECT ONE**

- A. $\dfrac{2}{\sqrt{4-x^{2}}}$
- B. $-\dfrac{1}{\sqrt{4-x^{2}}}$
- C. $\dfrac{x}{\sqrt{4-x^{2}}}$
- D. $\dfrac{1}{\sqrt{4-x^{2}}}$
- E. $\dfrac{1}{2\sqrt{4-x^{2}}}$

Answer / 作答：(　　　)　·　解析见 W6-03

---

### W6-04 反函数求导（IFT）

*做题技巧 · $(f^{-1})'(b)=\dfrac{1}{f'(a)}$，其中 $f(a)=b$；先找 $a$。*

Let $f(x)=x^{3}+x-1$. Given $f(1)=1$, find $(f^{-1})'(1)$.

**SELECT ONE**

- A. $4$
- B. $\dfrac{1}{4}$
- C. $\dfrac{1}{3}$
- D. $1$
- E. $3$

Answer / 作答：(　　　)　·　解析见 W6-04

---

### W6-05 隐函数求导

*做题技巧 · 两边对 $x$ 求导，$y$ 视为 $y(x)$，每项含 $y$ 就乘 $y'$；最后代点求值。*

If $x^{2}+xy+y^{2}=7$, find $y'$ at the point $(1,2)$.

**SELECT ONE**

- A. $\dfrac{4}{5}$
- B. $-2$
- C. $\dfrac{4}{3}$
- D. $-\dfrac{3}{4}$
- E. $-\dfrac{4}{5}$

Answer / 作答：(　　　)　·　解析见 W6-05

---

### W6-06 对数求导法

*做题技巧 · 底数和指数都含 $x$：两边取 $\ln$，$\ln y=x\ln x$，再隐式求导并乘回 $y$。*

Differentiate $y=x^{x}$ (for $x>0$).

**SELECT ONE**

- A. $x^{x}(\ln x+1)$
- B. $x^{x}\ln x$
- C. $x\cdot x^{x-1}$
- D. $x^{x}$
- E. $x^{x}(\ln x-1)$

Answer / 作答：(　　　)　·　解析见 W6-06

---

### W6-07 相关变化率

*做题技巧 · 先写几何关系 $V=\dfrac{4}{3}\pi r^{3}$，再对 $t$ 求导；$r$ 和 $dr/dt$ 都代当前值。*

A spherical balloon is being inflated so that its radius increases at $2\ \text{cm/s}$. How fast is the volume increasing when the radius is $5\ \text{cm}$?

**SELECT ONE**

- A. $100\pi\ \text{cm}^{3}/\text{s}$
- B. $40\pi\ \text{cm}^{3}/\text{s}$
- C. $200\pi\ \text{cm}^{3}/\text{s}$
- D. $500\pi\ \text{cm}^{3}/\text{s}$
- E. $20\pi\ \text{cm}^{3}/\text{s}$

Answer / 作答：(　　　)　·　解析见 W6-07
