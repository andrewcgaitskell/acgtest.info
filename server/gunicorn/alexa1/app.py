from flask import Flask
from ask_sdk_core.skill_builder import SkillBuilder
from flask_ask_sdk.skill_adapter import SkillAdapter

app = Flask(__name__)
skill_builder = SkillBuilder()
# Register your intent handlers to the skill_builder object

skill_adapter = SkillAdapter(
    skill=skill_builder.create(), skill_id=<SKILL_ID>, app=app)

@app.route("/")
def invoke_skill():
    return skill_adapter.dispatch_request()
