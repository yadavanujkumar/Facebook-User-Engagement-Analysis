#!/usr/bin/env python3
"""
Facebook User Engagement Analysis
==================================
This script performs exploratory data analysis on Facebook user data to identify
valuable users that can be focused on to increase business.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

def load_data(filepath):
    """Load the Facebook dataset."""
    df = pd.read_csv(filepath)
    print("Dataset loaded successfully!")
    print(f"Shape: {df.shape}")
    return df

def explore_data(df):
    """Perform initial data exploration."""
    print("\n" + "="*80)
    print("DATA EXPLORATION")
    print("="*80)
    
    print("\nFirst 5 rows:")
    print(df.head())
    
    print("\nDataset Info:")
    print(df.info())
    
    print("\nStatistical Summary:")
    print(df.describe())
    
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    print("\nGender Distribution:")
    print(df['gender'].value_counts())
    
    return df

def create_engagement_score(df):
    """
    Create an engagement score to identify valuable users.
    Considers multiple factors:
    - Friend count and friendships initiated
    - Likes given and received
    - Mobile and web engagement
    - Tenure (loyalty)
    """
    print("\n" + "="*80)
    print("CREATING ENGAGEMENT SCORE")
    print("="*80)
    
    # Normalize features to 0-1 scale
    df['friend_count_norm'] = (df['friend_count'] - df['friend_count'].min()) / \
                               (df['friend_count'].max() - df['friend_count'].min() + 1e-10)
    
    df['friendships_initiated_norm'] = (df['friendships_initiated'] - df['friendships_initiated'].min()) / \
                                        (df['friendships_initiated'].max() - df['friendships_initiated'].min() + 1e-10)
    
    df['likes_norm'] = (df['likes'] - df['likes'].min()) / \
                       (df['likes'].max() - df['likes'].min() + 1e-10)
    
    df['likes_received_norm'] = (df['likes_received'] - df['likes_received'].min()) / \
                                 (df['likes_received'].max() - df['likes_received'].min() + 1e-10)
    
    df['tenure_norm'] = (df['tenure'] - df['tenure'].min()) / \
                        (df['tenure'].max() - df['tenure'].min() + 1e-10)
    
    # Calculate total engagement (mobile + www)
    df['total_likes'] = df['mobile_likes'] + df['www_likes']
    df['total_likes_received'] = df['mobile_likes_received'] + df['www_likes_received']
    
    # Create weighted engagement score
    # Higher weights for active engagement (giving likes, initiating friendships)
    df['engagement_score'] = (
        0.25 * df['friend_count_norm'] +
        0.20 * df['friendships_initiated_norm'] +
        0.20 * df['likes_norm'] +
        0.20 * df['likes_received_norm'] +
        0.15 * df['tenure_norm']
    )
    
    # Categorize users
    df['user_category'] = pd.cut(df['engagement_score'], 
                                   bins=[0, 0.2, 0.5, 0.8, 1.0],
                                   labels=['Low Engagement', 'Medium Engagement', 
                                          'High Engagement', 'Very High Engagement'])
    
    print("\nEngagement Score Statistics:")
    print(df['engagement_score'].describe())
    
    print("\nUser Category Distribution:")
    print(df['user_category'].value_counts().sort_index())
    
    return df

def analyze_demographics(df):
    """Analyze demographics and their relationship with engagement."""
    print("\n" + "="*80)
    print("DEMOGRAPHIC ANALYSIS")
    print("="*80)
    
    print("\nAge Distribution:")
    print(df['age'].describe())
    
    print("\nEngagement by Gender:")
    gender_engagement = df.groupby('gender')['engagement_score'].agg(['mean', 'median', 'std'])
    print(gender_engagement)
    
    print("\nEngagement by Age Groups:")
    df['age_group'] = pd.cut(df['age'], bins=[0, 18, 25, 35, 50, 100],
                              labels=['<18', '18-25', '26-35', '36-50', '50+'])
    age_engagement = df.groupby('age_group')['engagement_score'].agg(['mean', 'median', 'count'])
    print(age_engagement)
    
    return df

def identify_valuable_users(df, top_n=1000):
    """Identify the most valuable users based on engagement score."""
    print("\n" + "="*80)
    print(f"IDENTIFYING TOP {top_n} VALUABLE USERS")
    print("="*80)
    
    valuable_users = df.nlargest(top_n, 'engagement_score')
    
    print(f"\nTop {top_n} Users Statistics:")
    print("\nFriend Count:")
    print(valuable_users['friend_count'].describe())
    
    print("\nLikes Given:")
    print(valuable_users['likes'].describe())
    
    print("\nLikes Received:")
    print(valuable_users['likes_received'].describe())
    
    print("\nTenure (days):")
    print(valuable_users['tenure'].describe())
    
    print("\nGender Distribution of Top Users:")
    print(valuable_users['gender'].value_counts())
    
    print("\nAge Distribution of Top Users:")
    print(valuable_users['age'].describe())
    
    return valuable_users

def analyze_platform_usage(df):
    """Analyze mobile vs web platform usage."""
    print("\n" + "="*80)
    print("PLATFORM USAGE ANALYSIS")
    print("="*80)
    
    # Calculate platform preferences
    df['mobile_preference'] = df['mobile_likes'] / (df['mobile_likes'] + df['www_likes'] + 1e-10)
    df['www_preference'] = df['www_likes'] / (df['mobile_likes'] + df['www_likes'] + 1e-10)
    
    # Identify primarily mobile or web users
    df['primary_platform'] = 'None'
    df.loc[df['mobile_preference'] > 0.7, 'primary_platform'] = 'Mobile'
    df.loc[df['www_preference'] > 0.7, 'primary_platform'] = 'Web'
    df.loc[(df['mobile_preference'] >= 0.3) & (df['mobile_preference'] <= 0.7), 'primary_platform'] = 'Both'
    
    print("\nPrimary Platform Distribution:")
    print(df['primary_platform'].value_counts())
    
    print("\nEngagement Score by Platform:")
    platform_engagement = df.groupby('primary_platform')['engagement_score'].agg(['mean', 'median', 'count'])
    print(platform_engagement)
    
    return df

def generate_recommendations(df, valuable_users):
    """Generate business recommendations based on analysis."""
    print("\n" + "="*80)
    print("BUSINESS RECOMMENDATIONS")
    print("="*80)
    
    total_users = len(df)
    high_engagement = len(df[df['engagement_score'] > 0.5])
    low_engagement = len(df[df['engagement_score'] < 0.2])
    
    print(f"\n1. USER SEGMENTATION INSIGHTS:")
    print(f"   - Total Users: {total_users:,}")
    print(f"   - High Engagement Users (score > 0.5): {high_engagement:,} ({high_engagement/total_users*100:.1f}%)")
    print(f"   - Low Engagement Users (score < 0.2): {low_engagement:,} ({low_engagement/total_users*100:.1f}%)")
    
    print(f"\n2. TARGET DEMOGRAPHICS:")
    top_gender = valuable_users['gender'].mode()[0]
    avg_age = valuable_users['age'].mean()
    print(f"   - Most engaged gender: {top_gender}")
    print(f"   - Average age of top users: {avg_age:.1f} years")
    
    print(f"\n3. PLATFORM STRATEGY:")
    mobile_users = len(df[df['primary_platform'] == 'Mobile'])
    web_users = len(df[df['primary_platform'] == 'Web'])
    both_users = len(df[df['primary_platform'] == 'Both'])
    print(f"   - Mobile-first users: {mobile_users:,} ({mobile_users/total_users*100:.1f}%)")
    print(f"   - Web-first users: {web_users:,} ({web_users/total_users*100:.1f}%)")
    print(f"   - Cross-platform users: {both_users:,} ({both_users/total_users*100:.1f}%)")
    
    print(f"\n4. ENGAGEMENT DRIVERS:")
    avg_friends_top = valuable_users['friend_count'].mean()
    avg_friends_all = df['friend_count'].mean()
    print(f"   - Top users have {avg_friends_top/avg_friends_all:.1f}x more friends than average")
    
    avg_likes_top = valuable_users['likes'].mean()
    avg_likes_all = df['likes'].mean()
    if avg_likes_all > 0:
        print(f"   - Top users give {avg_likes_top/avg_likes_all:.1f}x more likes than average")
    
    print(f"\n5. RECOMMENDATIONS:")
    print(f"   a) Focus retention efforts on the top {high_engagement:,} highly engaged users")
    print(f"   b) Create re-engagement campaigns for {low_engagement:,} low-engagement users")
    print(f"   c) Optimize mobile experience - {mobile_users/total_users*100:.1f}% prefer mobile")
    print(f"   d) Encourage friend connections - strong correlation with engagement")
    print(f"   e) Promote content creation and likes - key engagement indicators")
    
    return

def create_visualizations(df, valuable_users):
    """Create comprehensive visualizations."""
    print("\n" + "="*80)
    print("GENERATING VISUALIZATIONS")
    print("="*80)
    
    fig = plt.figure(figsize=(20, 16))
    
    # 1. Engagement Score Distribution
    plt.subplot(3, 3, 1)
    plt.hist(df['engagement_score'], bins=50, edgecolor='black', alpha=0.7)
    plt.xlabel('Engagement Score')
    plt.ylabel('Number of Users')
    plt.title('Distribution of User Engagement Scores')
    plt.axvline(df['engagement_score'].median(), color='red', linestyle='--', label='Median')
    plt.legend()
    
    # 2. User Category Distribution
    plt.subplot(3, 3, 2)
    category_counts = df['user_category'].value_counts()
    plt.pie(category_counts.values, labels=category_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title('User Categories by Engagement Level')
    
    # 3. Engagement by Gender
    plt.subplot(3, 3, 3)
    df.groupby('gender')['engagement_score'].mean().plot(kind='bar')
    plt.xlabel('Gender')
    plt.ylabel('Average Engagement Score')
    plt.title('Average Engagement Score by Gender')
    plt.xticks(rotation=0)
    
    # 4. Engagement by Age Group
    plt.subplot(3, 3, 4)
    df.groupby('age_group')['engagement_score'].mean().plot(kind='bar')
    plt.xlabel('Age Group')
    plt.ylabel('Average Engagement Score')
    plt.title('Average Engagement Score by Age Group')
    plt.xticks(rotation=45)
    
    # 5. Friend Count vs Engagement Score
    plt.subplot(3, 3, 5)
    plt.scatter(df['friend_count'], df['engagement_score'], alpha=0.1)
    plt.xlabel('Friend Count')
    plt.ylabel('Engagement Score')
    plt.title('Friend Count vs Engagement Score')
    
    # 6. Platform Usage Distribution
    plt.subplot(3, 3, 6)
    platform_counts = df['primary_platform'].value_counts()
    plt.bar(platform_counts.index, platform_counts.values)
    plt.xlabel('Primary Platform')
    plt.ylabel('Number of Users')
    plt.title('Primary Platform Distribution')
    plt.xticks(rotation=45)
    
    # 7. Tenure vs Engagement
    plt.subplot(3, 3, 7)
    plt.scatter(df['tenure'], df['engagement_score'], alpha=0.1)
    plt.xlabel('Tenure (days)')
    plt.ylabel('Engagement Score')
    plt.title('Tenure vs Engagement Score')
    
    # 8. Likes Given vs Received
    plt.subplot(3, 3, 8)
    plt.scatter(df['likes'], df['likes_received'], alpha=0.1)
    plt.xlabel('Likes Given')
    plt.ylabel('Likes Received')
    plt.title('Likes Given vs Likes Received')
    
    # 9. Top 20 Users by Engagement
    plt.subplot(3, 3, 9)
    top_20 = valuable_users.head(20)
    plt.barh(range(20), top_20['engagement_score'].values)
    plt.xlabel('Engagement Score')
    plt.ylabel('User Rank')
    plt.title('Top 20 Users by Engagement Score')
    plt.gca().invert_yaxis()
    
    plt.tight_layout()
    plt.savefig('/home/runner/work/Facebook-eda/Facebook-eda/facebook_eda_visualizations.png', 
                dpi=150, bbox_inches='tight')
    print("\nVisualizations saved to 'facebook_eda_visualizations.png'")
    
    # Create additional detailed plots
    fig2 = plt.figure(figsize=(20, 10))
    
    # Mobile vs Web Engagement
    plt.subplot(2, 3, 1)
    plt.scatter(df['mobile_likes'], df['www_likes'], alpha=0.1)
    plt.xlabel('Mobile Likes')
    plt.ylabel('Web Likes')
    plt.title('Mobile vs Web Platform Likes')
    
    # Age Distribution
    plt.subplot(2, 3, 2)
    plt.hist(df['age'], bins=30, edgecolor='black', alpha=0.7)
    plt.xlabel('Age')
    plt.ylabel('Number of Users')
    plt.title('Age Distribution of All Users')
    
    # Top Users Age Distribution
    plt.subplot(2, 3, 3)
    plt.hist(valuable_users['age'], bins=30, edgecolor='black', alpha=0.7, color='orange')
    plt.xlabel('Age')
    plt.ylabel('Number of Users')
    plt.title('Age Distribution of Top 1000 Users')
    
    # Friendships Initiated vs Friend Count
    plt.subplot(2, 3, 4)
    plt.scatter(df['friend_count'], df['friendships_initiated'], alpha=0.1)
    plt.xlabel('Friend Count')
    plt.ylabel('Friendships Initiated')
    plt.title('Friend Count vs Friendships Initiated')
    
    # Engagement Score by Tenure Groups
    plt.subplot(2, 3, 5)
    df['tenure_group'] = pd.cut(df['tenure'], bins=[0, 100, 365, 730, 10000],
                                  labels=['<100d', '100-365d', '1-2y', '2y+'])
    df.groupby('tenure_group')['engagement_score'].mean().plot(kind='bar')
    plt.xlabel('Tenure Group')
    plt.ylabel('Average Engagement Score')
    plt.title('Engagement Score by Tenure Group')
    plt.xticks(rotation=45)
    
    # Correlation Heatmap
    plt.subplot(2, 3, 6)
    corr_cols = ['friend_count', 'friendships_initiated', 'likes', 'likes_received', 
                 'tenure', 'engagement_score']
    correlation = df[corr_cols].corr()
    sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm', center=0)
    plt.title('Feature Correlation Heatmap')
    
    plt.tight_layout()
    plt.savefig('/home/runner/work/Facebook-eda/Facebook-eda/facebook_eda_detailed_analysis.png', 
                dpi=150, bbox_inches='tight')
    print("Detailed analysis saved to 'facebook_eda_detailed_analysis.png'")
    
    return

def save_valuable_users(valuable_users, filepath):
    """Save the list of valuable users to CSV."""
    output_cols = ['userid', 'age', 'gender', 'tenure', 'friend_count', 
                   'friendships_initiated', 'likes', 'likes_received',
                   'engagement_score', 'user_category', 'primary_platform']
    valuable_users[output_cols].to_csv(filepath, index=False)
    print(f"\nValuable users data saved to '{filepath}'")
    return

def main():
    """Main execution function."""
    print("="*80)
    print("FACEBOOK USER ENGAGEMENT ANALYSIS")
    print("Identifying Valuable Users for Business Growth")
    print("="*80)
    
    # Load data
    df = load_data('/home/runner/work/Facebook-eda/Facebook-eda/pseudo_facebook.csv')
    
    # Explore data
    df = explore_data(df)
    
    # Create engagement score
    df = create_engagement_score(df)
    
    # Analyze demographics
    df = analyze_demographics(df)
    
    # Analyze platform usage
    df = analyze_platform_usage(df)
    
    # Identify valuable users
    valuable_users = identify_valuable_users(df, top_n=1000)
    
    # Generate recommendations
    generate_recommendations(df, valuable_users)
    
    # Create visualizations
    create_visualizations(df, valuable_users)
    
    # Save valuable users list
    save_valuable_users(valuable_users, 
                       '/home/runner/work/Facebook-eda/Facebook-eda/valuable_users_list.csv')
    
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE!")
    print("="*80)
    print("\nOutputs generated:")
    print("1. facebook_eda_visualizations.png - Main visualization dashboard")
    print("2. facebook_eda_detailed_analysis.png - Detailed analysis charts")
    print("3. valuable_users_list.csv - List of top 1000 valuable users")
    print("\nThese insights can help Facebook:")
    print("- Target high-value users for retention")
    print("- Create personalized engagement campaigns")
    print("- Optimize platform features based on user preferences")
    print("- Drive business growth through data-driven decisions")
    
if __name__ == "__main__":
    main()
