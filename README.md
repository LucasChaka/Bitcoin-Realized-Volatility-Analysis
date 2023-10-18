# Bitcoin Realized Volatility Analysis 

The following is an in-depth exploration of the fascinating world of Bitcoin volatility. This project dives deep into the dynamics of Bitcoin's price movements, estimating its realized volatility in section 1 and exploring models to forecast volatility and it's real-world applications in section 2.

## Table of Contents
Section 1
- Introduction
- Measuring and Defining Volatility
   - Discrete-time Process
   - Continuous-time Process
- Overcoming Micro-Structure Noise Effect with Calendar Time Sampling
   - Micro-Structure Noise
   - Optimal Sampling
- Bitcoin Realized Volatility
   - Data
   - Bitcoin Daily Price Data Over Time
   - Bitcoin Return and Asset Return Styled Facts
   - Bitcoin Realized volatility
     
Section 2


Section 3
- Limitation and Further Considerations


## Introduction

In recent years, the finance industry has witnessed a technological revolution, ushering in an era of unprecedented possibilities. Technological advancements have paved the way for the collection and analysis of high-frequency financial data, offering invaluable insights into the ever-evolving dynamics of global markets. These high-frequency data streams, often characterized by irregular temporal spacing, provide a tick-by-tick record of essential financial variables. This financial transformation has significantly enhanced the measurement and estimation of volatility, a critical metric for gauging the risk associated with asset returns. Volatility quantifies the fluctuations and deviations of asset prices from their expected levels, making it an indispensable tool for investors and analysts alike.

In this project, the focus is volatility estimation and modeling, via the *Realized Volatility (RV)* estimator. While RV has long held a pivotal role in traditional financial domains such as forex, derivatives, and equity markets, its expansion into the cryptocurrency sphere, with a specific emphasis on Bitcoin, introduces a compelling layer of complexity. This endeavor seeks to unravel the mysteries of RV within the context of Bitcoin.

At the heart of this exploration lies a fundamental question: How does realized volatility (RV) manifest in the Bitcoin price time series? The mission at hand is clear—to assess and compare the performance of this model in deciphering the volatilities of Bitcoin's price movements. 

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


## Overcoming Micro-Structure Noise Effect with Calendar Time Sampling

### Micro-Structure Noise

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

To account for microstructure noise, the following assumptions can be considered:

1. In the case of IID noise structure:
   - $E(\varepsilon) = 0$

2. In the case of dependent noise structure:
   - $E(\varepsilon) = 0$
   - stationary-and-is-exponentially-declining as the time intervals increase

3. $V_{t,i} = \varepsilon_{t,i} - \varepsilon_{t,{i-1}}$ is constant.
4. Noise is independent of the price process.

If the data is contaminated by microstructure noise, then RV is not a consistent estimator of the true variance. Hence, microstructure noise bias exists.

### Optimal Sampling

In addition to microstructure noise bias, the estimation of tick-by-tick price series entails the accumulation of noise that affects the estimator's variance. This results in a bias/variance trade-off during the estimation process ([Bandi, F. M. Russell, J. R., (2004)][11]). The bias-variance trade-off refers to the relationship between the bias and variance of an estimator. In the context of volatility estimation, bias represents the difference between the expected value of the estimator and the true value of the volatility. On the other hand, variance measures the variability of the estimator's values around its expected value.

To estimate volatility in a financial time series, it is recommended to use an **optimal** equidistant sampling scheme where the intervals between the ticks are evenly spaced. Here's why:

Suppose there are intervals in a day, denoted as $0=\tau_0<\tau_1<.....<\tau_M=1$, and the length of the equidistant sub-intervals is represented as $\delta_{i,{M_t}}=\tau_i-\tau_{i-1}$. As $\delta_{i,{M_t}}$ approaches zero, the unobserved volatility in a continuous-time process, $\int_{\tau_{i-1}}^{\tau_i} \sigma(t+\tau)d\tau$, becomes a measure of true volatility. According to [Zhang, L., Mykland, P. A., Ait-Sahalia, Y. (2005)][12], when the observed price process includes both the true underlying price process and microstructure noise, it is shown that RV will be overwhelmed by the noise, leading to biased estimation. Therefore, it may be optimal to sample less frequently. However, here is the paradox: the lower the sampling frequency, the less RV converges to the true unobserved volatility. For example, shifting from 1-minute equidistant sampling to 1-hour equidistant sampling results in a reduced convergence to true unobserved volatility.

