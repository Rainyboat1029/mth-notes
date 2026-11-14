# Chapter 4 Applications of the Derivative: 中值定理与洛必达法则 知识详解与例题精解

## 第一部分：本节课知识详解 (Lecture 9 Summary)

### 4.6 Mean Value Theorem for Derivatives (微分中值定理)

#### 1. 罗尔定理 (Rolle's Theorem)

* **定理内容:** 若函数 $f$ 满足
  1. 在闭区间 $[a,b]$ 上连续 (continuous on $[a,b]$)；
  2. 在开区间 $(a,b)$ 内可导 (differentiable on $(a,b)$)；
  3. $f(a)=f(b)$（两端函数值相等），

  则至少存在一点 $c\in(a,b)$，使得
  $$f'(c)=0$$
* **几何意义 (Geometric Meaning):** 若曲线两端点等高，则在两端之间的曲线上至少存在一点，该点的切线是水平的（与 $x$ 轴平行）。这样的点可能不止一个。
* **三个条件缺一不可 (Why Each Hypothesis Matters):**
  * 去掉“$f(a)=f(b)$”：$f(x)=x$ 在 $[0,1]$ 上 $f'\equiv 1\neq 0$；
  * 去掉“在 $(a,b)$ 内可导”：$f(x)=|x|$ 在 $[-1,1]$ 上满足 $f(-1)=f(1)$，但在 $x=0$ 处不可导，且不存在 $f'(c)=0$ 的点；
  * 去掉“在 $[a,b]$ 上连续”：$f(x)=\dfrac{1}{x}$ 在 $[-1,1]$ 上不连续（在 $0$ 处无定义），结论失效。

#### 2. 罗尔定理的证明 (Proof of Rolle's Theorem)

* **证明思路:** 用最值存在定理（Theorem 4.1A）＋临界点定理（Theorem 4.1B）。
  1. 因为 $f$ 在闭区间 $[a,b]$ 上连续，由最值存在定理，$f$ 在 $[a,b]$ 上必取得最大值 $M$ 与最小值 $m$。
  2. **情形一 $M=m$:** 此时 $f$ 为常数函数，$f'(x)=0$ 对一切 $x\in(a,b)$ 成立，结论自然成立（而且强于所需）。
  3. **情形二 $M\neq m$:** 由于 $f(a)=f(b)$，最大值与最小值中至少有一个是在**内部点** $c\in(a,b)$ 处取得的（不可能两个极值都在端点上，否则 $f(a)=f(b)$ 会使 $M=m$）。
  4. 由临界点定理，$f$ 在该内部极值点处导数不存在或为零；而 $f$ 在 $(a,b)$ 内可导，故必有 $f'(c)=0$。$\blacksquare$
* **要点:** 罗尔定理的证明本质上是“极值点必为临界点”＋“两端等高迫使极值点落在内部”。

#### 3. 拉格朗日中值定理 (Mean Value Theorem for Derivatives / Theorem A)

* **定理内容:** 若 $f$ 在 $[a,b]$ 上连续、在 $(a,b)$ 内可导，则至少存在一点 $c\in(a,b)$，使得
  $$\frac{f(b)-f(a)}{b-a}=f'(c)$$
  等价地，
  $$f(b)-f(a)=f'(c)(b-a)$$
* **几何意义 (Geometric Meaning):** 连接两端点 $A(a,f(a))$ 与 $B(b,f(b))$ 的**割线 (secant line)** 的斜率为 $\dfrac{f(b)-f(a)}{b-a}$；定理断言，在 $A$、$B$ 之间的曲线上至少存在一点 $C$，其**切线 (tangent line)** 与割线 $AB$ **平行**。切线可能不止一条。
* **与罗尔定理的关系:** 罗尔定理是拉格朗日中值定理的特例——当 $f(a)=f(b)$ 时，割线斜率为 $0$，中值定理化为 $f'(c)=0$，正是罗尔定理。
* **注意 (Remarks):**
  * 定理只保证 $c$ **存在**，不保证唯一，也不给出 $c$ 的公式；
  * $c$ 必须严格位于开区间 $(a,b)$ 内，端点不算；
  * 两个条件（闭区间连续、开区间可导）缺一不可，下一节的例题 3 会看到“不可导导致结论失效”的例子。

#### 4. 中值定理的证明 (Proof of the MVT via an Auxiliary Function)

* **构造割线:** 过点 $(a,f(a))$ 的割线方程为
  $$y=g(x)=f(a)+m_{\sec}(x-a),\qquad m_{\sec}=\frac{f(b)-f(a)}{b-a}$$
* **构造辅助函数:** 令
  $$s(x)=f(x)-g(x)=f(x)-f(a)-\frac{f(b)-f(a)}{b-a}(x-a)$$
  则 $s(a)=0$，且 $s(b)=f(b)-f(a)-[f(b)-f(a)]=0$，即 $s(a)=s(b)$。
* **对 $s$ 用罗尔定理:** $s$ 在 $[a,b]$ 上连续、在 $(a,b)$ 内可导，且 $s(a)=s(b)$，故存在 $c\in(a,b)$ 使 $s'(c)=0$。而
  $$s'(x)=f'(x)-\frac{f(b)-f(a)}{b-a}$$
  于是 $0=f'(c)-\dfrac{f(b)-f(a)}{b-a}$，即 $f'(c)=\dfrac{f(b)-f(a)}{b-a}$。$\blacksquare$
* **方法要点:** “把要证的等式化为某个辅助函数导数为零”是证明中值定理类命题的通用套路：先减去割线（或减去待定线性函数），再用罗尔定理。

#### 🌟 课件例题与详解 (Lecture Examples & Solutions)

