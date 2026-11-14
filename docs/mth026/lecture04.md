# Chapter 2 Limits & Continuity: 指数与对数函数极限、函数连续性与介值定理 知识详解与例题全解

## 第一部分：本节课知识详解 (Lecture 4 Summary)

---

### 2.6 Limits of Exponential, Logarithmic & Inverse Functions (指数、对数与反函数极限)

#### 1. 指数函数的极限 (Limits of Exponential Functions)
* **概念与性质 (Properties):**
  对于底数 $a > 0$ 且 $a \neq 1$ 的指数函数 $f(x) = a^x$：
  1. **直接代入法 (Substitution):** 对任意实数 $c$，均有 $\lim_{x \to c} a^x = a^c$。
  2. **趋于无穷时的极限趋势 (Limits at $\pm\infty$):**
     * 当 $a > 1$ 时（例如自然底数 $e \approx 2.718$ 或底数 $2$）：
       $$\lim_{x \to \infty} a^x = \infty, \quad \lim_{x \to -\infty} a^x = 0$$
     * 当 $0 < a < 1$ 时（例如 $a = 1/2$）：
       $$\lim_{x \to \infty} a^x = 0, \quad \lim_{x \to -\infty} a^x = \infty$$

* **核心基本极限 (Core Exponential Limits):**
  $$\lim_{x \to \infty} e^x = \infty, \quad \lim_{x \to -\infty} e^x = 0$$
  $$\lim_{x \to \infty} \left(\frac{1}{2}\right)^x = 0, \quad \lim_{x \to -\infty} \left(\frac{1}{2}\right)^x = \infty$$

---

#### 2. 反函数的极限定理 (Limits for Inverse Functions)
* **定理内容 (Theorem C):**
  若函数 $f$ 存在反函数 $f^{-1}$，且在 $x = a$ 处的极限满足：
  $$\lim_{x \to a} f(x) = f(a) = c$$
  则反函数 $f^{-1}$ 在 $x = c$ 处的极限满足：
  $$\lim_{x \to c} f^{-1}(x) = f^{-1}(c) = a$$
* **几何与逻辑直观 (Geometric Intuition):**
  反函数的图像关于直线 $y = x$ 对称，定义域与值域互换，因此极限在对应点处保持连续映射关系。例如若 $\lim_{x \to 5} a^x = 8$，则必有 $\lim_{x \to 8} \log_a x = 5$。

---

#### 3. 对数函数的极限 (Limits of Logarithmic Functions)
* **定理内容 (Theorem D):**
  对于对数函数 $f(x) = \log_c x$（底数 $c > 0, c \neq 1$）：
  1. **内部点极限:** 若 $a > 0$，则 $\lim_{x \to a} \log_c x = \log_c a$。
  2. **无穷远处趋势 (当 $c > 1$ 时):**
     $$\lim_{x \to \infty} \log_c x = \infty, \quad \lim_{x \to 0^+} \log_c x = -\infty$$

---

#### 🌟 课件应用例题：连续复利投资模型 (Continuous Compounding Model)
* **Problem:** An investment of $\$2000$ yields $8\%$ interest per year compounded continuously. The value of the investment after $t$ years is given by $A(t) = 2000 e^{0.08t}$.
  (a) Find the value of the investment after $5$ years.
  (b) Find the time required for the investment to double in value.
* **Process (解题步骤):**
  (a) Evaluate $A(5)$:
      $$A(5) = 2000 e^{0.08 \times 5} = 2000 e^{0.4} \approx \$2983.60$$
  (b) Set $A(t_0) = 4000$ and solve for $t_0$:
      $$4000 = 2000 e^{0.08 t_0} \implies 2 = e^{0.08 t_0}$$
      Take the natural logarithm on both sides:
      $$\ln 2 = \ln\left(e^{0.08 t_0}\right) = 0.08 t_0 \implies t_0 = \frac{\ln 2}{0.08} = \frac{25}{2} \ln 2 \approx 8.66 \text{ years}$$
* **中文详解:** 
  (a) 5 年后的资金终值直接将 $t=5$ 代入连续复利公式 $A(t)$ 计算得到约 $\$2983.60$；
  (b) 投资翻倍意味着终值达到 $\$4000$，建立方程后两边取自然对数 $\ln$，解得翻倍所需时间 $t_0 = \frac{25}{2} \ln 2 \approx 8.66$ 年。

---

### 2.7 Continuity of Functions (函数的连续性)

