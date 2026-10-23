"""ZODE 切换器应用。

将代码源切换到 idk500 增强源（ZODE 分支）：写入代码源声明与用户选择后提示重启生效。
不进行任何游戏画面操作，运行即完成。
"""

from typing import Any

import yaml
from one_dragon.base.operation.application_base import Application
from one_dragon.base.operation.operation_node import operation_node
from one_dragon.base.operation.operation_round_result import OperationRoundResult
from one_dragon.utils import os_utils
from one_dragon.utils.log_utils import log
from zzz_od.context.zzz_context import ZContext

from . import zode_switcher_const


class ZodeSwitcherApp(Application):
    """ZODE 切换器应用。"""

    def __init__(self, ctx: ZContext):
        Application.__init__(
            self,
            ctx=ctx,
            app_id=zode_switcher_const.APP_ID,
            op_name=zode_switcher_const.APP_NAME,
        )

    def handle_init(self) -> None:
        """初始化节点编排。"""
        Application.handle_init(self)

    @operation_node(name="切换到 ZODE 增强源", is_start_node=True)
    def switch_to_zode(self) -> OperationRoundResult:
        """写入增强源声明与用户选择，提示重启生效。"""
        if (
            self.ctx.env_config.repository_url
            == zode_switcher_const.ZODE_REPOSITORY_URL
            and self.ctx.env_config.git_branch == zode_switcher_const.ZODE_BRANCH
        ):
            return self.round_success(status="当前已是 ZODE 增强源，无需重复切换")

        try:
            self._declare_repository()
        except Exception:
            log.error("写入代码源声明失败", exc_info=True)
            return self.round_fail(status="写入 config/repository.yml 失败，请查看日志")

        self.ctx.env_config.repository_url = zode_switcher_const.ZODE_REPOSITORY_URL
        self.ctx.env_config.git_branch = zode_switcher_const.ZODE_BRANCH
        return self.round_success(
            status="配置完成，请重启一条龙；重启后将自动从增强源更新代码（重启前请勿手动同步代码）",
        )

    def _declare_repository(self) -> None:
        """把增强源写入 config/repository.yml 的声明；声明已存在时不改写文件。"""
        repository_yml = os_utils.get_path_under_work_dir("config", "repository.yml")
        with open(repository_yml, encoding="utf-8") as file:
            data: dict[str, Any] = yaml.safe_load(file) or {}

        repositories: dict[str, Any] = data.get("repositories") or {}
        options: dict[str, Any] = repositories.get("options") or {}
        if zode_switcher_const.ZODE_REPOSITORY_ID in options:
            return

        options[zode_switcher_const.ZODE_REPOSITORY_ID] = {
            "label": zode_switcher_const.ZODE_REPOSITORY_LABEL,
            "url": zode_switcher_const.ZODE_REPOSITORY_URL,
            "use_proxy": False,
        }
        repositories["options"] = options
        data["repositories"] = repositories

        with open(repository_yml, "w", encoding="utf-8") as file:
            yaml.safe_dump(data, file, allow_unicode=True, sort_keys=False)
