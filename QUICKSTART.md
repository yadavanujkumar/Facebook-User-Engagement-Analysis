# Quick Start Guide - Facebook EDA Analysis

## Getting Started in 3 Steps

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Analysis
```bash
python3 facebook_eda_analysis.py
```

### Step 3: View Results
The analysis will generate:
- `facebook_eda_visualizations.png` - Main dashboard
- `facebook_eda_detailed_analysis.png` - Detailed charts
- `valuable_users_list.csv` - Top 1000 users

## What You'll Get

### Comprehensive Insights
- **User Engagement Scores**: Every user gets a calculated engagement score (0-1)
- **User Segmentation**: Users categorized by engagement level
- **Demographics Analysis**: Age, gender, and platform preferences
- **Valuable Users List**: Top 1000 users for targeted campaigns

### Business Recommendations
The analysis provides actionable recommendations:
1. Which users to focus on for retention
2. How to optimize mobile vs web experience
3. What drives user engagement (friends, likes, tenure)
4. Target demographics for marketing campaigns
5. Platform-specific strategies

### Visualizations Include
- Engagement score distribution
- User category pie chart
- Gender and age group analysis
- Platform usage (Mobile/Web/Both)
- Friend count vs engagement correlation
- Likes activity patterns
- Top 20 users ranking
- Feature correlation heatmap

## Understanding the Output

### Engagement Score
Calculated from 5 factors:
- **25%** Friend Count (social network size)
- **20%** Friendships Initiated (proactive behavior)
- **20%** Likes Given (content engagement)
- **20%** Likes Received (content value)
- **15%** Tenure (user loyalty)

### User Categories
- **Very High Engagement** (0.8-1.0): Top-tier users
- **High Engagement** (0.5-0.8): Highly engaged users
- **Medium Engagement** (0.2-0.5): Moderately engaged
- **Low Engagement** (0.0-0.2): Need re-engagement

### Platform Types
- **Mobile**: Users who primarily use mobile (>70% mobile likes)
- **Web**: Users who primarily use web (>70% web likes)
- **Both**: Cross-platform users (30-70% split)
- **None**: Users with no likes activity

## Customizing the Analysis

### Change Top Users Count
Edit line 227 in `facebook_eda_analysis.py`:
```python
valuable_users = identify_valuable_users(df, top_n=1000)  # Change 1000 to your desired number
```

### Adjust Engagement Weights
Edit lines 72-78 to adjust the importance of each factor:
```python
df['engagement_score'] = (
    0.25 * df['friend_count_norm'] +      # Adjust these weights
    0.20 * df['friendships_initiated_norm'] +
    0.20 * df['likes_norm'] +
    0.20 * df['likes_received_norm'] +
    0.15 * df['tenure_norm']
)
```

### Change User Categories
Edit line 82 to adjust engagement thresholds:
```python
df['user_category'] = pd.cut(df['engagement_score'], 
                              bins=[0, 0.2, 0.5, 0.8, 1.0],  # Adjust these bins
                              labels=['Low', 'Medium', 'High', 'Very High'])
```

## Troubleshooting

### Issue: Module not found
**Solution**: Install dependencies
```bash
pip install pandas numpy matplotlib seaborn
```

### Issue: CSV file not found
**Solution**: Ensure `pseudo_facebook.csv` is in the same directory
```bash
ls pseudo_facebook.csv  # Should show the file
```

### Issue: Visualizations not showing
**Solution**: Files are saved as PNG, no display needed
```bash
ls *.png  # Check if PNG files were created
```

### Issue: Permission denied
**Solution**: Run with proper permissions
```bash
chmod +x facebook_eda_analysis.py
python3 facebook_eda_analysis.py
```

## Advanced Usage

### Import as Module
You can import functions from the script:
```python
from facebook_eda_analysis import load_data, create_engagement_score

df = load_data('pseudo_facebook.csv')
df = create_engagement_score(df)
# Now you can use df for custom analysis
```

### Jupyter Notebook
Convert to Jupyter notebook for interactive analysis:
```bash
# Install jupyter
pip install jupyter

# Create a new notebook and import functions
jupyter notebook
```

## Need Help?

Common questions:
1. **How is engagement calculated?** - Weighted average of 5 key metrics
2. **What makes a valuable user?** - High engagement score, many friends, active likes
3. **Why mobile vs web matters?** - Platform optimization opportunities
4. **How to use the valuable users list?** - Target for retention, special campaigns

## Performance

- **Runtime**: ~5-10 seconds for 99,003 users
- **Memory**: ~50MB RAM required
- **Output Size**: ~1.3MB total (2 PNGs + 1 CSV)

## Next Steps

After running the analysis:
1. Review the visualizations to understand patterns
2. Check the valuable_users_list.csv for user IDs
3. Use insights for business strategy
4. Run periodically to track engagement trends
5. Customize weights based on business priorities

---

For detailed documentation, see [README.md](README.md)
