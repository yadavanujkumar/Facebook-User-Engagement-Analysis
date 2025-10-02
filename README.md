# Facebook User Engagement Analysis (EDA)

## Overview
This project performs comprehensive Exploratory Data Analysis (EDA) on Facebook user data to identify valuable users that can be focused on to increase business growth. The analysis provides actionable insights to help Facebook make intelligent decisions about user engagement and recommendations.

## Problem Statement
The Facebook dataset consists of user engagement metrics that need to be analyzed to identify which users should be prioritized for business growth. These valuable insights help Facebook:
- Identify high-value users for retention
- Understand user engagement patterns
- Make data-driven recommendations
- Optimize platform features based on user preferences

## Dataset
The `pseudo_facebook.csv` dataset contains 99,003 user records with the following features:
- **User Demographics**: userid, age, date of birth, gender
- **Engagement Metrics**: friend_count, friendships_initiated, tenure
- **Like Activity**: likes (given), likes_received
- **Platform Usage**: mobile_likes, mobile_likes_received, www_likes, www_likes_received

## Analysis Features

### 1. Engagement Score Calculation
A comprehensive engagement score is calculated for each user based on:
- **Friend Count** (25% weight): Social network size
- **Friendships Initiated** (20% weight): Proactive social behavior
- **Likes Given** (20% weight): Content engagement
- **Likes Received** (20% weight): Content creation value
- **Tenure** (15% weight): User loyalty

### 2. User Segmentation
Users are categorized into engagement levels:
- Very High Engagement (score > 0.8)
- High Engagement (0.5 - 0.8)
- Medium Engagement (0.2 - 0.5)
- Low Engagement (< 0.2)

### 3. Demographic Analysis
- Age group distribution and engagement patterns
- Gender-based engagement analysis
- Platform preference (Mobile vs Web vs Both)

### 4. Platform Usage Insights
- Mobile-first users: 50.6%
- Web-first users: 19.2%
- Cross-platform users: 7.7%

## Key Findings

### Top User Characteristics (Top 1000 Users)
- **Average Friend Count**: 2,934 friends (14.9x more than average)
- **Average Likes Given**: 1,572 (10.1x more than average)
- **Average Tenure**: 971 days
- **Gender Distribution**: 63.7% female, 36.1% male
- **Average Age**: 39.1 years

### Engagement Drivers
1. **Friend Connections**: Strong positive correlation with engagement
2. **Like Activity**: Both giving and receiving likes indicate engagement
3. **Platform Usage**: Cross-platform users show highest engagement
4. **Tenure**: Longer-tenured users tend to be more engaged

## Business Recommendations

### 1. User Segmentation Strategy
- Focus retention efforts on highly engaged users (top 1%)
- Create re-engagement campaigns for 99.1% low-engagement users
- Develop personalized experiences for different engagement levels

### 2. Platform Optimization
- Prioritize mobile experience (50.6% of users prefer mobile)
- Enhance cross-platform features to increase engagement
- Optimize for the growing mobile-first user base

### 3. Engagement Enhancement
- Encourage friend connections through recommendations
- Promote content creation and likes through gamification
- Implement features that drive user interactions

### 4. Target Demographics
- Focus on female users (higher engagement rates)
- Create age-appropriate features for different age groups
- Leverage the 50+ age group showing higher engagement

### 5. Retention Programs
- Reward long-tenured users with special features
- Create milestone celebrations for user anniversaries
- Develop loyalty programs for consistently engaged users

## Installation & Usage

### Prerequisites
```bash
pip install -r requirements.txt
```

### Running the Analysis
```bash
python3 facebook_eda_analysis.py
```

### Output Files
1. **facebook_eda_visualizations.png**: Main dashboard with 9 key visualizations
2. **facebook_eda_detailed_analysis.png**: Detailed analysis charts
3. **valuable_users_list.csv**: List of top 1000 valuable users with engagement metrics

## Visualizations
The analysis generates comprehensive visualizations including:
- Engagement score distribution
- User category breakdown
- Demographics analysis (gender, age groups)
- Platform usage patterns
- Friend count vs engagement correlation
- Likes activity patterns
- Top users ranking
- Feature correlation heatmap

## Project Structure
```
Facebook-eda/
├── README.md                              # Project documentation
├── LICENSE                                # MIT License
├── requirements.txt                       # Python dependencies
├── pseudo_facebook.csv                    # Dataset
├── facebook_eda_analysis.py              # Main analysis script
├── facebook_eda_visualizations.png       # Output visualizations
├── facebook_eda_detailed_analysis.png    # Detailed analysis charts
└── valuable_users_list.csv               # Top 1000 users list
```

## Technologies Used
- **Python 3.12+**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib**: Data visualization
- **Seaborn**: Statistical data visualization

## Key Insights Summary

| Metric | Value | Insight |
|--------|-------|---------|
| Total Users | 99,003 | Large user base for analysis |
| Mobile Users | 50.6% | Mobile-first strategy essential |
| Top Users (1000) | 1% | High-impact user segment |
| Female Engagement | Higher | Target demographic opportunity |
| Friend Count Impact | 14.9x | Critical engagement factor |
| Like Activity Impact | 10.1x | Content engagement driver |

## Future Enhancements
- Time-series analysis of engagement trends
- Predictive modeling for user churn
- Network analysis of friend connections
- Content recommendation system
- A/B testing framework for engagement strategies

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