#### 1. 连续性的直观与严格定义 (Definition of Continuity)
* **直观含义 (Intuitive Concept):**
  在物理与自然界中，连续变化的过程（如一天的气温变化 $T(t)$）其图像是一条**一笔画出、没有断裂**的平滑曲线；而脉冲电压 $V(t)$ 在开关切换时会发生突变，对应图像上的**断点 (Breaks)**。
* **连续三要素测试 (Continuity Test):**
  函数 $f(x)$ 在点 $x = c$ 处连续 (**continuous at $c$**)，**当且仅当**满足以下三个条件：
  1. **极限存在:** $\lim_{x \to c} f(x)$ 存在；
  2. **函数值有定义:** $f(c)$ 在 $c$ 处有定义（即 $c \in D(f)$）；
  3. **极限值等于函数值:** $\lim_{x \to c} f(x) = f(c)$。

  > 若上述三个条件中有**任何一个**不满足，则称函数 $f(x)$ 在点 $x = c$ 处**不连续 (discontinuous)**，$c$ 称为 $f(x)$ 的**间断点 (Point of Discontinuity)**。

---

#### 🌟 课件例题 1：补全点使函数连续 (To Make a Function Continuous)
* **Problem:** Let $f(x) = \frac{x^2 - 4}{x - 2}$ for $x \neq 2$. How should $f$ be defined at $x = 2$ in order to make it continuous there?
* **Process (解题步骤):**
  Calculate the limit as $x \to 2$:
  $$\lim_{x \to 2} \frac{x^2 - 4}{x - 2} = \lim_{x \to 2} \frac{(x - 2)(x + 2)}{x - 2} = \lim_{x \to 2} (x + 2) = 4$$
  To achieve continuity at $x = 2$, we must set $f(2) = \lim_{x \to 2} f(x) = 4$.
* **中文详解:** 
  原函数在 $x=2$ 处无定义，但极限存在且等于 4。要使函数在 $x=2$ 处连续，只需补充定义 $f(2) = 4$ 即可填补该“无定义洞”。

---

#### 2. 间断点的分类 (Classification of Points of Discontinuity)
* **可去间断点 (Removable Discontinuity):**
  若极限 $\lim_{x \to c} f(x)$ 存在，但 $f(c)$ 无定义或 $f(c) \neq \lim_{x \to c} f(x)$。可以通过重新定义 $f(c) = \lim_{x \to c} f(x)$ 来消除间断。
* **不可去间断点 (Nonremovable Discontinuity):**
  若极限 $\lim_{x \to c} f(x)$ 不存在（例如左右极限不相等形成的跳跃间断点，或趋于无穷的无穷间断点）。

---

#### 🌟 课件例题 2：间断点的全分析与分类
* **Problem:** Determine all points of discontinuity of $f(x) = \frac{\sin x}{x(1 - x)}$, and classify each point as removable or nonremovable.
* **Process (解题步骤):**
  1. Identify candidate points where the denominator is zero: $x = 0$ and $x = 1$.
  2. Analyze $x = 0$:
     $$\lim_{x \to 0} \frac{\sin x}{x(1 - x)} = \left(\lim_{x \to 0} \frac{\sin x}{x}\right) \cdot \left(\lim_{x \to 0} \frac{1}{1 - x}\right) = 1 \cdot 1 = 1$$
     Since the limit exists at $x = 0$, $x = 0$ is a **removable discontinuity**.
  3. Analyze $x = 1$:
     As $x \to 1^+$, $\sin 1 > 0$, $x \to 1$, and $1 - x \to 0^-$:
     $$\lim_{x \to 1^+} \frac{\sin x}{x(1 - x)} = -\infty$$
     As $x \to 1^-$, $1 - x \to 0^+$:
     $$\lim_{x \to 1^-} \frac{\sin x}{x(1 - x)} = +\infty$$
     Since the limit does not exist (infinite limit), $x = 1$ is a **nonremovable discontinuity**.
* **中文详解:**
  * 使分母为 0 的可疑点为 $x=0$ 和 $x=1$。
  * 在 $x=0$ 处，拆分为第一重要极限 $\lim_{x \to 0} \frac{\sin x}{x} = 1$ 与连续因子 $\frac{1}{1-x} \to 1$ 的乘积，极限值为 1 存在，故 $x=0$ 为**可去间断点**；
  * 在 $x=1$ 处，左右极限分别为 $+\infty$ 与 $-\infty$，极限不存在，故 $x=1$ 为**不可去（无穷）间断点**。

---

