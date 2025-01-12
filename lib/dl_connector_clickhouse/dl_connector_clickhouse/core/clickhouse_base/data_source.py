from __future__ import annotations

import abc
import logging
from typing import (
    TYPE_CHECKING,
    ClassVar,
)

from dl_constants.enums import JoinType
from dl_core.data_source.sql import (
    BaseSQLDataSource,
    StandardSQLDataSource,
    SubselectDataSource,
)

from dl_connector_clickhouse.core.clickhouse_base.constants import CONNECTION_TYPE_CLICKHOUSE
from dl_connector_clickhouse.core.clickhouse_base.query_compiler import ClickHouseQueryCompiler


if TYPE_CHECKING:
    from dl_core import us_connection  # noqa
    from dl_core.db import (  # noqa
        SchemaColumn,
        SchemaInfo,
    )


LOGGER = logging.getLogger(__name__)


class CommonClickHouseSubselectDataSource(SubselectDataSource):
    """Common subselect base for ClickHouse-based databases"""

    pass


class ClickHouseBaseMixin(BaseSQLDataSource):
    default_server_version = None
    supported_join_types: ClassVar[frozenset[JoinType]] = frozenset(
        {
            JoinType.inner,
            JoinType.left,
            JoinType.full,
            JoinType.right,
        }
    )
    compiler_cls = ClickHouseQueryCompiler

    def get_connect_args(self) -> dict:
        return dict(super().get_connect_args(), server_version=self.db_version or self.default_server_version)  # type: ignore  # TODO: fix  # noqa


class ActualClickHouseBaseMixin(ClickHouseBaseMixin):
    """
    Data source base class / mixin for actual ClickHouse (i.e. not chyt).
    """

    conn_type = CONNECTION_TYPE_CLICKHOUSE


class ClickHouseDataSourceBase(ActualClickHouseBaseMixin, StandardSQLDataSource, metaclass=abc.ABCMeta):  # type: ignore  # TODO: fix
    """ClickHouse table. Might not work correctly for views."""