The question at hand is determining the optimal frequency for data sampling. There are several options one can choose from: calendar time sampling, transaction time sampling, business time sampling, and tick-by-tick sampling, all of which aim to minimize microstructure noise bias. Although the above sampling techniques help minimize bias, other approaches account for a bias-variance trade-off, such as sparse sampling, a method to find the optimal frequency by minimizing Mean-Squared-Error (MSE), or first sampling the intervals equidistantly and determining optimal MSE. However, one recommendation that addresses both microstructure bias and the bias/variance trade-off is Kernel-based RV estimators. Additionally, in the estimation process of a Kernel based estimator, a 5-minute equidistant interval is employed as a benchmark. According to [Liu, L. Y., Patton, A. J., & Sheppard, K. (2015)][12], when 5-minute realized volatility (RV) is used as the benchmark of RV estimation, there is little evidence to suggest that it is significantly outperformed by any other measures in terms of estimation accuracy while addressing the previously mentioned estimation challenges. [Hansen et al. (2006)][14] and [Barndorff et al. (2008)][13] have extensively explored the topic of optimal sampling and Kernel-based RV estimators, addressing both issues in estimating RV.

The first estimator, proposed by [Hansen et al. (2006)][14], is an auto-correlation corrected RV:

$$
RV_t^{(HL)} = RV_t^{(all)} + 2\sum_{h=1}^H \frac{M}{M-h}\hat{\gamma}_h
$$

where

```math
\hat{\gamma}_h = \frac{M}{M-h}\sum_{j=1}^{(M-h)}r_{t,j}r_{j+h}
```


Here, $h = E(RV_t^{(all)}|I_t)$ and $H = 1$.

This estimator, under the assumptions of IID noise structure, was found to be unbiased but inconsistent. Therefore, [Barndorff et al. (2008)][13] proposed the flat-topped kernel estimator based on $r_{t,i} = r_{t,i}^* + \varepsilon_{t,i} - \varepsilon_{t,i-1}$:

```math
RV_t^{(BHLS)}=RV_t^{(all)}+\sum_{h=1}^H K(h-1/H). (\hat{\gamma}_h+\hat{\gamma}_{-h}),
```

where $k(x)$ for $x \in [0, 1]$ is a non-stochastic weight function such that the Kernel parameters are $k(0) = 1$ and $k(1) = 0$. The Kernel-based RV estimator ($RV_t^{(BHLS)}$) is employed in this project, which is an unbiased and consistent estimator.

## Bitcoin Realized Volatility
### Data

[bitcoincharts.com][4] offers high-frequency tick-by-tick data from several cryptocurrency exchange platforms. Among the exchange rate platforms listed, Kraken holds the highest volume of Bitcoins traded. The dataset covers a significant timeframe, ranging from January 8th, 2014, to March 14th, 2021. Notably, the data is continually refreshed, ensuring that the code can access the most current insights whenever it is executed. The exchange rate is between Bitcoin and the Euro

### Bitcoin Daily Price Data Over Time

#### **Figure 1: Bitcoin Daily Price, BTC-EUR, 2014-2023**

