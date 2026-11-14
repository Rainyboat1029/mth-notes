# Chapter 2 Limits: 无穷极限、无穷大处的极限与三角函数极限 知识详解与例题精解

## 第一部分：本节课知识详解 (Lecture 3 Summary)

---

### 2.4 Limits at Infinity; Infinite Limits (无穷大处的极限与无穷极限)

#### 1. 无穷大处的极限 (Limits at Infinity)

* **概念定义 (Definition):** 
* 当自变量 $x$ 无限增大（$x \to \infty$）或无限减小（$x \to -\infty$）时，函数 $f(x)$ 趋近于一个确定的有限实数 $L$，记作 $\lim_{x \to \infty} f(x) = L$ 或 $\lim_{x \to -\infty} f(x) = L$。
* **核心基本极限 (Core Limits):**
设 $k$ 为正整数（$k \in \mathbb{Z}^+$），则：
$$\lim_{x \to +\infty} \frac{1}{x^k} = 0, \quad \lim_{x \to -\infty} \frac{1}{x^k} = 0$$
* **运算法则 (Limit Laws at Infinity):**
主极限定理（Main Limit Theorem）关于四则运算、乘方、开方的法则在 $x \to \pm\infty$ 时依然适用。
* **求解有理函数/分式极限的标准技巧 (Standard Technique):**
**分子分母同除以分母中出现的最高次幂**（Divide numerator and denominator by the highest power of $x$ in the denominator）。

---

#### 🌟 课件例题与详解 (Lecture Examples & Solutions)

##### 【课件例题 1】证明有理函数的极限

**Problem:** Prove that $\lim_{x \to \infty} \frac{x}{1+x^2} = 0$.
* **Process (证明步骤):**
$$\lim_{x \to \infty} \frac{x}{1+x^2} = \lim_{x \to \infty} \frac{\frac{x}{x^2}}{\frac{1}{x^2} + \frac{x^2}{x^2}} = \lim_{x \to \infty} \frac{\frac{1}{x}}{\frac{1}{x^2} + 1} = \frac{0}{0 + 1} = 0$$
* **中文详解:** 分母的最高次幂为 $x^2$。将分子和分母同时除以 $x^2$，利用基本极限 $\lim_{x \to \infty} \frac{1}{x} = 0$ 与 $\lim_{x \to \infty} \frac{1}{x^2} = 0$，直接求得极限为 0。

##### 【课件例题 2】趋于负无穷时的分式极限

**Problem:** Find $\lim_{x \to -\infty} \frac{2x^3}{1+x^3}$.
* **Process (解题步骤):**
$$\lim_{x \to -\infty} \frac{2x^3}{1+x^3} = \lim_{x \to -\infty} \frac{2}{\frac{1}{x^3} + 1} = \frac{2}{0 + 1} = 2$$
* **中文详解:** 分母最高次项为 $x^3$，分子分母同除以 $x^3$ 后，$\frac{1}{x^3} \to 0$，得到极限值为 2。

---

#### 2. 数列的极限 (Limits of Sequences)

* **数列定义 (Sequences):** 数列 $\{a_n\}$ 是定义在正整数集 $\mathbb{Z}^+$ 上的函数 $f(n) = a_n$。
* **敛散性 (Convergence & Divergence):**
* 若当 $n \to \infty$ 时，$a_n$ 无限趋近于有限常数 $L$，则称数列**收敛**（converges）于 $L$，记作 $\lim_{n \to \infty} a_n = L$。
* 若极限不存在，则称数列**发散**（diverges）。
* **函数极限与数列极限的关系定理 (Bridge Proposition):**
* 若函数极限 $\lim_{x \to \infty} f(x) = A$ 成立，则对应的离散数列极限 $\lim_{n \to \infty} f(n) = A$ 必成立。
* 主极限定理与夹逼定理对数列极限完全适用。

---

#### 3. 无穷极限 (Infinite Limits)

