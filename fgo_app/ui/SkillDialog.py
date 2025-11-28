from fgo_app.ui.BaseDescriptionDialog import BaseDescriptionDialog

class SkillDescriptionDialog(BaseDescriptionDialog):
    def __init__(self, data, unlock_callback, can_unlock, parent=None):
        title = data.get("name")
        description = data.get("description", "")
        effects = data.get("effects", [])

        extra_fields = {
            "Action Type": data.get("action_type"),
            "Incantation": data.get("incantation"),
            "Prerequisite": data.get("prerequisite"),
        }

        super().__init__(
            title=title,
            description=description,
            effects=effects,
            extra_fields=extra_fields,
            unlock_callback=unlock_callback,
            can_unlock=can_unlock,
            parent=parent
        )