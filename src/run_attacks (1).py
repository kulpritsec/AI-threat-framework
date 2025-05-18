import os
import yaml
import subprocess
from config_parser import load_attack_config

def run_notebook(notebook_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    cmd = [
        "jupyter", "nbconvert",
        "--to", "notebook",
        "--execute", notebook_path,
        "--output", os.path.join(output_dir, os.path.basename(notebook_path))
    ]
    print(f"[+] Executing notebook: {notebook_path}")
    subprocess.run(cmd, check=True)

def log_results(output_dir, message):
    os.makedirs(output_dir, exist_ok=True)
    log_path = os.path.join(output_dir, "execution_log.txt")
    with open(log_path, "a") as log_file:
        log_file.write(message + "\n")
    print(f"[i] Logged: {message}")

def main():
    config = load_attack_config(os.path.join(os.path.dirname(__file__), "../config/attack_config.yaml"))
    notebook_base = os.path.join(os.path.dirname(__file__), "../notebooks")
    report_dir = config["logging"].get("output_dir", "./reports")

    if config.get("fgsm", {}).get("enabled", False):
        run_notebook(os.path.join(notebook_base, "fgsm_attack_demo.ipynb"), report_dir)
        if config["logging"]["enabled"]:
            log_results(report_dir, f"Executed FGSM attack notebook")

    if config.get("data_poisoning", {}).get("enabled", False):
        run_notebook(os.path.join(notebook_base, "data_poisoning_demo.ipynb"), report_dir)
        if config["logging"]["enabled"]:
            log_results(report_dir, f"Executed data poisoning notebook")

    if config.get("adversarial_training", {}).get("enabled", False):
        run_notebook(os.path.join(notebook_base, "adversarial_training_demo.ipynb"), report_dir)
        if config["logging"]["enabled"]:
            log_results(report_dir, f"Executed adversarial training notebook")

if __name__ == "__main__":
    main()
