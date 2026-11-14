# Chapter 4 Applications of the Derivative: 局部极值、优化问题与函数作图 知识详解与例题精解

## 第一部分：本节课知识详解 (Lecture 8 Summary)

### 4.3 Local Extrema and Extrema on Open Intervals (局部极值与开区间上的最值)

#### 1. 局部极值的定义 (Definition of Local Extrema)

设 $S$ 为函数 $f$ 的定义域，且 $c \in S$：

* **局部最大值 (Local Maximum Value):** 若存在包含 $c$ 的开区间 $(a,b)$，使得对 $(a,b) \cap S$ 中的所有 $x$ 都有 $f(c) \ge f(x)$，则称 $f(c)$ 为 $f$ 的一个局部最大值。
* **局部最小值 (Local Minimum Value):** 若存在包含 $c$ 的开区间 $(a,b)$，使得对 $(a,b) \cap S$ 中的所有 $x$ 都有 $f(c) \le f(x)$，则称 $f(c)$ 为 $f$ 的一个局部最小值。
* **局部极值 (Local Extreme Value):** 局部最大值与局部最小值的统称。
* **全局最值 (Global Maximum / Minimum Value):** 函数在集合 $S$ 上的最大值（若存在）称为全局最大值，最小值称为全局最小值。
* **两者关系 (Relationship):** 全局最大值一定是局部最大值，全局最小值一定是局部最小值；反过来不成立——局部极值可能不止一个，且可能都不是全局最值。
* **端点处的局部极值:** 若定义域区间 $I$ 的端点属于 $S$，端点处也可能取得局部极值（此时只与端点单侧邻近的点比较）。

#### 2. 局部极值可能出现的位置 (Where Do Local Extreme Values Occur?)

* **临界点定理 (Critical Point Theorem / Theorem 4.1B):** 设 $f$ 在包含点 $c$ 的区间 $I$ 上有定义。若 $f(c)$ 是极值，则 $c$ 必为**临界点 (critical point)**，即满足下列三者之一：

  1. $c$ 是区间 $I$ 的**端点 (end point)**；
  2. $c$ 是**驻点 (stationary point)**，即 $f'(c)=0$；
  3. $c$ 是**奇点 (singular point)**，即 $f'(c)$ 不存在。

* **Remark (要点):** 局部极值点只能从“端点、驻点、奇点”这三类临界点中产生；但临界点**不一定**是极值点（例如 $f(x)=x^3$ 在 $x=0$ 处 $f'(0)=0$，却没有极值）。因此找到临界点后，还必须用一阶或二阶导数判别法确认。

#### 3. 一阶导数判别法 (First Derivative Test / Theorem A)

设 $f$ 在包含驻点或奇点 $c$ 的开区间 $(a,b)$ 上连续（$c$ 可在 $(a,b)$ 内，也可为端点）：

1. 若在 $(a,c)$ 上 $f'(x)>0$，在 $(c,b)$ 上 $f'(x)<0$，即 $f'$ 由正变负，则 $f(c)$ 为**局部最大值**；
2. 若在 $(a,c)$ 上 $f'(x)<0$，在 $(c,b)$ 上 $f'(x)>0$，即 $f'$ 由负变正，则 $f(c)$ 为**局部最小值**；
3. 若 $f'(x)$ 在 $c$ 两侧保持同号，则 $f(c)$ **不是**局部极值。

* **记忆口诀:** 左正右负得极大，左负右正得极小，两侧同号无极值。
* **符号表 (Sign Chart):** 在数轴上标出全部临界点，在每个区间内取一个测试点判断 $f'$ 的符号，再按“$+ \to -$ 极大、$- \to +$ 极小、同号无极值”读出结论。

#### 🌟 课件例题与详解 (Lecture Examples & Solutions)

##### 【课件例题 1】用一阶导数判别法求局部极值

**Problem:** Find the local extreme values of $f(x)=\dfrac{1}{3}x^3-x^2-3x+4$ on $(-\infty,\infty)$.

* **Process (解题步骤):**
  1. Compute the derivative:
     $$f'(x)=x^2-2x-3=(x-3)(x+1)$$
  2. Find the critical points: $f'(x)=0 \implies x=-1,\ 3$；$f'$ 处处存在，无奇点；定义域为 $\mathbb{R}$，无端点。
  3. Determine the sign of $f'(x)$ on each interval:
     * $x<-1$：$f'(x)=(-)(-)=+$；
     * $-1<x<3$：$f'(x)=(-)(+)=-$；
     * $x>3$：$f'(x)=(+)(+)=+$。
  4. Apply the First Derivative Test:
     * $f'$ 在 $x=-1$ 处由正变负 $\implies f(-1)=\dfrac{17}{3}$ 为局部最大值；
     * $f'$ 在 $x=3$ 处由负变正 $\implies f(3)=-5$ 为局部最小值。
