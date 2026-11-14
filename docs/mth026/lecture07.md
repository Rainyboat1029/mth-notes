# Chapter 4 Applications of the Derivative: 最值、单调性与凹凸性 知识详解与例题精解

## 第一部分：本节课知识详解 (Lecture 7 Summary)

### 4.1 Maxima and Minima (函数的最大值与最小值)

#### 1. 全局最值定义 (Definition of Global Extrema)
设 $S$ 为函数 $f(x)$ 的定义域，$c \in S$：
* **全局最大值 (Maximum Value / Absolute Maximum):** 若对 $S$ 中的所有 $x$，均有 $f(c) \ge f(x)$，则称 $f(c)$ 为 $f$ 在 $S$ 上的**最大值**。
* **全局最小值 (Minimum Value / Absolute Minimum):** 若对 $S$ 中的所有 $x$，均有 $f(c) \le f(x)$，则称 $f(c)$ 为 $f$ 在 $S$ 上的**最小值**。
* **极值/最值 (Extreme Value):** 最大值与最小值的统称。
* **目标函数 (Objective Function):** 需要进行最值优化的函数。

---

#### 2. 最值存在性定理 (Max-Min Existence Theorem)
* **定理 (Theorem A):** 若函数 $f(x)$ 在**闭区间** $[a, b]$ 上**连续**，则 $f(x)$ 在该区间上必能取得全局最大值与全局最小值。
* **解析要点 (Key Insights):**
  * 条件缺一不可：定义域必须是**闭区间**且函数必须**连续**。
  * 若在开区间或包含间断点，最值可能不存在（例如 $f(x) = \frac{1}{x}$ 在 $(0, \infty)$ 上无最值）。

---

#### 3. 临界点定义与分类 (Critical Points)
根据**临界点定理 (Critical Point Theorem / Theorem B)**，连续函数在区间 $I$ 上的最值只能在**临界点 (Critical Points)** 处取得。临界点分为以下三类：
1. **驻点 (Stationary Points):** 函数一阶导数为零的区间内部点，即 $f'(c) = 0$。
2. **奇点/不可导点 (Singular Points):** 函数一阶导数不存在的区间内部点，即 $f'(c)$ DNE。
3. **端点 (End Points):** 定义域区间的边界点（如闭区间 $[a, b]$ 的端点 $a$ 与 $b$）。

---

#### 4. 闭区间上求最值的标准套路 (Procedure for Finding Extreme Values)
对于闭区间 $[a, b]$ 上的连续函数 $f(x)$：
1. **求出所有临界点：**
   * 解方程 $f'(x) = 0$ 找出区间 $(a, b)$ 内的驻点；
   * 找出区间 $(a, b)$ 内使 $f'(x)$ 不存在的奇点；
   * 记录端点 $a, b$。
2. **计算临界点处的函数值：** 求出 $f(x)$ 在所有临界点处的函数值。
3. **数值比较：** 其中最大的函数值为**全局最大值**，最小的函数值为**全局最小值**。

---

#### 🌟 课件例题与详解 (Lecture Examples & Solutions)

##### 【课件例题 1】求解三次多项式在闭区间上的最值
**Problem:** Find the critical points, maximum and minimum values of $f(x) = -2x^3 + 3x^2$ on $\left[-\frac{1}{2}, 2\right]$.
* **Process (解题步骤):**
  1. Find critical points:
     End points: $x = -\frac{1}{2}$ and $x = 2$.
     Find stationary points by solving $f'(x) = 0$:
     $$f'(x) = -6x^2 + 6x = -6x(x-1) = 0 \implies x = 0 \quad \text{or} \quad x = 1$$
     Both $0, 1 \in \left(-\frac{1}{2}, 2\right)$.
     Singular points: None (polynomial is differentiable everywhere).
     Critical points list: $x = -\frac{1}{2}, 0, 1, 2$.
  2. Evaluate $f(x)$ at each critical point:
     $$f\left(-\frac{1}{2}\right) = -2\left(-\frac{1}{8}\right) + 3\left(\frac{1}{4}\right) = \frac{1}{4} + \frac{3}{4} = 1$$
     $$f(0) = -2(0)^3 + 3(0)^2 = 0$$
     $$f(1) = -2(1)^3 + 3(1)^2 = 1$$
     $$f(2) = -2(8) + 3(4) = -16 + 12 = -4$$
  3. Compare values:
     The maximum value is $1$ (attained at $x = -\frac{1}{2}$ and $x = 1$).
     The minimum value is $-4$ (attained at $x = 2$).
