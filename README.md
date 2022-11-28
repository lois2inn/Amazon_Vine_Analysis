# Amazon_Vine_Analysis

Analysis of Amazon's vine review program using PySpark and AWS RDS with PostgreSQL.

## Overview

The project aims to help an account manager at BigMarket get an overview of what big data actually is. Then, Amazon reviews written by members of the paid Amazon Vine program are to be analyzed. The Amazon Vine program is a service that allows manufacturers and publishers to receive reviews for their products. Companies pay a small fee to Amazon and provide products to Amazon Vine members, who are then required to publish a review. The below tasks are accomplished:
- Explain how MapReduce processes big data within Hadoop context.
- Use Python's MRJob to practice MapReduce outside Hadoop system.
- Describe how NLP collects and analyzes text data. 
- Use PySpark in Google Colab to extract and process data.
- Use NLP in conjunction with PySpark to build NLP pipeline.
- Use AWS Simple Storage Service (S3) and relational databases for basic cloud storage.
- Analyze Amazon reviews written by members of the paid Amazon Vine program as follows:
  - Use PySpark to perform the ETL process to extract the Watch reviews dataset and transform the data. 
  - Connect to an AWS RDS instance, and load the transformed data into pgAdmin.
  - Use PySpark to determine if there is any bias toward favorable reviews from Vine members in dataset.

## Resources

- Apache Spark 3.3.1
- MRJob-0.7.4
- NLKT
- Google Colaboratory
- AWS Relational Database Service (RDS) and Simple Storage Service (S3)
- SQL and PgAdmin
- Amazon customer review datasets

## Results

### Extract-Transform-Load of Amazon Product Reviews

- Of the 50 datasets of amazon reviews, **Watches** category is analyzed for this project. The dataset can be found [here](https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_us_Watches_v1_00.tsv.gz).
- The Watches reviews dataset has over 960K reviews. All of the data is extracted into a dataframe, which is then transformed into four separate dataframes that match the database table schema as shown below: 
<table>
  <tr>
    <td><img src="images/customers_df.png" width="500"/></td>
    <td><img src="images/products_df.png" width="400"/></td>
  </tr>
  <tr>
    <td><img src="images/review_id_df.png" width="500"/></td>
    <td><img src="images/vine_df.png" width="400"/></td>
  </tr>
</table>

- The transformed data is uploaded into the appropriate database tables.
<table>
  <tr>
    <td><img src="images/customers_table.png" width="250"/></td>
    <td><img src="images/products_table.png" width="500"/></td>
  </tr>
  <tr>
    <td><img src="images/review_id_table.png" width="400"/></td>
    <td><img src="images/vine_table.png" width="400"/></td>
  </tr>
</table>

### Determine Bias of Amazon Reviews

- **PySpark** is used to analyze Vine reviews data, to determine if a paid Vine review makes a difference in the percentage of 5-star reviews. In order to focus on reviews that would be considered more likely to be helpful, the dataset is filtered so that:
  - the count of total votes is equal to or greater than 20.
  - Percentage of helpful votes to total votes is equal to or greater than 50%.
-  Based on above filters, there are **a total of 8390 helpful reviews** in Vine and non-Vine services combined.
<table>
  <tr><td>Total Reviews</td></tr>
  <tr><td><img src="images/total_reviews.png" width="600"/></td></tr>
</table>

- There are **47 reviews on Vine** services and **8343 reviews on non-Vine** services. This shows that Vine members made just 0.6% of total reviews while non-Vine members contributed over 99% of reviews.  
<table>
  <tr>
   <td>Vine Reviews:</td>
   <td>Non-Vine Reviews: </td>
 </tr>
 <tr>
   <td><img src="images/paid_reviews.png" width="500"/></td>
   <td><img src="images/unpaid_reviews.png" width="500"/></td>
 </tr>
</table>

- It is found that **15 Vine members gave five-star reviews** of the total 47 Vine reviews collected. That shows that **32% of Vine members gave 5-star ratings**.
- There are **4318 five-star non-Vine reviews** in the Watches category. This shows that around **52% of non-Vine reviews are 5-star ratings**.
<table>
  <tr><td>Review Summary:</td></tr>
  <tr><td><img src="images/summary_1.png" width="600"/></td></tr>
</table>

## Summary

- Based on the results above, it can be seen that there are very less Vine reviews compared to non-Vine reviews based on specified filter criteria in the  Watches category.
Vine members did not show bias when rating their products 
- State if there is any positivity bias for reviews in the Vine program. Use the results of your analysis to support your statement. 
- Then, provide one additional analysis that you could do with the dataset to support your statement.
<table>
  <tr>
   <td><img src="images/del_3.png" width="700"/></td>
 </tr>
 </table>
