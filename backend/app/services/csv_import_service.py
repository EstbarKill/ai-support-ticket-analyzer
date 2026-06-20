from pathlib import Path

import pandas as pd

from app.models.ticket import Ticket

from app.services.data_cleaner import DataCleaner


class CSVImportService:

    def load(self):

        root = Path(__file__).resolve().parents[3]

        csv_path = root / "dataset" / "tickets.csv"

        df = pd.read_csv(csv_path)

        tickets = []

        for _, row in df.iterrows():

            ticket = Ticket(
                ticket_id=DataCleaner.clean_text(
                    row.get("Ticket ID")
                ),

                customer_name=DataCleaner.clean_text(
                    row.get("Customer Name")
                ),

                customer_email=DataCleaner.clean_email(
                    row.get("Customer Email")
                ),

                customer_age=row.get(
                    "Customer Age"
                ),

                customer_gender=DataCleaner.clean_text(
                    row.get("Customer Gender")
                ),

                product_purchased=DataCleaner.clean_text(
                    row.get("Product Purchased")
                ),

                ticket_type=DataCleaner.clean_text(
                    row.get("Ticket Type")
                ),

                ticket_subject=DataCleaner.clean_text(
                    row.get("Ticket Subject")
                ),

                ticket_description=DataCleaner.clean_text(
                    row.get("Ticket Description")
                ),

                ticket_status=DataCleaner.clean_text(
                    row.get("Ticket Status")
                ),

                ticket_priority=DataCleaner.normalize_priority(
                    row.get("Ticket Priority")
                ),

                ticket_channel=DataCleaner.clean_text(
                    row.get("Ticket Channel")
                )
            )

            tickets.append(ticket)

        return tickets