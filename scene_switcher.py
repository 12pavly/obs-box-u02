import time
import logging
import subprocess
import json
import platform

# Configuration - replace with actual values
OBS_WS_URL = "ws://localhost:4444"
OBS_PASSWORD = "your_password_here"
SCENE_CONFIG = {
    "game": "Gaming Scene",
    "browser": "Desktop Scene",
    "code": "Coding Scene"
}

# Set up logging
logging.basicConfig(level=logging.INFO)

class OBSSceneSwitcher:
    def __init__(self):
        self.current_scene = None

    def get_active_window_title(self):
        """Fetch the title of the currently active window."""
        try:
            if platform.system() == "Linux":
                # Note: This requires xdotool on Linux systems
                output = subprocess.check_output(['xdotool', 'getactivewindow', 'getwindowname'])
                return output.decode('utf-8').strip()
            elif platform.system() == "Windows":
                logging.error("Windows support not implemented. Consider using pygetwindow")
                return None
            elif platform.system() == "Darwin":
                logging.error("macOS support not implemented. Consider using pygetwindow")
                return None
            else:
                logging.error(f"Unsupported platform: {platform.system()}")
                return None
        except subprocess.CalledProcessError as e:
            logging.error(f"Error getting active window: {e}")
            return None
        except FileNotFoundError:
            logging.error("xdotool not found. Please install xdotool or use pygetwindow for cross-platform compatibility")
            return None

    def switch_scene(self, scene_name):
        """Switch the OBS scene to the specified scene name."""
        if scene_name == self.current_scene:
            logging.info(f"Already in scene: {scene_name}")
            return
        
        logging.info(f"Switching to scene: {scene_name}")
        # TODO: Add OBS WebSocket handling here to switch scene
        # For example, using the obs-websocket-py library:
        # import obsws
        # ws = obsws.WSClient(OBS_WS_URL, OBS_PASSWORD)
        # ws.connect()
        # ws.call(obsws.Request('SetCurrentScene', {'scene-name': scene_name}))
        # ws.disconnect()

        self.current_scene = scene_name

    def run(self):
        """Main loop to monitor window titles and switch scenes."""
        logging.info("Starting OBS Scene Switcher...")
        while True:
            active_window_title = self.get_active_window_title()
            if active_window_title:
                for title, scene in SCENE_CONFIG.items():
                    if title.lower() in active_window_title.lower():
                        self.switch_scene(scene)
                        break
            time.sleep(1)  # Check every second

if __name__ == "__main__":
    switcher = OBSSceneSwitcher()
    switcher.run()
