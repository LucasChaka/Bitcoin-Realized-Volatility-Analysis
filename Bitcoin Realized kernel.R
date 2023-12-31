#The following is the code used to estimate the Flottopped Kernel based RV estimator.

rm(list=ls())

#Set Working Directory

setwd("C:/Users/lucas/Desktop/github project")
getwd()

#The data is too large, therefore, it might be neccessary to increase the memory capacity of R

memory.limit()

memory.limit(size=15000)

Bitcoin <- read.csv("Bitcoin.csv.gz", header = TRUE, sep = ",", quote = "\"", comment.char = "", skip = 0, nrows = -1)

head(Bitcoin)

#install necessary packages
install.packages("highfrequency")
library(xts)
library(zoo)
install.packages("lubridate")
library(lubridate)
require(data.table) #package for producing matrix tables in r
library(moments)

require(highfrequency)

time<-as_datetime(Bitcoin$time)

minute_interval <- as.xts(Bitcoin$price, order.by=time)


#Calculate Flat-top Kernel Based RV

rvKernel <- rKernelCov(rData = minute_interval, alignBy = "minutes",
                       alignPeriod = 5, makeReturns = TRUE)

head(rvKernel)

kv<-sqrt(rvKernel)

head(kv)

# Export the new data set
BitcoinRV <- as.data.frame(kv)

write.csv(BitcoinRV, file = "BitcoinRV.csv")





