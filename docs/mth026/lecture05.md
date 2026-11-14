# Chapter 3 The Derivatives: 导数概念、求导法则、三角导数、链式法则与高阶导数 知识详解

## 第一部分：本节课知识详解 (Lecture 5 Summary)

### 3.1 Two Problems with One Theme (同一个主题的两个问题)

#### 1. 切线问题 (The Tangent Line Problem)
* **割线与切线 (Secant & Tangent Lines):**
  设 $P(c, f(c))$ 为曲线 $y = f(x)$ 上一点，$Q(c+h, f(c+h))$ 为曲线上的邻近动点。
  * **割线斜率 (Slope of Secant Line):** 
    $$m_{\text{sec}} = \frac{f(c+h) - f(c)}{h}$$
  * **切线斜率 (Slope of Tangent Line):** 当动点 $Q$ 沿曲线无限趋近于 $P$（即 $h \to 0$）时，割线的极限位置即为切线。
    $$m_{\text{tan}} = \lim_{h \to 0} m_{\text{sec}} = \lim_{h \to 0} \frac{f(c+h) - f(c)}{h}$$
* **切线的点斜式方程 (Point-Slope Form of Tangent Line):**
  $$y = m_{\text{tan}}(x - c) + f(c)$$

---

#### 2. 瞬时速度问题 (Instantaneous Velocity Problem)
* **平均速度与瞬时速度 (Average & Instantaneous Velocity):**
  质点沿直线运动，位置函数为 $s = f(t)$。
  * 在时间区间 $[c, c+h]$ 内的**平均速度**：
    $$v_{\text{avg}} = \frac{f(c+h) - f(c)}{h}$$
  * 在 $t = c$ 时刻的**瞬时速度**（即平均速度当时间间隔 $h \to 0$ 时的极限）：
    $$v(c) = \lim_{h \to 0} v_{\text{avg}} = \lim_{h \to 0} \frac{f(c+h) - f(c)}{h}$$

---

#### 🌟 课件例题与详解 (Lecture Examples & Solutions)

##### 【课件例题 1】求抛物线在指定点的切线方程
**Problem:** Find the equation of the tangent lines to the curve $y = x^2 + 1$ at the points where $x = -2, -1, 0$.
* **Process (解题步骤):**
  For $f(x) = x^2 + 1$, compute the slope at an arbitrary point $x = c$:
  $$m_{\text{tan}} = \lim_{h \to 0} \frac{f(c+h) - f(c)}{h} = \lim_{h \to 0} \frac{((c+h)^2 + 1) - (c^2 + 1)}{h} = \lim_{h \to 0} \frac{2ch + h^2}{h} = \lim_{h \to 0} (2c + h) = 2c$$
  1. At $x = -2$: $f(-2) = 5$, $m_{\text{tan}} = 2(-2) = -4 \implies y - 5 = -4(x + 2) \implies y = -4x - 3$.
  2. At $x = -1$: $f(-1) = 2$, $m_{\text{tan}} = 2(-1) = -2 \implies y - 2 = -2(x + 1) \implies y = -2x$.
  3. At $x = 0$: $f(0) = 1$, $m_{\text{tan}} = 2(0) = 0 \implies y - 1 = 0(x - 0) \implies y = 1$.
* **中文详解:** 先根据极限定义求出抛物线在任意点 $c$ 处的通用切线斜率公式 $m = 2c$，然后分别代入 $x = -2, -1, 0$ 计算出具体的斜率与坐标点，最后写出对应的点斜式切线方程。

