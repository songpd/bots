import logging
import os
import sys

import discord
from discord import app_commands
from dotenv import load_dotenv

log = logging.getLogger("bot")


def format_latency(seconds: float) -> str:
    """지연 시간(초)을 'Pong! 42ms' 형식의 문자열로 변환한다."""
    return f"Pong! {round(seconds * 1000)}ms"


class Bot(discord.Client):
    def __init__(self) -> None:
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        # 슬래시 명령어를 디스코드에 등록한다 (전역 등록은 반영에 시간이 걸릴 수 있다).
        await self.tree.sync()

    async def on_ready(self) -> None:
        log.info("로그인 완료: %s (id=%s)", self.user, getattr(self.user, "id", None))


bot = Bot()


@bot.tree.command(name="ping", description="봇의 응답 속도를 확인합니다.")
async def ping(interaction: discord.Interaction) -> None:
    await interaction.response.send_message(format_latency(bot.latency))


def main() -> int:
    load_dotenv()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    token = os.getenv("DISCORD_TOKEN")
    if not token:
        log.error("DISCORD_TOKEN이 설정되지 않았습니다. .env 파일을 확인하세요.")
        return 1

    try:
        bot.run(token, log_handler=None)
    except discord.LoginFailure:
        log.error("토큰이 올바르지 않습니다. 발급받은 토큰을 다시 확인하세요.")
        return 1
    except Exception:
        log.exception("봇 실행 중 오류가 발생했습니다.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
