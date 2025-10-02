# Running the Facebook EDA Analysis

## Three Ways to Run the Analysis

### Option 1: Full Analysis (Recommended)
Complete analysis with all visualizations and insights.

```bash
python3 facebook_eda_analysis.py
```

**Duration**: ~10 seconds  
**Outputs**: 
- facebook_eda_visualizations.png (9 charts)
- facebook_eda_detailed_analysis.png (6 detailed charts)
- valuable_users_list.csv (top 1000 users)

**What it does**:
- Loads and explores 99,003 user records
- Calculates engagement scores for all users
- Segments users by engagement level
- Analyzes demographics (age, gender, platform)
- Identifies top 1000 valuable users
- Generates comprehensive visualizations
- Provides business recommendations

---

### Option 2: Quick Demo (Fast)
Quick overview of key findings in 30 seconds.

```bash
python3 quick_demo.py
```

**Duration**: ~5 seconds  
**Outputs**: Console output only (no files)

**What it does**:
- Shows top 10 users by friend count
- Platform preference breakdown
- Gender and age group insights
- Quick recommendations

**Perfect for**:
- First-time exploration
- Quick status check
- Presentations

---

### Option 3: Test Suite (Validation)
Validates that the analysis is working correctly.

```bash
python3 test_analysis.py
```

**Duration**: ~10 seconds  
**Outputs**: Test results in console

**What it does**:
- Tests data loading
- Validates engagement score calculation
- Checks user segmentation
- Verifies platform analysis
- Tests demographics analysis
- Validates top user identification
- Confirms output files exist
- Checks CSV structure

**Perfect for**:
- Validating installation
- Debugging issues
- Quality assurance

---

## Step-by-Step Guide

### First Time Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yadavanujkumar/Facebook-eda.git
   cd Facebook-eda
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   This installs:
   - pandas (data manipulation)
   - numpy (numerical computing)
   - matplotlib (visualization)
   - seaborn (statistical plots)

3. **Verify installation**
   ```bash
   python3 test_analysis.py
   ```
   
   You should see: "✅ ALL TESTS PASSED!"

### Running the Analysis

1. **Full analysis**
   ```bash
   python3 facebook_eda_analysis.py
   ```

2. **Check the outputs**
   ```bash
   ls -lh *.png *.csv
   ```
   
   You should see:
   - facebook_eda_visualizations.png (~700KB)
   - facebook_eda_detailed_analysis.png (~450KB)
   - valuable_users_list.csv (~83KB)

3. **View the results**
   - Open PNG files in any image viewer
   - Open CSV in Excel, Google Sheets, or text editor
   - Review console output for recommendations

### Interpreting Results

**Engagement Score**:
- 0.0 - 0.2: Low engagement (needs re-engagement)
- 0.2 - 0.5: Medium engagement (growth potential)
- 0.5 - 0.8: High engagement (target for retention)
- 0.8 - 1.0: Very high engagement (VIP treatment)

**Valuable Users CSV Columns**:
- `userid`: Unique user identifier
- `age`: User age
- `gender`: male/female
- `tenure`: Days on platform
- `friend_count`: Number of friends
- `friendships_initiated`: Proactive friend requests
- `likes`: Likes given
- `likes_received`: Likes received
- `engagement_score`: Calculated score (0-1)
- `user_category`: Engagement level
- `primary_platform`: Mobile/Web/Both/None

**Visualizations**:
1. Engagement distribution histogram
2. User category pie chart
3. Gender engagement comparison
4. Age group engagement
5. Friend count vs engagement scatter
6. Platform usage bar chart
7. Tenure vs engagement scatter
8. Likes given vs received scatter
9. Top 20 users ranking
10. Mobile vs web usage scatter
11. Age distributions (all vs top users)
12. Friend network analysis
13. Tenure group engagement
14. Feature correlation heatmap

---

## Common Use Cases

### Use Case 1: Identify VIP Users
```bash
# Run full analysis
python3 facebook_eda_analysis.py

# Extract top 100 users
head -101 valuable_users_list.csv > top_100_vip_users.csv
```

**Use the results for**:
- VIP program enrollment
- Premium feature access
- Direct support channel
- Special events invitations