#### 3. 常见初等函数的连续性定理 (Continuity of Elementary Functions)
1. **多项式函数 (Polynomials):** 在全体实数 $\mathbb{R}$ 上无条件连续。
2. **有理函数 (Rational Functions):** 在其定义域内（即排除分母为 0 的所有点）处处连续。
3. **绝对值与根式函数:**
   * 绝对值函数 $|x|$ 在 $\mathbb{R}$ 上连续；
   * 奇次根式 $x^{1/n}$ ($n$ 为奇数) 在 $\mathbb{R}$ 上连续；
   * 偶次根式 $x^{1/n}$ ($n$ 为偶数) 在所有正实数 $(0, \infty)$ 上连续。
4. **超越初等函数 (Transcendental Functions):**
   正弦、余弦、正切、余切、正割、余割、反三角函数、指数函数、对数函数在其**定义域内部 (Interior of Domain)** 均连续。
5. **初等函数连续性基本定理:**
   **一切初等函数在其自然定义域内都是连续的。**

---

#### 4. 复合函数的连续性与换元法 (Composite Limit Theorem & Variable Substitution)
* **复合函数极限交换定理 (Theorem E):**
  若 $\lim_{x \to c} g(x) = L$，且函数 $f$ 在 $u = L$ 处连续，则：
  $$\lim_{x \to c} f(g(x)) = f\left(\lim_{x \to c} g(x)\right) = f(L)$$
  *即：**对于连续函数，极限符号与函数作用符号可以自由交换位置。***

---

#### 🌟 课件例题 3：复合函数极限与换元计算
* **Problem:** Evaluate the following limits:
  (a) $\lim_{x \to 0} \sin\left(\frac{\sin x}{x}\right)$
  (b) $\lim_{x \to 0} \frac{\ln(1+x)}{x}$
  (c) $\lim_{x \to 0} \frac{e^x - 1}{x}$
* **Process (解题步骤):**
  (a) Since $\lim_{x \to 0} \frac{\sin x}{x} = 1$ and $\sin u$ is continuous at $u = 1$:
      $$\lim_{x \to 0} \sin\left(\frac{\sin x}{x}\right) = \sin\left(\lim_{x \to 0} \frac{\sin x}{x}\right) = \sin 1$$
  (b) Using logarithmic properties and the second important limit $\lim_{x \to 0} (1+x)^{1/x} = e$:
      $$\lim_{x \to 0} \frac{\ln(1+x)}{x} = \lim_{x \to 0} \ln\left((1+x)^{1/x}\right) = \ln\left(\lim_{x \to 0} (1+x)^{1/x}\right) = \ln e = 1$$
  (c) Let $u = e^x - 1 \implies e^x = 1+u \implies x = \ln(1+u)$. As $x \to 0$, $u \to 0$:
      $$\lim_{x \to 0} \frac{e^x - 1}{x} = \lim_{u \to 0} \frac{u}{\ln(1+u)} = \lim_{u \to 0} \frac{1}{\frac{\ln(1+u)}{u}} = \frac{1}{1} = 1$$
* **中文详解:**
  (a) 利用外层正弦函数的连续性，将极限符号收入内部，得 $\sin 1$；
  (b) 将分母的 $\frac{1}{x}$ 提为对数真数的指数，结合第二重要极限 $\lim_{x \to 0} (1+x)^{1/x} = e$，对数连续性得 $\ln e = 1$；
  (c) 采用换元法令 $u = e^x - 1$，将分子分母转化为 $\frac{u}{\ln(1+u)}$，利用 (b) 的结论直接求得极限为 1。

---

#### 🌟 课件例题 4：幂指函数 $f(x)^{g(x)}$ 的连续性与极限
* **Problem:** Evaluate $\lim_{x \to 0} (1 + x)^{2/\sin x}$.
* **Process (解题步骤):**
  Rewrite the base and exponent:
  $$\lim_{x \to 0} (1 + x)^{2/\sin x} = \lim_{x \to 0} \left[(1 + x)^{1/x}\right]^{\frac{2x}{\sin x}}$$
  Apply the Composite Limit Theorem:
  * Inner limit: $\lim_{x \to 0} (1 + x)^{1/x} = e$
  * Exponent limit: $\lim_{x \to 0} \frac{2x}{\sin x} = 2 \cdot \lim_{x \to 0} \frac{x}{\sin x} = 2 \cdot 1 = 2$
  Combine the limits:
  $$\lim_{x \to 0} (1 + x)^{2/\sin x} = e^2$$
* **中文详解:** 
  这是经典的 $1^\infty$ 型未定式。通过凑配第二重要极限结构 $(1+x)^{1/x}$，将指数拆分为 $\frac{2x}{\sin x}$。利用连续性，底数趋于 $e$，指数趋于 $2$，最终计算结果为 $e^2$。