##### 【课件例题 2】直线运动的瞬时速度与瞬时停止
**Problem:** An object moves along a coordinate line with position $s(t) = 12t - t^3$ feet after $t$ seconds.
(1) Find its instantaneous velocity at $t = \alpha$.
(2) When does the object come to a momentary stop?
* **Process (解题步骤):**
  (1) Compute instantaneous velocity $v(\alpha)$:
  $$v(\alpha) = \lim_{h \to 0} \frac{s(\alpha+h) - s(\alpha)}{h} = \lim_{h \to 0} \frac{[12(\alpha+h) - (\alpha+h)^3] - [12\alpha - \alpha^3]}{h}$$
  $$= \lim_{h \to 0} \frac{12h - (3\alpha^2 h + 3\alpha h^2 + h^3)}{h} = \lim_{h \to 0} (12 - 3\alpha^2 - 3\alpha h - h^2) = 12 - 3\alpha^2 \text{ ft/s}$$
  (2) Momentary stop occurs when $v(t) = 0$:
  $$12 - 3t^2 = 0 \implies t^2 = 4 \implies t = 2 \text{ seconds (since } t \ge 0\text{)}$$
* **中文详解:** 瞬时速度是位置差商当 $h \to 0$ 时的极限。展开分子的三次方并约去公因式 $h$，求得瞬时速度表达式为 $12 - 3\alpha^2$。令瞬时速度等于 0，结合时间非负的实际意义解得 $t = 2$ 秒时物体瞬时停止。

---

### 3.2 The Derivative (导数的概念与性质)

#### 1. 导数的严格定义 (Definition of the Derivative)
* **定义 (Definition):** 函数 $f$ 在 $x$ 处的**导数** (Derivative) 记作 $f'(x)$（读作 "f prime"），其定义为差商的极限：
  $$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$
* **可导性 (Differentiability):** 若该极限存在，则称函数 $f$ 在 $x$ 处**可导** (differentiable)。求导的过程称为**微分** (differentiation)。
* **变化率 (Rate of Change):** 平均变化率 $\frac{\Delta y}{\Delta x} = \frac{f(x_2) - f(x_1)}{x_2 - x_1}$ 当 $\Delta x \to 0$ 时的极限，即为 $y$ 关于 $x$ 的**瞬时变化率** (instantaneous rate of change)。

#### 2. 导数的等价极限表达形式 (Equivalent Forms)
$$f'(c) = \lim_{h \to 0} \frac{f(c+h) - f(c)}{h} = \lim_{\Delta x \to 0} \frac{f(c+\Delta x) - f(c)}{\Delta x} = \lim_{x \to c} \frac{f(x) - f(c)}{x - c}$$

#### 3. 莱布尼茨记号与微分算子 (Leibniz Notation & Operators)
* 导数常用的记号包括：$f'(x)$， $y'$， $D_x f(x)$， $\frac{dy}{dx}$， $\frac{d}{dx} f(x)$。
* $D_x$ 或 $\frac{d}{dx}$ 称为**微分算子** (differentiation operator)。

#### 4. 可导与连续的关系 (Differentiability Implies Continuity)
* **核心定理 (Theorem):** 若 $f(x)$ 在点 $c$ 处**可导**，则 $f(x)$ 在点 $c$ 处**必连续**。
* **定理证明 (Proof):**
  要证 $\lim_{x \to c} f(x) = f(c)$，等价于证增量 $\lim_{\Delta x \to 0} \Delta y = 0$。
  $$\lim_{\Delta x \to 0} \Delta y = \lim_{\Delta x \to 0} \left( \frac{\Delta y}{\Delta x} \cdot \Delta x \right) = \left( \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} \right) \cdot \left( \lim_{\Delta x \to 0} \Delta x \right) = f'(c) \cdot 0 = 0$$
  故 $f(x)$ 在 $c$ 处连续。
* **避坑要领 (Converse is False):** **连续不一定可导**！经典反例：$f(x) = |x|$ 在 $x = 0$ 处连续，但左导数 $(-1)$ 与右导数 $(+1)$ 不相等，故不可导。

#### 5. 函数不可导的典型几何特征 (Non-differentiable Points)
1. **尖点/角点 (Corner / Cusp):** 图像在该点左右两侧切线斜率不相等（如 $y = |x|$ 在 $x = 0$ 处）。
2. **垂直切线 (Vertical Tangent):** 极限 $\lim_{h \to 0} \frac{f(c+h)-f(c)}{h} = \infty$。
3. **间断点 (Discontinuity):** 函数在该点不连续，则必然不可导。

---

