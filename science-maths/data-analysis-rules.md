# Data Analysis Rules and Guidelines

When performing data analysis, follow these comprehensive rules to ensure high-quality, reproducible, and ethical work.

## Data Understanding and Exploration

- **Always start with data exploration before analysis.** Understand the structure, shape, and basic characteristics of your dataset.
- **Examine data types, missing values, and distributions** before making assumptions about the data.
- **Document data sources, collection methods, and any known limitations** in your analysis.
- **Check for duplicates, outliers, and anomalies** early in the exploration phase.
- **Understand the business context and domain knowledge** before applying statistical methods.
- **Verify data quality issues** such as inconsistent formats, encoding problems, or data entry errors.
- **Examine relationships between variables** through correlation analysis and cross-tabulations before building models.
- **Document the sample size and any sampling methods** used in data collection.

## Data Cleaning and Preprocessing

- **Handle missing values explicitly.** Document your strategy (imputation, deletion, or flagging) and justify it based on the data and analysis goals.
- **Preserve original data.** Always work on copies of the original dataset; never modify source data.
- **Document all data transformations** including filtering, aggregations, and feature engineering steps.
- **Validate data after transformations** to ensure transformations worked as expected.
- **Handle outliers thoughtfully.** Don't automatically remove outliers; investigate their cause and impact first.
- **Standardise or normalise features** when appropriate, but document why and which method you used.
- **Create reproducible data cleaning pipelines** that can be rerun on new data.
- **Check for data leakage** between training and test sets, especially in time-series data.
- **Validate categorical encodings** to ensure they match the intended analysis approach.

## Statistical Methodology

- **Choose appropriate statistical tests** based on data distribution, sample size, and assumptions.
- **Verify assumptions** of statistical tests (normality, independence, homogeneity of variance) before applying them.
- **Report effect sizes, not just p-values.** P-values alone don't indicate practical significance.
- **Use confidence intervals** to communicate uncertainty in estimates.
- **Avoid p-hacking and multiple comparison problems.** Adjust significance levels when performing multiple tests.
- **Consider non-parametric alternatives** when assumptions aren't met.
- **Document the rationale** for choosing specific statistical methods over alternatives.
- **Report both statistical and practical significance** in your findings.
- **Use appropriate sample size calculations** before collecting data when possible.

## Data Visualisation

- **Choose visualisations that match your data type and analysis goals.** Use bar charts for categorical data, scatter plots for relationships, histograms for distributions.
- **Label axes clearly** with descriptive names and units of measurement.
- **Use colour thoughtfully.** Ensure visualisations are accessible to colour-blind viewers and use colour to convey meaning, not decoration.
- **Avoid misleading visualisations.** Don't truncate axes without clear indication, use appropriate scales, and avoid 3D charts when 2D would suffice.
- **Include context and reference points** in visualisations (e.g., benchmarks, historical averages).
- **Make visualisations reproducible** by using code-based plotting libraries rather than manual chart creation.
- **Use consistent styling** across all visualisations in a single analysis.
- **Include titles and captions** that explain what the visualisation shows and any important context.
- **Consider your audience** when choosing visualisation complexity and detail level.

## Model Building and Validation

- **Split data appropriately** into training, validation, and test sets before any model building.
- **Never use test data** for model selection or hyperparameter tuning.
- **Use cross-validation** when sample size is limited, but understand its limitations.
- **Compare multiple models** using appropriate metrics and validation procedures.
- **Avoid overfitting.** Use regularisation, feature selection, or simpler models when appropriate.
- **Evaluate models using multiple metrics** relevant to the problem (accuracy, precision, recall, F1, AUC, etc.).
- **Validate model assumptions** and check residuals for regression models.
- **Test model performance on unseen data** before finalising conclusions.
- **Document model hyperparameters** and the process used to select them.
- **Consider model interpretability** alongside predictive performance, especially for business applications.

## Reproducibility

- **Use version control** for all analysis code and scripts.
- **Set random seeds** for any random processes (sampling, train/test splits, model initialisation) to ensure reproducibility.
- **Document package versions** and environment setup (use requirements.txt, environment.yml, or similar).
- **Organise code into logical sections** with clear comments explaining each step.
- **Save intermediate results** when computations are time-consuming, but document how to regenerate them.
- **Use relative paths** and avoid hardcoded absolute paths in your code.
- **Create clear, executable scripts** that can be run from start to finish without manual intervention.
- **Document any manual steps** or decisions that can't be automated.

## Documentation and Reporting

- **Write clear, concise analysis reports** that explain methodology, findings, and limitations.
- **Include code alongside results** in reports when using notebooks or literate programming tools.
- **Document data sources and collection dates** in all reports.
- **Explain statistical methods** in terms your audience can understand.
- **Report uncertainty and limitations** honestly; don't overstate confidence in results.
- **Include visualisations** that support your key findings.
- **Provide actionable insights** based on your analysis, not just statistical results.
- **Document assumptions** made during the analysis and their potential impact.
- **Include a methods section** that allows others to understand and replicate your work.

## Ethical Considerations