* **中文详解:** 
  求导得 $f'(x) = -6x(x-1)$，令其为零求得驻点 $x=0, 1$；加上端点 $x=-1/2, 2$，共 4 个临界点。分别算出函数值为 $1, 0, 1, -4$，比较后得出最大值为 1（在 $x=-1/2$ 与 $x=1$ 处取得），最小值为 $-4$（在 $x=2$ 处取得）。

##### 【课件例题 2】包含奇点（不可导点）的函数最值
**Problem:** Find the maximum and minimum values of $F(x) = x^{2/3}$ on $[-1, 2]$.
* **Process (解题步骤):**
  1. Find derivative:
     $$F'(x) = \frac{2}{3}x^{-1/3} = \frac{2}{3\sqrt[3]{x}}$$
  2. Identify critical points:
     End points: $x = -1$ and $x = 2$.
     Stationary points: $F'(x) = 0$ has no solution.
     Singular point: $F'(0)$ is undefined (denominator is zero at $x = 0 \in (-1, 2)$).
     Critical points list: $x = -1, 0, 2$.
  3. Evaluate $F(x)$ at critical points:
     $$F(-1) = (-1)^{2/3} = 1$$
     $$F(0) = 0^{2/3} = 0$$
     $$F(2) = 2^{2/3} = \sqrt[3]{4} \approx 1.5874$$
  4. Conclusion:
     The maximum value is $\sqrt[3]{4}$ (at $x = 2$).
     The minimum value is $0$ (at $x = 0$).
* **中文详解:** 
  $x=0$ 处一阶导数分母为零使得 $F'(0)$ 不存在，因此 $x=0$ 是奇点（尖点）。将奇点 $x=0$ 与端点 $x=-1, 2$ 计算比较，可得最大值为 $\sqrt[3]{4}$，最小值为 0。

---

### 4.2 Monotonicity and Concavity (函数的单调性与凹凸性)

#### 1. 单调性与一阶导数 (Monotonicity & First Derivative)
* **单调性定理 (Monotonicity Theorem / Theorem A):** 设 $f$ 在区间 $I$ 上连续，且在 $I$ 的内部可导：
  1. 若对 $I$ 内部的所有 $x$，均有 $f'(x) > 0$，则 $f(x)$ 在 $I$ 上**单调递增 (Increasing)**。
  2. 若对 $I$ 内部的所有 $x$，均有 $f'(x) < 0$，则 $f(x)$ 在 $I$ 上**单调递减 (Decreasing)**。
* **补充说明 (Isolated Zeros):** 若 $f'(x) \ge 0$ 且等于 0 的点仅为**孤立零点**（如 $y = x - \sin x$ 导数为 $1 - \cos x \ge 0$），函数依然在整体区间上严格单调递增。

---

#### 2. 凹凸性与二阶导数 (Concavity & Second Derivative)
* **定义 (Definition):** 设 $f$ 在区间 $I$ 上可导：
  * **凹向上 (Concave Up, CU):** 若切线斜率 $f'(x)$ 在 $I$ 上单调递增（即曲线位于切线上方），称 $f$ 凹向上。
  * **凹向下 (Concave Down, CD):** 若切线斜率 $f'(x)$ 在 $I$ 上单调递减（即曲线位于切线下方），称 $f$ 凹向下。
* **凹凸性定理 (Concavity Theorem / Theorem B):** 设 $f$ 在区间 $I$ 上二阶可导：
  1. 若对 $I$ 内部的所有 $x$，均有 $f''(x) > 0$，则 $f(x)$ 在 $I$ 上**凹向上 (CU)**。
  2. 若对 $I$ 内部的所有 $x$，均有 $f''(x) < 0$，则 $f(x)$ 在 $I$ 上**凹向下 (CD)**。

