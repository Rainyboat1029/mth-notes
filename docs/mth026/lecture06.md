# Chapter 3 Derivatives: 指数、对数、反三角函数导数，隐微分与相关变化率 知识详解与例题精解

## 第一部分：本节课知识详解 (Lecture 6 Summary)

### 3.9 Derivatives of Exponential and Logarithmic Functions (指数函数与对数函数的导数)

#### 1. 单调性定理与反函数存在性 (Monotonicity Theorem & Existence of Inverse Functions)
* **定理内容 (Monotonicity Theorem):** 若函数 $f(x)$ 在区间 $I$ 上连续且在内部可导，只要其导数 $f'(x) > 0$（或 $f'(x) < 0$）对内部所有 $x$ 恒成立，则 $f(x)$ 在区间 $I$ 上是严格单调递增（或递减）的，且必存在反函数 $f^{-1}(x)$。
* **单调性与反函数的联系:** 严格单调性是反函数存在的充分条件，原函数与反函数具有相同的单调性。

---

#### 🌟 课件例题与详解 (Lecture Examples & Solutions)

##### 【课件例题 1】证明反函数的存在性
**Problem:** Show that $f(x) = x^5 + 2x + 1$ has an inverse.
* **Process (证明步骤):**
  Compute the derivative of $f(x)$:
  $$f'(x) = D_x(x^5 + 2x + 1) = 5x^4 + 2$$
  Analyze the sign of $f'(x)$:
  Since $x^4 \ge 0$ for all $x \in \mathbb{R}$, we have $5x^4 + 2 \ge 2 > 0$ for all $x \in \mathbb{R}$.
  By the Monotonicity Theorem, $f(x)$ is strictly increasing on $(-\infty, \infty)$ and therefore possesses an inverse function $f^{-1}(x)$.
* **中文详解:** 对多项式求导得到 $f'(x) = 5x^4 + 2$。由于偶次方 $x^4 \ge 0$，因此 $f'(x) \ge 2 > 0$ 在全实数域恒成立。根据单调性定理，函数严格单调递增，故必存在反函数。

---

#### 2. 反函数求导定理 (Inverse Function Theorem, IFT)
* **定理内容 (Inverse Function Theorem):** 设 $f(x)$ 在区间 $I$ 上连续、严格单调且可导。若在某点 $x$ 处 $f'(x) \neq 0$，则其反函数 $f^{-1}$ 在对应的 $y = f(x)$ 点处可导，其导数为原函数在该点导数的倒数：
  $$(f^{-1})'(y) = \frac{1}{f'(x)} \quad \text{或写作} \quad \frac{dx}{dy} = \frac{1}{\frac{dy}{dx}}$$
* **避坑要点 (Caution):** 求解 $(f^{-1})'(y_0)$ 时，分母中代入的是 $y_0$ 对应的**原函数自变量 $x_0$**（满足 $f(x_0) = y_0$），而**绝不是**直接将 $y_0$ 代入原导数！即 $(f^{-1})'(y_0) \neq \frac{1}{f'(y_0)}$。

---

##### 【课件例题 2】应用反函数求导定理
**Problem:** Let $f(x) = x^5 + 2x + 1$. Find $(f^{-1})'(4)$.
* **Process (解题步骤):**
  1. Find the point $x$ corresponding to $y = 4$:
     Set $f(x) = 4 \implies x^5 + 2x + 1 = 4 \implies x^5 + 2x - 3 = 0$.
     By inspection, $x = 1$ is a real solution, so $f(1) = 4$ and $f^{-1}(4) = 1$.
  2. Compute the derivative of $f(x)$ at $x = 1$:
     $f'(x) = 5x^4 + 2 \implies f'(1) = 5(1)^4 + 2 = 7$.
  3. Apply the Inverse Function Theorem:
     $$(f^{-1})'(4) = \frac{1}{f'(f^{-1}(4))} = \frac{1}{f'(1)} = \frac{1}{7}$$
* **中文详解:** 
  1. 第一步：先找出使 $f(x) = 4$ 的自变量 $x$。观察易得 $x = 1$，即 $f^{-1}(4) = 1$。
  2. 第二步：计算原函数在 $x = 1$ 处的导数 $f'(1) = 7 \neq 0$。
  3. 第三步：代入倒数公式得 $(f^{-1})'(4) = \frac{1}{7}$。

---

#### 3. 指数与对数函数的求导公式 (Derivatives of Logarithmic and Exponential Functions)
* **核心求导公式 (Core Formulas):**
  $$\begin{aligned}
  D_x(\ln x) &= \frac{1}{x} \quad (x > 0) & D_x(e^x) &= e^x \\
  D_x(\log_a x) &= \frac{1}{x \ln a} \quad (a > 0, a \neq 1) & D_x(a^x) &= a^x \ln a \quad (a > 0)
  \end{aligned}$$
* **结合链式法则的复合形式 (Chain Rule Extensions):**
  $$(\ln u(x))' = \frac{u'(x)}{u(x)}, \quad (e^{u(x)})' = e^{u(x)} u'(x)$$