- **Protect privacy and confidentiality.** Never share personally identifiable information or sensitive data.
- **Consider bias in data collection and analysis.** Be aware of sampling bias, selection bias, and other sources of bias.
- **Avoid discriminatory practices.** Check models for fairness across different groups and demographics.
- **Be transparent about limitations** and potential misuse of your analysis.
- **Respect data use agreements** and terms of service when working with external data.
- **Consider the societal impact** of your analysis and how results might be interpreted or misused.
- **Document ethical considerations** and any steps taken to address them.

## Code Quality for Data Analysis

- **Write readable, well-commented code.** Future you (and others) will thank you.
- **Use meaningful variable names** that describe what the data represents, not just its structure.
- **Break complex analyses into functions** that can be tested and reused.
- **Handle errors gracefully** with appropriate error messages and logging.
- **Avoid hardcoded values.** Use configuration files or constants for parameters that might change.
- **Follow consistent coding style** within your analysis project.
- **Remove or comment out exploratory code** that isn't needed for the final analysis.
- **Use appropriate data structures** (DataFrames, arrays, dictionaries) for your analysis needs.
- **Optimise code for readability first**, then performance if needed.

## Performance and Efficiency

- **Profile code** to identify bottlenecks before optimising.
- **Use vectorised operations** instead of loops when working with large datasets.
- **Consider memory usage** when working with large datasets; use chunking or sampling when appropriate.
- **Cache expensive computations** when the same calculation is needed multiple times.
- **Use appropriate data types** (e.g., categorical types for strings with few unique values) to save memory.
- **Consider parallel processing** for independent computations that can run simultaneously.
- **Don't prematurely optimise.** Focus on correctness and clarity first.

## Validation and Quality Assurance

- **Sanity check results** against domain knowledge and expectations.
- **Compare results** with similar analyses or benchmarks when available.
- **Test edge cases** and boundary conditions in your analysis.
- **Verify calculations manually** for critical results or use known test cases.
- **Check for data consistency** across different parts of your analysis.
- **Review code** before finalising analysis, or have someone else review it.
- **Validate data transformations** by examining intermediate results.
- **Test assumptions** about data distributions and relationships.

## Communication and Collaboration

- **Tailor your communication** to your audience's technical level and needs.
- **Use clear, non-technical language** when explaining results to non-technical stakeholders.
- **Provide context** for statistical findings; explain what they mean in practical terms.
- **Highlight key findings** clearly rather than burying them in technical details.
- **Be prepared to explain your methodology** and defend your choices.
- **Listen to feedback** from domain experts and incorporate their insights.
- **Share code and data** (when appropriate) to enable collaboration and peer review.

## Specific Analysis Types

### Time Series Analysis
- **Check for stationarity** before applying time series models.
- **Handle seasonality and trends** appropriately for your analysis goals.
- **Use appropriate time-based cross-validation** when evaluating time series models.
- **Consider temporal dependencies** and autocorrelation in your analysis.

### Causal Inference
- **Distinguish correlation from causation** clearly in your reporting.
- **Consider confounding variables** and use appropriate methods (e.g., randomised experiments, instrumental variables, difference-in-differences).
- **Document assumptions** required for causal claims.
- **Be cautious about causal claims** from observational data.

### Machine Learning
- **Start with simple models** before moving to complex ones.
- **Use appropriate evaluation metrics** for your problem type (classification, regression, clustering).
- **Interpret model results** in the context of your problem, not just model performance metrics.
- **Consider model explainability** and use techniques like feature importance, SHAP values, or LIME when needed.

### Survey and Experimental Data
- **Document survey methodology** including sampling method, response rate, and potential biases.
- **Check for non-response bias** and its potential impact on results.
- **Use appropriate statistical tests** for experimental designs (t-tests, ANOVA, etc.).
- **Report effect sizes** and practical significance alongside statistical significance.

## Common Pitfalls to Avoid

- **Don't cherry-pick results** that support a preconceived conclusion.
- **Avoid data dredging** (testing many hypotheses without adjusting for multiple comparisons).
- **Don't ignore missing data** or assume it's missing at random without investigation.
- **Avoid overfitting** by using overly complex models on small datasets.
- **Don't confuse statistical significance with practical significance.**
- **Avoid making causal claims** from correlational analyses without proper methodology.
- **Don't ignore outliers** without understanding their cause and impact.
- **Avoid using inappropriate statistical tests** that violate assumptions.
- **Don't report results without context** or interpretation.
- **Avoid black box analyses** that can't be understood or reproduced.

## Tools and Libraries

- **Use established, well-maintained libraries** for statistical analysis and visualisation.
- **Document which tools and versions** you used in your analysis.
- **Prefer reproducible tools** (code-based) over point-and-click interfaces for analysis.
- **Use appropriate tools** for your data size and analysis complexity.
- **Learn your tools deeply** rather than using many tools superficially.

---

**Remember:** Good data analysis is transparent, reproducible, and honest about limitations. The goal is to extract meaningful insights while maintaining scientific rigour and ethical standards. When in doubt, prioritise clarity, reproducibility, and ethical considerations over speed or convenience.

