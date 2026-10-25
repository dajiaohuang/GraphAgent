import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--planner",
    choices=("deepseek", "gpt-3.5-turbo-0125"),
    default="deepseek",
)
parser.add_argument("--executor", type=str, default="graphagent")

args = parser.parse_args()