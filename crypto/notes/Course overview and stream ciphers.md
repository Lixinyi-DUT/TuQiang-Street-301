---
title: 课程综述和流加密
date: 2016-7-11 21:02:00
---
## 一次一密和流加密

### 信息理论安全

首先探讨一些历史性的已被攻破的加密方法，以此讨论什么是安全的密码体系。

#### 对称密码
>定义： 一个定义在$\left(\cal K,\cal M,\cal C\right)$空间上的密码（加解密）体系是一对*高效*的算法$\left(\mathbf{E},\mathbf{D}\right)$

其中$\cal K$,$\cal M$和$\cal C$分别表示秘钥空间，明文空间和明文空间。而加密算法$\mathbf{E}$是将$\cal M$映射到$\cal C$的算法： $$\mathbf{E}:\cal K\times M\to  C$$ 解密算法$\mathbf{D}$则反之：$$\mathbf{D}:\cal K\times C\to  M$$
对于任意的密文$m$和秘钥$k$，进行一次加密操作再进行一次解密操作都可以恢复原来的明文，也就是$$s.t.\quad \forall m \in {\cal M},k \in {\cal K} \to D\left( {k,E\left( {k,m} \right)} \right) = m$$这个命题是对于对称密码体系当然成立的，等式$D\left( {k,E\left( {k,m} \right)} \right) = m$被称为一致性等式（*consistency equation*）。所谓高效，在理论上是指这对算法都能在依赖于输入规模的多项式时间内运行完成，更实际的高效则是指在固定时间内完成。$\mathbf{E}$往往是随机的，而$D$则是一定的。

#### 一次一密(*One Time Pad*)