#### 🌟 课件例题与详解 (Lecture Examples & Solutions)

##### 【课件例题 3】用导数定义求三次多项式导数
**Problem:** Differentiate $f(x) = x^3 + 7x$ using the limit definition.
* **Process (解题步骤):**
  $$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h} = \lim_{h \to 0} \frac{[(x+h)^3 + 7(x+h)] - [x^3 + 7x]}{h}$$
  $$= \lim_{h \to 0} \frac{(x^3 + 3x^2 h + 3xh^2 + h^3 + 7x + 7h) - (x^3 + 7x)}{h}$$
  $$= \lim_{h \to 0} \frac{3x^2 h + 3xh^2 + h^3 + 7h}{h} = \lim_{h \to 0} (3x^2 + 3xh + h^2 + 7) = 3x^2 + 7$$
* **中文详解:** 严格按照导数定义展开 $(x+h)^3$，消去不含 $h$ 的项 $x^3$ 与 $7x$ 后，提取公因式 $h$ 约分，再令 $h \to 0$ 即可求得导数 $3x^2 + 7$。

##### 【课件例题 4】导数定义的极限变式计算
**Problem:** Suppose $f'(c) = 2$. Evaluate (a) $\lim_{h \to 0} \frac{f(c+2h) - f(c)}{h}$ and (b) $\lim_{h \to 0} \frac{f(c+h) - f(c-h)}{h}$.
* **Process (解题步骤):**
  (a) Let $p = 2h$. As $h \to 0$, $p \to 0$:
  $$\lim_{h \to 0} \frac{f(c+2h) - f(c)}{h} = \lim_{p \to 0} \frac{f(c+p) - f(c)}{p/2} = 2 \lim_{p \to 0} \frac{f(c+p) - f(c)}{p} = 2 f'(c) = 2(2) = 4$$
  (b) Add and subtract $f(c)$ in the numerator:
  $$\lim_{h \to 0} \frac{f(c+h) - f(c-h)}{h} = \lim_{h \to 0} \left[ \frac{f(c+h) - f(c)}{h} + \frac{f(c) - f(c-h)}{h} \right]$$
  For the second term, let $t = -h \implies \lim_{t \to 0} \frac{f(c+t) - f(c)}{t} = f'(c)$:
  $$= f'(c) + f'(c) = 2 f'(c) = 2(2) = 4$$
* **中文详解:** (a) 通过换元 $p = 2h$ 将分母配凑成与分子括号内相同的步长 $2h$，从而导出 $2f'(c)$；(b) 采用“拆项加减 $f(c)$”的标准技巧，将其拆分为左侧导数与右侧导数之和，得到 $2f'(c)$。

##### 【课件例题 5】分段函数的导数计算
**Problem:** Let $f(x) = \begin{cases} \frac{1 - \cos x}{x} & \text{if } x \neq 0 \\ 0 & \text{if } x = 0 \end{cases}$. Find $f'(x)$ for every $x$.
* **Process (解题步骤):**
  1. For $x \neq 0$, apply the Quotient Rule:
     $$f'(x) = \frac{(1-\cos x)' \cdot x - (1-\cos x) \cdot (x)'}{x^2} = \frac{\sin x \cdot x - (1 - \cos x)}{x^2} = \frac{x\sin x + \cos x - 1}{x^2}$$
  2. For $x = 0$, apply the definition of the derivative:
     $$f'(0) = \lim_{x \to 0} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0} \frac{\frac{1-\cos x}{x} - 0}{x} = \lim_{x \to 0} \frac{1-\cos x}{x^2}$$
     Rationalize the numerator:
     $$\lim_{x \to 0} \frac{(1-\cos x)(1+\cos x)}{x^2(1+\cos x)} = \lim_{x \to 0} \frac{\sin^2 x}{x^2(1+\cos x)} = \left(\lim_{x \to 0} \frac{\sin x}{x}\right)^2 \cdot \lim_{x \to 0} \frac{1}{1+\cos x} = 1^2 \cdot \frac{1}{2} = \frac{1}{2}$$
     Conclusion:
     $$f'(x) = \begin{cases} \frac{x\sin x + \cos x - 1}{x^2} & \text{if } x \neq 0 \\ \frac{1}{2} & \text{if } x = 0 \end{cases}$$