* **概念定义 (Definition):**
* 当 $x \to c$ 时，若 $f(x)$ 无限增大，记作 $\lim_{x \to c} f(x) = \infty$；若无限减小，记作 $\lim_{x \to c} f(x) = -\infty$。
* **关于“极限存在性”的理解 (Caution on Existence):**
* 严格来说，因为 $\infty$ 不是实数，此时实数意义下的极限是不存在的（DNE）。
* 课件中规范表述为：极限在**无穷意义下存在**（"exists in the infinite sense"）。

---

#### 🌟 课件例题与详解 (Lecture Examples & Solutions)

##### 【课件例题 3】单侧无穷极限的符号判断

**Problem:** Analyze $\lim_{x \to 2^-} \frac{1}{x-2}$ and $\lim_{x \to 2^+} \frac{1}{x-2}$.
* **Process (解析过程):**
* As $x \to 2^-$, $x < 2 \implies x - 2 \to 0^-$ (negative) $\implies \lim_{x \to 2^-} \frac{1}{x-2} = -\infty$
* As $x \to 2^+$, $x > 2 \implies x - 2 \to 0^+$ (positive) $\implies \lim_{x \to 2^+} \frac{1}{x-2} = +\infty$
* **中文详解:** 当 $x$ 从左侧趋近于 2 时，$x-2$ 为负微小量，倒数为 $-\infty$；当 $x$ 从右侧趋近于 2 时，$x-2$ 为正微小量，倒数为 $+\infty$。

##### 【课件例题 4】复杂分式的单侧无穷极限

**Problem:** Evaluate $\lim_{x \to 2^+} \frac{x+1}{(x-3)(x-2)}$.
* **Process (解题步骤):**
As $x \to 2^+$, evaluate each factor:
$x + 1 \to 3 > 0$
$x - 3 \to -1 < 0$
$x - 2 \to 0^+ > 0$
Denominator $(x-3)(x-2) \to (-1)(0^+) = 0^-$ (negative close to zero)
$$\lim_{x \to 2^+} \frac{x+1}{(x-3)(x-2)} = \frac{3}{0^-} = -\infty$$
* **中文详解:** 逐项分析趋势：分子趋于正数 3，分母第一项趋于 $-1$，第二项趋于正微小量 $0^+$，故分母整体为负微小量 $0^-$。正数除以负微小量，结果为 $-\infty$。

---

#### 4. 渐近线 (Horizontal and Vertical Asymptotes)

* **垂直渐近线 (Vertical Asymptote, VA):**
* 若直线 $x = c$ 满足 $\lim_{x \to c^+} f(x) = \pm\infty$ 或 $\lim_{x \to c^-} f(x) = \pm\infty$ 中至少一条，则 $x = c$ 为曲线 $y = f(x)$ 的垂直渐近线。
* *寻找方法*：通常出现在分式函数分母为 0 但分子不为 0 的点。
* **水平渐近线 (Horizontal Asymptote, HA):**
* 若直线 $y = b$ 满足 $\lim_{x \to \infty} f(x) = b$ 或 $\lim_{x \to -\infty} f(x) = b$，则 $y = b$ 为曲线 $y = f(x)$ 的水平渐近线。

---

#### 🌟 课件例题与详解 (Lecture Examples & Solutions)

##### 【课件例题 5】有理函数的渐近线全解

**Problem:** Find all vertical and horizontal asymptotes of $f(x) = \frac{2x}{x-1}$.
* **Process (解题步骤):**
1. Vertical Asymptote:
 Denominator is zero at $x = 1$.
 $\lim_{x \to 1^+} \frac{2x}{x-1} = +\infty$ and $\lim_{x \to 1^-} \frac{2x}{x-1} = -\infty$.
 So $x = 1$ is a vertical asymptote.
