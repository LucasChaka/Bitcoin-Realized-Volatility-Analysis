# Bitcoin Realized Volatility Analysis 

The following is an in-depth exploration of the fascinating world of Bitcoin price volatility. This project dives deep into the dynamics of Bitcoin's price movements, exploring the Hetrogenous Autoregressive Realized Volatility (HAR-RV) model and it's real-world applications to this captivating digital currency.

## Table of Contents
- Introduction
- Data Sourcing
- Downloading Data using API's
- Financial Asset Returns vs Bitcoin Return Stylized Facts
- The Theory Behind the Model
- HAR-RV Model for Bitcoin
- Results and Conclusion

## Analysis Overview

The analysis includes regression results and discussions on the effectiveness of HAR-RV model in capturing volatility in Bitcoin return time series. The conclusion highlights the need for further research to incorporate additional estimation methods, and models and improve forecasting accuracy. This repository serves as a valuable resource for researchers and analysts interested in understanding and modeling volatility in cryptocurrency markets.

## Introduction

In recent years, the finance industry has witnessed a technological revolution, ushering in an era of unprecedented possibilities. Technological advancements have paved the way for the collection and analysis of high-frequency financial data, offering invaluable insights into the ever-evolving dynamics of global markets. These high-frequency data streams, often characterized by irregular temporal spacing, provide a tick-by-tick record of essential financial variables. This financial transformation has significantly enhanced the measurement and estimation of volatility, a critical metric for gauging the risk associated with asset returns. Volatility quantifies the fluctuations and deviations of asset prices from their expected levels, making it an indispensable tool for investors and analysts alike.

In this project, the focus is volatility estimation and modeling, via the *Realized Volatility (RV)* estimator and the *HAR-RV* model. While RV has long held a pivotal role in traditional financial domains such as forex, derivatives, and equity markets, its expansion into the cryptocurrency sphere, with a specific emphasis on Bitcoin, introduces a compelling layer of complexity. This endeavor seeks to unravel the mysteries of RV within the context of Bitcoin.

At the heart of this exploration lies a fundamental question: How does realized volatility (RV) manifest in the Bitcoin price time series, and can the HAR-RV model effectively capture it? The mission at hand is clear—to assess and compare the performance of this model in deciphering the volatilities of Bitcoin's price movements. 

## Measuring and Defining Volatility

Volatility refers to the degree of variation in the returns of a financial instrument over a certain period of time. It is a statistical measure of the dispersion of returns and is often used as a measure of risk ([Anderson et al. (2010)][2]). However, as thoroughly explained by [Anderson et al. (2006)][5], volatility is inherently unobservable, leaving room to rely on a proxy for measuring the volatility of an asset's returns. To measure volatility, there are two main categories of approaches: parametric and non-parametric models for volatility estimation. Parametric models include ARCH (Auto-Regressive Conditional Heteroskedasticity) models, stochastic volatility models, and continuous-time volatility models. On the other hand, non-parametric volatility measurements focus on quantifying volatility without relying on specific functional form assumptions. Such measurements include modeling *Instantaneous Volatility* and *Realized Volatility* measures. In this context, the purpose of this project comes to light — to harness the power of realized volatility as a tool for estimation and analysis, unlocking new insights into financial markets.

[Andersen (2008)][3] defined realized volatility as a fully non-parametric approach for measuring the true volatility over a specific trading period. The objective for now is to estimate realized volatility in a simple and non-parametric manner. This enables us to demonstrate how realized volatility is estimated in both discrete-time and continuous-time processes.

### Discrete-time Process

Suppose you have a tick-by-tick price of an asset at day t in a discrete-time process at irregularly spaced time intervals. Then the return of the asset at a specific point in time would be given as

$$
r_{t,i} = \ln P_{t,i} - \ln P_{t-1,i}
$$

Here, $\ln P_{t,i} - \ln P_{t-1,i}$ represents the natural logarithm of the asset price at times t and t-1, and $r_{t,i}$ represents the return of an asset with all the observation points. The sum of all the log returns can be calculated as

$$
r_t = \sum_{i=1}^M r_{t,i}
$$

where M is the total number of observations within the specific trading day. M can consist of thousands of observations. The realized variance can then be defined as the sum of all available intra-day high-frequency squared returns.

