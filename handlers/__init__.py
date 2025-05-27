from .start import start_handlers  # <-- Corrected here
from .verify import verify_handler
from .link import link_handler
from .batch import batch_handler
from .stats import stats_handler
from .admin import admin_handlers

def register_handlers(app):
    start_handlers(app)     # <-- matches start.py
    verify_handler(app)
    link_handler(app)
    batch_handler(app)
    stats_handler(app)
    admin_handlers(app)
