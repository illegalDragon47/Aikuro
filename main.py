import asyncio

from app.agent.aikuro import Aikuro
from app.logger import logger

r"""
    _    _ _
   / \  (_) | ___   _ _ __ ___
  / _ \ | | |/ / | | | '__/ _ \
 / ___ \| |   <| |_| | | | (_) |
/_/   \_\_|_|\_\\__,_|_|  \___/
       by Autonomous GUILD

📊 Enterprise AI Solution Suite 📊
"""

async def main():
    agent = Aikuro()
    try:
        prompt = input("🌟 Enter your business requirement: ")
        if not prompt.strip():
            logger.warning("🤔 Nothing entered. Please specify your requirements.")
            return

        logger.warning("🚀 Processing your enterprise request...")
        await agent.run(prompt)
        logger.info("✅ Your request has been processed successfully!")
    except KeyboardInterrupt:
        logger.warning("🛑 Operation interrupted.")


if __name__ == "__main__":
    asyncio.run(main())
