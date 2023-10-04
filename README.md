# Bitcoin Realized Volatility Analysis 

The following is an in-depth exploration of the fascinating world of Bitcoin price volatility. In this project, we dive deep into the dynamics of Bitcoin's price movements, exploring a range of models and their real-world applications to this captivating digital currency.

## Table of Contents
- Introduction
- Data Sourcing
- Downloading Data using API's
- Financial Asset Returns vs Bitcoin Return Stylized Facts
- The Theory Behind the Model
- HAR-RV Model for Bitcoin
- Results and Conclusion

## Analysis Overview

The analysis includes regression results and discussions on the effectiveness of different financial time-series models in capturing volatility in Bitcoin return time series. The conclusion highlights the need for further research to incorporate additional estimation methods and improve forecasting accuracy. This repository serves as a valuable resource for researchers and analysts interested in understanding and modeling volatility in cryptocurrency markets.

## Introduction

In recent years, the world of finance has undergone a technological revolution, ushering in a new era of possibilities. Technological advancements have enabled the collection and analysis of high-frequency financial data, offering invaluable insights into the ever-evolving dynamics of markets. These high-frequency data streams, often characterized by irregular temporal spacing, provide a tick-by-tick record of essential financial variables. Such a financial transformation aids in improving the measurement and estimation of volatility, a critical metric in gauging the risk associated with asset returns. Volatility quantifies the fluctuations and deviations of asset prices from their expected levels, making it an indispensable tool for investors and analysts alike.
In this intriguing project, we embark on a journey into the realm of volatility estimation and modeling, guided by the Realized Volatility (RV) estimator. While RV has long been a staple in traditional financial domains like forex, derivatives, and equity markets, its foray into the cryptocurrency arena, with a specific focus on the ever-persistent Bitcoin, adds a compelling layer of complexity. Here, we endeavor to unravel the mysteries of RV within the context of Bitcoin and the broader cryptocurrency market.
At the heart of our exploration lies a fundamental question: How does realized volatility (RV) manifest in the Bitcoin price time series, and can various models effectively capture it? Our mission is clear—to assess and compare the performance of these models in deciphering the intricacies of Bitcoin's price movements. Join us as we embark on this research journey, not only to delve into the theoretical underpinnings but also to unravel the practical dimensions of RV analysis in the realm of Bitcoin.

## Data Sourcing

In the original research, an in-depth analysis was conducted using regularly updated, tick-by-tick high-frequency data sourced from an API connecting R to the Kraken Cryptocurrency Exchange market. The dataset covered a significant timeframe, ranging from January 8<sup>th</sup>, 2014, to March 14<sup>th</sup>, 2021. Notably, the data is continually refreshed, ensuring that the code can access the most current insights whenever it is executed.

For the purpose of data visualization, some data was initially obtained from Yahoo Finance! However, the project has evolved to sharpen its focus. Consequently, data from Yahoo Finance! will no longer be utilized. It's important to note that the analysis exclusively considers the BTC-EUR exchange rate.

### The R-Code

### The equivalent Python code

## Measuring and Defining Volatility

Volatility refers to the degree of variation in the returns of a financial instrument over a certain period of time. It is a statistical measure of the dispersion of returns and is often used as a measure of risk ([Anderson et.al (2010)][2]). To measure volatility, there are two main categories of approaches: the the parametric and non-parametric models for volatility estimation. The parametric models include ARCH (Auto-Regressive Conditional Heteroskedasticity) Models, stochastic volatility models and continuous-time volatility models. On the other hand, the non-parametric volatility measurements focus on quantifying volatility without relying on specific functional form assumptions. Such measurements include modeling Instantaneous Volatility and Realized Volatility Measures.

[Andersen (2008)][3] defined realized volatility as a fully non-parametric approach for the ex-post measurement of the true realized return variation over a specific trading period. The objective is to estimate realized volatility in a simple and non-parametric manner. This enables us to demonstrate how volatility is estimated as a discrete-time or continuous-time process.

Realized volatility quantifies notional volatility over fixed-length time intervals, h > 0  

### Discrete-time Process

Suppose a tick-by-tick price of an asset at day t in a discrete-time process at an irregularly spaced time interval. Then the return of the asset at a point in time would be given as

$$
r_{t,i} = \ln P_{t,i} - \ln P_{t-1,i}
$$

where $\ln P_{t,i} - \ln P_{t-1,i}$ is the natural logarithm of the price at times t and t-1, and $r_{t,i}$ is the return of an asset with all the observation points. Then the sum of all the log returns will be

$$
r_t = \sum_{i=1}^M r_{t,i}
$$

where M is the total number of observations within the specific trading day. M can be thousands of observations. Then the realized variance can be defined as the sum of all available intra-day high-frequency squared returns.

$$
RV_t^{(all)} = \sum_{i=1}^M r_{t,i}^2
$$

