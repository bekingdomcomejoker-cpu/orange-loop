#!/usr/bin/env python3
import os
import sys
import yaml
import time

class OrangeLoop:
    def __init__(self, config_path="config/loop.yaml"):
        self.nodes = [
            "Human", "Sentinel", "Mind", "Form", "Gate", "Voice", "Heart", "Whisper"
        ]
        self.hands = ["Smith", "Gate", "Scout"]
        self.load_config(config_path)

    def load_config(self, path):
        if os.path.exists(path):
            with open(path, 'r') as f:
                self.config = yaml.safe_load(f)
        else:
            self.config = {}

    def run_node(self, node_id, input_data):
        print(f"[Node {node_id}: {self.nodes[node_id]}] Processing...")
        time.sleep(0.5)
        return f"Output from {self.nodes[node_id]}"

    def run_hand(self, hand_name, task):
        print(f"[Hand: {hand_name}] Working on: {task}")
        time.sleep(1)
        return f"Result from {hand_name}"

    def start(self):
        print("🍊 Orange Loop v1.1 Started")
        while True:
            user_input = input("\n[Node 0: Human] > ")
            if user_input.lower() in ['exit', 'quit']:
                break
            
            current_data = user_input
            
            # Primary Loop: 0 -> 1 -> 2 -> 3 -> 4
            for i in range(1, 5):
                current_data = self.run_node(i, current_data)
                
                # Branching at Node 4
                if i == 4:
                    if ":" in user_input:
                        cmd, task = user_input.split(":", 1)
                        cmd = cmd.strip().lower()
                        if cmd in [h.lower() for h in self.hands]:
                            hand_result = self.run_hand(cmd.capitalize(), task.strip())
                            current_data += f" | Hand Result: {hand_result}"

            # Primary Loop: 5 -> 6 -> 7 -> 0
            for i in range(5, 8):
                current_data = self.run_node(i, current_data)
            
            print(f"\n[Final Output] {current_data}")

if __name__ == "__main__":
    loop = OrangeLoop()
    loop.start()
