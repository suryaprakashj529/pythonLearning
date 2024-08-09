import asyncio

class BatchFetcher:
    # The `database` has an `async_fetch` method
    # that you should use in your code. This method
    # takes in a record id and returns a record.
    def __init__(self, database):
        # Write your code here.
        self.database = database

    async def fetch_records(self, record_ids):
        pending_records = []
        for record_id in record_ids:
            pending_records.append(self.database.async_fetch(record_id))

        return await asyncio.gather(*pending_records)

    # Write your code here.
