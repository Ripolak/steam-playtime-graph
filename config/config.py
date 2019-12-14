from config.config_loader import load_config

# region Static configuration

STEAMSPY_URL = "http://steamspy.com"
CONFIG_FILE = "config.json"

# endregion

# region User configuration
user_config = load_config(CONFIG_FILE)

PROFILE_NAME = user_config["steam_profile_name"]
STEAM_API_KEY = user_config["steam_api_key"]
MAX_STUDIOS_AMOUNT = int(user_config.get("max_bars_amount", 15))
MINIMUM_HOURS = int(user_config.get("minimum_hours", None))
MEASURE_BY = user_config.get("measure_by", "developer").lower()

GRAPH_TITLE = user_config.get("graph_title", "Amount of hours spent")
X_LABEL = user_config.get("x_label", "Company")
Y_LABEL = user_config.get("y_label", "Hours")

# endregion
