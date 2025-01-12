from dl_api_lib_testing.configuration import ApiTestEnvironmentConfiguration
from dl_core_testing.configuration import DefaultCoreTestConfiguration
from dl_testing.containers import get_test_container_hostport


# Infra settings
CORE_TEST_CONFIG = DefaultCoreTestConfiguration(
    host_us_http=get_test_container_hostport("us", fallback_port=51911).host,
    port_us_http=get_test_container_hostport("us", fallback_port=51911).port,
    host_us_pg=get_test_container_hostport("pg-us", fallback_port=51910).host,
    port_us_pg_5432=get_test_container_hostport("pg-us", fallback_port=51910).port,
    us_master_token="AC1ofiek8coB",
    core_connector_ep_names=["bitrix_gds", "postgresql"],
)

COMPENG_URL = f'postgresql://datalens:qwerty@{get_test_container_hostport("db-postgres-13", fallback_port=52301).as_pair()}/test_data'
API_TEST_CONFIG = ApiTestEnvironmentConfiguration(
    api_connector_ep_names=["bitrix_gds", "postgresql"],
    core_test_config=CORE_TEST_CONFIG,
    ext_query_executer_secret_key="_some_test_secret_key_",
    bi_compeng_pg_url=COMPENG_URL,
)

BITRIX_PORTALS = dict(
    default="gds.office.bitrix.ru",
    datalens="datalens.bitrix24.ru",
    invalid="some_portal",
)
DB_NAME = "default"
TABLE_NAME = "crm_deal"
SMART_TABLE_NAME = "crm_dynamic_items_180"