---

#### 3. 拐点 (Inflection Points)
* **定义 (Definition):** 设 $f(x)$ 在 $c$ 处连续，若点 $(c, f(c))$ 左右两侧的凹凸性发生改变（从凹向上变为凹向下，或从凹向下变为凹向上），则称 $(c, f(c))$ 为 $f(x)$ 的**拐点 (Inflection Point)**。
* **寻找拐点候选点:** 解方程 $f''(x) = 0$ 或找出使 $f''(x)$ 不存在的点，再通过符号分析验证其左右两侧二阶导数是否变号。

---

#### 🌟 课件例题与详解 (Lecture Examples & Solutions)

##### 【课件例题 3】一阶导数孤立零点与单调性
**Problem:** Determine whether $g(x) = x - \sin x$ is increasing on $[0, \infty)$.
* **Process (解题步骤):**
  1. Compute the first derivative:
     $$g'(x) = 1 - \cos x$$
  2. Analyze the sign of $g'(x)$:
     Since $-1 \le \cos x \le 1$ for all $x$, we have $g'(x) = 1 - \cos x \ge 0$.
     $g'(x) = 0 \iff \cos x = 1 \iff x = 2k\pi \quad (k \in \mathbb{Z})$.
  3. Conclusion:
     The derivative is strictly positive except at isolated points $x = 0, 2\pi, 4\pi, \dots$. Therefore, by the extended Monotonicity Theorem, $g(x)$ is strictly increasing on $[0, \infty)$.
* **中文详解:** 
  一阶导数 $g'(x) = 1 - \cos x \ge 0$ 恒成立，仅在 $2k\pi$ 等孤立点处等于 0，不破坏整体单调性，因此函数在 $[0, \infty)$ 上单调递增。

##### 【课件例题 4】多项式函数的单调区间
**Problem:** Find where $f(x) = 2x^3 - 3x^2 - 12x + 7$ is increasing and where it is decreasing.
* **Process (解题步骤):**
  1. Find $f'(x)$ and factor:
     $$f'(x) = 6x^2 - 6x - 12 = 6(x^2 - x - 2) = 6(x+1)(x-2)$$
  2. Set up sign intervals with critical points $x = -1$ and $x = 2$:
     * On $(-\infty, -1)$: $x+1 < 0, x-2 < 0 \implies f'(x) > 0 \implies$ Increasing.
     * On $(-1, 2)$: $x+1 > 0, x-2 < 0 \implies f'(x) < 0 \implies$ Decreasing.
     * On $(2, \infty)$: $x+1 > 0, x-2 > 0 \implies f'(x) > 0 \implies$ Increasing.
  3. Conclusion:
     $f(x)$ is increasing on $(-\infty, -1]$ and $[2, \infty)$; decreasing on $[-1, 2]$.
* **中文详解:** 
  通过因式分解得到 $f'(x) = 6(x+1)(x-2)$，判断导数符号：在 $(-\infty, -1]$ 与 $[2, \infty)$ 上 $f'(x) \ge 0$ 为增区间；在 $[-1, 2]$ 上 $f'(x) \le 0$ 为减区间。

##### 【课件例题 5】有理函数的单调区间
**Problem:** Determine where $g(x) = \frac{x}{1+x^2}$ is increasing and where it is decreasing.
* **Process (解题步骤):**
  1. Compute $g'(x)$ using the quotient rule:
     $$g'(x) = \frac{1 \cdot (1+x^2) - x \cdot 2x}{(1+x^2)^2} = \frac{1 - x^2}{(1+x^2)^2} = \frac{(1+x)(1-x)}{(1+x^2)^2}$$
  2. Since denominator $(1+x^2)^2 > 0$ for all $x$, the sign of $g'(x)$ depends on $(1+x)(1-x)$:
     * $g'(x) > 0 \iff 1 - x^2 > 0 \iff -1 < x < 1 \implies$ Increasing on $[-1, 1]$.
     * $g'(x) < 0 \iff 1 - x^2 < 0 \iff x < -1 \text{ or } x > 1 \implies$ Decreasing on $(-\infty, -1]$ and $[1, \infty)$.