![Fig 1_ Bitcoin Daily price, BTC-EUR](https://github.com/LucasChaka/Bitcoin-Realized-Volatility-Analysis/assets/140816619/955cce6b-14a5-4809-9730-acdcb0157124)

Source: [Section 1 - Python Code](Section%201_Python%20Code.ipynb)


### Bitcoin Return and Asset Return Stylized Facts

Financial returns exhibit generally accepted statistical characteristics. These stylized facts provide analysts with insights into how data on asset returns can be analyzed. Since there are several arguments that suggest Bitcoin behaves more like an asset than a currency (refer to [Baur, D. G., & Dimpfl, T. (2017)][15] and [Baur, D. G., & Dimpfl, T. (2021)][16]), it's worth analyzing whether it's worthwhile to estimate RV. The following are some common characteristics of asset returns:

- **Absence of Autocorrelations:** Autocorrelations of asset returns are often insignificant, except for very small intra-day time scales (mostly 20 minutes). [Cont (2001)][17]
- **Leptokurtic Distribution:** According to [Rydberg (2000)][18], the distribution of returns has tails that are heavier than the tails of a normal distribution. Most empirical findings for financial assets show that the distribution for daily returns is leptokurtic.
- **Gain-Loss Asymmetry:** According to [Cont (2001)][17], one observes large draw-downs in asset prices and asset index values but not equally large upward movements. [Rydberg (2000)][18] also noted that there is evidence that the distribution of asset returns is slightly negatively skewed.
- **Aggregational Gaussianity:** As the time scale (t) increases from intra-day to daily to weekly to monthly and so on, the returns distribution looks more like a normal distribution. As [Rydberg (2000)][18] puts it, "For decreasing sampling frequencies, the central limit law sets in, and the distribution of the log-returns tends toward a Gaussian law."

#### **Figure 2(a): Bitcoin Hourly Autocorrelation function**
![Fig 2(a) Bitcoin Hourly Autocorrelation function](https://github.com/LucasChaka/Bitcoin-Realized-Volatility-Analysis/assets/140816619/ffeb4aa3-3b9b-4e4b-a53f-17f4b327c0fc)
Source: [Python Code](Python%Code.ipynb)

#### **Figure 2(b): Bitcoin Daily Autocorrelation function**
![Fig 2(b) Bitcoin Daily Autocorrelation function](https://github.com/LucasChaka/Bitcoin-Realized-Volatility-Analysis/assets/140816619/6246ecfc-0c38-4361-aee8-8ddd93ba869a)
Source: [Python Code](Python%Code.ipynb)

#### **Figure 2(c): Bitcoin Weekly Autocorrelation function**
![Fig 2(c) Bitcoin Weekly Autocorrelation function](https://github.com/LucasChaka/Bitcoin-Realized-Volatility-Analysis/assets/140816619/b80c9c7e-0e74-4b25-846e-b1857301c21c)
Source: [Python Code](Python%Code.ipynb)

#### **Figure 2(d): Bitcoin Monthly Autocorrelation function**
![Fig 2(d) Bitcoin Monthly Autocorrelation function](https://github.com/LucasChaka/Bitcoin-Realized-Volatility-Analysis/assets/140816619/ce7fc122-9b19-4780-8474-230cb28f50b6)
Source: [Python Code](Python%Code.ipynb)

#### **Figure 3(a): Bitcoin Hourly Interval Distribution**
![Fig 3(a) Bitcoin Hourly Interval Distribution](https://github.com/LucasChaka/Bitcoin-Realized-Volatility-Analysis/assets/140816619/1d50e887-1708-4f89-86c9-838f27090e21)
Source: [Python Code](Python%Code.ipynb)

#### **Figure 3(b): Bitcoin Daily Interval Distribution**
![Fig 3(b) Bitcoin Daily Interval Distribution](https://github.com/LucasChaka/Bitcoin-Realized-Volatility-Analysis/assets/140816619/fe53fc38-5490-466f-97d9-f2867222b058)
Source: [Python Code](Python%Code.ipynb)

#### **Figure 3(c): Bitcoin Weekly Interval Distribution**
![Fig 3(c) Bitcoin Weekly Interval Distribution](https://github.com/LucasChaka/Bitcoin-Realized-Volatility-Analysis/assets/140816619/f0eb0c15-74f6-4e03-9c95-b330602b0a2d)
Source: [Python Code](Python%Code.ipynb)

- **Volatility Clustering:** Different measures of volatility display positive autocorrelation over several days, quantifying the fact that high-volatility events tend to cluster in time. [Cont (2001)][17] also explained volatility clustering as large price variations that are more likely to be followed by large price variations.

#### **Figure 4: Bitcoin Log return**
![Fig 4_Bitcoin Log return](https://github.com/LucasChaka/Bitcoin-Realized-Volatility-Analysis/assets/140816619/a3ac831a-f8c5-4ff2-ad50-b920eab38a67)
Source: [Python Code](Python%Code.ipynb)

The figures above illustrate how Bitcoin's returns exhibit characteristics similar to the stylized facts. In Figure 2(a), it can be observed that the autocorrelation function is significant for the majority of lags. Figure 2(b) reveals that, except for lags 1, 7, and 10, most lags are not significant. As the time scale (t) increases from daily to weekly or monthly, the significance decreases across all 10 lags, indicating the absence of autocorrelation. Furthermore, in Figure 3, it is noticable that the returns tend to approach a normal distribution as time (t) increases from hourly to daily to monthly. Notably, Figure 3(a) displays a leptokurtic distribution in the hourly interval. Thus, it can be concluded that aggregational Gaussianity is observed. The returns also exhibit negative skewness, suggesting gain-loss asymmetry. Additionally, Figure 4 illustrates volatility clustering, for example, around the 2018 and 2021-2022 time periods. Consequently, it can be assumed, for further analysis, that Bitcoin follows the behavior of other assets in its returns.

### Bitcoin Realized volatility

Based on the flat-topped kernel-based RV estimator explained above, the Bitcoin realized volatility is depicted as follows:

#### **Fig 5: Bitcoin Realized Volatility**
![Fig 5_ Bitcoin Realized Volatility](https://github.com/LucasChaka/Bitcoin-Realized-Volatility-Analysis/assets/140816619/b8a201dc-49e5-4348-bf88-5b3dba913985)
Source: [Python Code](Python%Code.ipynb), [Bitcoin Realized Kernel](Bitcoin%Realized%Kernel.R)

*Note: The estimation for the RV is conducted using the R package 'highfrequency.' Analysts can also use the same R package through the Python rpy2 package. However, I find it easier and more time-efficient to estimate the RV in R than in Python.*

## Reference

Ait-Sahalia, Y., Yu, J. (2008). High frequency market microstructure noise estimates and liquidity measures (No. w13825). National Bureau of Economic Research.

Andersen, T. G., & Benzoni, L. (2008). Realized Volatility, Working Paper 2008-14.

Andersen, T. G., Bollerslev, T., Christoffersen, P. F., & Diebold, F. X. (2006). Volatility and correlation forecasting. Handbook of economic forecasting, 1, 777-878.

Andersen, T. G., Bollerslev, T., & Diebold, F. X. (2005). Roughing It Up: Including Jump Components in the Measurement. Modeling and Forecast (ing of Return Volatility,tTech. rep., NBER.

Andersen, T. G., Bollerslev, T., Diebold, F. X., & Ebens, H. (2001). The distribution of realized stock return volatility. Journal of financial economics, 61(1), 43-76.

Andersen, T. G., Bollerslev, T., & Diebold, F. X. (2010). Parametric and nonparametric volatility measurement. In Handbook of financial econometrics: Tools and techniques (pp. 67-137). North-Holland.

Baur, D. G., & Dimpfl, T. (2017). Realized bitcoin volatility. SSRN, 2949754, 1-26.

Baur, D. G., & Dimpfl, T. (2021). The volatility of Bitcoin and its role as a medium of exchange and a store of value. Empirical Economics, 61(5), 2663-2683.

Bandi, F. M. Russell, J. R., (2004). Microstructure noise, realized volatility, and optimal sampling. In Econometric Society 2004 Latin American Meetings (No. 220). Econometric Society.

Barndorff‐Nielsen, O. E., Hansen, P. R., Lunde, A., & Shephard, N. (2008). Designing realized kernels to measure the ex post variation of equity prices in the presence of noise. Econometrica, 76(6), 1481-1536.

Cont, R. (2001). Empirical properties of asset returns: stylized facts and statistical issues. Quantitative finance, 1(2), 223.

Duong, D., & Swanson, N. R. (2011). Volatility in discrete and continuous-time models: A survey with new evidence on large and small jumps. In Missing data methods: Time-series methods and applications (Vol. 27, pp. 179-233). Emerald Group Publishing Limited.

Hansen, P. and Lunde, A. (2006). Realized variance and market microstructure noise. Journal of Business and Economic Statistics, 24, 127-218.

Liu, L. Y., Patton, A. J., & Sheppard, K. (2015). Does anything beat 5-minute RV? A comparison of realized measures across multiple asset classes. Journal of Econometrics, 187(1), 293-311.

McAleer, M., Medeiros, M. C. (2008). Realized volatility: A review. Econometric Reviews, 27(1-3), 10-45.

Rydberg, T. H. (2000). Realistic statistical modelling of financial data. International Statistical Review, 68(3), 233-258.

Zhang, L., Mykland, P. A., At-Sahalia, Y. (2005). A tale of two time scales: Determining integrated volatility with noisy high-frequency data. Journal of the American Statistical Association, 100(472), 1394-1411.

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
[11]: http://repec.org/esLATM04/up.3725.1082044351.pdf
[12]: https://www.sciencedirect.com/science/article/abs/pii/S0304407615000329
[12]: https://www.princeton.edu/~yacine/twoscales.pdf
[13]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=620203
[14]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=506542
[15]: https://www.researchgate.net/publication/317994265_Realized_Bitcoin_Volatility
[16]: https://link.springer.com/article/10.1007/s00181-020-01990-5
[17]: http://rama.cont.perso.math.cnrs.fr/pdf/empirical.pdf
[18]: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1751-5823.2000.tb00329.x
