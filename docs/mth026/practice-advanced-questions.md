# MTH026 Calculus I · Week 1–6 综合提高卷 (Advanced Integrated Set)

> **20 题 · 英文题干 · 五选一 · 跨周综合**
> 难度高于《Week 1–6 练习册》：每题 2–4 步，多数把两个知识点串在一起。专门补练习册和 LM Core 样卷的缺口——反三角回主值、有理化反求参数、负无穷根式变号、分段可导、$1^{\infty}$ 型、IVT 配合极值、导数定义、反函数二阶导、对数求导、相关变化率。
> 使用方法：先整卷限时 60 分钟做完，再对照《综合卷解析册》；解析册开头有 20 题答案速查表。

**覆盖范围**

| 周次 | 题号 | 综合的考点 |
|---|---|---|
| Week 1 | X1-01 … X1-05 | 定义域（对数+根式）、反函数与值域、反三角回主值、三角复合、差商型极限 |
| Week 2 | X2-01 … X2-02 | $0/0$ 反求参数、有理化反求参数 |
| Week 3 | X3-01 … X3-02 | 根式差在 $+\infty$、$\sqrt{x^{2}}=|x|$ 在 $-\infty$ |
| Week 4 | X4-01 … X4-04 | 分段可导、$1^{\infty}$、指数增量+三角极限、IVT 与极值 |
| Week 5 | X5-01 … X5-03 | 导数定义与夹逼、切线、乘积+链式高阶导 |
| Week 6 | X6-01 … X6-04 | 隐函数、反函数二阶导、对数求导、相关变化率 |

**作答格式**：每题在 `Answer / 作答：(　　　)` 中写选项字母；解析册按题号 X1-01 … X6-04 对应。

---

## Week 1 · Functions, Inverse and Trigonometry

### X1-01 定义域（对数与根式取交）

*做题技巧 · 分式对数的真数用符号表解；根号与对数各得一个区间，最后取交集，端点逐一看是否可取。*

Find the natural domain of $f(x)=\ln\dfrac{x-1}{x+2}+\sqrt{9-x^{2}}$.

**SELECT ONE**

- A. $[-3,\,-2)\cup(1,\,3]$
- B. $(-3,\,-2)\cup(1,\,3)$
- C. $[-3,\,-2]\cup[1,\,3]$
- D. $(-\infty,\,-2)\cup(1,\,\infty)$
- E. $[-3,\,3]$

Answer / 作答：(　　　)　·　解析见 X1-01

---

### X1-02 反函数与值域

*做题技巧 · 把 $e^{x}$ 当成一个未知量整体解出来；反函数的定义域就是原函数的值域，用 $x\to\pm\infty$ 的两端极限确定。*

Let $f(x)=\dfrac{e^{x}-1}{e^{x}+1}$. Find $f^{-1}(x)$ and its domain.

**SELECT ONE**

- A. $\ln\dfrac{1-x}{1+x}$，定义域 $(-1,\,1)$
- B. $\ln\dfrac{1+x}{1-x}$，定义域 $(0,\,\infty)$
- C. $\ln\dfrac{1+x}{1-x}$，定义域 $(-1,\,1)$
- D. $\ln\dfrac{x-1}{x+1}$，定义域 $|x|>1$
- E. $\ln\dfrac{1+x}{1-x}$，定义域 $[-1,\,1]$

Answer / 作答：(　　　)　·　解析见 X1-02

---

### X1-03 反三角回主值（余角）

*做题技巧 · 先看弧度落在哪个象限，把 $\sin$ 换成 $\cos\!\left(\frac{\pi}{2}-\theta\right)$，保证最终角落在 $\arccos$ 的值域 $[0,\pi]$ 里。*

Evaluate $\arccos\left(\sin\dfrac{11\pi}{10}\right)$.

**SELECT ONE**

- A. $\dfrac{11\pi}{10}$
- B. $\dfrac{3\pi}{5}$
- C. $-\dfrac{\pi}{10}$
- D. $\dfrac{\pi}{10}$
- E. $\dfrac{7\pi}{10}$

Answer / 作答：(　　　)　·　解析见 X1-03

---

### X1-04 反三角与三角复合

*做题技巧 · 令 $\theta=\arctan(\cdot)$ 画直角三角形；$\arctan$ 的值域是 $\left(-\frac{\pi}{2},\frac{\pi}{2}\right)$，在那里 $\cos\theta>0$。*

Evaluate $\cos\left(\arctan\left(-\dfrac{4}{3}\right)\right)$ without using a calculator.

**SELECT ONE**

- A. $-\dfrac{4}{5}$
- B. $-\dfrac{3}{5}$
- C. $\dfrac{4}{5}$
- D. $\dfrac{3}{5}$
- E. $\dfrac{5}{4}$

Answer / 作答：(　　　)　·　解析见 X1-04

