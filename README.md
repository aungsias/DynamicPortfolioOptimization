![Eigen](eigen.png)

## About

Welcome to ***Eigen***, an evolving repository showcasing my work primarily in finance and machine learning, with occasional forays into other business and economics domains. Created to archive and disseminate my ongoing endeavors, Eigen is subject to regular and frequent updates, both in content and structure.

The projects within this repository are comprehensive undertakings aimed at solving conundrums mainly within the capital markets; the projects therefore center at the intersection of finance, programming, and data science. The repo serves as a conduit for my own intellectual curiosity, but I hope it engenders insights that are useful for everyone else. Regardless of whichever project you peruse, I hope you walk away having learned at least something!

Feel free to explore, and thank you for taking the time to visit my repository.

## Installation

To clone the repository and install required packages for this project, follow these steps:

```bash
# Clone the repository
git clone https://github.com/aungsias/Eigen.git

# Navigate to the project directory
cd Eigen

# Install required packages
pip install -r requirements.txt
```

## Contact Info

- Email: [aungsi.as99@gmail.com](mailto:aungsi.as99@gmail.com)
- LinkedIn: [Aung Si](https://www.linkedin.com/in/aungsi99)

## Project Catalogue

- [DynamicAssetManagement](DynamicAssetManagement) - In this project, I engineered a dynamic, machine learning-driven framework for adaptive sector-based investment. Through biannual model recalibrations, the strategy remains agile, adjusting to market shifts and optimizing asset allocation. A 16-year backtest shows it outperforms traditional benchmarks like the S&P 500. The architecture incorporates risk management via a custom loss function, making it suitable for long-only portfolios. I also discuss its limitations and propose avenues for future refinement.

- [DeepLearningPortfolioOptimization](DeepLearningPortfolioOptimization) - The endeavor involves employing neural networks for portfolio optimization, inspired by a [paper from the University of Oxford](DeepLearningPortfolioOptimization/reference_paper/DeepLearningForPortfolioOptimization_Oxford.pdf) but diverges notably in execution. It explores both leveraged and non-leveraged strategies, with notable modifications like eschewing volatility scaling and employing different activation functions. The LSTM model, particularly in a leveraged setting, outperformed others and the VTI index significantly over a decade-long backtesting period. The methodology also showcases a forward-looking approach as opposed to the static nature of traditional Mean Variance Optimization. The detailed examination of models' performance during the COVID-19 downturn displayed the adaptability of LSTM models in asset allocation, substantiating the potential of neural networks in financial portfolio optimization.

This project focuses on using neural networks for optimizing investment portfolios, drawing inspiration from a University of Oxford study but with significant differences in implementation. This includes experimenting with both leveraged and non-leveraged investment strategies, opting out of volatility scaling, and using various activation functions in the models depdending on whether the strategy is leverage on or leverage off. The Long Short-Term Memory (LSTM) neural network, especially when applied to leveraged investments, demonstrated superior performance compared to other models and the VTI index across a ten-year backtesting period. This approach is also forward-looking, contrasting with the static nature of traditional Mean-Variance Optimization techniques. The LSTM models showed resilience and outperformance even within regimes of market turmoil, namely the Q1 market crash of 2020 caused in by the COVID-19 pandemic.