where $RV_t^{(all)}$ is the realized variance as labeled by [McAleer (2008)]. The square root of the realized variance is the realized volatility. If the intra-day returns are uncorrelated, then $RV^{(all)}$ is an unbiased estimator of the latent volatility, which is not purely based on observables [Robert Engle, 2001].

#### Continuous-time Process

Suppose the log price of an asset at day t follows a continuous-time diffusion process where the total differential of the price at time (t+\tau) is as follows:

$$
dp(t+\tau) = \mu(t+\tau)d\tau + \sigma(t+\tau)dW(t+\tau)
$$

where $0 \leq \tau \leq 1$, and t = 1, 2, .... In this equation, $\mu(t+\tau)$ is the drift term, $\sigma(t+\tau)$ is the instantaneous volatility, $W(t+\tau)$ is the standard Brownian motion, and $\tau$ is the grid of observation times. There is linearity between $\sigma(t+\tau)$ and $W(t+\tau)$. As [Danyliv et al. (2019)] define it, the instantaneous volatility is simply the volatility at literally few time intervals or at the spot.

If continuously compounded daily returns over [t-h, t] are given by $r_t = P(t) - P(t-h)$, as defined by [Andersen (2005)], and Gaussian conditional on an information set $I_t$:

$$
I_t = \left[\mu(t+\tau), \sigma(t+\tau)\right]_{\tau=0}^{\tau=1}
$$

then $r_t|I_t$ is normally distributed with a mean as a definite integral of the drift term and standard deviation as a definite integral of the instantaneous volatility.

$$
r_t|I_t \sim \mathcal{N}\left(\int_0^1 \mu(t+\tau)d\tau, \int_0^1 \sigma(t+\tau)d\tau\right)
$$

Integrated volatility $\sigma(t+\tau)d\tau$ is then a measure of ex-post volatility (a volatility measurement weighted against a portfolio return in time) [McAleer (2008)].

##### Distributional Property of Realized Volatility

So far, we have implicitly assumed that there is no micro-structure noise effect. Without micro-structure noise effect, RV is a consistent estimator of the true volatility and asymptotically normally distributed.

Micro-structure noise can be viewed as the correlation between the disturbance term $\epsilon$ at time t and t-1. When the observations are noisy, the true structure of the observed log-returns $r_{t,i}$ is given by an MA(1) process [Aït-Sahalia et al. (2008)]. If

$$
P_{t,i} = P_{t,i}^* - \varepsilon_{t,i}
$$

where $\varepsilon_{t,i}$ is the Micro-structure noise and $P_{t,i}^*$ is the true price process, then

$$
r_{t,i} = r_{t,i}^* + \varepsilon_{t,i} - \varepsilon_{t,{i-1}}
$$

where $r_{t,i}^*$ is the log return of the true price process. Then the existence of the Micro-structure noise implies that equation (1) is not a consistent estimator of the true unobserved volatility. To account for Micro-structure noise, the following assumptions can be considered:

1. In the case of IID Noise Structure:
   - $E(\varepsilon) = 0$

2. In the case of Dependent Noise Structure:
   - $E(\varepsilon) = 0$
   - stationary-and-is-exponentially-declining as the time intervals increase

3. $V_{t,i} = \varepsilon_{t,i} - \varepsilon_{t,{i-1}}$ is constant.
4. Noise is independent of the price process.

If the data is contaminated by Micro-Noise Structure, then RV is not a consistent estimator of the Integrated variance. Hence, Micro-Structure Noise Bias exists. The mathematical explanation of Micro-Structure Noise Bias is presented in Appendix B.

### The Theory of Sampling Irregularly Spaced Financial Data

In financial markets, prices are observed at discrete and irregularly spaced time intervals. To estimate volatility in a financial time-series, it is recommended to use equidistant sampling schemes where the intervals between the ticks are evenly spaced. This helps minimize bias and variance in the estimation process, hence minimize the bias-variance trade off. The bias-variance trade-off refers to the relationship between the bias and variance of an estimator in statistical analysis. In the context of volatility estimation, such as realized volatility (RV), the bias represents the difference between the expected value of the estimator and the true value of the volatility. On the other hand, the variance measures the variability of the estimator's values around its expected value.


## Reference

Andersen, Torben G., Tim Bollerslev, and Francis X. Diebold. "Parametric and nonparametric volatility measurement." Handbook of financial econometrics: Tools and techniques. North-Holland, 2010. 67-137.

Andersen, T. G., & Benzoni, L. (2008). Realized Volatility, Working Paper 2008-14.

[1]: https://example.com/andersen-2008.pdf
[2]: https://example.com/andersen-2008.pdf](https://www.sas.upenn.edu/~fdiebold/papers/paper50/abd071102.pdf
[3]: https://www.chicagofed.org/-/media/publications/working-papers/2008/wp2008-14-pdf.pdf




