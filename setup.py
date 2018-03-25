from setuptools import setup, find_packages  

setup(
    name="line-chart-cli",
    version="0.0.1",
    description="Small CLI tool to view line chart from CSV file.",
    author="Fuji Haruka",
    url="https://github.com/FujiHaruka/line-chart-cli",
    packages=find_packages(),
    install_requires=["matplotlib"],
    entry_points={
        "console_scripts": "line-chart = line_chart.line_chart:main"
    },
    license="MIT"
)
