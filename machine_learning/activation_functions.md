# Activation function table
> There are many different types of functions.
>
> Each neural network is used to update weights by calculating prediction errors in the Artificial Intelligence learning phase.

The details are well organized [here](https://ko.wikipedia.org/wiki/%EC%9D%B8%EA%B3%B5_%EC%8B%A0%EA%B2%BD%EB%A7%9D).

[https://github.com/yourname/github-link](https://github.com/dbader/)

| __Number__ | __Activation function__ | __Equation__ | __Case__ | __one-dimensional graph__ |
|:---:|:---:|:---:|:---:|:---:|
| 1 | Linear function | $\phi(z) = z$ | Adalin, Linear Regression | ![download](https://user-images.githubusercontent.com/105290026/194353264-846c6b68-e211-4d72-939c-efc596b0d367.png) |
| 2 | Heavyside function | ![image](https://user-images.githubusercontent.com/105290026/194367022-abac654d-4f2b-4143-b68f-6d41bc04b82b.png) | Perceptron type | ![download](https://user-images.githubusercontent.com/105290026/194358187-764341b5-1f00-4b81-9ab8-c6abca693301.png) |
| 3 | Sign(um) function | ![image](https://user-images.githubusercontent.com/105290026/194367824-a27d3864-7c80-4969-bcd3-6bfc3009d6f9.png) | Perceptron type | ![download](https://user-images.githubusercontent.com/105290026/194367494-9a78639f-ced3-4ffd-874f-218771030ad9.png) |
| 4 | Partial Linear funtion | ![image](https://user-images.githubusercontent.com/105290026/194373970-9998f132-98fb-4f05-81bf-b4d927344562.png) | Support vector machine | ![download](https://user-images.githubusercontent.com/105290026/194368262-344cb90c-2390-4bcd-90d9-85d2762b0dda.png) |
| 5 | Simoid (logistic) function | ![image](https://user-images.githubusercontent.com/105290026/194373789-b0e5e935-bb10-47a0-b422-f84d963f440d.png) | Logistic Regression, Multi-Layer Perceptron(MLP) | ![download](https://user-images.githubusercontent.com/105290026/194371219-e46bfde2-e95e-466d-94e2-59fcc555b8e6.png) |
| 6 | Hyperbolic tangent (tanh) function | ![image](https://user-images.githubusercontent.com/105290026/194374758-3ce91841-1adc-468c-9113-0b671eecd939.png) | Multi-Layer Perceptron(MLP) | ![download](https://user-images.githubusercontent.com/105290026/194374420-52c2a8cf-9f21-4d0f-b505-e87317095010.png) |
| 7 | ReLU function (Rectified Linear Unit) | ![image](https://user-images.githubusercontent.com/105290026/194376686-1a5d0bc8-57d6-4fd6-ab8d-8ff07aa56564.png) | Multi-Layer Perceptron(MLP), CNN(Convolutional Neural Networks) | ![download](https://user-images.githubusercontent.com/105290026/194375403-90439c65-2c0d-4018-bb66-a451204ce084.png) |

<!--
$$\phi(z) = \begin{cases}-1 & \quad (z \leq -\frac{1}{2})\\\z + \frac{1}{2} & (-\frac{1}{2} \leq z \leq \frac{1}{2})\\\1 & \quad \\; (z \geq \frac{1}{2})\\ \end{cases}$$

$$\phi(z) = \frac{\mathrm{e}^{z} - \mathrm{e}^{-z}}{\mathrm{e}^{z} + \mathrm{e}^{-z}\}$$
-->
