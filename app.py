from matplotlib.pyplot import figure
from importlib.metadata import distribution

import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats  

st.set_page_config(page_title="Distribution Lab",layout="wide")
st.title("Choose any Probability Distributions")

#distributions from now 

distribution = st.sidebar.selectbox(
    "Choose Distribution",[
        "Bernoulli",
        "Binomial",
        "Normal",
        "Poisson",
        "Exponential",
        "Central Limit Theorem Analysis",
        "Monte Carlo Simulation"
    ]
)


#bernoulli

if distribution == "Bernoulli":
    st.header("Bernouli Distribution")
    p = st.slider("Probablity of Success",0.0,1.0,0.5)
    outcomes =[0,1]
    probs = [1-p,p]
    fig,ax = plt.subplots()
    ax.bar(outcomes,probs)
    ax.set_xticks([0,1])
    ax.set_xlabel("outcome")
    ax.set_ylabel("Probability")
    st.pyplot(fig)
    st.write(f"Mean : {p}")
    st.write(f"Variance : {p*(1-p)}")
    
elif distribution == "Binomial":
 st.header("Binomial Distribution")
 n = st.slider("Number of trials",1,200,10)
 p = st.slider("Probability of success",0.0,1.0,0.5)
 x = np.arange(0,n+1)
 y = stats.binom.pmf(x,n,p)
 
 fig,ax = plt.subplots(figsize=(10,6))
 ax.stem(x,y)

 ax.set_xlabel("Number of successes")
 ax.set_ylabel("Probability")
 ax.set_title("Binomial Distribution")
 st.pyplot(fig)
 st.write(f"expected value : {n*p:.3f}")
 st.write(f"Variance : {n*p*(1-p):.3f}")
 st.write(f"Standard Deviation : {np.sqrt(n*p*(1-p)):.3f}")
 st.info("CHANGE N AND SEE HOW THE Distribution CHANGES BROOO")
 


 #normal
elif distribution == "Normal":
     st.header("Normal Distribution")
     mu = st.slider("mean(mu)",-10.0,10.0,0.0)
     sigma = st.slider("Standard deviation(sigma)",0.1,10.0,1.0)
     x = np.linspace(mu - 5*sigma,mu+5*sigma,1000)
     y = stats.norm.pdf(x,mu,sigma)

     fig,ax = plt.subplots(figsize=[10,5])
     ax.plot(x,y)
     ax.set_title("Normal Distribution")
     ax.set_xlabel("X")
     ax.set_ylabel("Probability Density")
     st.pyplot(fig)
     st.write(f"Mean : {mu:.2f}")
     st.write(f"Variance : {sigma**2:.2f}")
     st.info("Increase the sigma to see the bell curve get wider")

elif distribution == "Poisson":
    st.header("Poisson Distribution")
    lam = st.slider("lambda average (lambda)",1,200,10)
    x = np.arange(0,lam*4)
    y = stats.poisson.pmf(x,lam)

    fig,ax = plt.subplots(figsize=(10,6))
    ax.stem(x,y)
    ax.set_title("Poisson Distribution")
    
    ax.set_xlabel("No of events(k)")
    ax.set_ylabel("Probability mass function")
    st.pyplot(fig)
    st.write(f"expected value : {lam:.3f}")
    st.write(f"Variance : {lam:.3f}")
    st.info("At large lambda values (>30), Poisson behaves like guassian distribution(Normal)")
    
elif distribution == "Exponential":
    st.header("Exponential Distribution")
    lam = st.slider("Enter lambda bro ",0.1,5.0,1.0)

    x = np.linspace(0,10,1000)
    y = stats.expon.pdf(x,scale=1/lam)

    fig,ax = plt.subplots(figsize=[10,6])
    ax.plot(x,y)

    ax.set_title("Exponential distribution")
    ax.set_xlabel("Time to next event")
    ax.set_ylabel("Density")
    st.pyplot(fig)
    st.write(f"Expected value : {1/lam:.2f}")
    st.info("Used for getting waiting times between poisson events")

elif distribution == "Central Limit Theorem Analysis":
    st.header("Central Limit Theorem")
    sample_size = st.slider("Sample Size (n)",1,500,30)
    num_samples = st.slider("Number of Samples",100,10000,1000)
    means = []

    for _ in range(num_samples):
        sample = np.random.uniform(0,1,sample_size)
        means.append(np.mean(sample))

    fig,ax = plt.subplots(figsize=[10,6])
    plt.hist(means,bins=30)
    ax.set_title("Distribution of Sample Means")
    ax.set_xlabel("Sample means")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)
    st.write(f"Expected mean : {np.mean(means):.2f}")
    st.info("As sample size increases , the distribution approaches normal distribution that is Gaussian shaped") 

#montecarlo

elif distribution =="Monte Carlo Simulation":
    st.header("Monte Carlo simulation")
    flips = st.slider("Number of coin flips",1,1000,100)
    p = st.slider("Probablity of heads(assuming fairness)",0.0,1.0,0.5)
    results = np.random.choice([0,1],size=flips,p=[1-p,p])

    cumulative_heads = np.cumsum(results)
    #cumulative heads ratio is the probabllity of each in an array op shit bro
    cumulative_heads_ratio = cumulative_heads / np.arange(1,flips +1)

    fig,ax = plt.subplots(figsize=[10,5])
    ax.plot(cumulative_heads_ratio)
    ax.axhline(p,linestyle='--')

    ax.set_title("Monte carlo Coin Flip example ")
    ax.set_xlabel("Number of flips")
    ax.set_ylabel("Proportion of Flips")
    st.pyplot(fig)
    st.write(f"Final Experimental Probability = {cumulative_heads_ratio[-1]:.4f}")
    st.write(f"True Probability = {p}")

    st.info(
        "Observe how repeated simulations converge toward the true probability.")
    
    
    