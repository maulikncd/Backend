"""
Production-ready refresh token cleanup job.

This module provides a standalone function to clean up inactive refresh tokens
older than 7 days from the database. Designed to be called from schedulers
or cron jobs without requiring FastAPI dependencies.
"""

from __future__ import annotations

import logging
from datetime import datetime, timedelta
from typing import Optional

from sqlalchemy.orm import Session

from app.Auth.db.session import SessionLocal
from app.Auth.models.refresh_token import RefreshToken

logger = logging.getLogger(__name__)


def cleanup_inactive_refresh_tokens(days_old: int = 7, dry_run: bool = False) -> dict:
    """
    Clean up inactive refresh tokens older than specified days.
    
    Args:
        days_old: Number of days old for token cleanup (default: 7)
        dry_run: If True, only count tokens to be deleted without actually deleting them
        
    Returns:
        dict: Summary of cleanup operation with counts and any errors
    """
    # Calculate the cutoff date
    cutoff_date = datetime.utcnow() - timedelta(days=days_old)
    
    result = {
        "tokens_deleted": 0,
        "tokens_found": 0,
        "errors": [],
        "cutoff_date": cutoff_date.isoformat(),
        "dry_run": dry_run
    }
    
    # Create database session
    db: Optional[Session] = None
    try:
        db = SessionLocal()
        
        # Query for inactive tokens older than cutoff date
        query = db.query(RefreshToken).filter(
            RefreshToken.is_active == False,
            RefreshToken.created_at < cutoff_date
        )
        
        # Count tokens to be deleted
        tokens_to_delete = query.all()
        result["tokens_found"] = len(tokens_to_delete)
        
        if dry_run:
            logger.info(f"DRY RUN: Found {result['tokens_found']} inactive refresh tokens older than {days_old} days")
            return result
        
        # Delete the tokens
        for token in tokens_to_delete:
            try:
                db.delete(token)
                result["tokens_deleted"] += 1
                logger.debug(f"Deleted refresh token {token.refresh_token_id} for user {token.user_id}")
            except Exception as e:
                error_msg = f"Failed to delete refresh token {token.refresh_token_id}: {str(e)}"
                logger.error(error_msg)
                result["errors"].append(error_msg)
        
        # Commit the transaction
        if result["tokens_deleted"] > 0:
            db.commit()
            logger.info(f"Successfully deleted {result['tokens_deleted']} inactive refresh tokens older than {days_old} days")
        else:
            logger.info(f"No inactive refresh tokens found older than {days_old} days")
            
    except Exception as e:
        error_msg = f"Database error during cleanup: {str(e)}"
        logger.error(error_msg, exc_info=True)
        result["errors"].append(error_msg)
        if db:
            db.rollback()
    finally:
        if db:
            db.close()
    
    return result


def main() -> None:
    """
    Main entry point for running the cleanup job directly.
    Can be called from command line or scheduler.
    """
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    logger.info("Starting refresh token cleanup job")
    
    try:
        # Run the cleanup
        result = cleanup_inactive_refresh_tokens(days_old=7, dry_run=False)
        
        # Log results
        logger.info(f"Cleanup completed: {result['tokens_deleted']} tokens deleted out of {result['tokens_found']} found")
        
        if result['errors']:
            logger.warning(f"Cleanup completed with {len(result['errors'])} errors")
            for error in result['errors']:
                logger.error(f"Error: {error}")
        else:
            logger.info("Cleanup completed successfully with no errors")
            
    except Exception as e:
        logger.error(f"Fatal error in cleanup job: {str(e)}", exc_info=True)
        raise


if __name__ == "__main__":
    main()
