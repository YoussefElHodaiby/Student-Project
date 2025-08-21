#!/usr/bin/env python3
"""
Test runner script for the Student API project
"""
import subprocess
import sys
import os


def run_tests():
    """Run all tests with proper configuration"""
    # Ensure we're in the right directory
    os.chdir('/Users/youssefelhodaiby/PycharmProjects/apicourse')
    
    # Activate virtual environment and run tests
    commands = [
        # Basic test run
        ["python", "-m", "pytest", "-v"],
        
        # Test run with coverage (if you want to add coverage later)
        # ["python", "-m", "pytest", "-v", "--cov=student_api"],
        
        # Test run with HTML report
        ["python", "-m", "pytest", "-v", "--html=reports/report.html", "--self-contained-html"]
    ]
    
    for i, cmd in enumerate(commands, 1):
        print(f"\n{'='*50}")
        print(f"Running test command {i}: {' '.join(cmd)}")
        print(f"{'='*50}")
        
        try:
            result = subprocess.run(cmd, capture_output=False, text=True)
            if result.returncode != 0:
                print(f"Test command {i} failed with return code {result.returncode}")
            else:
                print(f"Test command {i} completed successfully")
        except Exception as e:
            print(f"Error running test command {i}: {e}")


if __name__ == "__main__":
    run_tests()