---

#### 5. 区间上的连续性 (Continuity on Intervals)
* **单侧连续性 (One-Sided Continuity):**
  * **右连续 (Right Continuous at $a$):** $\lim_{x \to a^+} f(x) = f(a)$；
  * **左连续 (Left Continuous at $b$):** $\lim_{x \to b^-} f(x) = f(b)$。
* **区间连续性定义:**
  * 函数 $f$ 在**开区间 $(a, b)$** 上连续，若它在开区间的每个点处均连续；
  * 函数 $f$ 在**闭区间 $[a, b]$** 上连续，若它在 $(a, b)$ 内处处连续，且在左端点 $a$ 处**右连续**，在右端点 $b$ 处**左连续**。

---

#### 6. 闭区间上连续函数的全局性质：介值定理与零点定理

##### **介值定理 (Intermediate Value Theorem, IVT)**
* **定理内容 (Theorem F):**
  设函数 $f(x)$ 在闭区间 $[a, b]$ 上**连续**，且 $W$ 为介于 $f(a)$ 与 $f(b)$ 之间的任意实数。则在开区间 $(a, b)$ 内**至少存在一点 $c$**，使得：
  $$f(c) = W$$
* **几何意义:**
  连续函数的图像是一条不间断的曲线。从水平线 $y = f(a)$ 连到 $y = f(b)$，曲线必然会与中间的任意水平线 $y = W$ 至少相交一次。

##### **零点定理 (Zero Point Theorem)**
* **推论:** 若 $f(x)$ 在 $[a, b]$ 上连续，且端点值异号（即 $f(a) \cdot f(b) < 0$），则方程 $f(x) = 0$ 在 $(a, b)$ 内至少有一个实根 $c$。

---

#### 🌟 课件例题 5：介值定理证明超越方程根的存在性与二分法
* **Problem:** Use the Intermediate Value Theorem to show that the equation $x = \cos x$ has a solution between $x = 0$ and $x = \pi/2$.
* **Process (证明步骤):**
  1. Define a auxiliary function: Let $f(x) = x - \cos x$, and set $W = 0$.
  2. Check continuity: $f(x)$ is the difference of two elementary functions ($y = x$ and $y = \cos x$), so $f(x)$ is continuous on the closed interval $[0, \pi/2]$.
  3. Evaluate end points:
     $$f(0) = 0 - \cos 0 = -1 < 0$$
     $$f\left(\frac{\pi}{2}\right) = \frac{\pi}{2} - \cos\left(\frac{\pi}{2}\right) = \frac{\pi}{2} > 0$$
  4. Apply IVT: Since $W = 0$ lies strictly between $f(0) = -1$ and $f(\pi/2) = \pi/2$, by the Intermediate Value Theorem, there exists at least one $c \in (0, \pi/2)$ such that $f(c) = 0$.
  5. Conclusion: $c - \cos c = 0 \implies c = \cos c$, so $c$ is a solution to $x = \cos x$.

* **二分法延伸 (Bisection Method Remark):**
  进一步考察中点 $x = \pi/4$：
  $$f\left(\frac{\pi}{4}\right) = \frac{\pi}{4} - \cos\left(\frac{\pi}{4}\right) = \frac{\pi}{4} - \frac{\sqrt{2}}{2} = \frac{\pi - 2\sqrt{2}}{4} \approx \frac{3.1416 - 2.8284}{4} > 0$$
  由于 $f(0) < 0$ 且 $f(\pi/4) > 0$，根的范围被成功缩小至更精细的区间 $(0, \pi/4)$。这种不断折半区间逼近零点的方法称为**二分法 (Bisection Method)**。

---

#### 🌟 课件例题 6：不动点定理证明 (Fixed Point Theorem)
* **Problem:** Prove that if $f$ is continuous on $[0, 1]$ and satisfies $0 \le f(x) \le 1$ for all $x \in [0, 1]$, then there exists a number $c \in [0, 1]$ such that $f(c) = c$.
* **Process (证明步骤):**
  1. Define the auxiliary function $g(x) = f(x) - x$.
  2. Since $f(x)$ and $x$ are continuous on $[0, 1]$, $g(x)$ is continuous on $[0, 1]$.
  3. Evaluate $g(x)$ at the boundaries:
     * $g(0) = f(0) - 0 = f(0) \ge 0$ (since $f(x) \ge 0$);
     * $g(1) = f(1) - 1 \le 0$ (since $f(x) \le 1$).
  4. Case analysis:
     * If $g(0) = 0$, then $f(0) = 0$, so $c = 0$ is the required number;
     * If $g(1) = 0$, then $f(1) = 1$, so $c = 1$ is the required number;
     * If $g(0) > 0$ and $g(1) < 0$, then $0$ lies between $g(0)$ and $g(1)$. By the Zero Point Theorem, there exists some $c \in (0, 1)$ such that $g(c) = 0$.
  5. Thus $f(c) - c = 0 \implies f(c) = c$.