$$
RV_t^{(all)} = \sum_{i=1}^M r_{t,i}^2
$$

Here, $RV_t^{(all)}$ is the realized variance as labeled by [McAleer (2008)][6]. The square root of the realized variance is the realized volatility. If the intra-day returns are uncorrelated, then $RV^{(all)}$ is an unbiased estimator of the true unobservable volatility.

### Continuous-time Process

While prices are typically observed at discrete and irregularly spaced intervals in practice, for mathematical explanation within a continuous-time setting, the aim is to quantify the true, unobserved volatility. It's important to note that the discrete-time process serves as an approximation of the continuous-time process ([Duong, D., & Swanson, N. R. (2011)][8]).

Consider the log price of an asset at day t, which follows a diffusion process. The total differential of the price at time $(t+\tau)$ is described as:

$$
dp(t+\tau) = \mu(t+\tau)d\tau + \sigma(t+\tau)dW(t+\tau)
$$

Here, $0 \leq \tau \leq 1$, and t = 1, 2, .... In this equation, $\mu(t+\tau)$ represents the drift term, $\sigma(t+\tau)$ signifies the spot volatility, $W(t+\tau)$ stands for the standard Brownian motion, and $\tau$ denotes the grid of observation times. It's worth noting that there exists a linear relationship between $\sigma(t+\tau)$ and $W(t+\tau)$. 

If we define continuously compounded daily returns over [t-h, t] as $r_t = P(t) - P(t-h)$, following the definition by [Andersen (2005)][7], and assume these returns are Gaussian conditional on an information set $I_t$:

$$
I_t = \left[\mu(t+\tau), \sigma(t+\tau)\right]_{\tau=0}^{\tau=1}
$$

Then, $r_t|I_t$ follows a normal distribution. Its mean is represented as a definite integral of the drift term, and its standard deviation is a definite integral of the volatility.

$$
r_t|I_t \sim \mathcal{N}\left(\int_0^1 \mu(t+\tau)d\tau, \int_0^1 \sigma(t+\tau)d\tau\right)
$$

The integrated volatility, denoted as $\int_0^1 \sigma(t+\tau)d\tau$, serves as a measure of volatility that has been adjusted against a portfolio return over time ([McAleer (2008)][6]).


### Overcoming Micro-Structure Noise Effect with Calendar Time Sampling

#### Micro-Structure Noise

When prices are observed tick-by-tick, their values deviate from their 'efficient values' due to various market frictions, such as price discreteness, infrequent trading, or bid-ask bounce effects. This phenomenon is commonly referred to in finance and econometric literature as the microstructure noise effect. According to [Anderson et al. (2001)][9], these market microstructure features generally have little impact when analyzing longer-horizon interdaily returns (e.g., in an hourly format). However, they can significantly distort the distributional properties of high-frequency intraday returns when measured tick-by-tick.

Up to this point, it has been implicitly assumed that there is no microstructure noise effect. In the absence of microstructure noise, RV serves as a consistent estimator of the true unobservable volatility and follows an asymptotic normal distribution. Microstructure noise arises from the correlation between the disturbance term ε at time $t$ and time $t-1$ as explained by [Aït-Sahalia et al. (2008)][10].

If the observed prices are expressed as:

$$
P_{t,i} = P_{t,i}^* - \varepsilon_{t,i}
$$

where ε_{t,i} represents the microstructure noise and P_{t,i}^* is the true price process, then:

$$
r_{t,i} = r_{t,i}^* + \varepsilon_{t,i} - \varepsilon_{t,{i-1}}
$$

where r_{t,i}^* represents the log return of the true price process. The presence of microstructure noise implies that $RV_t^{(all)}$ is not a consistent estimator of the true unobserved volatility.

To account for Micro-structure noise, the following assumptions can be considered:

1. In the case of IID Noise Structure:
   - $E(\varepsilon) = 0$

2. In the case of Dependent Noise Structure:
   - $E(\varepsilon) = 0$
   - stationary-and-is-exponentially-declining as the time intervals increase

3. $V_{t,i} = \varepsilon_{t,i} - \varepsilon_{t,{i-1}}$ is constant.
4. Noise is independent of the price process.

