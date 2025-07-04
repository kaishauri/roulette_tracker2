from setuptools import setup, find_packages

setup(
    name="roulette_tracker",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pyqt5",
        "pyqtgraph",
        "pyautogui",
        # add any other dependencies your project uses
    ],
    author="Your Name",
    description="Roulette Tracker Application",
    include_package_data=True,
)