#!/usr/bin/env python3

import logging
import sys
from typing import Optional

def setup_logger(verbose: bool = False) -> logging.Logger:
    """Set up and configure logger with appropriate log level."""
    logger = logging.getLogger('chm_processor')
    
    # Clear any existing handlers
    if logger.handlers:
        logger.handlers.clear()
    
    # Set log level based on verbose flag
    log_level = logging.DEBUG if verbose else logging.INFO
    logger.setLevel(log_level)
    
    # Create console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    
    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    
    # Add handler to logger
    logger.addHandler(console_handler)
    
    return logger