2. Horizontal Asymptote:
 $\lim_{x \to \infty} \frac{2x}{x-1} = \lim_{x \to \infty} \frac{2}{1 - \frac{1}{x}} = 2$.
 $\lim_{x \to -\infty} \frac{2x}{x-1} = 2$.
 So $y = 2$ is a horizontal asymptote.
* **中文详解:** 
* 垂直渐近线：令分母为零得候选点 $x=1$，验证左右极限趋于无穷，确认 $x=1$ 为 VA。
* 水平渐近线：计算 $x \to \pm\infty$ 时的极限均等于 2，确认 $y=2$ 为 HA。

##### 【课件例题 6】反正切函数的渐近线

**Problem:** Find the asymptotes of $y = \arctan x$.
* **Process (解题步骤):**
$\lim_{x \to \infty} \arctan x = \frac{\pi}{2}$
$\lim_{x \to -\infty} \arctan x = -\frac{\pi}{2}$
Horizontal Asymptotes: $y = \frac{\pi}{2}$ and $y = -\frac{\pi}{2}$.
Vertical Asymptotes: None (since $\arctan x$ is defined and continuous on $\mathbb{R}$).
* **中文详解:** $y = \arctan x$ 定义域为全实数，无垂直渐近线；在正负无穷处的极限分别为 $\frac{\pi}{2}$ 与 $-\frac{\pi}{2}$，故有两条水平渐近线。

---

---

### 2.5 Limits Involving Trigonometric Functions (包含三角函数的极限)

#### 1. 三角函数的直接代入定理 (Substitution Theorem)

* **定理内容 (Theorem):** 对其定义域内任意实数 $c$，三角函数均满足直接代入法：
$$\lim_{t \to c} \sin t = \sin c, \quad \lim_{t \to c} \cos t = \cos c, \quad \lim_{t \to c} \tan t = \tan c 	等$$

##### 【课件例题 7】三角函数直接代入

**Problem:** Evaluate $\lim_{t \to 0} \frac{t^2 \cos t}{t+1}$.

* **Process:** $\lim_{t \to 0} \frac{t^2 \cos t}{t+1} = \frac{0^2 \cdot \cos 0}{0 + 1} = \frac{0 \cdot 1}{1} = 0$.
* **中文详解:** 分母在 $t=0$ 处等于 1 不为零，直接代入 $t=0$ 即可算出极限为 0。

---

#### 2. 第一重要极限与延伸公式 (The First Important Limit)

* **核心定理 (Theorem B1):**
$$\lim_{t \to 0} \frac{\sin t}{t} = 1$$
* **延伸公式 (Special Limits):**
$$\lim_{t \to 0} \frac{1-\cos t}{t} = 0, \quad \lim_{t \to 0} \frac{1-\cos t}{t^2} = \frac{1}{2}, \quad \lim_{t \to 0} \frac{\tan t}{t} = 1$$

---

#### 🌟 课件核心证明与详解 (Lecture Proofs)

##### 【课件证明 1】第一重要极限的几何夹逼证明

**Proof Idea (证明逻辑):**
1. 在单位圆中，比较扇形与三角形面积关系：
$$	area(	sector OBC) \le 	area(\Delta OBP) \le 	area(	sector OAP)$$
2. 代入面积公式：
$$\frac{1}{2} \cos^2 t |t| \le \frac{1}{2} \cos t |\sin t| \le \frac{1}{2} |t|$$
3. 同除以 $\frac{1}{2} |t| \cos t$，得到缩放不等式：
$$\cos t \le \frac{\sin t}{t} \le \frac{1}{\cos t}$$
4. 当 $t \to 0$ 时，两端极限 $\lim_{t \to 0} \cos t = 1$ 且 $\lim_{t \to 0} \frac{1}{\cos t} = 1$。
5. 由**夹逼定理 (Squeeze Theorem)**，证明得 $\lim_{t \to 0} \frac{\sin t}{t} = 1$。

##### 【课件证明 2】$\lim_{t \to 0} \frac{1-\cos t}{t} = 0$ 的代数化简

