"""ZODE 切换器工厂。

工厂文件必须以 _factory.py 结尾才能被自动发现。
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from one_dragon.base.operation.application.application_factory import ApplicationFactory

from . import zode_switcher_const

if TYPE_CHECKING:
    from zzz_od.context.zzz_context import ZContext


class ZodeSwitcherFactory(ApplicationFactory):
    """ZODE 切换器工厂。"""

    def __init__(self, ctx: ZContext):
        ApplicationFactory.__init__(self, zode_switcher_const)
        self.ctx: ZContext = ctx

    def create_application(self, instance_idx: int, group_id: str):
        from .zode_switcher_app import ZodeSwitcherApp

        return ZodeSwitcherApp(self.ctx)
