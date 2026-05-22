from config import get_logger, settings
from agents.base_agent import create_base_agent
from core.models import get_streaming_model

logger = get_logger(__name__)

def main():
    logger.info("正在初始化 Base Agent...")
    try:
        # 获取 ChatModel 实例
        llm = get_streaming_model()
        
        # 创建默认的 Base Agent，并传入模型实例
        agent = create_base_agent(model=llm, tools=[])
        
        # 测试同步调用
        test_query = "请问，今天是几号？现在几点几点？"
        logger.info(f"发送测试问题: {test_query}")
        
        response = agent.invoke(test_query)
        logger.info(f"Agent 同步调用回复:\n{response}")
        
    except Exception as e:
        logger.error(f"调用 Agent 时发生错误: {e}")

if __name__ == "__main__":
    main()
