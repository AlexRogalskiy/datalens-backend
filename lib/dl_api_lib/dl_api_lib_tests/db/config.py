from typing import ClassVar

from dl_api_lib_testing.configuration import ApiTestEnvironmentConfiguration
from dl_core_testing.configuration import DefaultCoreTestConfiguration
from dl_testing.containers import get_test_container_hostport

from dl_connector_clickhouse.formula.constants import ClickHouseDialect as D


CORE_TEST_CONFIG = DefaultCoreTestConfiguration(
    host_us_http=get_test_container_hostport("us", fallback_port=52500).host,
    port_us_http=get_test_container_hostport("us", fallback_port=52500).port,
    host_us_pg=get_test_container_hostport("db-postgres", fallback_port=52509).host,
    port_us_pg_5432=get_test_container_hostport("db-postgres", fallback_port=52509).port,
    us_master_token="AC1ofiek8coB",
    core_connector_ep_names=["clickhouse", "postgresql"],
)


class CoreConnectionSettings:
    DB_NAME: ClassVar[str] = "test_data"
    HOST: ClassVar[str] = get_test_container_hostport("db-clickhouse", fallback_port=52510).host
    PORT: ClassVar[int] = get_test_container_hostport("db-clickhouse", fallback_port=52510).port
    USERNAME: ClassVar[str] = "datalens"
    PASSWORD: ClassVar[str] = "qwerty"


DB_URLS = {
    D.CLICKHOUSE_22_10: f"clickhouse://datalens:qwerty@"
    f'{get_test_container_hostport("db-clickhouse", fallback_port=52510).as_pair()}/test_data',
}
DB_CORE_URL = DB_URLS[D.CLICKHOUSE_22_10]

API_TEST_CONFIG = ApiTestEnvironmentConfiguration(
    api_connector_ep_names=["clickhouse", "postgresql"],
    core_test_config=CORE_TEST_CONFIG,
    ext_query_executer_secret_key="_some_test_secret_key_",
    bi_compeng_pg_url=(
        f"postgresql://us:us@"
        f'{get_test_container_hostport("db-postgres", fallback_port=52509).as_pair()}/us-db-ci_purgeable'
    ),
)
