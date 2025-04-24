-- Q1: Find the top 5 regions with the highest average AI Adoption Rate (%)

This query selects top 5 countries with the highest average AI adoption rate.

Select country, round(avg(ai_adoption_rate),2) as Avg_AI_Adoption_Rate
from AIimpact_Data
group by Country 
order by Avg_AI_Adoption_Rate desc
limit 5;

-- Q2: Calculate the average Revenue Increase Due to AI (%) grouped by Year.

This query gives what the average revenue increase due to AI per year.


Select year, round(avg(revenue_increase_due_to_ai),2) as avg_revenue_increase
from AIimpact_Data
group by YEAR
order by year desc;



-- Q3: List all countries where Job Loss Due to AI (%) is greater than 20%.

This query selects countries where the percentage of job loss due to AI exceeds 20%.


select
	country,
	Job_Loss_Due_to_AI
from AIimpact_Data
where Job_Loss_Due_to_AI > 20;



-- Q4: Create a classification where: AI Adoption Rate (%) > 70 → 'High' 40–70 → 'Medium' <40 → 'Low'

This query classifies AI adoption into three categories based on the adoption rate:
•	High: AI adoption rate > 70%
•	Medium: 40% ≤ AI adoption rate ≤ 70%
•	Low: AI adoption rate < 40%

Select
	ai_adoption_rate,
	case
		when`AI_Adoption_Rate` > 70 then 'High'
		when`AI_Adoption_Rate` between 40 and 70 then 'Medium'
		when`AI_Adoption_Rate` < 40 then 'Low'
	end as ai_adoption_rate_pct
From aiimpact_data
order by ai_adoption_rate desc;



-- Q5: Find the Year and Country combination with the highest AI-Generated Content Volume.

This query returns the country and year combination with the highest AI-generated content volume.

WITH RankedData AS (
    SELECT country, year, ai_generated_content_volume,
           ROW_NUMBER() OVER (ORDER BY ai_generated_content_volume DESC) AS first_rank
    FROM aiimpact_data
)

SELECT country, year, ai_generated_content_volume
FROM RankedData
WHERE first_rank = 1;