##### 【课件例题 1】平均速度与瞬时速度（中值定理的物理意义）

**Problem:** If $s(t)=t^2-t-2$ is the position of an object moving along a coordinate line, find the average velocity over $[3,6]$ and the time $t$ at which the instantaneous velocity equals the average velocity.

* **Process (解题步骤):**
  1. Instantaneous velocity:
     $$v(t)=s'(t)=2t-1$$
  2. Average velocity over $[3,6]$:
     $$v_{\text{avg}}=\frac{s(6)-s(3)}{6-3}=\frac{(36-6-2)-(9-3-2)}{3}=\frac{28-4}{3}=8$$
  3. Set the instantaneous velocity equal to the average velocity:
     $$2t-1=8\implies t=\frac{9}{2}$$
* **中文详解:** 中值定理的物理版本是：在任何一段时间内，物体的平均速度必在某个瞬间被“瞬时速度”取到。本题中 $s(t)=t^2-t-2$ 是位置函数，求导得瞬时速度 $v(t)=2t-1$；平均速度为 $\frac{s(6)-s(3)}{3}=\frac{28-4}{3}=8$。令 $2t-1=8$ 得 $t=\frac92$，恰好落在区间 $(3,6)$ 内，与中值定理的结论一致。注意中值定理保证这样的 $t$ **至少存在一个**，本题中由于 $v(t)$ 是线性函数，解唯一。

##### 【课件例题 2】验证中值定理并求全部 $c$

**Problem:** Let $f(x)=x^3-x^2-x+1$ on $[-1,2]$. Find all numbers $c$ satisfying the conclusion of the Mean Value Theorem.

* **Process (解题步骤):**
  1. $f$ 是多项式，在 $[-1,2]$ 上连续、在 $(-1,2)$ 内可导，前提成立。
  2. Compute the secant slope:
     $$\frac{f(2)-f(-1)}{2-(-1)}=\frac{3-0}{3}=1$$
     其中 $f(2)=8-4-2+1=3$，$f(-1)=-1-1+1+1=0$。
  3. Derivative:
     $$f'(x)=3x^2-2x-1$$
  4. Solve $f'(c)=1$:
     $$3c^2-2c-1=1\implies 3c^2-2c-2=0\implies c=\frac{2\pm\sqrt{4+24}}{6}=\frac{1\pm\sqrt{7}}{3}$$
  5. Numerically, $c_1=\dfrac{1-\sqrt{7}}{3}\approx-0.55$，$c_2=\dfrac{1+\sqrt{7}}{3}\approx1.22$，两者都落在 $(-1,2)$ 内。
* **中文详解:** 先求端点函数值：$f(2)=3$、$f(-1)=0$，割线斜率为 $\frac{3-0}{3}=1$。再令导数 $f'(x)=3x^2-2x-1$ 等于 $1$，得二次方程 $3c^2-2c-2=0$，用求根公式得 $c=\frac{1\pm\sqrt7}{3}$，约等于 $-0.55$ 与 $1.22$，都在开区间 $(-1,2)$ 内。这说明中值定理中的 $c$ 可以不唯一——本题恰有两个。考试中解出 $c$ 后一定要逐一检查是否落在开区间内，不在的必须舍去。

##### 【课件例题 3】中值定理结论失效的情形（不可导点）

**Problem:** Let $f(x)=x^{2/3}$ on $[-8,27]$. Show that the conclusion of the Mean Value Theorem fails and explain why.

* **Process (解题步骤):**
  1. Compute the derivative:
     $$f'(x)=\frac{2}{3}x^{-1/3}=\frac{2}{3\sqrt[3]{x}},\qquad x\neq 0$$
  2. Compute the secant slope:
     $$\frac{f(27)-f(-8)}{27-(-8)}=\frac{9-4}{35}=\frac{1}{7}$$
     其中 $27^{2/3}=9$，$(-8)^{2/3}=4$。
  3. Solve $f'(c)=\dfrac17$:
     $$\frac{2}{3}c^{-1/3}=\frac{1}{7}\implies c^{-1/3}=\frac{3}{14}\implies c=\left(\frac{14}{3}\right)^3=\frac{2744}{27}\approx101.6$$
  4. 该 $c$ 不在 $(-8,27)$ 内，故不存在满足结论的 $c$：结论确实失效。
  5. 原因：$f$ 在 $x=0$ 处不可导（$f'(x)=\frac{2}{3\sqrt[3]{x}}$ 在 $0$ 处无定义，曲线在该点有垂直切线），中值定理“在 $(a,b)$ 内可导”的条件不满足。
* **中文详解:** 本题是“定理条件缺失导致结论失效”的典型反例。$f(x)=x^{2/3}$ 在 $[-8,27]$ 上连续，但在 $x=0$ 处不可导——导数 $\frac{2}{3\sqrt[3]{x}}$ 在原点趋于无穷，对应图像上的尖点（垂直切线）。形式上解 $f'(c)=\frac17$ 得到的 $c=\left(\frac{14}{3}\right)^3\approx101.6$ 已经跑到区间外面，因此在 $(-8,27)$ 内根本不存在满足要求的点。这提醒我们：**使用中值定理前必须先检查“闭区间连续、开区间可导”这两个条件**；特别是含有 $\sqrt[3]{x}$、$|x|$ 这类在个别点不可导的函数时，要先找出不可导点。

#### 5. 中值定理的三个重要应用 (Three Applications of the MVT)

