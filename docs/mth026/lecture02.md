# Chapter 2 Limits: 极限概念与极限运算法则 知识详解与例题精解

## 第一部分：本节课知识详解 (Lecture 2 Summary)

---

### 2.1 Introduction to Limits (极限引论与直观概念)

#### 1. 引出极限概念的三大经典问题 (Motivation for Limits)

在物理、工程与数学中，许多量无法仅通过有限次代数运算求得，而必须通过研究无限变化过程的演变趋势来确定：
* **瞬时速度问题 (Instantaneous Velocity):** 
* 在时间区间 $[c, c+h]$ 内，物体的平均速度 (**average velocity**) 为 $v_{\text{avg}} = \frac{s(c+h) - s(c)}{h}$。
* 当时间间隔长度 $h \to 0$ 时，平均速度的极限即为 $t = c$ 时刻的**瞬时速度** (**instantaneous velocity**):
    $$v(c) = \lim_{h \to 0} \frac{s(c+h) - s(c)}{h}$$
* 瞬时速度的概念直接引出了微积分的核心工具——**导数** (**Derivative**)。
* **圆面积逼近问题 (Area of a Circle):** 圆的面积是当内接正多边形 (**inscribed regular polygon**) 的边数 $n \to \infty$ 时，其面积的极限。
* **曲线弧长问题 (Arc Length of a Curve):** 曲线的精确长度是用多段连续直线段 (折线段) 逼近，当分段数量 $n \to \infty$ 时的极限值。
* **思想精髓:** 极限方法实现了“从有限到无限”、“从静态到动态”、“从近似到精确”的伟大飞跃。

#### 2. 函数极限的直观定义 (Intuitive Definition of Limits)

* **符号表示与读法:** 
$$\lim_{x \to c} f(x) = L$$
读作：“*The limit of $f(x)$ as $x$ approaches $c$ is $L$*”（当 $x$ 趋近于 $c$ 时，$f(x)$ 的极限是 $L$）。
* **双重耦合运动 (Two Coupled Motions):** 
1. 自变量 $x$ 越来越接近 $c$（但保持 $x \neq c$）；
2. 这一过程“迫使”因变量 $f(x)$ 越来越接近某一个确定的常数 $L$。
* **核心铁律 (Key Principle):** 
* **$f(c)$ 的取值完全无关 (The value at $c$ is irrelevant):** 极限完全取决于 $f(x)$ 在 $c$ 点**去心邻域** (**punctured neighborhood**) 上的局部行为。
* **极限值 $\neq$ 函数值 (Limit $\neq$ Function Value):** 即使 $f(c)$ 未定义（例如分母为0）或者 $f(c) \neq L$，极限 $\lim_{x \to c} f(x) = L$ 依然可以完美存在。

#### 3. 极限不存在 (Does Not Exist, DNE) 的三种典型情形

当 $x \to c$ 时，若 $f(x)$ 无法逼近某**单一有限常数** $L$，则称极限不存在 (DNE):
* **情形 1: 趋于无穷/无界 (Unboundedness / Infinity):** 
* 例如 $\lim_{x \to 0} \frac{1}{x^2} = \infty$。由于 $\frac{1}{x^2}$ 不趋向于任何有限实数，因此在实常数范围内其极限不存在 (DNE)。
* **情形 2: 存在跳跃/左右极限不相等 (Jump Discontinuity):** 
* 例如最大整数函数 (**greatest integer function**, 记作 $[x]$ 或 $[\![x]\!]$): 当 $x \to 2^-$ 时，$[\![x]\!] = 1$；当 $x \to 2^+$ 时，$[\![x]\!] = 2$。因左右两端趋近的值不同，$[\![x]\!]$ 不存在。
* **情形 3: 无限剧烈震荡 (Infinite Oscillation):** 
* 例如 $\lim_{x \to 0} \sin\left(\frac{1}{x}\right)$。在原点附近的任意小邻域内，$\sin(1/x)$ 都会在 $-1$ 与 $1$ 之间无限次震荡，无法固定靠近某单一数值。

#### 4. 单侧极限 (One-Sided Limits)

* **右极限 (Right-Hand Limit):** $\lim_{x \to c^+} f(x) = L$（当 $x$ 从 $c$ 的右侧/大于 $c$ 的方向趋向于 $c$ 时）。
* **左极限 (Left-Hand Limit):** $\lim_{x \to c^-} f(x) = L$（当 $x$ 从 $c$ 的左侧/小于 $c$ 的方向趋向于 $c$ 时）。
* **双侧极限存在充要条件 (Theorem A):**
$$\lim_{x \to c} f(x) = L \iff \lim_{x \to c^-} f(x) = L \text{ and } \lim_{x \to c^+} f(x) = L$$
即：双侧极限存在的**充要条件**是左极限与右极限同时存在且相等。

