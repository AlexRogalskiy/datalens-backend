from dl_api_connector.i18n.localizer import CONFIGS as BI_API_CONNECTOR_CONFIGS
from dl_api_lib_testing.connection_form_base import ConnectionFormTestBase

from dl_connector_greenplum.api.connection_form.form_config import GreenplumConnectionFormFactory
from dl_connector_greenplum.api.i18n.localizer import CONFIGS as BI_CONNECTOR_GREENPLUM_CONFIGS


class TestGreenplumConnectionForm(ConnectionFormTestBase):
    CONN_FORM_FACTORY_CLS = GreenplumConnectionFormFactory
    TRANSLATION_CONFIGS = BI_API_CONNECTOR_CONFIGS + BI_CONNECTOR_GREENPLUM_CONFIGS
