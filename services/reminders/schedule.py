"""Reminder schedule kept in Redis."""
import redis

cache = redis.Redis(host="cache")


def schedule_reminder(visit_id, when):
    cache.setex(f"reminder:{visit_id}", 86400, when)