#### 5. 数值计算与计算器的陷阱 (Calculator Pitfalls)

仅凭计算器代入小数值生成表格可能会因浮点数舍入误差 (**rounding error**) 导致错误结论（例如计算 $\lim_{x \to 0} (x^2 - 0.0001 \cos x)$ 时，若精度不足易误判为 $0$，而正确代数计算结果为 $-0.0001$）。因此，必须依靠严谨的代数定理进行推导。

---

---

### 2.3 Limit Theorems (极限定理与计算法则)

#### 1. 基本极限定理 (Basic Limits)

* **常数函数极限 (Constant Function):** $\lim_{x \to c} k = k$
* **恒等函数极限 (Identity Function):** $\lim_{x \to c} x = c$

#### 2. 主极限定理 (Main Limit Theorem / Theorem 2.3A)

设 $n$ 为正整数，$k$ 为常数，且极限 $\lim_{x \to c} f(x)$ 与 $\lim_{x \to c} g(x)$ 均存在，则：
1.  **常数倍法则 (Constant Multiple Rule):** $\lim_{x \to c} [k f(x)] = k \lim_{x \to c} f(x)$
2.  **加法与减法法则 (Sum & Difference Rule):** $\lim_{x \to c} [f(x) \pm g(x)] = \lim_{x \to c} f(x) \pm \lim_{x \to c} g(x)$
3.  **乘法法则 (Product Rule):** $\lim_{x \to c} [f(x) \cdot g(x)] = [\lim_{x \to c} f(x)] \cdot [\lim_{x \to c} g(x)]$
4.  **除法法则 (Quotient Rule):** $\lim_{x \to c} \frac{f(x)}{g(x)} = \frac{\lim_{x \to c} f(x)}{\lim_{x \to c} g(x)}$，前提是 $\lim_{x \to c} g(x) \neq 0$
5.  **乘方法则 (Power Rule):** $\lim_{x \to c} [f(x)]^n = [\lim_{x \to c} f(x)]^n$
6.  **开方法则 (Root Rule):** $\lim_{x \to c} \sqrt[n]{f(x)} = \sqrt[n]{\lim_{x \to c} f(x)}$（当 $n$ 为偶数时，要求 $\lim_{x \to c} f(x) > 0$）

#### 3. 直接代入定理 (Substitution Theorem / Theorem 2.3B)

* 若 $f$ 为**多项式函数** (**Polynomial Function**) 或**有理函数** (**Rational Function**)，且 $f(c)$ 在实数域上有定义（对于有理函数即分母在 $c$ 处不为 0），则：
$$\lim_{x \to c} f(x) = f(c)$$

#### 4. 未定式 $0/0$ 与因子消去法 (Indeterminate Form $0/0$ & Theorem 2.3C)

* **消去定理 (Theorem 2.3C):** 若在包含 $c$ 的某个去心开区间内，$f(x) = g(x)$ 对所有 $x \neq c$ 成立，且 $\lim_{x \to c} g(x)$ 存在，则：
$$\lim_{x \to c} f(x) = \lim_{x \to c} g(x)$$
* **解题核心套路 (Key Strategy for $0/0$ Form):** 
直接代入出现 $0/0$ 时，必须先利用**因式分解** (**Factoring**)、**分子/分母有理化** (**Rationalization**) 或**通分**等代数手段，约去导致分子分母同时为零的公因子 $(x-c)$，再代入求极限。

#### 5. 极限的保号性 (Sign-Preserving Property)

* 若 $\lim_{x \to c} f(x) = L > 0$（或 $< 0$），则在 $c$ 点的某个充分小的去心邻域内，函数值 $f(x)$ 必严格大于 0（或小于 0）。

#### 6. 夹逼定理 / 三明治定理 (Squeeze Theorem / Theorem 2.3D)

* **定理内容:** 设函数 $f, g, h$ 满足在 $c$ 点的去心邻域内：
$$f(x) \le g(x) \le h(x)$$
若 $\lim_{x \to c} f(x) = \lim_{x \to c} h(x) = L$，则中间函数的极限也必为 $L$:
$$\lim_{x \to c} g(x) = L$$
* **重要应用举例:** 已知 $1 - \frac{x^2}{6} \le \frac{\sin x}{x} \le 1$ ($x \neq 0$)。
因为 $\lim_{x \to 0} \left(1 - \frac{x^2}{6}\right) = 1$ 且 $\lim_{x \to 0} 1 = 1$，由夹逼定理直接推导出重要三角极限：
$$\lim_{x \to 0} \frac{\sin x}{x} = 1$$