---

### 3.10 Derivatives of Inverse Trigonometric Functions (反三角函数的导数)

#### 1. 三大核心反三角函数导数公式
$$\begin{aligned}
D_x(\arcsin x) &= \frac{1}{\sqrt{1-x^2}} \quad (-1 < x < 1) \\
D_x(\arccos x) &= -\frac{1}{\sqrt{1-x^2}} \quad (-1 < x < 1) \\
D_x(\arctan x) &= \frac{1}{1+x^2} \quad (-\infty < x < \infty)
\end{aligned}$$

---

##### 【课件推导】$\arcsin x$ 导数公式的严格证明
**Proof (证明步骤):**
1. Let $y = \arcsin x$. By definition, $x = \sin y$ where $y \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$.
2. By the Inverse Function Theorem:
   $$\frac{dy}{dx} = \frac{1}{\frac{dx}{dy}} = \frac{1}{\cos y}$$
3. Since $y \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$, $\cos y > 0$, so $\cos y = \sqrt{1 - \sin^2 y} = \sqrt{1 - x^2}$.
4. Substituting $\cos y = \sqrt{1 - x^2}$ yields:
   $$D_x(\arcsin x) = \frac{1}{\sqrt{1 - x^2}}$$

---

### 3.7 Implicit Differentiation & Logarithmic Differentiation (隐函数求导与对数求导法)

#### 1. 显函数与隐函数的概念 (Explicit vs. Implicit Functions)
* **显函数 (Explicit Function):** 形如 $y = f(x)$，将因变量 $y$ 显式地用含自变量 $x$ 的表达式表示。
* **隐函数 (Implicit Function):** 形如 $F(x, y) = 0$，因变量 $y$ 与自变量 $x$ 混杂在方程中，难以或无法解出显式表达式 $y = f(x)$。

#### 2. 隐函数求导法 (Implicit Differentiation Procedure)
1. **两端求导:** 将方程 $F(x, y) = 0$ 两端同时对自变量 $x$ 求导。
2. **应用链式法则:** 对于包含 $y$ 的项，将其看作 $x$ 的复合函数 $y(x)$，使用链式法则求导（即对 $y$ 求导后必须乘上因子的导数 $\frac{dy}{dx}$ 或 $y'$）。
3. **整理解出 $y'$:** 将所有包含 $y'$ 的项移到方程左边，其余项移到右边，提取公因式解出 $y'$。

---

##### 【课件例题 3】多项式隐函数求导
**Problem:** Find $y'$ if $y^3 + 7y - x^3 = 0$.
* **Process (解题步骤):**
  Differentiate both sides with respect to $x$:
  $$D_x(y^3) + D_x(7y) - D_x(x^3) = D_x(0)$$
  Apply chain rule to $y$-terms:
  $$3y^2 y' + 7y' - 3x^2 = 0$$
  Factor out $y'$:
  $$y'(3y^2 + 7) = 3x^2 \implies y' = \frac{3x^2}{3y^2 + 7}$$
* **中文详解:** 方程两端对 $x$ 求导，$y^3$ 求导为 $3y^2 y'$，$7y$ 求导为 $7y'$。合并 $y'$ 提取公因式，直接解得 $y' = \frac{3x^2}{3y^2 + 7}$。

---