* **(a) 单调性定理（§4.2 Theorem A）:** 若 $f$ 在区间 $I$ 上连续、在 $I$ 的内部可导：
  * 若对 $I$ 内所有 $x$ 有 $f'(x)>0$，则 $f$ 在 $I$ 上**递增**；
  * 若对 $I$ 内所有 $x$ 有 $f'(x)<0$，则 $f$ 在 $I$ 上**递减**。

  **证明:** 任取 $x_1<x_2$，在 $[x_1,x_2]$ 上用中值定理，存在 $c\in(x_1,x_2)$ 使
  $$f(x_2)-f(x_1)=f'(c)(x_2-x_1)>0$$
  故 $f(x_2)>f(x_1)$，即 $f$ 递增；$f'<0$ 的情形同理。$\blacksquare$

* **(b) 导数相同则相差常数（Theorem B）:** 若 $F'(x)=G'(x)$ 对一切 $x\in(a,b)$ 成立，则存在常数 $C$，使
  $$F(x)=G(x)+C,\qquad x\in(a,b)$$
  即“导数相同的两个函数只相差一个常数”。

  **证明:** 令 $H(x)=F(x)-G(x)$，则 $H'(x)=0$。取定 $x_1\in(a,b)$，令 $C=H(x_1)$；对任意 $x\in(a,b)$，在 $x$ 与 $x_1$ 之间用中值定理，存在 $c$ 使
  $$H(x)-H(x_1)=H'(c)(x-x_1)=0$$
  故 $H(x)=H(x_1)=C$，即 $F(x)=G(x)+C$。$\blacksquare$

* **(c) 证明不等式（MVT 估计法）:** 若已知 $|f'(x)|\le M$ 对区间内一切 $x$ 成立，则由中值定理
  $$|f(b)-f(a)|=|f'(c)|\,|b-a|\le M|b-a|$$
  这是证明形如“$|f(b)-f(a)|\le M(b-a)$”类不等式的标准方法。

---

### 4.7 Indeterminate Forms of Type 0/0 (0/0 型不定式)

#### 1. 什么是不定式 (What "0/0" Really Means)

* **典型问题:** 求下列极限时，分子、分母的极限都是 $0$：
  $$\lim_{x\to 0}\frac{\sin x}{x},\qquad \lim_{x\to 3}\frac{x^2-9}{x^2-x-6},\qquad \lim_{x\to a}\frac{f(x)-f(a)}{x-a}$$
* **为什么不能直接用极限四则运算:** 主极限定理（Theorem 2.3A）要求分母的极限不为 $0$；此处分母极限为 $0$，法则失效。
* **记号的含义:** $\dfrac00$ **不是**数值除法，而是“两个都趋于 $0$ 的函数之比”这一**形式 (form)** 的记号。结果并不确定：可能为 $0$、非零有限数、$\pm\infty$，也可能不存在。例如
  $$\lim_{x\to 0}\frac{x}{x}=1,\qquad \lim_{x\to 0}\frac{x^2}{x}=0,\qquad \lim_{x\to 0}\frac{x}{x^2}=\infty$$
  三者都是 $\frac00$ 型，结果却完全不同——这正是“不定”二字的含义。

#### 2. 洛必达法则（0/0 型，Theorem A）

* **定理内容:** 设
  1. $\displaystyle\lim_{x\to u}f(x)=\lim_{x\to u}g(x)=0$；
  2. 在 $u$ 的某去心邻域内 $f$、$g$ 可导，且 $g'(x)\neq 0$；
  3. $\displaystyle\lim_{x\to u}\frac{f'(x)}{g'(x)}$ 存在（有限或 $\pm\infty$），

  则
  $$\lim_{x\to u}\frac{f(x)}{g(x)}=\lim_{x\to u}\frac{f'(x)}{g'(x)}$$
  其中 $u$ 可以是 $a$、$a^-$、$a^+$、$-\infty$ 或 $+\infty$。
* **要点:** 法则把一个极限**替换**为另一个极限，新极限可能更简单，且可能不再是 $\frac00$ 型；它是“替换”而不是“相等变形”，因此每次使用后都要重新判断形式。
* **常见误解:** 洛必达法则**不是**对分式用商法则求导；正确做法是分子、分母**分别**求导。

#### 3. 使用步骤与三个陷阱 (Procedure and Pitfalls)

* **Step 1 判断形式:** 先代入（或分析）确认是 $\frac00$ 型；不是就不能用。
* **Step 2 分别求导:** 对分子、分母分别求导，得到新的商。
* **Step 3 重新判断:** 若新商仍是 $\frac00$（或 $\frac{\infty}{\infty}$），可再次使用；一旦分子或分母的极限非零，立即停止并直接代入。
* **陷阱 1（不该用而用）:** 第一次求导后已不是不定式，却继续求导（见例题 7）。
* **陷阱 2（越求越复杂）:** 反复求导使式子更繁，此时应改写（见例题 8）。
* **陷阱 3（极限不存在）:** 若 $\lim\dfrac{f'}{g'}$ 不存在（例如振荡），法则失效，但原极限仍可能存在；此时需改用其他方法（夹逼、等价无穷小等）。

#### 🌟 课件例题与详解 (Lecture Examples & Solutions)

##### 【课件例题 4】两个基本极限：$\frac{\sin x}{x}$ 与 $\frac{1-\cos x}{x^2}$

**Problem:** Use L'Hôpital's Rule to show that $\displaystyle\lim_{x\to 0}\frac{\sin x}{x}=1$ and $\displaystyle\lim_{x\to 0}\frac{1-\cos x}{x^2}=\frac12$.

* **Process (解题步骤):**
  1. Both limits are of the form $\dfrac00$.
  2. First limit, one application:
     $$\lim_{x\to 0}\frac{\sin x}{x}\overset{L}{=}\lim_{x\to 0}\frac{\cos x}{1}=1$$
  3. Second limit, two applications:
     $$\lim_{x\to 0}\frac{1-\cos x}{x^2}\overset{L}{=}\lim_{x\to 0}\frac{\sin x}{2x}\overset{L}{=}\lim_{x\to 0}\frac{\cos x}{2}=\frac12$$
