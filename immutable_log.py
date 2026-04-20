"""
Immutable Audit Log
-------------------
Append-only compliance log.
"""
import hashlib

class AuditLog:
    def __init__(self):
        self.entries = []

    def append(self, entry):
        hashed = hashlib.sha256(str(entry).encode()).hexdigest()
        self.entries.append((entry, hashed))