* **中文详解:** 当 $x \neq 0$ 时，直接使用商法则求导；当 $x = 0$ 时，标准求导法则失效，必须回归导数极限定义，结合分子有理化与第一重要极限 $\lim_{x \to 0} \frac{\sin x}{x} = 1$ 计算得出 $f'(0) = 1/2$。

---

### 3.3 Rules for Finding Derivatives (求导法则与线性算子)

#### 1. 基础初等函数求导法则 (Basic Rules)
* **常数法则 (Constant Function Rule):** $D_x(k) = 0$
* **恒等函数法则 (Identity Function Rule):** $D_x(x) = 1$
* **幂法则 (Power Rule):** 对任意实数 $r$，有：
  $$D_x(x^r) = r x^{r-1}$$
  * *推导补充:* 当 $r = n$ 为正整数时，利用二项式展开定理证明；当 $r = -n$ 为负整数时，利用商法则证明。

#### 2. 导数的线性运算与算子性质 (Linearity)
微分算子 $D_x$ 是一个**线性算子** (Linear Operator)，满足：
* **常数倍法则 (Constant Multiple Rule):** $[k f(x)]' = k f'(x)$
* **和差法则 (Sum & Difference Rules):** $[f(x) \pm g(x)]' = f'(x) \pm g'(x)$

#### 3. 乘法与商法则 (Product and Quotient Rules)
* **乘法法则 (Product Rule):**
  $$(f \cdot g)'(x) = f(x)g'(x) + f'(x)g(x)$$
* **商法则 (Quotient Rule):**
  $$\left( \frac{f}{g} \right)'(x) = \frac{g(x)f'(x) - f(x)g'(x)}{[g(x)]^2} \quad (g(x) \neq 0)$$
  * *特例:* $\left( \frac{1}{g} \right)' = \frac{-g'}{g^2}$

---

#### 🌟 课件例题与详解 (Lecture Examples & Solutions)

##### 【课件例题 6】切线方程的导数应用
**Problem:** Find the equation of the tangent line to the curve $y = 1/x$ at $x = 2$.
* **Process (解题步骤):**
  1. Point on the curve: At $x = 2$, $y = 1/2 \implies (2, 1/2)$.
  2. Derivative & Slope: $\frac{dy}{dx} = (x^{-1})' = -x^{-2} = -\frac{1}{x^2}$.
     At $x = 2$, $m_{\text{tan}} = -\frac{1}{2^2} = -\frac{1}{4}$.
  3. Tangent Line Equation: $y - \frac{1}{2} = -\frac{1}{4}(x - 2) \implies y = -\frac{1}{4}x + 1$.
* **中文详解:** 利用幂法则算出导函数 $y' = -1/x^2$，代入 $x=2$ 求得切线斜率 $m = -1/4$，结合切点 $(2, 1/2)$ 用点斜式导出切线方程。

---

### 3.4 Derivatives of Trigonometric Functions (三角函数的导数)

#### 1. 六大三角函数导数公式汇总 (Trigonometric Derivatives)
1. $D_x(\sin x) = \cos x$
2. $D_x(\cos x) = -\sin x$
3. $D_x(\tan x) = \sec^2 x$
4. $D_x(\cot x) = -\csc^2 x$
5. $D_x(\sec x) = \sec x \tan x$
6. $D_x(\csc x) = -\csc x \cot x$

#### 2. 正弦导数公式的严格极限证明 (Proof of $(\sin x)' = \cos x$)
由导数定义与和角公式：
$$D_x(\sin x) = \lim_{h \to 0} \frac{\sin(x+h) - \sin x}{h} = \lim_{h \to 0} \frac{\sin x \cos h + \cos x \sin h - \sin x}{h}$$
$$= (-\sin x) \cdot \lim_{h \to 0} \frac{1-\cos h}{h} + (\cos x) \cdot \lim_{h \to 0} \frac{\sin h}{h}$$
利用极限 Theorem B: $\lim_{h \to 0} \frac{1-\cos h}{h} = 0$ 与 $\lim_{h \to 0} \frac{\sin h}{h} = 1$：
$$= (-\sin x) \cdot 0 + (\cos x) \cdot 1 = \cos x$$