* **中文详解:** 两个极限代入后都是 $\frac00$ 型。第一个只需一次洛必达：分子导数为 $\cos x$、分母导数为 $1$，代入 $x=0$ 得 $1$。第二个第一次求导后得到 $\frac{\sin x}{2x}$，仍是 $\frac00$ 型，再用一次得 $\frac{\cos x}{2}$，代入得 $\frac12$。注意第二个极限也可用半角公式 $1-\cos x=2\sin^2\frac{x}{2}$ 直接得出 $\frac12$，两种方法结果一致；$\frac{\sin x}{x}\to 1$ 是重要极限，也是 $\sin x$ 导数公式的基础，应当熟记。

##### 【课件例题 5】$\dfrac{\tan 2x}{\ln(1+x)}$

**Problem:** Find $\displaystyle\lim_{x\to 0}\frac{\tan 2x}{\ln(1+x)}$.

* **Process (解题步骤):**
  1. As $x\to 0$: $\tan 2x\to 0$ and $\ln(1+x)\to 0$, so the form is $\dfrac00$.
  2. Apply L'Hôpital's Rule once:
     $$\lim_{x\to 0}\frac{\tan 2x}{\ln(1+x)}\overset{L}{=}\lim_{x\to 0}\frac{2\sec^2(2x)}{\frac{1}{1+x}}=\lim_{x\to 0}2(1+x)\sec^2(2x)$$
  3. Substitute $x=0$: $2\cdot 1\cdot 1=2$.
* **中文详解:** 分子 $\tan 2x$ 求导时要用链式法则，得 $2\sec^2(2x)$；分母 $\ln(1+x)$ 的导数为 $\frac{1}{1+x}$。把除法化为乘法后得到 $2(1+x)\sec^2(2x)$，此时已不是不定式，直接代入 $x=0$ 得 $2$。本题的关键是**分母是 $\ln(1+x)$ 时，求导会出现 $\frac{1}{1+x}$，把它翻上去变成乘法**，比保留繁分数更清楚。也可用等价无穷小 $\tan 2x\sim 2x$、$\ln(1+x)\sim x$，立刻得 $2$。

##### 【课件例题 6】$\dfrac{\sin x-x}{x^3}$

**Problem:** Find $\displaystyle\lim_{x\to 0}\frac{\sin x-x}{x^3}$.

* **Process (解题步骤):**
  1. As $x\to 0$: $\sin x-x\to 0$ and $x^3\to 0$, so the form is $\dfrac00$.
  2. Apply L'Hôpital's Rule three times:
     $$\lim_{x\to 0}\frac{\sin x-x}{x^3}\overset{L}{=}\lim_{x\to 0}\frac{\cos x-1}{3x^2}\overset{L}{=}\lim_{x\to 0}\frac{-\sin x}{6x}\overset{L}{=}\lim_{x\to 0}\frac{-\cos x}{6}=-\frac16$$
* **中文详解:** 第一次求导得 $\frac{\cos x-1}{3x^2}$（仍是 $\frac00$），第二次得 $\frac{-\sin x}{6x}$（仍是 $\frac00$），第三次得 $\frac{-\cos x}{6}$，代入得 $-\frac16$。为什么要连用三次？因为每求一次导，分子的“零阶”就降低一次：$\sin x-x$ 是 $x^3$ 阶小量，要降到常数阶需要三次。也可用泰勒展开 $\sin x=x-\frac{x^3}{6}+o(x^3)$，直接读出 $\frac{\sin x-x}{x^3}\to-\frac16$——遇到“三角函数减多项式”的 $\frac00$ 型，泰勒展开往往比三次求导更快、更不易错。

##### 【课件例题 7】典型错误：什么时候必须停止求导

**Problem:** Find $\displaystyle\lim_{x\to 0}\frac{1-\cos x}{x^2+3x}$.

* **Process (解题步骤):**
  1. As $x\to 0$: $1-\cos x\to 0$ and $x^2+3x\to 0$, so the form is $\dfrac00$; one application is legitimate:
     $$\lim_{x\to 0}\frac{1-\cos x}{x^2+3x}\overset{L}{=}\lim_{x\to 0}\frac{\sin x}{2x+3}$$
  2. Now the numerator tends to $0$ but the denominator tends to $3\neq 0$: the quotient is **no longer** indeterminate, so
     $$\lim_{x\to 0}\frac{\sin x}{2x+3}=\frac{0}{3}=0$$
  3. **Wrong** (a second application would give $\frac{\cos x}{2}\to\frac12$), because after the first step the form is not $\frac00$.
* **中文详解:** 这是考试中最常见的错误之一。第一次洛必达后得到 $\frac{\sin x}{2x+3}$，此时分母趋于 $3$ 而不是 $0$，商已经不是不定式，极限直接为 $\frac03=0$，**必须停止**。如果机械地再求一次导，得到 $\frac{\cos x}{2}\to\frac12$，答案就错了。判断标准很简单：每次求导后先看分子、分母的极限，只要有一个非零，就立刻代入；洛必达法则的前提（$\frac00$ 或 $\frac{\infty}{\infty}$）一旦不满足，就不能再用。

##### 【课件例题 8】越求越复杂：先改写再求极限

**Problem:** Find $\displaystyle\lim_{x\to\infty}\frac{e^{-x}}{x^{-1}}$.

