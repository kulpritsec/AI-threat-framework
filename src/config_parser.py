import yaml
import os

def load_attack_config(config_path="config/attack_config.yaml"):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def print_config_summary(config):
    print("=== Attack Scenario Configuration ===")
    for key, settings in config.items():
        print(f"\n[{key.upper()}]")
        for k, v in settings.items():
            print(f"{k}: {v}")

if __name__ == "__main__":
    CONFIG_PATH = os.path.join(os.path.dirname(__file__), '../config/attack_config.yaml')
    config = load_attack_config(CONFIG_PATH)
    print_config_summary(config)
