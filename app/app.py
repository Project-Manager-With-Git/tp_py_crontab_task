from schema_entry import EntryPoint


class Application(EntryPoint):
    _name = "tp_py_crontab_task"
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "required": ["address", "log_level"],
        "properties": {
            "app_version": {
                "type": "string",
                "title": "v",
                "description": "应用版本"
            },
            "app_name": {
                "type": "string",
                "title": "n",
                "description": "应用名"
            },
            "log_level": {
                "type": "string",
                "title": "l",
                "description": "log等级",
                "enum": ["DEBUG", "INFO", "WARN", "ERROR"],
                "default": "DEBUG"
            },
            "update_period": {
                "type": "string",
                "description": "定时更新的间隔,使用crontab的格式",
                "default": "37 * * * *"
            }
        }
    }