---

#### 🌟 课件例题与详解 (Lecture Examples & Solutions)

##### 【课件例题 7】三角函数乘积与商的导数
**Problem:** Find the derivatives of (a) $y = \tan x \sec x$ and (b) $y = \frac{1-\cos x}{x}$.
* **Process (解题步骤):**
  (a) By Product Rule:
  $$D_x(y) = D_x(\tan x) \cdot \sec x + \tan x \cdot D_x(\sec x) = \sec^2 x \cdot \sec x + \tan x \cdot (\sec x \tan x) = \sec^3 x + \tan^2 x \sec x$$
  (b) By Quotient Rule (for $x \neq 0$):
  $$\frac{dy}{dx} = \frac{(1-\cos x)' \cdot x - (1-\cos x) \cdot (x)'}{x^2} = \frac{\sin x \cdot x - (1 - \cos x)}{x^2} = \frac{x\sin x + \cos x - 1}{x^2}$$
* **中文详解:** (a) 题应用乘法法则并代入正切与正割的导数公式化简；(b) 题应用商法则并注意分子中由 $(-\cos x)' = \sin x$ 带来的变号。

---

### 3.5 The Chain Rule (复合函数求导的链式法则)

#### 1. 链式法则定理 (The Chain Rule)
* **定理 (Theorem):** 设 $y = f(u)$ 且 $u = g(x)$。若 $g$ 在 $x$ 处可导，且 $f$ 在 $u = g(x)$ 处可导，则复合函数 $y = f(g(x))$ 在 $x$ 处可导，其导数为：
  $$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} \quad \text{或} \quad (f \circ g)'(x) = f'(g(x)) \cdot g'(x)$$
* **口诀法则:** 复合函数的导数等于“外层函数对中间变量的导数”乘以“中间变量对自变量的导数”。

#### 2. 多层复合扩展 (Multiple Composites)
若 $y = f(u), u = g(v), v = h(x)$，则：
$$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dv} \cdot \frac{dv}{dx}$$

---

#### 🌟 课件例题与详解 (Lecture Examples & Solutions)

##### 【课件例题 8】复合分式幂函数求导
**Problem:** Find $\frac{dy}{dx}$ for $y = \frac{1}{(2x^5 - 7)^3}$.
* **Process (解题步骤):**
  Rewrite $y = (2x^5 - 7)^{-3}$. Let $u = 2x^5 - 7 \implies y = u^{-3}$:
  $$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} = (-3u^{-4}) \cdot (10x^4) = -3(2x^5 - 7)^{-4} \cdot (10x^4) = \frac{-30x^4}{(2x^5 - 7)^4}$$
* **中文详解:** 避开繁琐的商法则，将分式写成负指数幂 $u^{-3}$ 的形式，再利用链式法则先对外层求导得 $-3u^{-4}$，再乘以内层求导得 $10x^4$。

##### 【课件例题 9】三层复合三角函数求导
**Problem:** Find $D_x(\sin(\cos(x^2)))$.
* **Process (解题步骤):**
  Identify inner and outer functions: $y = \sin u, u = \cos v, v = x^2$.
  $$D_x(\sin(\cos(x^2))) = \cos(\cos(x^2)) \cdot D_x(\cos(x^2))$$
  $$= \cos(\cos(x^2)) \cdot (-\sin(x^2)) \cdot D_x(x^2) = \cos(\cos(x^2)) \cdot (-\sin(x^2)) \cdot (2x) = -2x \cos(\cos(x^2)) \sin(x^2)$$
* **中文详解:** 从最外层正弦函数开始层层剥离：正弦变余弦 $\cos(\cos(x^2))$，乘以中间层余弦变负正弦 $-\sin(x^2)$，再乘以最内层二次方导数 $2x$。

