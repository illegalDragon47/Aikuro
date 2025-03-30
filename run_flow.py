import asyncio
import time

from app.agent.aikuro import Aikuro
from app.flow.flow_factory import FlowFactory, FlowType
from app.logger import logger

r"""
    _    _ _
   / \  (_) | ___   _ _ __ ___
  / _ \ | | |/ / | | | '__/ _ \
 / ___ \| |   <| |_| | | | (_) |
/_/   \_\_|_|\_\\__,_|_|  \___/
       by Autonomous GUILD

📊 AIKURO Multi-Agent Enterprise Solution 📊
"""

async def run_flow():
    agents = {
        "aikuro": Aikuro(),
    }

    try:
        prompt = input("🔍 Describe your complex business requirements: ")

        if prompt.strip().isspace() or not prompt:
            logger.warning("⚠️ No input detected. Please specify your business requirements.")
            return

        flow = FlowFactory.create_flow(
            flow_type=FlowType.PLANNING,
            agents=agents,
        )
        logger.warning("Processing your request...")

        try:
            start_time = time.time()
            result = await asyncio.wait_for(
                flow.execute(prompt),
                timeout=3600,  # 60 minute timeout for the entire execution
            )
            elapsed_time = time.time() - start_time
            logger.info(f"Request processed in {elapsed_time:.2f} seconds")
            logger.info(result)
        except asyncio.TimeoutError:
            logger.error("Request processing timed out after 1 hour")
            logger.info(
                "Operation terminated due to timeout. Please try a simpler request."
            )

    except KeyboardInterrupt:
        logger.info("Operation cancelled by user.")
    except Exception as e:
        logger.error(f"Error: {str(e)}")


if __name__ == "__main__":
    asyncio.run(run_flow())
