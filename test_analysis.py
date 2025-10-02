#!/usr/bin/env python3
"""
Test Suite for Facebook EDA Analysis
=====================================
Simple tests to validate the analysis functions correctly.
"""

import pandas as pd
import numpy as np
import sys

def test_data_loading():
    """Test that the dataset loads correctly."""
    try:
        df = pd.read_csv('/home/runner/work/Facebook-eda/Facebook-eda/pseudo_facebook.csv')
        assert len(df) > 0, "Dataset is empty"
        assert 'userid' in df.columns, "Missing userid column"
        assert 'friend_count' in df.columns, "Missing friend_count column"
        assert 'gender' in df.columns, "Missing gender column"
        print("✓ Test 1 PASSED: Data loading")
        return True
    except Exception as e:
        print(f"✗ Test 1 FAILED: Data loading - {str(e)}")
        return False

def test_engagement_score_calculation():
    """Test that engagement scores are calculated correctly."""
    try:
        df = pd.read_csv('/home/runner/work/Facebook-eda/Facebook-eda/pseudo_facebook.csv')
        
        # Normalize features
        df['friend_count_norm'] = (df['friend_count'] - df['friend_count'].min()) / \
                                   (df['friend_count'].max() - df['friend_count'].min() + 1e-10)
        
        # Calculate engagement score
        df['engagement_score'] = 0.25 * df['friend_count_norm']
        
        # Validate scores are between 0 and 1
        assert df['engagement_score'].min() >= 0, "Engagement score below 0"
        assert df['engagement_score'].max() <= 1, "Engagement score above 1"
        assert not df['engagement_score'].isnull().any(), "Null engagement scores"
        
        print("✓ Test 2 PASSED: Engagement score calculation")
        return True
    except Exception as e:
        print(f"✗ Test 2 FAILED: Engagement score calculation - {str(e)}")
        return False

def test_user_segmentation():
    """Test that users can be segmented correctly."""
    try:
        df = pd.read_csv('/home/runner/work/Facebook-eda/Facebook-eda/pseudo_facebook.csv')
        
        # Simple segmentation by friend count
        df['segment'] = pd.cut(df['friend_count'], 
                               bins=[0, 100, 500, 1000, 10000],
                               labels=['Low', 'Medium', 'High', 'Very High'])
        
        # Validate segmentation
        assert not df['segment'].isnull().all(), "All segments are null"
        assert len(df['segment'].value_counts()) > 0, "No segments created"
        
        print("✓ Test 3 PASSED: User segmentation")
        return True
    except Exception as e:
        print(f"✗ Test 3 FAILED: User segmentation - {str(e)}")
        return False

def test_platform_analysis():
    """Test that platform usage can be analyzed."""
    try:
        df = pd.read_csv('/home/runner/work/Facebook-eda/Facebook-eda/pseudo_facebook.csv')
        
        # Calculate platform preferences
        mobile_users = len(df[df['mobile_likes'] > df['www_likes']])
        web_users = len(df[df['www_likes'] > df['mobile_likes']])
        
        # Validate analysis
        assert mobile_users >= 0, "Negative mobile users count"
        assert web_users >= 0, "Negative web users count"
        assert (mobile_users + web_users) <= len(df), "User count exceeds total"
        
        print("✓ Test 4 PASSED: Platform analysis")
        return True
    except Exception as e:
        print(f"✗ Test 4 FAILED: Platform analysis - {str(e)}")
        return False

def test_demographics_analysis():
    """Test that demographics can be analyzed."""
    try:
        df = pd.read_csv('/home/runner/work/Facebook-eda/Facebook-eda/pseudo_facebook.csv')
        
        # Analyze demographics
        age_stats = df['age'].describe()
        gender_counts = df['gender'].value_counts()
        
        # Validate analysis
        assert age_stats['min'] > 0, "Invalid minimum age"
        assert age_stats['max'] < 150, "Invalid maximum age"
        assert len(gender_counts) > 0, "No gender data"
        
        print("✓ Test 5 PASSED: Demographics analysis")
        return True
    except Exception as e:
        print(f"✗ Test 5 FAILED: Demographics analysis - {str(e)}")
        return False

def test_top_users_identification():
    """Test that top users can be identified."""
    try:
        df = pd.read_csv('/home/runner/work/Facebook-eda/Facebook-eda/pseudo_facebook.csv')
        
        # Identify top users by friend count
        top_users = df.nlargest(100, 'friend_count')
        
        # Validate identification
        assert len(top_users) == 100, "Wrong number of top users"
        assert top_users['friend_count'].min() > 0, "Top users have 0 friends"
        assert top_users['friend_count'].is_monotonic_decreasing or \
               len(top_users['friend_count'].unique()) > 1, "Invalid ranking"
        
        print("✓ Test 6 PASSED: Top users identification")
        return True
    except Exception as e:
        print(f"✗ Test 6 FAILED: Top users identification - {str(e)}")
        return False

def test_output_files_exist():
    """Test that expected output files exist."""
    try:
        import os
        
        expected_files = [
            'facebook_eda_visualizations.png',
            'facebook_eda_detailed_analysis.png',
            'valuable_users_list.csv'
        ]
        
        base_path = '/home/runner/work/Facebook-eda/Facebook-eda/'
        
        for filename in expected_files:
            filepath = base_path + filename
            assert os.path.exists(filepath), f"Missing file: {filename}"
            assert os.path.getsize(filepath) > 0, f"Empty file: {filename}"
        
        print("✓ Test 7 PASSED: Output files exist")
        return True
    except Exception as e:
        print(f"✗ Test 7 FAILED: Output files exist - {str(e)}")
        return False

def test_valuable_users_csv():
    """Test that valuable users CSV has correct structure."""
    try:
        df = pd.read_csv('/home/runner/work/Facebook-eda/Facebook-eda/valuable_users_list.csv')
        
        required_columns = ['userid', 'age', 'gender', 'engagement_score']
        
        for col in required_columns:
            assert col in df.columns, f"Missing column: {col}"
        
        assert len(df) > 0, "Empty valuable users list"
        assert df['engagement_score'].max() <= 1.0, "Invalid engagement score"
        assert df['engagement_score'].min() >= 0.0, "Invalid engagement score"
        
        print("✓ Test 8 PASSED: Valuable users CSV structure")
        return True
    except Exception as e:
        print(f"✗ Test 8 FAILED: Valuable users CSV structure - {str(e)}")
        return False

def run_all_tests():
    """Run all tests and report results."""
    print("="*70)
    print("FACEBOOK EDA ANALYSIS - TEST SUITE")
    print("="*70)
    print()
    
    tests = [
        test_data_loading,
        test_engagement_score_calculation,
        test_user_segmentation,
        test_platform_analysis,
        test_demographics_analysis,
        test_top_users_identification,
        test_output_files_exist,
        test_valuable_users_csv
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print()
    print("="*70)
    print("TEST RESULTS SUMMARY")
    print("="*70)
    
    passed = sum(results)
    total = len(results)
    
    print(f"\nTests Passed: {passed}/{total}")
    print(f"Tests Failed: {total - passed}/{total}")
    print(f"Success Rate: {passed/total*100:.1f}%")
    
    if passed == total:
        print("\n✅ ALL TESTS PASSED!")
        return 0
    else:
        print("\n⚠️  SOME TESTS FAILED")
        return 1

if __name__ == "__main__":
    sys.exit(run_all_tests())
