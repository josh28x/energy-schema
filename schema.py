from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass 

class TelemetryRecord:
  timestamp: datetime
  source: str
  power_kw: Optional[float] = None
  voltage_v: Optional[float] = None
  current_a: Optional[float] = None
  frequency_hz: Optional[float] = None
  status: Optional[str] = None

  @staticmethod
  def from_dict(data:dict) 