---

### X1-05 差商型极限

*做题技巧 · 二项式展开只保留到 $h^{2}$ 项；也可以认出它是 $f(x)=x^{5}$ 在 $x=1$ 处的二阶导数的一半。*

Evaluate $\displaystyle\lim_{h\to 0}\frac{(1+h)^{5}-1-5h}{h^{2}}$.

**SELECT ONE**

- A. $10$
- B. $5$
- C. $20$
- D. $0$
- E. 不存在（DNE）

Answer / 作答：(　　　)　·　解析见 X1-05

---

## Week 2 · Limits and Limit Theorems

### X2-01 反求参数（$0/0$ 型）

*做题技巧 · 分母趋于 0 而极限存在 ⇒ 分子也必须趋于 0，这是第一个方程；再把分子因式分解成 $(x-2)(x+c)$，商式在 $x=2$ 的值就是极限。*

If $\displaystyle\lim_{x\to 2}\frac{x^{2}+ax+b}{x-2}=5$, find $a+b$.

**SELECT ONE**

- A. $-1$
- B. $-5$
- C. $1$
- D. $5$
- E. $-7$

Answer / 作答：(　　　)　· 解析见 X2-01

---

### X2-02 有理化反求参数

*做题技巧 · 分子乘共轭 $\sqrt{1+kx}+1$ 后约掉 $x$，剩下的极限是 $\frac{k}{2}$。*

If $\displaystyle\lim_{x\to 0}\frac{\sqrt{1+kx}-1}{x}=3$, find $k$.

**SELECT ONE**

- A. $\dfrac{3}{2}$
- B. $3$
- C. $12$
- D. $-6$
- E. $6$

Answer / 作答：(　　　)　· 解析见 X2-02

---

## Week 3 · Infinite Limits and Trig Limits

### X3-01 根式差在 $+\infty$

*做题技巧 · 有理化，或分子分母同除 $x$；最终极限是最高次系数之比的一半。*

Evaluate $\displaystyle\lim_{x\to\infty}\left(\sqrt{x^{2}+6x}-x\right)$.

**SELECT ONE**

- A. $0$
- B. $6$
- C. $3$
- D. $\dfrac{3}{2}$
- E. $+\infty$

Answer / 作答：(　　　)　· 解析见 X3-01

---

### X3-02 负无穷根式必须变号

*做题技巧 · $x\to-\infty$ 时 $\sqrt{4x^{2}+5x+1}=-2x\sqrt{1+\frac{5}{4x}+\frac{1}{4x^{2}}}$，负号不能丢。*

Evaluate $\displaystyle\lim_{x\to-\infty}\left(\sqrt{4x^{2}+5x+1}+2x\right)$.

**SELECT ONE**

- A. $\dfrac{5}{4}$
- B. $-\dfrac{5}{2}$
- C. $+\infty$
- D. $-\dfrac{5}{4}$
- E. $0$

Answer / 作答：(　　　)　· 解析见 X3-02

---

## Week 4 · Exponential Limits, Continuity and IVT

### X4-01 分段函数可导

*做题技巧 · 可导必连续：先让左右函数值在 $x=1$ 相等；再让左右导数相等。两个方程解两个参数。*

Let $f(x)=\begin{cases}x^{2}+ax+b,&x\le 1,\\[2pt] 3x+1,&x>1.\end{cases}$ If $f$ is differentiable at $x=1$, find $a+b$.

**SELECT ONE**

- A. $3$
- B. $-1$
- C. $1$
- D. $5$
- E. $2$

Answer / 作答：(　　　)　· 解析见 X4-01

---

### X4-02 $1^{\infty}$ 型

*做题技巧 · 先把括号化成 $1+\frac{4}{x-1}$，再用 $\lim_{u\to 0}(1+u)^{1/u}=e$；指数上的 $x$ 要跟着换元。*

Evaluate $\displaystyle\lim_{x\to\infty}\left(\frac{x+3}{x-1}\right)^{2x}$.

**SELECT ONE**

- A. $e^{4}$
- B. $e^{6}$
- C. $e^{2}$
- D. $1$
- E. $e^{8}$

Answer / 作答：(　　　)　· 解析见 X4-02

---

### X4-03 指数增量与三角极限

*做题技巧 · 拆成三个标准块的乘积：$\frac{e^{6x}-1}{6x}$、$\frac{3x}{\sin 3x}$ 和常数。*

Evaluate $\displaystyle\lim_{x\to 0}\frac{e^{6x}-1}{\sin 3x}$.

**SELECT ONE**

- A. $6$
- B. $2$
- C. $3$
- D. $0$
- E. $\dfrac{1}{2}$

Answer / 作答：(　　　)　· 解析见 X4-03

---

### X4-04 三次方程有三个实根

