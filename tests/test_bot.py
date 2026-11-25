import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import bot  # noqa: E402


def test_format_latency_rounds_to_milliseconds():
    assert bot.format_latency(0.0424) == "Pong! 42ms"


def test_format_latency_zero():
    assert bot.format_latency(0) == "Pong! 0ms"


def test_main_returns_1_without_token(monkeypatch):
    monkeypatch.delenv("DISCORD_TOKEN", raising=False)
    monkeypatch.setattr(bot, "load_dotenv", lambda: None)
    assert bot.main() == 1


def test_ping_command_is_registered():
    assert bot.bot.tree.get_command("ping") is not None