### Use Case 2: Re-engagement Campaign
```bash
# Run full analysis to identify low engagement users
python3 facebook_eda_analysis.py

# In Python, filter for low engagement
python3 << 'PYTHON'
import pandas as pd
df = pd.read_csv('pseudo_facebook.csv')
# Add engagement logic from main script
# Filter for engagement_score < 0.2
# Export to re_engagement_targets.csv
PYTHON
```

**Use the results for**:
- Email campaigns
- Push notifications
- Special offers
- Friend suggestions

### Use Case 3: Platform Optimization
```bash
# Run quick demo for platform insights
python3 quick_demo.py

# Look for "Platform Preferences" section
```

**Use the results for**:
- Mobile app improvements
- Web experience enhancements
- Cross-platform features
- Resource allocation

### Use Case 4: Demographic Targeting
```bash
# Run full analysis
python3 facebook_eda_analysis.py

# Review age group and gender sections
```

**Use the results for**:
- Targeted marketing campaigns
- Age-appropriate features
- Gender-specific content
- Demographic expansion

---

## Troubleshooting

### Problem: ModuleNotFoundError
```
ModuleNotFoundError: No module named 'pandas'
```

**Solution**:
```bash
pip install pandas numpy matplotlib seaborn
# or
pip install -r requirements.txt
```

### Problem: File not found
```
FileNotFoundError: pseudo_facebook.csv
```

**Solution**:
```bash
# Make sure you're in the correct directory
cd /path/to/Facebook-eda

# Verify the file exists
ls pseudo_facebook.csv
```

### Problem: Permission denied
```
PermissionError: [Errno 13] Permission denied
```

**Solution**:
```bash
# Make scripts executable
chmod +x facebook_eda_analysis.py
chmod +x quick_demo.py
chmod +x test_analysis.py

# Or run with python3 directly
python3 facebook_eda_analysis.py
```

### Problem: Empty visualizations
```
No output images generated
```

**Solution**:
```bash
# Check if matplotlib backend is configured
python3 -c "import matplotlib; print(matplotlib.get_backend())"

# If needed, set backend
export MPLBACKEND=Agg
python3 facebook_eda_analysis.py
```

### Problem: Memory error
```
MemoryError
```

**Solution**:
```bash
# Reduce dataset size for testing
head -10000 pseudo_facebook.csv > test_sample.csv

# Modify script to use test_sample.csv
# Then scale back up
```

---

## Performance Tips

### Faster Execution
- Use SSD storage for datasets
- Close other memory-intensive applications
- Use Python 3.8+ for better performance

### Lower Memory Usage
- Process data in chunks if needed
- Remove intermediate DataFrames
- Use categorical data types for gender

### Better Visualizations
- Increase DPI for higher quality: `plt.savefig('file.png', dpi=300)`
- Change figure size: `plt.figure(figsize=(30, 24))`
- Adjust color schemes in the script

---

## Automation

### Daily Analysis (Cron Job)
```bash
# Add to crontab (crontab -e)
0 2 * * * cd /path/to/Facebook-eda && python3 facebook_eda_analysis.py

# This runs analysis daily at 2 AM
```

### Weekly Email Report
```bash
# Create a wrapper script
#!/bin/bash
cd /path/to/Facebook-eda
python3 facebook_eda_analysis.py
mail -s "Facebook EDA Weekly Report" you@example.com -a facebook_eda_visualizations.png < report.txt
```

### Integration with BI Tools
Export results to your BI tool:
```python
# Add to script
df.to_sql('facebook_engagement', engine, if_exists='replace')
```

---

## Next Steps

After running the analysis:

1. **Review Findings**
   - Read INSIGHTS.md for detailed insights
   - Check RESULTS.md for comparison tables
   - Study visualizations carefully

2. **Take Action**
   - Prioritize recommendations
   - Create action items
   - Assign responsibilities

3. **Monitor Progress**
   - Re-run analysis monthly
   - Track success metrics
   - Adjust strategies

4. **Share Results**
   - Present to stakeholders
   - Distribute valuable_users_list.csv
   - Discuss implementation plans

---

## Questions?

For more information:
- **README.md**: Project overview and documentation
- **QUICKSTART.md**: Getting started guide
- **INSIGHTS.md**: Detailed business insights
- **RESULTS.md**: Analysis results and metrics

---

**Happy Analyzing! 📊**