* **中文详解:** 先求导并因式分解得到 $f'(x)=(x-3)(x+1)$，临界点为 $x=-1$ 与 $x=3$。用符号表判断：$x=-1$ 左侧导数为正、右侧为负，函数先增后减，故 $f(-1)=\frac{17}{3}$ 是局部最大值（山顶）；$x=3$ 左侧导数为负、右侧为正，函数先减后增，故 $f(3)=-5$ 是局部最小值（谷底）。注意本例中局部极大值 $17/3$ 反而大于局部极小值 $-5$，这是“局部”二字的含义——只与附近点比较。

---

##### 【课件例题 2】奇点处的局部极值

**Problem:** Find the local extreme values of $f(x)=(\sin x)^{2/3}$ on $\left(-\dfrac{\pi}{6},\dfrac{2\pi}{3}\right)$.

* **Process (解题步骤):**
  1. Differentiate using the chain rule:
     $$f'(x)=\frac{2}{3}(\sin x)^{-1/3}\cos x=\frac{2\cos x}{3\sqrt[3]{\sin x}}$$
  2. Find the critical points:
     * $x=0$ 处 $\sin 0=0$，$f'(0)$ 不存在 —— **奇点 (singular point)**；
     * $x=\dfrac{\pi}{2}$ 处 $\cos\dfrac{\pi}{2}=0$，$f'\left(\dfrac{\pi}{2}\right)=0$ —— **驻点 (stationary point)**。
  3. Determine the sign of $f'(x)$ on each subinterval:
     * $\left(-\dfrac{\pi}{6},0\right)$：$\sin x<0,\ \cos x>0 \implies f'(x)<0$；
     * $\left(0,\dfrac{\pi}{2}\right)$：$\sin x>0,\ \cos x>0 \implies f'(x)>0$；
     * $\left(\dfrac{\pi}{2},\dfrac{2\pi}{3}\right)$：$\sin x>0,\ \cos x<0 \implies f'(x)<0$。
  4. Apply the First Derivative Test:
     * $f'$ 在 $x=0$ 处由负变正 $\implies f(0)=0$ 为局部最小值；
     * $f'$ 在 $x=\dfrac{\pi}{2}$ 处由正变负 $\implies f\left(\dfrac{\pi}{2}\right)=1$ 为局部最大值。
* **中文详解:** 本题的关键在于“奇点也能是极值点”。$f'(x)=\frac{2\cos x}{3\sqrt[3]{\sin x}}$ 在 $x=0$ 处分母为零，导数不存在，但函数本身在 $x=0$ 处连续且取到最小值 $0$。符号表显示 $f'$ 在 $0$ 左右由负变正，所以 $x=0$ 是局部极小点；在 $\frac{\pi}{2}$ 处导数由正变负，是局部极大点。由于区间是开区间，这两个局部极值恰好也是该区间上的全局最小值和全局最大值。这也说明：**求极值不能只解 $f'(x)=0$，还要检查导数不存在的点**。

#### 4. 二阶导数判别法 (Second Derivative Test / Theorem B)

设 $f'$ 与 $f''$ 在包含 $c$ 的开区间 $(a,b)$ 内存在，且 $f'(c)=0$：

1. 若 $f''(c)<0$，则 $f(c)$ 为**局部最大值**；
2. 若 $f''(c)>0$，则 $f(c)$ 为**局部最小值**。