* **Process (解题步骤):**
  1. As $x\to\infty$: $e^{-x}\to 0$ and $x^{-1}\to 0$, so the form is $\dfrac00$. But repeated applications do not simplify:
     $$\frac{e^{-x}}{x^{-1}}\overset{L}{=}\frac{-e^{-x}}{-x^{-2}}=\frac{e^{-x}}{x^{-2}}\overset{L}{=}\frac{-e^{-x}}{-2x^{-3}}=\cdots$$
     分母的幂次越来越负，式子越来越复杂。
  2. Instead, rewrite the quotient:
     $$\lim_{x\to\infty}\frac{e^{-x}}{x^{-1}}=\lim_{x\to\infty}\frac{x}{e^{x}}$$
     which is of the form $\dfrac{\infty}{\infty}$.
  3. Apply L'Hôpital's Rule:
     $$\lim_{x\to\infty}\frac{x}{e^{x}}\overset{L}{=}\lim_{x\to\infty}\frac{1}{e^{x}}=0$$
* **中文详解:** 直接对 $\frac{e^{-x}}{x^{-1}}$ 用洛必达，分子分母的“幂次方向”相反，每求一次导分母的负幂次就更深一层，永远化简不完。正确做法是先**代数改写**：$\frac{e^{-x}}{x^{-1}}=\frac{x}{e^{x}}$，变成 $\frac{\infty}{\infty}$ 型，一次洛必达即得 $0$。这体现了使用洛必达法则的一条经验：**求导之前先看能否用代数变形让形式变简单**；幂次、指数、对数混在一起时尤其如此。

---

### 4.8 Other Indeterminate Forms (其他类型不定式)

#### 1. $\dfrac{\infty}{\infty}$ 型洛必达法则

