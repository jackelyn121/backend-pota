from src.core.database import Base

# Import all models to ensure they are registered with SQLAlchemy metadata
from src.models.users import User
from src.models.audit_logs import AuditLog
from src.models.farmers import Farmer
from src.models.planting_intents import PlantingIntent
from src.models.offtake_requests import OfftakeRequest
from src.models.raw_plant_reports import RawPlantReport
from src.models.report_planting_intents import ReportPlantingIntent
from src.models.report_submission import ReportSubmission
from src.models.report_validation_history import ReportValidationHistory
from src.models.forecasts import Forecast
from src.models.price_data import PriceData
from src.models.buyers import Buyer
from src.models.buyer_registry import BuyerRegistry
from src.models.buyer_status import BuyerStatus
from src.models.etl_run_log import ETLRunLog