import json
import os

class Config:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.scene_mappings = {}
        self.load_config()
    
    def load_config(self):
        """Load configuration from a JSON file."""
        if not os.path.exists(self.config_file):
            print(f"Config file {self.config_file} not found. Loading default settings.")
            self.scene_mappings = {
                "Notepad": "Text Editor Scene",
                "Chrome": "Web Browser Scene"
            }
            self.save_config()  # Save default settings
            return
        
        try:
            with open(self.config_file, 'r') as f:
                self.scene_mappings = json.load(f)
                print("Configuration loaded successfully.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from config file: {e}")
            self.scene_mappings = {}
        except Exception as e:
            print(f"Unexpected error loading config: {e}")
            self.scene_mappings = {}
    
    def save_config(self):
        """Save current configuration to a JSON file."""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.scene_mappings, f, indent=4)
                print("Configuration saved successfully.")
        except Exception as e:
            print(f"Error saving config file: {e}")

    def add_mapping(self, window_title, scene_name):
        """Add a new window title to scene mapping."""
        if window_title in self.scene_mappings:
            print(f"Warning: '{window_title}' is already mapped to '{self.scene_mappings[window_title]}'. Overwriting.")
        self.scene_mappings[window_title] = scene_name
        self.save_config()
    
    def remove_mapping(self, window_title):
        """Remove a window title from scene mapping."""
        if window_title in self.scene_mappings:
            del self.scene_mappings[window_title]
            self.save_config()
        else:
            print(f"Warning: '{window_title}' not found in mappings.")
    
    def get_scene_for_window(self, window_title):
        """Get the OBS scene name for a given window title."""
        return self.scene_mappings.get(window_title, None)

# Example usage:
if __name__ == "__main__":
    config = Config()
    config.add_mapping("Visual Studio Code", "Code Editor Scene")
    print(config.get_scene_for_window("Chrome"))  # Should return "Web Browser Scene" or None if not mapped
