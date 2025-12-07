# wheelbot_agent.py (runs on a NEW Pi)

from uagents import Agent, Context, Model
import RPi.GPIO as GPIO
import asyncio

# -------------------------------
# Models
# -------------------------------
class Command(Model):
    direction: str
    reason: str
    obstacle_type: str

class Status(Model):
    old_pos: tuple
    new_pos: tuple
    obstacle_type: str


# -------------------------------
# CONFIGURATION (CHANGE THESE)
# -------------------------------
NEW_PI_IP = "10.64.173.150"  # ← change to NEW Pi IP

agent = Agent(
    name="wheelbot_agent",          # ← unique name
    seed="wheelbot_agent_seed",     # ← unique seed
    port=8003,                      # ← new port NOT used elsewhere
    endpoint=[f"http://{NEW_PI_IP}:8003/submit"]
)


# -------------------------------
# GPIO Setup
# -------------------------------
GPIO.setmode(GPIO.BCM)

