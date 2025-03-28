import subprocess

def run_tests():
    # Run pytest with Allure
    subprocess.run(["pytest", "--env=dev","reruns=2", "--alluredir=reports/"])
    # Generate and serve the Allure report
    subprocess.run(["allure", "serve", "reports/"])

if __name__ == "__main__":
    run_tests()