import json
from datetime import datetime
from pathlib import Path

REPORTS = Path(__file__).resolve().parent.parent / 'reports'
REPORTS.mkdir(exist_ok=True)

def save_report(report, filename=None):
    if filename is None:
        filename = REPORTS / f"scan_report_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
    else:
        filename = REPORTS / filename
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump({'created': datetime.utcnow().isoformat(), 'results': report}, f, indent=2)
    return str(filename)