* **几何直观 (Geometric Intuition):** 在驻点处切线水平。若曲线凹向下（$f''<0$，像倒扣的碗），则驻点是山顶；若曲线凹向上（$f''>0$，像正放的碗），则驻点是谷底。
* **证明思路 (Proof Sketch):** 由二阶导数定义
  $$f''(c)=\lim_{x\to c}\frac{f'(x)-f'(c)}{x-c}=\lim_{x\to c}\frac{f'(x)}{x-c}$$
  若 $f''(c)<0$，则在 $c$ 的某去心邻域内 $\dfrac{f'(x)}{x-c}<0$：当 $x<c$ 时 $f'(x)>0$，当 $x>c$ 时 $f'(x)<0$，由一阶判别法知 $f(c)$ 为局部最大值。$f''(c)>0$ 的情形同理。
* **失效情形 (Caution):** 若 $f''(c)=0$，二阶判别法**失效**，必须回到一阶判别法。例如 $f(x)=x^3$ 与 $f(x)=x^4$ 在 $x=0$ 处都有 $f'(0)=f''(0)=0$，但前者无极值、后者取极小值。

##### 【课件例题 3】用二阶导数判别法求局部极值

**Problem:** Use the Second Derivative Test to find the local extreme values of $f(x)=\dfrac{1}{3}x^3-x^2-3x+4$.

* **Process (解题步骤):**
  1. First derivative and critical points (as in Example 1):
     $$f'(x)=x^2-2x-3=(x-3)(x+1) \implies x=-1,\ 3$$
  2. Second derivative:
     $$f''(x)=2x-2$$
  3. Evaluate $f''$ at each stationary point:
     * $f''(-1)=2(-1)-2=-4<0 \implies f(-1)=\dfrac{17}{3}$ 为局部最大值；
     * $f''(3)=2(3)-2=4>0 \implies f(3)=-5$ 为局部最小值。
* **中文详解:** 与例题 1 相比，二阶导数法只需计算驻点处的 $f''$ 符号，不必做完整的符号表，速度更快。$f''(-1)=-4<0$ 说明曲线在 $x=-1$ 附近凹向下，驻点处是山顶，故为局部极大；$f''(3)=4>0$ 说明凹向上，故为局部极小。两种判别法结论完全一致。

---

##### 【课件例题 4】二阶导数判别法失效的情形

**Problem:** Discuss the behavior of $f(x)=x^3$ and $g(x)=x^4$ at $x=0$ using the derivative tests.

* **Process (解题步骤):**
  1. For $f(x)=x^3$: $f'(x)=3x^2$, $f''(x)=6x$; $f'(0)=0$, $f''(0)=0$.
     * 一阶判别法：$f'(x)=3x^2>0$ 在 $x=0$ 两侧同号 $\implies$ $x=0$ 不是极值点（是驻点拐点）。
  2. For $g(x)=x^4$: $g'(x)=4x^3$, $g''(x)=12x^2$; $g'(0)=0$, $g''(0)=0$.
     * 一阶判别法：$g'$ 在 $x=0$ 左侧为负、右侧为正 $\implies g(0)=0$ 为局部最小值。
  3. Conclusion: $f''(0)=0$ 时二阶判别法不能下结论，必须用一阶判别法（或更高阶导数）继续判断。
* **中文详解:** 两个函数在 $x=0$ 处都满足 $f'(0)=0$ 且 $f''(0)=0$，但 $x^3$ 在原点两侧都单调递增（导数恒非负），故原点不是极值点；$x^4$ 在原点两侧先减后增，取到最小值 $0$。这说明 **$f''(c)=0$ 只是“判别法失效”，不是“没有极值”**，考试中遇到这种点一定要回到一阶导数符号表。

#### 5. 开区间上的全局最值 (Global Extrema on Open Intervals)

* **存在性 (Existence):** 连续函数在**开区间**上不一定能取到最大值或最小值。例如 $f(x)=\dfrac{1}{x}$ 在 $(0,\infty)$ 上既无最大值也无最小值；又如 $f(x)=x$ 在 $(0,1)$ 上无最值。
* **分析思路 (Strategy):** 先用一阶导数确定单调区间与局部极值，再考察区间端点处的**单侧极限**，判断函数值是否能“逼近但取不到”某个值。
* **推论 (Corollary):** 若 $f$ 在开区间上可导，且该区间内**只有一个驻点** $c$，并且 $c$ 是局部极值点，则 $c$ 必为全局极值点。
  * “单峰” (single-peak) 情形 $\implies$ 全局最大值；
  * “单谷” (single-valley) 情形 $\implies$ 全局最小值。
* **注意 (Caution):** 推论要求“唯一驻点 **且** 该点确为局部极值”。仅有唯一驻点不够：$f(x)=x^3$ 在 $\mathbb{R}$ 上唯一驻点为 $0$，但 $0$ 不是极值点，函数也没有全局最值。

##### 【课件例题 5】开区间上的全局最值（高斯型函数）

**Problem:** Find the global maximum and minimum values of $f(x)=e^{-x^2/2}$ on $(-\infty,\infty)$, if they exist.

* **Process (解题步骤):**
  1. Differentiate:
     $$f'(x)=-x\,e^{-x^2/2}$$
     因 $e^{-x^2/2}>0$ 恒成立，故 $f'(x)=0 \iff x=0$。
  2. Determine monotonicity:
     * $x<0$：$f'(x)>0$，$f$ 递增；
     * $x>0$：$f'(x)<0$，$f$ 递减。
  3. First Derivative Test: $f'$ 在 $x=0$ 处由正变负 $\implies f(0)=1$ 为局部最大值。由于 $x=0$ 是唯一驻点，由推论知它也是全局最大值。
  4. Check the behavior at infinity:
     $$\lim_{x\to\pm\infty}e^{-x^2/2}=0$$
     但 $e^{-x^2/2}>0$ 对一切 $x$ 成立，$0$ 永远取不到，故**没有全局最小值**（下确界为 $0$）。
* **中文详解:** $f'(x)=-xe^{-x^2/2}$ 的符号只由 $-x$ 决定：左侧为正、右侧为负，所以 $x=0$ 是唯一的“山顶”，且是全局最大值 $1$。当 $x\to\pm\infty$ 时函数值趋于 $0$ 但恒大于 $0$，因此最小值不存在，下确界为 $0$。这是开区间最值问题的典型结论：**最值可能“只趋近、不取到”**。

#### 6. 求最值的两套标准流程 (Two Standard Procedures)

| 情形 | 闭区间 $[a,b]$ 上的连续函数 | 开区间 $(a,b)$ 上的可导函数 |
| :--- | :--- | :--- |
| 1 | 求 $f'(x)$，解 $f'(x)=0$ 得驻点 | 求 $f'(x)$，解 $f'(x)=0$ 得驻点 |
| 2 | 找出区间内所有奇点（$f'$ 不存在处） | 找出区间内所有奇点 |
| 3 | 把端点 $a,b$ 也列为候选点 | 端点不是候选点，改为计算 $x\to a^+$、$x\to b^-$ 的极限 |
| 4 | 计算所有候选点的函数值 | 用一阶或二阶判别法判断驻点/奇点的极值性 |
| 5 | 比较大小，最大者为全局最大，最小者为全局最小 | 结合单调性与端点极限确定全局最值（或说明不存在） |

* **要点:** 闭区间用“候选点枚举 + 比较”；开区间用“单调性/极值 + 端点极限”。开区间上若唯一驻点且为局部极值，可直接由推论断言全局极值。

---

### 4.4 Practical Problems (Optimization / 优化问题)

#### 1. 优化问题五步法 (A Summary of the Method)

1. **画图设元 (Draw and label):** 画出几何图形，用字母表示所有相关长度，并在图上标出已知量与未知量。
2. **写出目标函数 (Objective function):** 把要求最大/最小的量（面积、体积、成本等）写成变量的函数 $F$。
3. **消元化单变量 (Eliminate variables):** 利用约束条件（如周长固定、相似三角形、勾股定理）把 $F$ 化为**一个**变量的函数，并根据几何意义写出定义域。
4. **求临界点 (Find critical points):** 在定义域内解 $F'=0$，并检查 $F'$ 不存在的点与端点。
5. **判别并作答 (Test and answer):** 开区间用一阶/二阶判别法；闭区间比较各候选点函数值；最后回到实际问题，写清单位与所问的量。

#### 2. 建模要点 (Modeling Tips)

* **约束方程 vs 目标函数:** 先写约束（如 $2x+2y=100$、$\frac{r}{h}=\frac{b}{a}$），再把它代入目标函数消元。
* **定义域来自几何:** 长度非负、内接要求、盒子边长不能超过纸板尺寸的一半等，务必写清 $x$ 的范围。
* **端点检验:** 若定义域是开区间，最优点在内部时用导数判别；若定义域是闭区间，还要比较端点值。
* **单位统一:** 长度、面积、体积单位全程一致，答案注明单位。

#### 🌟 课件例题与详解 (Lecture Examples & Solutions)

##### 【课件例题 6】纸板做无盖盒（开区间 + 二阶导数检验）

**Problem:** A rectangular box is to be made from a piece of cardboard 24 inches long and 9 inches wide by cutting out identical squares from the four corners and turning up the sides. Find the dimensions of the box of maximum volume. What is this volume?

* **Process (解题步骤):**
  1. Let $x$ be the side length of each cut-out square. Then the base is $(24-2x)$ by $(9-2x)$, and the height is $x$.
  2. The volume is
     $$V(x)=(24-2x)(9-2x)x,\qquad 0<x<\frac{9}{2}$$
  3. Expand and differentiate:
     $$V(x)=4x^3-66x^2+216x$$
     $$V'(x)=12x^2-132x+216=12(x^2-11x+18)=12(x-2)(x-9)$$
  4. Critical points: $x=2$ and $x=9$；只有 $x=2$ 落在定义域 $\left(0,\frac{9}{2}\right)$ 内。
  5. Second Derivative Test:
     $$V''(x)=24x-132,\qquad V''(2)=48-132=-84<0$$
     故 $x=2$ 给出最大值。
  6. Compute:
     $$V(2)=(24-4)(9-4)(2)=20\cdot 5\cdot 2=200$$
     盒子尺寸为 $20\text{ in}\times 5\text{ in}\times 2\text{ in}$，最大体积为 $200\text{ in}^3$。
* **中文详解:** 四角剪去边长为 $x$ 的正方形后折起，底面为 $(24-2x)\times(9-2x)$，高为 $x$，于是体积 $V(x)=(24-2x)(9-2x)x$。求导得 $V'(x)=12(x-2)(x-9)$，在 $(0,4.5)$ 内唯一驻点为 $x=2$。因为 $V''(2)=-84<0$，该驻点为极大值点；又定义域是开区间且两端 $V\to 0$，故也是全局最大值。代入得体积 $200$ 立方英寸，盒子尺寸 $20\times 5\times 2$ 英寸。

##### 【课件例题 7】圆锥内接圆柱（相似三角形约束）

**Problem:** A cylinder is inscribed in a cone of base radius $b$ and height $a$. Find the radius and height of the cylinder of maximum volume.

* **Process (解题步骤):**
  1. Let $r$ and $h$ be the radius and height of the cylinder. By similar triangles (axial cross-section):
     $$\frac{a-h}{r}=\frac{a}{b}\implies h=a-\frac{a}{b}r,\qquad 0<r<b$$
  2. Volume of the cylinder:
     $$V(r)=\pi r^2h=\pi r^2\left(a-\frac{a}{b}r\right)=\pi ar^2-\frac{\pi a}{b}r^3$$
  3. Differentiate:
     $$V'(r)=2\pi ar-\frac{3\pi a}{b}r^2=\pi ar\left(2-\frac{3r}{b}\right)$$
  4. Critical points: $r=0$（端点，舍去）与 $r=\dfrac{2b}{3}$。
  5. Second Derivative Test:
     $$V''(r)=2\pi a-\frac{6\pi a}{b}r,\qquad V''\left(\frac{2b}{3}\right)=2\pi a-4\pi a=-2\pi a<0$$
     故 $r=\dfrac{2b}{3}$ 给出最大值。
  6. Then
     $$h=a-\frac{a}{b}\cdot\frac{2b}{3}=\frac{a}{3},\qquad V_{\max}=\pi\left(\frac{2b}{3}\right)^2\cdot\frac{a}{3}=\frac{4\pi ab^2}{27}$$
* **中文详解:** 关键是用轴截面中的相似三角形把高 $h$ 用半径 $r$ 表示：$\frac{a-h}{r}=\frac{a}{b}$，得 $h=a-\frac{a}{b}r$。代入圆柱体积公式后得到只含 $r$ 的函数 $V(r)=\pi ar^2-\frac{\pi a}{b}r^3$。求导得 $V'(r)=\pi ar\left(2-\frac{3r}{b}\right)$，唯一内部驻点 $r=\frac{2b}{3}$；由 $V''<0$ 知为极大，结合端点 $r\to 0$ 与 $r\to b$ 时体积趋于 $0$，它是全局最大。此时高为 $\frac{a}{3}$，最大体积为 $\frac{4\pi ab^2}{27}$。也可用闭区间 $[0,b]$ 比较端点与驻点值，结论相同。

##### 【课件例题 8】半圆内接矩形（闭区间比较法）

**Problem:** A rectangle is inscribed in a semicircle of radius $r$ with its base on the diameter. Find the dimensions of the rectangle of maximum area.

* **Process (解题步骤):**
  1. Place the semicircle as $x^2+y^2=r^2$, $y\ge 0$. Let the upper-right vertex be $(x,y)$ with $0\le x\le r$; then the rectangle has width $2x$ and height $y=\sqrt{r^2-x^2}$.
  2. Area:
     $$A(x)=2x\sqrt{r^2-x^2},\qquad 0\le x\le r$$
  3. Differentiate (product/chain rule):
     $$A'(x)=2\sqrt{r^2-x^2}+2x\cdot\frac{-x}{\sqrt{r^2-x^2}}=\frac{2(r^2-x^2)-2x^2}{\sqrt{r^2-x^2}}=\frac{2(r^2-2x^2)}{\sqrt{r^2-x^2}}$$
  4. Critical points: $A'(x)=0\implies x=\dfrac{r}{\sqrt{2}}$；端点 $x=0$ 与 $x=r$ 处 $A=0$。
  5. Compare:
     $$A\left(\frac{r}{\sqrt{2}}\right)=2\cdot\frac{r}{\sqrt{2}}\cdot\sqrt{r^2-\frac{r^2}{2}}=2\cdot\frac{r}{\sqrt{2}}\cdot\frac{r}{\sqrt{2}}=r^2$$
     故最大面积为 $r^2$，此时宽 $2x=\sqrt{2}\,r$，高 $y=\dfrac{r}{\sqrt{2}}$。
* **中文详解:** 设矩形右上顶点为 $(x,y)$，则宽为 $2x$、高为 $y=\sqrt{r^2-x^2}$，面积 $A(x)=2x\sqrt{r^2-x^2}$，定义域是闭区间 $[0,r]$。求导并通分得 $A'(x)=\frac{2(r^2-2x^2)}{\sqrt{r^2-x^2}}$，驻点 $x=\frac{r}{\sqrt{2}}$。因为端点 $x=0,r$ 处面积为 $0$，而驻点处 $A=r^2>0$，故驻点即为最大值点。最大矩形宽 $\sqrt{2}r$、高 $\frac{r}{\sqrt{2}}$，面积 $r^2$。

#### 3. Self-Study 补充例题 (Further Exercises)

##### 【课件例题 9】三次多项式的局部极值（二阶导数法）

**Problem:** Find the local extreme values of $f(x)=x^3-3x^2+2$.

* **Process (解题步骤):**
  1. $$f'(x)=3x^2-6x=3x(x-2)\implies x=0,\ 2$$
  2. $$f''(x)=6x-6$$
  3. $f''(0)=-6<0\implies f(0)=2$ 为局部最大值；
     $f''(2)=6>0\implies f(2)=8-12+2=-2$ 为局部最小值。
* **中文详解:** 求导得 $f'(x)=3x(x-2)$，驻点为 $0$ 与 $2$。二阶导数 $f''(x)=6x-6$：在 $0$ 处为 $-6<0$，故 $f(0)=2$ 是局部极大；在 $2$ 处为 $6>0$，故 $f(2)=-2$ 是局部极小。本题也可用一阶导数符号表验证。

##### 【课件例题 10】椭圆内接最大矩形（显函数法与隐函数法）

**Problem:** Find the dimensions of the rectangle of maximum area inscribed in the ellipse $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$.

* **Process (解题步骤):**
  1. By symmetry, let the first-quadrant vertex be $(x,y)$; the rectangle has width $2x$ and height $2y$, so
     $$A=4xy$$
  2. **Method 1 (explicit):** From the ellipse equation,
     $$y=b\sqrt{1-\frac{x^2}{a^2}},\qquad 0\le x\le a$$
     $$A(x)=4bx\sqrt{1-\frac{x^2}{a^2}}$$
     $$A'(x)=4b\left[\sqrt{1-\frac{x^2}{a^2}}+x\cdot\frac{-x/a^2}{\sqrt{1-x^2/a^2}}\right]=\frac{4b\left(a^2-2x^2\right)}{a^2\sqrt{1-x^2/a^2}}$$
     令 $A'=0$ 得 $x=\dfrac{a}{\sqrt{2}}$，此时 $y=\dfrac{b}{\sqrt{2}}$。
  3. **Method 2 (implicit):** Differentiate the constraint implicitly:
     $$\frac{2x}{a^2}+\frac{2y}{b^2}y'=0\implies y'=-\frac{b^2x}{a^2y}$$
     Set $\dfrac{dA}{dx}=4y+4xy'=0$:
     $$4y+4x\left(-\frac{b^2x}{a^2y}\right)=0\implies a^2y^2=b^2x^2\implies \frac{x^2}{a^2}=\frac{y^2}{b^2}$$
     Combined with the ellipse equation, $\dfrac{x^2}{a^2}=\dfrac{y^2}{b^2}=\dfrac12$.
  4. Hence
     $$x=\frac{a}{\sqrt{2}},\quad y=\frac{b}{\sqrt{2}};\qquad \text{dimensions } \sqrt{2}a\times\sqrt{2}b,\quad A_{\max}=4\cdot\frac{a}{\sqrt{2}}\cdot\frac{b}{\sqrt{2}}=2ab$$
  5. Endpoints $x=0$ and $x=a$ give $A=0$, so the critical point is the global maximum.
* **中文详解:** 方法一直接由椭圆方程解出 $y=b\sqrt{1-x^2/a^2}$，代入 $A=4xy$ 得单变量函数，求导后分子为 $4b(a^2-2x^2)$，驻点 $x=\frac{a}{\sqrt{2}}$，对应 $y=\frac{b}{\sqrt{2}}$。方法二对约束方程隐求导得 $y'=-\frac{b^2x}{a^2y}$，再令 $\frac{dA}{dx}=4y+4xy'=0$，化简得 $a^2y^2=b^2x^2$，即 $\frac{x^2}{a^2}=\frac{y^2}{b^2}$。结合椭圆方程得两者都等于 $\frac12$。两种方法结论一致：最大矩形边长为 $\sqrt{2}a$ 与 $\sqrt{2}b$，最大面积 $2ab$。

---

### 4.5* Graphing Functions Using Calculus (用微积分作函数图像)

#### 1. 作图四步法 (General Procedure)

* **Step 1 预分析 (Pre-calculus analysis):**
  * 定义域 (domain) 与值域 (range)；
  * 对称性 (symmetry)：偶函数 $f(-x)=f(x)$ 关于 $y$ 轴对称，奇函数 $f(-x)=-f(x)$ 关于原点对称；
  * 截距 (intercepts)：令 $y=0$ 求 $x$ 截距，令 $x=0$ 求 $y$ 截距。
* **Step 2 微积分分析 (Calculus analysis):**
  * 用 $f'$ 求临界点、单调区间、局部极值；
  * 用 $f''$ 求凹凸区间与拐点 (inflection points)；
  * 求渐近线 (asymptotes)。
* **Step 3 描点 (Plot key points):** 标出临界点、拐点、截距以及若干辅助点。
* **Step 4 连线 (Sketch):** 按单调性与凹凸性，用光滑曲线连接各关键点，注意渐近线附近的行为。

#### 2. 渐近线 (Asymptotes)

* **水平渐近线 (Horizontal Asymptote):** 若 $\lim_{x\to+\infty}f(x)=L$ 或 $\lim_{x\to-\infty}f(x)=L$，则 $y=L$ 是水平渐近线。
* **垂直渐近线 (Vertical Asymptote):** 若 $\lim_{x\to a^+}f(x)=\pm\infty$ 或 $\lim_{x\to a^-}f(x)=\pm\infty$，则 $x=a$ 是垂直渐近线。对有理函数，分母的零点（分子不同时为零）是垂直渐近线的候选点。
* **斜渐近线 (Slant Asymptote):** 若 $f(x)-(mx+c)\to 0$（$x\to\pm\infty$），则 $y=mx+c$ 为斜渐近线；当分子次数比分母恰好多 $1$ 时出现。

#### 🌟 课件例题与详解 (Lecture Examples & Solutions)

##### 【课件例题 11】有理函数的完整分析

**Problem:** For $f(x)=\dfrac{x^2}{x^2+1}$, $-\infty<x<\infty$, find:
(1a) the intervals on which $f$ is increasing and decreasing;
(1b) the local and global extreme values;
(2a) the intervals of upward and downward concavity;
(2b) the inflection points;
(3) all asymptotes; then sketch the graph.

* **Process (解题步骤):**
  1. Rewrite the function to simplify differentiation:
     $$f(x)=\frac{x^2}{x^2+1}=1-\frac{1}{x^2+1}$$
  2. First derivative:
     $$f'(x)=\frac{2x}{(x^2+1)^2}$$
     $f'(x)=0\iff x=0$；$f'$ 处处存在，无奇点。
  3. **(1a) Monotonicity:**
     * $x<0$：$f'(x)<0\implies f$ 递减；
     * $x>0$：$f'(x)>0\implies f$ 递增。
     故 $f$ 在 $(-\infty,0]$ 上递减，在 $[0,\infty)$ 上递增。
  4. **(1b) Extreme values:** 由一阶判别法，$x=0$ 为局部极小点，$f(0)=0$。由于 $x=0$ 是唯一驻点且为极小点，$f(0)=0$ 也是全局最小值。又
     $$\lim_{x\to\pm\infty}\frac{x^2}{x^2+1}=1$$
     但 $\dfrac{x^2}{x^2+1}<1$ 恒成立（分母比分子大 $1$），$1$ 取不到，故**没有全局最大值**，值域为 $[0,1)$。
  5. Second derivative:
     $$f''(x)=\frac{2(x^2+1)^2-2x\cdot 2(x^2+1)\cdot 2x}{(x^2+1)^4}=\frac{2(x^2+1)-8x^2}{(x^2+1)^3}=\frac{2(1-3x^2)}{(x^2+1)^3}$$
  6. **(2a) Concavity:** $f''(x)=0\iff x=\pm\dfrac{1}{\sqrt{3}}$。
     * $\left(-\infty,-\dfrac{1}{\sqrt{3}}\right)$：$1-3x^2<0\implies f''<0$，凹向下 (CD)；
     * $\left(-\dfrac{1}{\sqrt{3}},\dfrac{1}{\sqrt{3}}\right)$：$1-3x^2>0\implies f''>0$，凹向上 (CU)；
     * $\left(\dfrac{1}{\sqrt{3}},\infty\right)$：$1-3x^2<0\implies f''<0$，凹向下 (CD)。
  7. **(2b) Inflection points:** $f''$ 在 $x=\pm\dfrac{1}{\sqrt{3}}$ 两侧变号，且
     $$f\left(\pm\frac{1}{\sqrt{3}}\right)=\frac{1/3}{1+1/3}=\frac{1}{4}$$
     故拐点为 $\left(-\dfrac{1}{\sqrt{3}},\dfrac{1}{4}\right)$ 与 $\left(\dfrac{1}{\sqrt{3}},\dfrac{1}{4}\right)$。
  8. **(3) Asymptotes:**
     * 水平渐近线：$\lim_{x\to\pm\infty}f(x)=1\implies y=1$；
     * 垂直渐近线：分母 $x^2+1\neq 0$，无垂直渐近线；
     * 无斜渐近线（已有水平渐近线）。
  9. **Sign table:**

     | 区间 | $(-\infty,-\frac{1}{\sqrt{3}})$ | $-\frac{1}{\sqrt{3}}$ | $(-\frac{1}{\sqrt{3}},0)$ | $0$ | $(0,\frac{1}{\sqrt{3}})$ | $\frac{1}{\sqrt{3}}$ | $(\frac{1}{\sqrt{3}},\infty)$ |
     | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
     | $f'(x)$ | $-$ | $-$ | $-$ | $0$ | $+$ | $+$ | $+$ |
     | $f''(x)$ | $-$ | $0$ | $+$ | $+$ | $+$ | $0$ | $-$ |
     | $f(x)$ | 递减、凹下 | 拐点 | 递减、凹上 | 极小值 $0$ | 递增、凹上 | 拐点 | 递增、凹下 |

  10. **Sketch:** 曲线关于 $y$ 轴对称（偶函数），过原点 $(0,0)$，在 $x=0$ 处取最小值 $0$，向两侧递增并分别以 $y=1$ 为水平渐近线；在 $x=\pm\frac{1}{\sqrt{3}}$ 处由凹下变凹上、再由凹上变凹下，拐点高度均为 $\frac14$。

* **中文详解:** 先把函数改写为 $1-\frac{1}{x^2+1}$，求导更方便。$f'(x)=\frac{2x}{(x^2+1)^2}$，符号只由 $x$ 决定：左负右正，故 $x=0$ 是全局最小点，最小值为 $0$。由于 $\frac{x^2}{x^2+1}<1$ 恒成立且极限为 $1$，函数没有最大值，值域 $[0,1)$。二阶导数 $f''(x)=\frac{2(1-3x^2)}{(x^2+1)^3}$ 的零点为 $\pm\frac{1}{\sqrt{3}}$：中间区间 $f''>0$（凹向上），两侧 $f''<0$（凹向下），故有两个拐点，纵坐标均为 $\frac14$。渐近线方面，$\lim_{x\to\pm\infty}f=1$ 给出水平渐近线 $y=1$，分母恒正故无垂直渐近线。整条曲线关于 $y$ 轴对称，最低点在原点，两侧分别从 $0$ 单调上升到接近 $1$。
