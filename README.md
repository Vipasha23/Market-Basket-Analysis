# Market-Basket-Analysis

## Abstract
In this project, the objective of **Market Basket Analysis** is to increase sales by identifying products bought together by customers. Based on e-commerce data or prediction, recommendations will be displayed on the e-commerce website. I have applied **Association Rules** and various measures of Market Basket Analysis to understand the recommender system.

The process involved:
1. Handling missing data.
2. Data loss management.
3. Data visualization.
4. Applying the Apriori algorithm for Association Rules.

Finally, I concluded the results based on this analysis.

## Introduction
**Market Basket Analysis** is an essential topic for every online or offline retail business.

### What is Market Basket Analysis?
Market Basket Analysis is a modeling method used to identify products that are purchased together. In other words, if a customer buys one product, what is the probability that they will buy another product along with it? This technique is also called **Affinity Analysis**.

The goal of Market Basket Analysis is to increase sales by identifying products frequently bought together. Based on this data, recommendations can be displayed on e-commerce websites.

Before diving into association rules, let’s first understand the **Recommender System**.

### Recommender System
A recommender system collects customer purchasing behavior and predicts products that are likely to be bought together. Based on these predictions, it recommends a list of products to the customer. For instance, Amazon and Netflix use recommendation systems extensively.

## Association Rules

### What are Association Rules?
**Association Rules** are a method of **Data Mining**. The idea is to find statistical associations between items in large datasets, such as items purchased together in a supermarket. Unlike strict deterministic rules, association rules are statistical.

### Use Cases of Association Rules
1. **Medicine**: Used to help diagnose patients by analyzing symptom relationships.
2. **Retail**: Helps retailers understand purchasing patterns and adjust marketing strategies.
3. **User Experience (UX) Design**: Optimizes website user interfaces based on user behavior.
4. **Entertainment**: Used by platforms like Netflix and Spotify for content recommendations.

### How Association Rules Work
Association rules use **support**, **confidence**, and **lift** as measures of interestingness in data mining. These are calculated using the frequency of items appearing together in transactions. The Apriori algorithm helps discover these relationships.

### Key Metrics of Association Rules

1. **Support**:
   - **Definition**: Support is the proportion of transactions in the dataset that contain a particular itemset.
   - **Formula**:
     \[
     \text{Support}(A) = \frac{\text{Number of transactions containing } A}{\text{Total number of transactions}}
     \]
   - **Interpretation**: How frequently the itemset appears in the dataset.

2. **Confidence**:
   - **Definition**: Confidence is the likelihood that item `B` is purchased when item `A` is purchased.
   - **Formula**:
     \[
     \text{Confidence}(A \Rightarrow B) = \frac{\text{Support of } (A \text{ and } B)}{\text{Support of } A}
     \]
   - **Interpretation**: The probability of purchasing `B` given that `A` is already purchased.

3. **Lift**:
   - **Definition**: Lift shows how much more likely `B` is purchased when `A` is purchased compared to when `B` is purchased independently.
   - **Formula**:
     \[
     \text{Lift}(A \Rightarrow B) = \frac{\text{Confidence}(A \Rightarrow B)}{\text{Support of } B}
     \]
   - **Interpretation**: Lift measures the strength of an association between items `A` and `B`. A lift value greater than 1 indicates that `A` and `B` are more likely to be bought together than separately.

## Apriori Algorithm

The **Apriori Algorithm** is one of the most popular algorithms used in market basket analysis. It works by identifying frequent itemsets and expanding them step-by-step to discover association rules.

### Steps:
1. Set a **minimum support threshold**.
2. Generate frequent itemsets that meet the support threshold.
3. Use these itemsets to generate association rules.

### Example of Apriori Rule:
If a customer buys milk and bread, there is a likelihood they will also buy butter. This is expressed with support, confidence, and lift.

## Conclusion
Using market basket analysis, we can better understand customer purchasing behavior and use that knowledge to recommend products more effectively, thereby increasing sales and improving customer satisfaction.