**Proof (证明步骤):**
$$\lim_{t \to 0} \frac{1-\cos t}{t} = \lim_{t \to 0} \frac{(1-\cos t)(1+\cos t)}{t(1+\cos t)} = \lim_{t \to 0} \frac{1-\cos^2 t}{t(1+\cos t)} = \lim_{t \to 0} \frac{\sin^2 t}{t(1+\cos t)}$$
$$= \left(\lim_{t \to 0} \frac{\sin t}{t}\right) \cdot \left(\lim_{t \to 0} \frac{\sin t}{1+\cos t}\right) = 1 \cdot \frac{0}{1+1} = 0$$

---

#### 3. 夹逼定理与有界函数性质在三角极限中的应用

##### 【课件例题 8】$x \to 0$ 时的振荡夹逼

**Problem:** Find $\lim_{x \to 0} x \cos\left(\frac{1}{x}\right)$.
* **Process (解题步骤):**
Since $-1 \le \cos\left(\frac{1}{x}\right) \le 1$ for all $x \neq 0$:
$$-|x| \le x \cos\left(\frac{1}{x}\right) \le |x|$$
Since $\lim_{x \to 0} (-|x|) = 0$ and $\lim_{x \to 0} |x| = 0$:
By the Squeeze Theorem, $\lim_{x \to 0} x \cos\left(\frac{1}{x}\right) = 0$.
* **中文详解:** 余弦函数是有界的（介于 $-1$ 和 $1$ 之间），乘以趋于 0 的因子 $x$ 后，由夹逼定理可知极限为 0。

##### 【课件例题 9】$x \to \infty$ 时的正弦衰减

**Problem:** Find $\lim_{x \to \infty} \frac{\sin x}{x}$.
* **Process (解题步骤):**
For $x > 0$, since $-1 \le \sin x \le 1$:
$$-\frac{1}{x} \le \frac{\sin x}{x} \le \frac{1}{x}$$
Since $\lim_{x \to \infty} \left(-\frac{1}{x}\right) = 0$ and $\lim_{x \to \infty} \frac{1}{x} = 0$:
By the Squeeze Theorem, $\lim_{x \to \infty} \frac{\sin x}{x} = 0$.
* **中文详解:** 正弦函数分子在 $[-1, 1]$ 振荡，而分母趋于 $+\infty$。建立夹逼不等式，两端极限均为 0，故原极限为 0。

##### 【课件例题 10】$y = \frac{\sin x}{x}$ 的渐近线避坑分析

**Problem:** Find all asymptotes of $y = \frac{\sin x}{x}$.
* **Process (解析):**
* Horizontal Asymptote: $\lim_{x \to \pm\infty} \frac{\sin x}{x} = 0 \implies y = 0$ (the $x$-axis) is a horizontal asymptote.
* Vertical Asymptote: At $x = 0$, $\lim_{x \to 0} \frac{\sin x}{x} = 1 \neq \pm\infty$.
* Conclusion: $x = 0$ is **NOT** a vertical asymptote! There are NO vertical asymptotes.
* **中文详解（避坑重点）:** 虽然 $x=0$ 使分母为零，但因为 $\lim_{x \to 0} \frac{\sin x}{x} = 1$（是一个有限常数而非无穷大），所以 $x=0$ 只是可去间断点，**绝不是**垂直渐近线！该函数只有 $y=0$ 一条水平渐近线。

---

#### 4. 关键推论：无穷小量乘有界函数定理 (Infinitesimal × Bounded Function)

* **推论 (Corollary):** 若 $\lim_{x \to c} f(x) = 0$（即 $f(x)$ 为无穷小量），且函数 $g(x)$ 在 $c$ 的去心邻域内**有界**（ bounded, 即存在 $M > 0$ 使 $|g(x)| \le M$），则：
$$\lim_{x \to c} f(x) g(x) = 0$$
