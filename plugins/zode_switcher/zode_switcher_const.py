"""ZODE 切换器插件常量定义。

一键将一条龙的代码源切换到 idk500 增强源（ZODE 分支），无需手动编辑配置文件。
"""

# ============ 核心常量 (必需) ============
APP_ID = "zode_switcher"
APP_NAME = "ZODE 切换器"
DEFAULT_GROUP = False  # True: 出现在一条龙列表, False: 独立工具
NEED_NOTIFY = False  # 是否需要通知

# ============ 插件元数据 (可选，用于 GUI 显示) ============
PLUGIN_AUTHOR = "idk500"
PLUGIN_HOMEPAGE = "https://github.com/idk500/ZenlessZoneZero-OneDragon"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "一键切换代码源到 idk500 增强源（ZODE 分支），配置后重启生效"

# ============ 增强源信息 ============
ZODE_REPOSITORY_ID = "idk500_cnb"
ZODE_REPOSITORY_LABEL = "idk500 增强源 CNB"
ZODE_REPOSITORY_URL = "https://cnb.cool/zzz1d/ZODE.git"
ZODE_BRANCH = "zode"