##### 【课件例题 4】隐函数在给定点处的切线斜率
**Problem:** Find $y'$ at the point $(0, 1)$ for $y^3 - x y^2 - \cos(xy) = 0$.
* **Process (解题步骤):**
  Differentiate both sides implicitly with respect to $x$:
  $$3y^2 y' - \left( y^2 + 2xy y' \right) - \left[ -\sin(xy) \cdot (y + xy') \right] = 0$$
  $$3y^2 y' - y^2 - 2xy y' + \sin(xy)(y + xy') = 0$$
  Substitute $x = 0$ and $y = 1$ directly into the differentiated equation:
  $$3(1)^2 y' - (1)^2 - 2(0)(1)y' + \sin(0)(1 + 0 \cdot y') = 0$$
  $$3y' - 1 - 0 + 0 = 0 \implies 3y' = 1 \implies y' = \frac{1}{3}$$
* **中文详解:** 求导后再将坐标 $(0, 1)$ 直接代入算斜率，比先解出符号表达式再代入更为高效。中间项 $xy^2$ 与 $\cos(xy)$ 需要分别应用乘积法则和链式法则。

---

#### 3. 对数求导法 (Logarithmic Differentiation)
* **适用场景:** 
  1. **幂指函数:** 底数与指数均含有自变量 $x$ 的函数，形如 $y = f(x)^{g(x)}$。
  2. **复杂代数式:** 包含大量连乘、连除、乘方、开方的分式结构。
* **解题四步法:**
  1. 两端取自然对数: $\ln y = \ln f(x)$
  2. 利用对数性质将乘除拆为加减，将指数降为系数
  3. 两端对 $x$ 隐求导: $\frac{1}{y} y' = \dots$
  4. 两端同乘以 $y$ 解出 $y'$

---

##### 【课件例题 5】$y = x^x$ ($x > 0$) 的两种求导法
* **Method 1 (转化为指数形式):**
  Rewrite $y = x^x$ using exponential identity $x = e^{\ln x}$:
  $$y = (e^{\ln x})^x = e^{x \ln x}$$
  Apply chain rule and product rule:
  $$y' = e^{x \ln x} \cdot D_x(x \ln x) = x^x \left( 1 \cdot \ln x + x \cdot \frac{1}{x} \right) = x^x(\ln x + 1)$$
* **Method 2 (对数求导法):**
  Take natural logarithm on both sides:
  $$\ln y = \ln(x^x) = x \ln x$$
  Differentiate implicitly with respect to $x$:
  $$\frac{1}{y} y' = D_x(x \ln x) = 1 \cdot \ln x + x \cdot \frac{1}{x} = \ln x + 1$$
  Multiply by $y$:
  $$y' = y(\ln x + 1) = x^x(\ln x + 1)$$
* **中文详解:** 两种方法均非常经典。方法一利用恒等式 $x^x = e^{x \ln x}$；方法二先取自然对数化简再隐求导，结果完全一致。

---

##### 【课件例题 6】幂指函数 $y = (x^2+1)^{\sin x}$ 求导
**Problem:** Find $\frac{dy}{dx}$ for $y = (x^2 + 1)^{\sin x}$.
* **Process (解题步骤):**
  Take natural logarithm on both sides:
  $$\ln y = \ln (x^2 + 1)^{\sin x} = \sin x \cdot \ln(x^2 + 1)$$
  Differentiate implicitly with respect to $x$:
  $$\frac{1}{y} \frac{dy}{dx} = D_x(\sin x) \cdot \ln(x^2 + 1) + \sin x \cdot D_x \ln(x^2 + 1)$$
  $$\frac{1}{y} \frac{dy}{dx} = \cos x \ln(x^2 + 1) + \sin x \cdot \frac{2x}{x^2 + 1}$$
  Multiply by $y = (x^2 + 1)^{\sin x}$:
  $$\frac{dy}{dx} = (x^2 + 1)^{\sin x} \left[ \cos x \ln(x^2 + 1) + \frac{2x \sin x}{x^2 + 1} \right]$$
* **中文详解:** 取对数后，右边变为 $\sin x \cdot \ln(x^2+1)$，求导时使用乘积法则，$\ln(x^2+1)$ 复合项求导得到 $\frac{2x}{x^2+1}$。最后乘回 $y$ 的原表达式。

---

##### 【课件例题 7】复杂根式分式的对数拆解求导
**Problem:** Find $D_x \left( \frac{\sqrt{1-x^2}}{(x+1)^{2/3}} \right)$.
* **Process (解题步骤):**
  Let $y = \frac{\sqrt{1-x^2}}{(x+1)^{2/3}} = \frac{(1-x^2)^{1/2}}{(x+1)^{2/3}}$.
  Take natural logarithm on both sides:
  $$\ln y = \ln \left( \frac{(1-x^2)^{1/2}}{(x+1)^{2/3}} \right) = \frac{1}{2}\ln(1-x^2) - \frac{2}{3}\ln(x+1)$$
  Differentiate with respect to $x$:
  $$\frac{y'}{y} = \frac{1}{2} \cdot \frac{-2x}{1-x^2} - \frac{2}{3} \cdot \frac{1}{x+1} = -\frac{x}{1-x^2} - \frac{2}{3(x+1)}$$
  Multiply by $y$:
  $$y' = \frac{\sqrt{1-x^2}}{(x+1)^{2/3}} \left[ -\frac{x}{1-x^2} - \frac{2}{3(x+1)} \right]$$
* **中文详解:** 对于分子分母均包含根式和乘方的复杂分式，先取对数将其拆解为加减法，避免了繁琐的商法则求导。

---

### 3.8 Related Rates (相关变化率)

#### 1. 概念与解题步骤 (Systematic Procedure)
* **概念定义:** 相关变化率问题研究的是两个或多个随时间 $t$ 变化的物理量之间的变化率联系。
* **解题规范五步法:**
  1. **画图与设变量 (Diagram & Variables):** 建立直角坐标系或几何图形，用字母表示随时间 $t$ 变化的变量。
  2. **明确已知与所求 (Given & Wanted):** 明确给出已知变化率（如 $\frac{dx}{dt}$）与特定时刻的条件，指出要求解的变化率（如 $\frac{dy}{dt}$）。
  3. **建立几何/物理关系方程 (Relating Equation):** 利用勾股定理、相似三角形、体积公式等建立变量间的几何或物理等式。
  4. **对时间 $t$ 隐求导 (Differentiate w.r.t $t$):** 方程两端同时对时间 $t$ 隐求导（应用链式法则）。
  5. **代入数值求解 (Substitute & Solve):** 将特定时刻的已知数值代入求导后的方程，解出目标变化率。

---

#### 🌟 课件经典应用例题与解析

##### 【课件例题 8】气球上升与观察者距离变化率 (勾股定理模型)
**Problem:** A small balloon is released 150 feet away from an observer on level ground. It rises straight up at 8 ft/s. How fast is the distance from observer to balloon increasing when the balloon is 50 feet high?
* **Process (解题步骤):**
  1. Variables: Let $h(t)$ be the height of the balloon and $s(t)$ be the distance from the observer to the balloon.
  2. Given: $\frac{dh}{dt} = 8\text{ ft/s}$.
  3. Wanted: $\frac{ds}{dt}$ at the instant when $h = 50\text{ ft}$.
  4. Relating equation (Pythagorean theorem):
     $$s^2 = h^2 + (150)^2$$
  5. Differentiate implicitly with respect to $t$:
     $$2s \frac{ds}{dt} = 2h \frac{dh}{dt} \implies s \frac{ds}{dt} = h \frac{dh}{dt}$$
  6. Calculate $s$ when $h = 50$:
     $$s = \sqrt{50^2 + 150^2} = \sqrt{2500 + 22500} = \sqrt{25000} = 50\sqrt{10}\text{ ft}$$
  7. Substitute values into the rate equation:
     $$(50\sqrt{10}) \frac{ds}{dt} = (50)(8) \implies \frac{ds}{dt} = \frac{400}{50\sqrt{10}} = \frac{8}{\sqrt{10}} = \frac{4\sqrt{10}}{5}\text{ ft/s}$$
* **中文详解:** 建立直角三角形，斜边 $s$ 与直角边 $h$ 满足勾股定理 $s^2 = h^2 + 150^2$。两端对时间 $t$ 隐求导得 $s \frac{ds}{dt} = h \frac{dh}{dt}$。代入 $h=50$ 时求得的 $s = 50\sqrt{10}$，解得距离增加速率为 $\frac{4\sqrt{10}}{5}\text{ ft/s}$。

---

##### 【课件例题 9】圆锥容器注水水面上升速率 (相似三角形与体积模型)
**Problem:** Water is poured into a conical tank at $8\text{ ft}^3/\text{min}$. The tank is 12 ft high and has radius 6 ft at the top. How fast is the water level rising when water is 4 ft deep?
* **Process (解题步骤):**
  1. Variables: Let $V(t)$ be the volume of water, $h(t)$ be the water depth, and $r(t)$ be the top radius of water.
  2. Given: $\frac{dV}{dt} = 8\text{ ft}^3/\text{min}$.
  3. Wanted: $\frac{dh}{dt}$ at the instant when $h = 4\text{ ft}$.
  4. Use similar triangles to eliminate $r$:
     $$\frac{r}{h} = \frac{6}{12} \implies r = \frac{h}{2}$$
  5. Express volume in terms of $h$ only:
     $$V = \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi \left(\frac{h}{2}\right)^2 h = \frac{\pi}{12} h^3$$
  6. Differentiate implicitly with respect to $t$:
     $$\frac{dV}{dt} = \frac{\pi}{12} \cdot 3h^2 \frac{dh}{dt} = \frac{\pi h^2}{4} \frac{dh}{dt}$$
  7. Substitute $h = 4$ and $\frac{dV}{dt} = 8$:
     $$8 = \frac{\pi(4)^2}{4} \frac{dh}{dt} \implies 8 = 4\pi \frac{dh}{dt} \implies \frac{dh}{dt} = \frac{2}{\pi}\text{ ft/min}$$
* **中文详解:** 利用圆锥截面的相似三角形关系 $\frac{r}{h} = \frac{6}{12}$ 将半径消去，得到仅含高度的体积公式 $V = \frac{\pi}{12}h^3$。两端对 $t$ 隐求导得 $\frac{dV}{dt} = \frac{\pi h^2}{4} \frac{dh}{dt}$，代入已知值算出水面上升速率为 $\frac{2}{\pi}\text{ ft/min}$。

---

##### 【课件例题 10】悬崖观察艇视角变化率 (三角函数模型)
**Problem:** A woman on a cliff 250 ft above water watches a motorboat approaching directly below. If the boat approaches at $20\text{ ft/s}$, at what rate is the angle of the telescope changing when the boat is 250 ft from shore?
* **Process (解题步骤):**
  1. Variables: Let $x(t)$ be the distance from the boat to the shore, and $\theta(t)$ be the angle of the telescope.
  2. Given: $\frac{dx}{dt} = -20\text{ ft/s}$ (negative because $x$ is decreasing).
  3. Wanted: $\frac{d\theta}{dt}$ at the instant when $x = 250\text{ ft}$.
  4. Relating equation:
     $$\tan \theta = \frac{x}{250}$$
  5. Differentiate implicitly with respect to $t$:
     $$\sec^2 \theta \frac{d\theta}{dt} = \frac{1}{250} \frac{dx}{dt}$$
  6. Calculate $\theta$ and $\sec^2 \theta$ when $x = 250$:
     $$\tan \theta = \frac{250}{250} = 1 \implies \theta = \frac{\pi}{4} \implies \sec^2\left(\frac{\pi}{4}\right) = 2$$
  7. Substitute values into the rate equation:
     $$2 \frac{d\theta}{dt} = \frac{1}{250}(-20) = -\frac{2}{25} \implies \frac{d\theta}{dt} = -\frac{1}{25} = -0.04\text{ rad/s}$$
* **中文详解:** 建立正切方程 $\tan \theta = \frac{x}{250}$。因为艇朝岸边靠近，距离 $x$ 随时间递减，故已知变化率为负数 $\frac{dx}{dt} = -20$。对 $t$ 隐求导后，代入 $x=250$ 时的 $\theta = \frac{\pi}{4}$ 与 $\sec^2\theta = 2$，算出视角变化率为 $-0.04\text{ rad/s}$。