If the data is contaminated by Micro-Noise Structure, then RV is not a consistent estimator of the true variance. Hence, Micro-Structure Noise Bias exists.

#### Calendar Time Sampling


[bitcoincharts.com][4] offers
 
 The dataset covered a significant timeframe, ranging from January 8<sup>th</sup>, 2014, to March 14<sup>th</sup>, 2021. Notably, the data is continually refreshed, ensuring that the code can access the most current insights whenever it is executed.

For the purpose of data visualization, some data was initially obtained from Yahoo Finance! However, the project has evolved to sharpen its focus. Consequently, data from Yahoo Finance! will no longer be utilized. It's important to note that the analysis exclusively considers the BTC-EUR exchange rate.

### The R-Code

### The equivalent Python code



### The Theory of Sampling Irregularly Spaced Financial Data

In financial markets, prices are observed at discrete and irregularly spaced time intervals. To estimate volatility in a financial time-series, it is recommended to use equidistant sampling schemes where the intervals between the ticks are evenly spaced. This helps minimize bias and variance in the estimation process, hence minimize the bias-variance trade off. The bias-variance trade-off refers to the relationship between the bias and variance of an estimator in statistical analysis. In the context of volatility estimation, such as realized volatility (RV), the bias represents the difference between the expected value of the estimator and the true value of the volatility. On the other hand, the variance measures the variability of the estimator's values around its expected value.


## Reference

Andersen, T. G., Bollerslev, T., & Diebold, F. X. (2010). Parametric and nonparametric volatility measurement. In Handbook of financial econometrics: Tools and techniques (pp. 67-137). North-Holland.

Andersen, T. G., & Benzoni, L. (2008). Realized Volatility, Working Paper 2008-14.

Andersen, T. G., Bollerslev, T., Christoffersen, P. F., & Diebold, F. X. (2006). Volatility and correlation forecasting. Handbook of economic forecasting, 1, 777-878.

Andersen, T. G., Bollerslev, T., & Diebold, F. X. (2005). Roughing It Up: Including Jump Components in the Measurement. Modeling and Forecast (ing of Return Volatility, tTech. rep., NBER.

Duong, D., & Swanson, N. R. (2011). Volatility in discrete and continuous-time models: A survey with new evidence on large and small jumps. In Missing data methods: Time-series methods and applications (Vol. 27, pp. 179-233). Emerald Group Publishing Limited.

Andersen, T. G., Bollerslev, T., Diebold, F. X., & Ebens, H. (2001). The distribution of realized stock return volatility. Journal of financial economics, 61(1), 43-76.

McAleer, M., Medeiros, M. C. (2008). Realized volatility: A review. Econometric Reviews, 27(1-3), 10-45.

Ait-Sahalia, Y., Yu, J. (2008). High frequency market microstructure noise estimates and liquidity measures (No. w13825). National Bureau of Economic Research.

[1]: https://example.com/andersen-2008.pdf
[2]: https://www.sas.upenn.edu/~fdiebold/papers/paper50/abd071102.pdf
[3]: https://www.chicagofed.org/-/media/publications/working-papers/2008/wp2008-14-pdf.pdf
[4]: bitcoincharts.com
[5]: http://public.econ.duke.edu/~boller/Published_Papers/abcd_hand_06.pdf
[6]: https://www.econ.puc-rio.br/uploads/adm/trabalhos/files/td531.pdf
[7]: https://deliverypdf.ssrn.com/delivery.php?ID=677119021086096013109002116117123088095008049065074002106017127113127117012041003020017039115082104096066071054002066122116087083123002118031067001003122084095121007007117009027001110117073087082&EXT=pdf&INDEX=TRUE
[8]: https://deliverypdf.ssrn.com/delivery.php?ID=641117074119118074094029091091090024016073027027075062101005089022078127102114127011096100063045053098009090094096104027099029059021009023036089082101027094068017055042007104067113000100023002119005085029096069093124093080112003084111100096066071&EXT=pdf&INDEX=TRUE
[9]: https://www.sas.upenn.edu/~fdiebold/papers/paper41/abde.pdf
[10]: https://www.nber.org/system/files/working_papers/w13825/w13825.pdf

