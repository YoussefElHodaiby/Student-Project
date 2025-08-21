#!/usr/bin/env python3
"""
Test runner script for the Student and Book API project
"""
import subprocess
import sys
import os


def run_tests():
    """Run all tests with proper configuration"""
    # Ensure we're in the right directory
    os.chdir('/Users/youssefelhodaiby/PycharmProjects/apicourse')
    
    # Test commands for different scenarios
    commands = [
        # Run all tests
        ["python", "-m", "pytest", "-v"],
        
        # Run only student tests
        ["python", "-m", "pytest", "test_student.py", "-v"],
        
        # Run only book tests  
        ["python", "-m", "pytest", "test_books.py", "-v"],
        
        # Run with HTML report
        ["python", "-m", "pytest", "-v", "--html=reports/report.html", "--self-contained-html"],
        
        # Run tests by markers (if needed)
        # ["python", "-m", "pytest", "-m", "student", "-v"],
        # ["python", "-m", "pytest", "-m", "book", "-v"],
    ]
    
    for i, cmd in enumerate(commands, 1):
        print(f"\n{'='*60}")
        print(f"Running test command {i}: {' '.join(cmd)}")
        print(f"{'='*60}")
        
        try:
            result = subprocess.run(cmd, capture_output=False, text=True)
            if result.returncode != 0:
                print(f"Test command {i} failed with return code {result.returncode}")
            else:
                print(f"Test command {i} completed successfully")
        except Exception as e:
            print(f"Error running test command {i}: {e}")


if __name__ == "__main__":
    print("🧪 Starting API Testing Suite")
    print("📋 Tests will run for both Student and Book endpoints")
    print("🚀 Make sure your API server is running on http://localhost:8082")
    print()
    
    run_tests()