*做题技巧 · 求导找两个驻点，算出局部极大值和局部极小值；三个实根 ⇔ 极大值 $>0>$ 极小值。*

For which values of $k$ does the equation $x^{3}-3x+k=0$ have three distinct real roots?

**SELECT ONE**

- A. $-2<k<2$
- B. $-1<k<1$
- C. $k<-2$ 或 $k>2$
- D. $0<k<2$
- E. 任意实数 $k$

Answer / 作答：(　　　)　· 解析见 X4-04

---

## Week 5 · Derivatives and Differentiation Rules

### X5-01 导数定义与夹逼

*做题技巧 · 在 $x=0$ 处只能用定义：$f'(0)=\lim_{h\to0}\frac{f(h)-f(0)}{h}$，然后对 $h\sin\frac{1}{h}$ 用夹逼。*

Let $f(x)=\begin{cases}x^{2}\sin\dfrac{1}{x},&x\neq 0,\\[2pt] 0,&x=0.\end{cases}$ Find $f'(0)$.

**SELECT ONE**

- A. $1$
- B. 不存在
- C. $0$
- D. $\dfrac{1}{2}$
- E. $+\infty$

Answer / 作答：(　　　)　· 解析见 X5-01

---

### X5-02 切线

*做题技巧 · 直线 $y=x+b$ 的斜率是 1，所以切点满足 $\frac{1}{x}=1$；求出切点后回代求 $b$。*

The line $y=x+b$ is tangent to the curve $y=\ln x$. Find $b$.

**SELECT ONE**

- A. $0$
- B. $1$
- C. $-2$
- D. $-1$
- E. $e$

Answer / 作答：(　　　)　· 解析见 X5-02

---

### X5-03 乘积法则与链式法则（高阶）

*做题技巧 · 先乘积法则再对 $e^{2x}$ 用链式；求二阶时把 $e^{2x}$ 提出来能少犯错。*

Let $f(x)=x^{2}e^{2x}$. Find $f''(0)$.

**SELECT ONE**

- A. $0$
- B. $2$
- C. $4$
- D. $6$
- E. $8$

Answer / 作答：(　　　)　· 解析见 X5-03

---

## Week 6 · Implicit, Inverse, Logarithmic and Related Rates

### X6-01 隐函数求导

*做题技巧 · 两边对 $x$ 求导，$e^{xy}$ 要用链式法则产生 $(y+xy')$；最后代点。*

If $e^{xy}=x+y$, find $\dfrac{dy}{dx}$ at the point $(0,\,1)$.

**SELECT ONE**

- A. $1$
- B. $-1$
- C. $e$
- D. $2$
- E. $0$

Answer / 作答：(　　　)　· 解析见 X6-01

---

### X6-02 反函数的二阶导数

*做题技巧 · 先由 $f(1)=1$ 得 $g(1)=1$；再用 $g'(x)=\frac{1}{f'(g(x))}$ 推出 $g''(x)=-\frac{f''(g(x))}{[f'(g(x))]^{3}}$。*

Let $f(x)=x^{3}+x-1$ and $g=f^{-1}$. Find $g''(1)$.

**SELECT ONE**

- A. $-\dfrac{1}{4}$
- B. $\dfrac{1}{4}$
- C. $-\dfrac{3}{32}$
- D. $-\dfrac{3}{16}$
- E. $\dfrac{3}{32}$

Answer / 作答：(　　　)　· 解析见 X6-02

---

### X6-03 对数求导法

*做题技巧 · 两边取 $\ln$ 得 $\ln y=(\ln x)^{2}$，再隐式求导，最后把 $y=x^{\ln x}$ 代回去。*

Let $y=x^{\ln x}$ for $x>0$. Find $\left.\dfrac{dy}{dx}\right|_{x=e}$.

**SELECT ONE**

- A. $2$
- B. $e$
- C. $\dfrac{2}{e}$
- D. $1$
- E. $2e$

Answer / 作答：(　　　)　· 解析见 X6-03

---

### X6-04 相关变化率

*做题技巧 · 设底端距墙 $x$、顶端高 $y$，约束是 $x^{2}+y^{2}=10^{2}$；对 $t$ 求导后代入 $x=6,\ \frac{dx}{dt}=1$。*

A 10 ft ladder leans against a vertical wall. Its bottom slides away from the wall at $1\ \text{ft/s}$. How fast is the top of the ladder sliding down when the bottom is $6\ \text{ft}$ from the wall?

**SELECT ONE**

- A. $\dfrac{4}{3}\ \text{ft/s}$
- B. $\dfrac{5}{8}\ \text{ft/s}$
- C. $\dfrac{1}{2}\ \text{ft/s}$
- D. $\dfrac{3}{4}\ \text{ft/s}$
- E. $1\ \text{ft/s}$

Answer / 作答：(　　　)　· 解析见 X6-04