##### 【课件例题 10】抽象复合函数求导
**Problem:** Assume $F$ is differentiable. Express the derivatives of (a) $\frac{d}{dx}[F(x^3)]$ and (b) $\frac{d}{dx}[\{F(x)\}^3]$.
* **Process (解题步骤):**
  (a) Inner function is $u = x^3$, outer is $F(u)$:
      $$\frac{d}{dx}[F(x^3)] = F'(x^3) \cdot \frac{d}{dx}(x^3) = 3x^2 F'(x^3)$$
  (b) Inner function is $u = F(x)$, outer is $u^3$:
      $$\frac{d}{dx}[\{F(x)\}^3] = 3\{F(x)\}^2 \cdot \frac{d}{dx}F(x) = 3\{F(x)\}^2 F'(x)$$
* **中文详解:** 辨析复合顺序：(a) 题内层是 $x^3$，先对外层 $F$ 求导得 $F'(x^3)$ 再乘内层 $3x^2$；(b) 题外层是立方，先对外层求导得 $3[F(x)]^2$ 再乘内层 $F'(x)$。

---

### 3.6 Higher-Order Derivatives (高阶导数与物理应用)

#### 1. 高阶导数记号 (Higher-Order Derivative Notations)
* 一阶导数 (First): $f'(x) = y' = D_x y = \frac{dy}{dx}$
* 二阶导数 (Second): $f''(x) = y'' = D_x^2 y = \frac{d^2 y}{dx^2}$
* 三阶导数 (Third): $f'''(x) = y''' = D_x^3 y = \frac{d^3 y}{dx^3}$
* $n$ 阶导数 ($n$-th): $f^{(n)}(x) = y^{(n)} = D_x^n y = \frac{d^n y}{dx^n}$

#### 2. 运动学物理应用 (Velocity & Acceleration)
若质点的位置函数为 $s = f(t)$：
* **速度 (Velocity):** $v(t) = \frac{ds}{dt} = s'(t)$
* **加速度 (Acceleration):** $a(t) = \frac{dv}{dt} = \frac{d^2s}{dt^2} = s''(t)$

---

#### 🌟 课件例题与详解 (Lecture Examples & Solutions)

##### 【课件例题 11】三角高阶导数的周期规律
**Problem:** Let $y = \sin 2x$. Find $\frac{d^3y}{dx^3}, \frac{d^4y}{dx^4}$, and $\frac{d^{12}y}{dx^{12}}$.
* **Process (解题步骤):**
  $$\frac{dy}{dx} = 2\cos 2x$$
  $$\frac{d^2y}{dx^2} = -2^2\sin 2x$$
  $$\frac{d^3y}{dx^3} = -2^3\cos 2x = -8\cos 2x$$
  $$\frac{d^4y}{dx^4} = 2^4\sin 2x = 16\sin 2x$$
  Observe that every 4 derivatives, the trigonometric function returns to $\sin 2x$ with a multiplier of $2^n$:
  $$\frac{d^{12}y}{dx^{12}} = 2^{12}\sin 2x = 4096\sin 2x$$
* **中文详解:** 计算前四阶导数发现周期规律：阶数每增加 4，三角函数部分回归原式 $\sin 2x$，系数每次求导乘以 2。因为 12 是 4 的倍数，故十二阶导数为 $2^{12}\sin 2x$。

##### 【课件例题 12】质点运动的速度与加速度
**Problem:** An object moves along a coordinate line with $s(t) = 2t^2 - 12t + 8$ (in cm, $t \ge 0$). Find its velocity and acceleration.
* **Process (解题步骤):**
  $$v(t) = \frac{ds}{dt} = (2t^2 - 12t + 8)' = 4t - 12 \text{ cm/s}$$
  $$a(t) = \frac{d^2s}{dt^2} = v'(t) = (4t - 12)' = 4 \text{ cm/s}^2$$
* **中文详解:** 一阶导数代表瞬时速度 $v(t) = 4t - 12$；二阶导数代表加速度 $a(t) = 4$（为恒定加速度）。
