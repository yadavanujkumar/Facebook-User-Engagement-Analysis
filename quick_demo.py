#!/usr/bin/env python3
"""
Quick Demo - Facebook EDA Analysis
===================================
This script provides a quick 30-second demo of the key findings.
"""

import pandas as pd
import warnings
warnings.filterwarnings('ignore')

def main():
    print("="*70)
    print("FACEBOOK USER ENGAGEMENT ANALYSIS - QUICK DEMO")
    print("="*70)
    
    # Load data
    print("\n📊 Loading dataset...")
    df = pd.read_csv('/home/runner/work/Facebook-eda/Facebook-eda/pseudo_facebook.csv')
    print(f"   ✓ Loaded {len(df):,} user records")
    
    # Basic stats
    print("\n📈 Dataset Overview:")
    print(f"   • Average Age: {df['age'].mean():.1f} years")
    print(f"   • Gender Split: {len(df[df['gender']=='male']):,} male, {len(df[df['gender']=='female']):,} female")
    print(f"   • Average Friends: {df['friend_count'].mean():.0f}")
    print(f"   • Average Tenure: {df['tenure'].mean():.0f} days")
    
    # Top users
    print("\n🌟 Top 10 Users by Friend Count:")
    top_friends = df.nlargest(10, 'friend_count')[['userid', 'age', 'gender', 'friend_count', 'likes', 'tenure']]
    print(top_friends.to_string(index=False))
    
    # Platform usage
    mobile_users = len(df[df['mobile_likes'] > df['www_likes']])
    web_users = len(df[df['www_likes'] > df['mobile_likes']])
    
    print("\n📱 Platform Preferences:")
    print(f"   • Mobile-first: {mobile_users:,} users ({mobile_users/len(df)*100:.1f}%)")
    print(f"   • Web-first: {web_users:,} users ({web_users/len(df)*100:.1f}%)")
    
    # Engagement insights
    high_engagement = df[df['friend_count'] > 1000]
    print("\n💡 High Engagement Users (>1000 friends):")
    print(f"   • Count: {len(high_engagement):,} users")
    print(f"   • Average Likes: {high_engagement['likes'].mean():.0f}")
    print(f"   • Average Tenure: {high_engagement['tenure'].mean():.0f} days")
    
    # Gender insights
    print("\n👥 Engagement by Gender:")
    for gender in ['male', 'female']:
        gender_df = df[df['gender'] == gender]
        print(f"   • {gender.capitalize()}: {len(gender_df):,} users, "
              f"Avg Friends: {gender_df['friend_count'].mean():.0f}, "
              f"Avg Likes: {gender_df['likes'].mean():.0f}")
    
    # Age groups
    print("\n🎂 Engagement by Age Group:")
    age_bins = [0, 18, 25, 35, 50, 150]
    age_labels = ['<18', '18-25', '26-35', '36-50', '50+']
    df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels)
    
    for age_group in age_labels:
        age_df = df[df['age_group'] == age_group]
        if len(age_df) > 0:
            print(f"   • {age_group}: {len(age_df):,} users, "
                  f"Avg Friends: {age_df['friend_count'].mean():.0f}")
    
    # Key recommendations
    print("\n" + "="*70)
    print("🎯 KEY RECOMMENDATIONS")
    print("="*70)
    print("\n1. MOBILE OPTIMIZATION")
    print(f"   → {mobile_users/len(df)*100:.1f}% prefer mobile - prioritize mobile UX")
    
    print("\n2. FRIEND CONNECTIONS")
    print(f"   → Users with >1000 friends are {len(high_engagement)/len(df)*100:.2f}% of base")
    print(f"   → They are {high_engagement['likes'].mean()/df['likes'].mean():.1f}x more engaged")
    print("   → Implement better friend suggestions")
    
    print("\n3. GENDER-SPECIFIC STRATEGIES")
    male_avg = df[df['gender']=='male']['friend_count'].mean()
    female_avg = df[df['gender']=='female']['friend_count'].mean()
    if female_avg > male_avg:
        print(f"   → Female users have {female_avg/male_avg:.1f}x more friends")
        print("   → Create female-focused engagement features")
    else:
        print(f"   → Male users have {male_avg/female_avg:.1f}x more friends")
        print("   → Create male-focused engagement features")
    
    print("\n4. RE-ENGAGEMENT OPPORTUNITY")
    inactive = len(df[df['friend_count'] == 0])
    print(f"   → {inactive:,} users have 0 friends ({inactive/len(df)*100:.1f}%)")
    print("   → Launch friend connection campaigns")
    
    print("\n" + "="*70)
    print("For full analysis, run: python3 facebook_eda_analysis.py")
    print("="*70)

if __name__ == "__main__":
    main()