* **定理内容:** 设 $\displaystyle\lim_{x\to u}|f(x)|=\lim_{x\to u}|g(x)|=\infty$，且 $f$、$g$ 在 $u$ 的去心邻域内可导、$g'(x)\neq 0$，若 $\displaystyle\lim_{x\to u}\frac{f'(x)}{g'(x)}$ 存在（有限或 $\pm\infty$），则
  $$\lim_{x\to u}\frac{f(x)}{g(x)}=\lim_{x\to u}\frac{f'(x)}{g'(x)}$$
  $u$ 同样可以是 $a$、$a^\pm$、$\pm\infty$。
* **要点:** $\frac{\infty}{\infty}$ 型与 $\frac00$ 型的法则形式完全相同，只是前提从“都趋于 $0$”换成“都趋于 $\pm\infty$”。

##### 【课件例题 9】$\dfrac{x}{e^x}\to 0$ 的推广：$\dfrac{x^a}{e^x}\to 0$（$a>0$）

**Problem:** Show that for any positive real number $a$, $\displaystyle\lim_{x\to\infty}\frac{x^a}{e^x}=0$.

* **Process (解题步骤):**
  1. Let $m$ be the greatest integer less than $a$; then $m<a\le m+1$.
  2. Apply L'Hôpital's Rule $m+1$ times:
     $$\lim_{x\to\infty}\frac{x^a}{e^x}\overset{L}{=}\lim_{x\to\infty}\frac{ax^{a-1}}{e^x}\overset{L}{=}\lim_{x\to\infty}\frac{a(a-1)x^{a-2}}{e^x}\overset{L}{=}\cdots\overset{L}{=}\lim_{x\to\infty}\frac{a(a-1)\cdots(a-m)x^{a-m-1}}{e^x}$$
  3. Since $a-m-1\le 0$, write it as
     $$\lim_{x\to\infty}\frac{a(a-1)\cdots(a-m)}{x^{m+1-a}e^{x}}=0$$
     因为 $m+1-a\ge 0$ 且 $e^x\to\infty$，分母趋于无穷，分子为常数。
* **中文详解:** 这是“指数增长快于任意幂函数”的严格证明。思路是反复使用洛必达法则，每次分子降一次幂，直到幂指数 $\le 0$（变成常数或负幂），此时分母仍然是指数函数 $e^x\to\infty$，故极限为 $0$。令 $m$ 为小于 $a$ 的最大整数，则最多用 $m+1$ 次就能把分子的幂次降到 $\le 0$。结论 $x^a/e^x\to 0$ 说明：无论幂次多高，$e^x$ 最终都会压倒它。

##### 【课件例题 10】$\dfrac{\ln x}{x^a}\to 0$（$a>0$）

**Problem:** Show that for any $a>0$, $\displaystyle\lim_{x\to\infty}\frac{\ln x}{x^a}=0$.

* **Process (解题步骤):**
  1. As $x\to\infty$, the form is $\dfrac{\infty}{\infty}$.
  2. Apply L'Hôpital's Rule once:
     $$\lim_{x\to\infty}\frac{\ln x}{x^a}\overset{L}{=}\lim_{x\to\infty}\frac{\frac1x}{ax^{a-1}}=\lim_{x\to\infty}\frac{1}{ax^{a}}=0$$
* **中文详解:** 只需一次洛必达：分子 $\ln x$ 的导数为 $\frac1x$，分母 $x^a$ 的导数为 $ax^{a-1}$，相除后 $\frac{1}{ax^a}$，由于 $a>0$，分母趋于无穷，极限为 $0$。结合例题 9，我们得到三个函数的**增长速度排序**：
  $$\ln x\ \ll\ x^a\ \ll\ e^x\qquad(\text{当 }x\to\infty)$$
  即对数增长最慢、幂函数居中、指数增长最快；“$\ll$”表示前者除以后者趋于 $0$。这个排序在比较无穷大阶、判断级数收敛性时非常有用。

#### 2. $0\cdot\infty$ 型 (Product Forms)

* **处理原则:** 洛必达法则不能直接用于乘积，必须先**化积为商**：
  $$f\cdot g=\frac{f}{1/g}\quad\text{或}\quad\frac{g}{1/f}$$
  选择的标准是：变形后得到 $\frac00$ 或 $\frac{\infty}{\infty}$，且求导后更简单（通常把“对数型”因子放在分子、“幂型”因子放在分母）。
* **常见错误:** 直接把乘积的两因子分别求导，这没有任何依据。

##### 【课件例题 11】$\tan x\cdot\ln(\sin x)$（$x\to\pi/2^-$）

**Problem:** Find $\displaystyle\lim_{x\to\pi/2^-}\left(\tan x\cdot\ln(\sin x)\right)$.

* **Process (解题步骤):**
  1. As $x\to\pi/2^-$: $\ln(\sin x)\to\ln 1=0$ and $\tan x\to+\infty$, so the form is $0\cdot\infty$.
  2. Rewrite as a quotient:
     $$\tan x\cdot\ln(\sin x)=\frac{\ln(\sin x)}{\cot x}$$
     now the form is $\dfrac{0}{0}$.
  3. Apply L'Hôpital's Rule:
     $$\lim_{x\to\pi/2^-}\frac{\ln(\sin x)}{\cot x}\overset{L}{=}\lim_{x\to\pi/2^-}\frac{\frac{\cos x}{\sin x}}{-\csc^2 x}=\lim_{x\to\pi/2^-}\left(-\cos x\sin x\right)=0$$
* **中文详解:** $0\cdot\infty$ 型，先把 $\tan x$ 写成 $\frac{1}{\cot x}$，把乘积变成商 $\frac{\ln(\sin x)}{\cot x}$，此时分子、分母都趋于 $0$，是 $\frac00$ 型。求导后分子为 $\frac{\cos x}{\sin x}=\cot x$，分母为 $-\csc^2x$，相除化简为 $-\cos x\sin x$，代入 $x=\frac{\pi}{2}$ 得 $0$。选择这种变形的原因是：$\ln(\sin x)$ 求导后变成 $\cot x$，与分母的 $\cot x$ 结构相近，容易化简；若反过来把 $\ln$ 放到分母，会得到 $\frac{\tan x}{1/\ln(\sin x)}$，求导后更复杂。

##### 【课件例题 12】$\dfrac{\ln x}{\cot x}$（$x\to 0^+$）

**Problem:** Find $\displaystyle\lim_{x\to 0^+}\frac{\ln x}{\cot x}$.

* **Process (解题步骤):**
  1. As $x\to 0^+$: $\ln x\to-\infty$ and $\cot x\to+\infty$, so the form is $\dfrac{-\infty}{\infty}$.
  2. A direct application gives
     $$\frac{\frac1x}{-\csc^2 x}=-\frac{\sin^2 x}{x}$$
     这比原式更繁（"Not a good idea"）。
  3. Rewrite instead:
     $$\frac{\ln x}{\cot x}=\ln x\cdot\tan x=\ln x\cdot\frac{\sin x}{\cos x}$$
     由于 $\frac{\sin x}{x}\to 1$，可写成 $x\ln x\cdot\frac{\sin x}{x}\cdot\frac{1}{\cos x}$，而 $x\ln x\to 0$，故极限为 $0$。
  4. 也可对 $\frac{\sin^2 x}{x}$ 用一次洛必达：
     $$\lim_{x\to 0^+}\left(-\frac{\sin^2 x}{x}\right)\overset{L}{=}\lim_{x\to 0^+}\left(-2\sin x\cos x\right)=0$$
* **中文详解:** 这是课件中“直接求导不是好主意”的例子：对 $\frac{\ln x}{\cot x}$ 直接洛必达，得到 $-\frac{\sin^2x}{x}$，虽然仍可继续做（再对 $\frac{\sin^2x}{x}$ 用一次洛必达即可得 $0$），但更自然的做法是先化简：$\frac{\ln x}{\cot x}=\ln x\tan x=\frac{\sin x}{\cos x}\ln x$，利用 $\sin x\sim x$ 得 $\approx x\ln x\to 0$。两种路径结论相同，但**先化简再求导**更不容易出错。

#### 3. $\infty-\infty$ 型 (Difference Forms)

* **处理原则:** 通过**通分**、**有理化**或**提取公因子**把差化成商，再按 $\frac00$ 或 $\frac{\infty}{\infty}$ 型处理。
* **常见错误:** 把两项分别取极限再相减（$\infty-\infty$ 无意义）。

##### 【课件例题 13】$\dfrac{x}{x-1}-\dfrac{1}{\ln x}$（$x\to 1^+$）

**Problem:** Find $\displaystyle\lim_{x\to 1^+}\left(\frac{x}{x-1}-\frac{1}{\ln x}\right)$.

* **Process (解题步骤):**
  1. As $x\to 1^+$: $\frac{x}{x-1}\to+\infty$ and $\frac{1}{\ln x}\to+\infty$, so the form is $\infty-\infty$.
  2. Combine over the common denominator $(x-1)\ln x$:
     $$\frac{x}{x-1}-\frac{1}{\ln x}=\frac{x\ln x-(x-1)}{(x-1)\ln x}=\frac{x\ln x-x+1}{(x-1)\ln x}$$
  3. Now the form is $\dfrac00$. Apply L'Hôpital's Rule:
     $$\overset{L}{=}\lim_{x\to 1^+}\frac{\ln x+1-1}{\ln x+\frac{x-1}{x}}=\lim_{x\to 1^+}\frac{\ln x}{\ln x+1-\frac1x}$$
  4. Still $\dfrac00$ at $x=1$; apply again:
     $$\overset{L}{=}\lim_{x\to 1^+}\frac{\frac1x}{\frac1x+\frac{1}{x^2}}=\lim_{x\to 1^+}\frac{x}{x+1}=\frac12$$
* **中文详解:** $\infty-\infty$ 型的标准动作是**通分**：把两项合并成 $\frac{x\ln x-x+1}{(x-1)\ln x}$，分子、分母都趋于 $0$，成为 $\frac00$ 型。第一次洛必达后分子为 $\ln x$，分母为 $\ln x+1-\frac1x$，代入 $x=1$ 仍是 $0/0$；第二次求导后分子 $\frac1x$、分母 $\frac1x+\frac1{x^2}$，化简为 $\frac{x}{x+1}$，代入得 $\frac12$。也可令 $t=x-1$ 用泰勒展开验证：分子 $x\ln x-x+1=(1+t)\ln(1+t)-t=\frac{t^{2}}{2}+O(t^{3})$，分母 $(x-1)\ln x=t\ln(1+t)=t^{2}+O(t^{3})$，两者同阶，比值 $\to\frac12$，与洛必达结果一致。

#### 4. 幂指函数 $f(x)^{g(x)}$：$1^\infty$、$\infty^0$、$0^0$ 型

* **统一方法（取对数）:** 令 $y=f(x)^{g(x)}$，则
  $$\ln y=g(x)\ln f(x)$$
  先求 $\displaystyle\lim\ln y=L$（此时通常化为 $0\cdot\infty$ 型），再由指数函数的连续性得
  $$\lim y=e^{L}$$
* **为什么不能直接代入:** $1^\infty$ 的底数趋于 $1$、指数趋于 $\infty$，两种力量相互竞争，结果可能是 $1$、$e$、$e^2$、$0$、$\infty$ 等，必须先取对数把指数“拉下来”。
* **三种形式:** $1^\infty$、$\infty^0$、$0^0$ 都通过取对数化为 $0\cdot\infty$ 型，再化积为商。

##### 【课件例题 14】$(1+x)^{\cot x}$（$1^\infty$ 型）

**Problem:** Find $\displaystyle\lim_{x\to 0^+}(1+x)^{\cot x}$.

* **Process (解题步骤):**
  1. As $x\to 0^+$: $1+x\to 1$ and $\cot x\to+\infty$, so the form is $1^\infty$.
  2. Let $y=(1+x)^{\cot x}$; then
     $$\ln y=\cot x\ln(1+x)=\frac{\ln(1+x)}{\tan x}$$
     which is of the form $\dfrac00$.
  3. Apply L'Hôpital's Rule:
     $$\lim_{x\to 0^+}\ln y=\lim_{x\to 0^+}\frac{\ln(1+x)}{\tan x}\overset{L}{=}\lim_{x\to 0^+}\frac{\frac{1}{1+x}}{\sec^2 x}=1$$
  4. Therefore
     $$\lim_{x\to 0^+}y=\lim_{x\to 0^+}e^{\ln y}=e^{1}=e$$
* **中文详解:** $1^\infty$ 型不能直接写 $1^\infty=1$，因为底数略大于 $1$、指数很大，结果可能大于 $1$。标准做法是取对数：$\ln y=\cot x\ln(1+x)=\frac{\ln(1+x)}{\tan x}$，这是 $\frac00$ 型，一次洛必达得 $\frac{1/(1+x)}{\sec^2x}\to 1$，故 $\ln y\to 1$，$y\to e$。注意最后一步用到了“$\lim e^{\ln y}=e^{\lim\ln y}$”，即 $e^x$ 连续。

##### 【课件例题 15】$(\tan x)^{\cos x}$（$\infty^0$ 型）

**Problem:** Find $\displaystyle\lim_{x\to\pi/2^-}(\tan x)^{\cos x}$.

* **Process (解题步骤):**
  1. As $x\to\pi/2^-$: $\tan x\to+\infty$ and $\cos x\to 0^+$, so the form is $\infty^0$.
  2. Let $y=(\tan x)^{\cos x}$; then
     $$\ln y=\cos x\ln(\tan x)=\frac{\ln(\tan x)}{\sec x}$$
     which is of the form $\dfrac{\infty}{\infty}$.
  3. Apply L'Hôpital's Rule:
     $$\lim_{x\to\pi/2^-}\ln y\overset{L}{=}\lim_{x\to\pi/2^-}\frac{\frac{\sec^2 x}{\tan x}}{\sec x\tan x}=\lim_{x\to\pi/2^-}\frac{\cos x}{\sin^2 x}=0$$
  4. Therefore
     $$\lim_{x\to\pi/2^-}y=e^{0}=1$$
* **中文详解:** $\infty^0$ 型，同样取对数：$\ln y=\cos x\ln(\tan x)$，把 $\cos x$ 写成 $\frac{1}{\sec x}$，得到 $\frac{\ln(\tan x)}{\sec x}$，即 $\frac{\infty}{\infty}$ 型。求导时分子为 $\frac{\sec^2x}{\tan x}$、分母为 $\sec x\tan x$，化简得 $\frac{\cos x}{\sin^2x}$，当 $x\to\frac{\pi}{2}^-$ 时趋于 $0$。故 $\ln y\to 0$，$y\to e^0=1$。这个例子说明“$\infty^0$”并不总是 $\infty$ 或 $1$，必须具体计算。

##### 【课件例题 16】$x^x$（$0^0$ 型）

**Problem:** Find $\displaystyle\lim_{x\to 0^+}x^x$.

* **Process (解题步骤):**
  1. As $x\to 0^+$: $x\to 0^+$ and $x\to 0$, so the form is $0^0$.
  2. Let $y=x^x$; then
     $$\ln y=x\ln x$$
     which is of the form $0\cdot(-\infty)$.
  3. Rewrite and apply L'Hôpital's Rule:
     $$\lim_{x\to 0^+}x\ln x=\lim_{x\to 0^+}\frac{\ln x}{1/x}\overset{L}{=}\lim_{x\to 0^+}\frac{1/x}{-1/x^2}=\lim_{x\to 0^+}(-x)=0$$
  4. Therefore
     $$\lim_{x\to 0^+}x^x=e^{0}=1$$
* **中文详解:** $0^0$ 型是最容易误判的形式：底数和指数都趋于 $0$，直觉上可能猜 $0$ 或 $1$，正确答案是 $1$。取对数得 $\ln y=x\ln x$，这是 $0\cdot(-\infty)$ 型；把 $x$ 写成 $\frac{1}{1/x}$，化为 $\frac{\ln x}{1/x}$（$\frac{-\infty}{\infty}$ 型），一次洛必达得 $-x\to 0$，故 $y\to e^0=1$。$x\ln x\to 0$ 这个极限本身也值得记住。

#### 5. 七种不定式总结 (The Seven Indeterminate Forms)

| 形式 (Form) | 典型例子 (Example) | 处理方式 (Method) |
| :--- | :--- | :--- |
| $\dfrac00$ | $\displaystyle\lim_{x\to 0}\frac{\sin x}{x}$ | 直接洛必达 |
| $\dfrac{\infty}{\infty}$ | $\displaystyle\lim_{x\to\infty}\frac{x}{e^x}$ | 直接洛必达 |
| $0\cdot\infty$ | $\displaystyle\lim_{x\to 0^+}x\ln x$ | 化积为商 |
| $\infty-\infty$ | $\displaystyle\lim_{x\to 1^+}\left(\frac{x}{x-1}-\frac{1}{\ln x}\right)$ | 通分、有理化 |
| $0^0$ | $\displaystyle\lim_{x\to 0^+}x^x$ | 取对数 |
| $\infty^0$ | $\displaystyle\lim_{x\to\pi/2^-}(\tan x)^{\cos x}$ | 取对数 |
| $1^\infty$ | $\displaystyle\lim_{x\to 0^+}(1+x)^{1/x}$ | 取对数 |

* **Remark 1:** 每一种不定式都是两种“相反力量”的竞争（例如 $1^\infty$ 中底数趋于 $1$ 想把结果拉向 $1$，指数趋于 $\infty$ 想把它拉大），所以结果不能凭直觉，必须计算。
* **Remark 2:** 洛必达法则**直接**适用于 $\frac00$ 与 $\frac{\infty}{\infty}$；其余五种必须先变形。

#### 6. 非不定式 (Non-Indeterminate Forms)

* 有些形式看起来“奇怪”，但其实**不是**不定式，因为两种力量方向一致，结果确定：
  $$\frac{0}{\infty}=0,\qquad \frac{\infty}{0}=\infty,\qquad \infty\cdot\infty=\infty,\qquad \infty+\infty=\infty,\qquad 0^\infty=0,\qquad \infty^\infty=\infty$$
* **判断要点:** 不要一看到 $0$、$\infty$ 就套洛必达；先判断是否真的“两种力量对抗”。

##### 【课件例题 17】$(\sin x)^{\cot x}$（非不定式，结果为 $0$）

**Problem:** Show that $\displaystyle\lim_{x\to 0^+}(\sin x)^{\cot x}=0$.

* **Process (解题步骤):**
  1. Let $y=(\sin x)^{\cot x}$; then
     $$\ln y=\cot x\ln(\sin x)=\frac{\cos x}{\sin x}\ln(\sin x)$$
  2. As $x\to 0^+$: $\frac{\cos x}{\sin x}\to+\infty$ and $\ln(\sin x)\to-\infty$，故 $\ln y\to(+\infty)\cdot(-\infty)=-\infty$ ——这是**非不定式**（两个因子“同向”把结果推向 $-\infty$），不需要洛必达。
  3. Therefore
     $$\lim_{x\to 0^+}\ln y=-\infty\implies\lim_{x\to 0^+}y=\lim_{x\to 0^+}e^{\ln y}=0$$
* **中文详解:** 这个例子提醒我们**不要见极限就套洛必达**。$\ln y=\frac{\cos x}{\sin x}\ln(\sin x)$ 中，$\frac{\cos x}{\sin x}\to+\infty$，而 $\ln(\sin x)\to-\infty$，两者相乘是 $(+\infty)\cdot(-\infty)=-\infty$，方向一致、结果确定，属于非不定式。于是 $\ln y\to-\infty$，$y\to 0$。对比例题 14（$1^\infty$ 型，结果为 $e$）：同样是幂指函数，形式不同，处理方式和结果都不同，**先判断形式**永远是第一步。

#### 7. 洛必达法则使用检查表 (Checklist)

1. **判断形式:** 是七种不定式中的哪一种？不是不定式就不能用洛必达。
2. **先化简:** 能否用等价无穷小、三角恒等式、代数变形、泰勒展开简化？化简往往比求导更快。
3. **分别求导:** 分子、分母各自求导，不要用商法则。
4. **每次重新判断:** 求导后立即检查形式；一旦分子或分母极限非零，停止并直接代入。
5. **循环检查:** 若反复求导使式子更复杂（如 $e^{-x}/x^{-1}$），改用代数改写。
6. **幂指函数取对数:** $0^0$、$\infty^0$、$1^\infty$ 先令 $y=f^g$，求 $\lim\ln y$，再还原 $e^{L}$。
7. **法则失效时:** 若 $\lim f'/g'$ 不存在（如振荡），洛必达法则无法给出结论，需改用夹逼定理、等价无穷小或泰勒展开。