* **中文详解:** 构造辅助函数 $g(x) = f(x) - x$。利用已知条件 $0 \le f(x) \le 1$ 推出端点值 $g(0) \ge 0$ 且 $g(1) \le 0$。如果端点取等号则直接得出不动点；若严格异号，则由零点定理可知区间内部必存在 $c$ 使得 $g(c) = 0 \implies f(c) = c$。

---

#### 7. 第二重要极限与 $1^\infty$ 型未定式 (The Second Important Limit)
* **第二重要极限标准型 (Standard Forms):**
  $$\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x = e, \quad \lim_{h \to 0} (1 + h)^{1/h} = e$$
* **复合换元推广定理 (Generalization via Variable Substitution):**
  1. 若 $\lim_{x \to c} u(x) = \infty$，则 $\lim_{x \to c} \left(1 + \frac{1}{u(x)}\right)^{u(x)} = e$；
  2. 若 $\lim_{x \to c} u(x) = 0$（且 $u(x) \neq 0$），则 $\lim_{x \to c} \left(1 + u(x)\right)^{1/u(x)} = e$。

---

#### 🌟 课件例题 7：$1^\infty$ 型极限经典综合例题
* **Problem:** Evaluate $\lim_{x \to 0} \left(x + e^{x/3}\right)^{3/x}$.
* **Process (解题步骤):**
  1. Identify the form: As $x \to 0$, $x + e^{x/3} \to 0 + 1 = 1$, and exponent $\frac{3}{x} \to \infty$. This is a $1^\infty$ indeterminate form.
  2. Let $u(x) = x + e^{x/3} - 1$. Note that as $x \to 0$, $u(x) \to 0$.
  3. Express the base as $1 + u(x)$:
     $$\lim_{x \to 0} \left(x + e^{x/3}\right)^{3/x} = \lim_{x \to 0} \left(1 + u(x)\right)^{3/x}$$
  4. Supply the required exponent $\frac{1}{u(x)}$ for the second important limit:
     $$\lim_{x \to 0} \left(1 + u(x)\right)^{3/x} = \lim_{x \to 0} \left[\left(1 + u(x)\right)^{1/u(x)}\right]^{\frac{3 u(x)}{x}}$$
  5. Evaluate the inner limit:
     $$\lim_{x \to 0} \left(1 + u(x)\right)^{1/u(x)} = \lim_{u \to 0} (1 + u)^{1/u} = e$$
  6. Evaluate the exponent limit $\lim_{x \to 0} \frac{3 u(x)}{x}$:
     $$\lim_{x \to 0} \frac{3\left(x + e^{x/3} - 1\right)}{x} = 3 \left(\lim_{x \to 0} \frac{x}{x} + \lim_{x \to 0} \frac{e^{x/3} - 1}{x}\right)$$
     Let $t = \frac{x}{3}$. As $x \to 0$, $t \to 0$:
     $$\lim_{x \to 0} \frac{e^{x/3} - 1}{x} = \lim_{t \to 0} \frac{e^t - 1}{3t} = \frac{1}{3} \cdot \lim_{t \to 0} \frac{e^t - 1}{t} = \frac{1}{3} \cdot 1 = \frac{1}{3}$$
     So the exponent limit is:
     $$3 \left(1 + \frac{1}{3}\right) = 3 + 1 = 4$$
  7. Combine the results:
     $$\lim_{x \to 0} \left(x + e^{x/3}\right)^{3/x} = e^4$$

* **中文详解:** 
  这是非常经典的 $1^\infty$ 型未定式。
  第一步：将底数写为 $1 + u(x)$ 的标准形式，其中 $u(x) = x + e^{x/3} - 1 \to 0$；
  第二步：强制凑出核心指数次方 $\frac{1}{u(x)}$，使括号内底数转化为趋于 $e$ 的结构；
  第三步：计算剩余指数部分 $\lim_{x \to 0} \frac{3 u(x)}{x}$，将其拆分为 $3\left(1 + \frac{e^{x/3}-1}{x}\right)$，利用换元 $t = x/3$ 计算出指数极限为 $4$；
  最终求得结果为 $e^4$。