* **中文详解:** 
  利用商法则求导，分母恒正，分子为 $1-x^2$。因此在区间 $[-1, 1]$ 上 $g'(x) \ge 0$ 单调递增；在 $(-\infty, -1]$ 与 $[1, \infty)$ 上 $g'(x) \le 0$ 单调递减。

##### 【课件例题 6】奇点处的拐点判定
**Problem:** Find all points of inflection of $F(x) = x^{1/3} + 2$.
* **Process (解题步骤):**
  1. Compute first and second derivatives:
     $$F'(x) = \frac{1}{3}x^{-2/3} = \frac{1}{3\sqrt[3]{x^2}}$$
     $$F''(x) = -\frac{2}{9}x^{-5/3} = -\frac{2}{9\sqrt[3]{x^5}}$$
  2. Analyze candidates for inflection points:
     $F''(x) = 0$ has no solution.
     $F''(x)$ is undefined at $x = 0$.
  3. Check sign changes of $F''(x)$ around $x = 0$:
     * For $x < 0$: $x^5 < 0 \implies \sqrt[3]{x^5} < 0 \implies F''(x) = -\frac{2}{9(-)} > 0 \implies$ Concave Up.
     * For $x > 0$: $x^5 > 0 \implies \sqrt[3]{x^5} > 0 \implies F''(x) = -\frac{2}{9(+)} < 0 \implies$ Concave Down.
  4. Conclusion:
     Since $F(x)$ is continuous at $x = 0$ and concavity changes from CU to CD, $(0, F(0)) = (0, 2)$ is an inflection point.
* **中文详解:** 
  二阶导数在 $x=0$ 处不存在。当 $x<0$ 时 $F''(x) > 0$（凹向上），当 $x>0$ 时 $F''(x) < 0$（凹向下）。二阶导数在 $x=0$ 左右变号且函数在此点连续，故 $(0, 2)$ 是拐点。

##### 【课件例题 7】综合分析单调性、凹凸性与拐点
**Problem:** Analyze $f(x) = \frac{1}{3}x^3 - x^2 - 3x + 4$ for monotonicity, concavity, and inflection points.
* **Process (解题步骤):**
  1. Compute derivatives:
     $$f'(x) = x^2 - 2x - 3 = (x+1)(x-3)$$
     $$f''(x) = 2x - 2 = 2(x-1)$$
  2. Set up summary table:
     * $f'(x) = 0 \implies x = -1, 3$ (Stationary points)
     * $f''(x) = 0 \implies x = 1$ (Inflection point candidate)

  | Interval / Point | $(-\infty, -1)$ | $x = -1$ | $x \in (-1, 1)$ | $x = 1$ | $x \in (1, 3)$ | $x = 3$ | $(3, \infty)$ |
  | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
  | **$f'(x)$** | $+$ | $0$ | $-$ | $-$ | $-$ | $0$ | $+$ |
  | **$f''(x)$** | $-$ | $-$ | $-$ | $0$ | $+$ | $+$ | $+$ |
  | **Behavior** | Inc, CD | Local Max | Dec, CD | Inflection Pt | Dec, CU | Local Min | Inc, CU |

  3. Conclusion:
     * Increasing on $(-\infty, -1]$ and $[3, \infty)$; Decreasing on $[-1, 3]$.
     * Concave Down on $(-\infty, 1)$; Concave Up on $(1, \infty)$.
     * Inflection Point: $\left(1, f(1)\right) = \left(1, \frac{1}{3} - 1 - 3 + 4\right) = \left(1, \frac{1}{3}\right)$.
* **中文详解:** 
  求得一阶导数零点为 $-1, 3$，二阶导数零点为 $1$。列表综合分析可知：在 $(-\infty, -1]$ 和 $[3, \infty)$ 递增，在 $[-1, 3]$ 递减；在 $(-\infty, 1)$ 凹向下，在 $(1, \infty)$ 凹向上；拐点坐标为 $\left(1, \frac{1}{3}\right)$。
