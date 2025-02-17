import logging
import urllib.request
from astrbot.api.star import Context, Star, register
from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.event.filter import event_message_type, EventMessageType

# 获取当前模块 logger
logger = logging.getLogger(__name__)

@register("ame", "shirool", "回复a醋", "1.0", "https://github.com/shirool/astrbot_plugin_sh")
class CrazyThursdayPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @event_message_type(EventMessageType.ALL)
    async def on_message(self, event: AstrMessageEvent) -> MessageEventResult:
        """
        当消息中包含 "ame" 时回复 "a醋"
        """
        msg_obj = event.message_obj

        text = msg_obj.message_str or ""

        logger.debug("=== Debug: AstrBotMessage ===")
        logger.debug("Bot ID: %s", msg_obj.self_id)
        logger.debug("Session ID: %s", msg_obj.session_id)
        logger.debug("Message ID: %s", msg_obj.message_id)
        logger.debug("Sender: %s", msg_obj.sender)
        logger.debug("Group ID: %s", msg_obj.group_id)
        logger.debug("Message Chain: %s", msg_obj.message)
        logger.debug("Raw Message: %s", msg_obj.raw_message)
        logger.debug("Timestamp: %s", msg_obj.timestamp)
        logger.debug("============================")

        if "ame" in text.lower():  # 改为检测 ame（不区分大小写）
            # 直接返回固定响应
            return event.plain_result("a醋")

        # 保留原有疯狂星期四逻辑（如需完全替换可删除此部分）
        if "疯狂星期四" in text:
            try:
                with urllib.request.urlopen("https://vme.im/api?format=text") as resp:
                    result_bytes = resp.read()
                    result_text = result_bytes.decode("utf-8", errors="replace")
            except Exception as e:
                result_text = f"获取信息失败: {e}"

            yield event.plain_result(result_text)
