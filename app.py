"""
UPI Tax Help - A skeleton app for parsing UPI/GST transaction documents,
categorizing expenses and scheduling compliance reminders.

This module provides functions to parse PDF statements, categorize
transactions based on simple heuristics and schedule reminder events.
Real PDF parsing and scheduling logic should be implemented.
"""

from datetime import datetime


def parse_upi_pdf(file_path: str) -> list:
    """
    Parse a UPI/GST statement PDF and return a list of raw transaction strings.

    Parameters
    ----------
    file_path : str
        Path to the PDF file.

    Returns
    -------
    list
        A list of transaction lines extracted from the PDF.
    """
    # TODO: replace this stub with PDF parsing using pdfplumber, camelot, etc.
    transactions = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                if "UPI" in line:
                    transactions.append(line.strip())
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return transactions


def categorize_transactions(transactions: list) -> dict:
    """
    Categorize transactions into high-level expense groups.

    Parameters
    ----------
    transactions : list
        List of transaction strings.

    Returns
    -------
    dict
        Mapping of category name to list of matching transactions.
    """
    categories: dict[str, list] = {}
    for txn in transactions:
        lower = txn.lower()
        if any(kw in lower for kw in ("coffee", "restaurant", "food")):
            category = "Food & Dining"
        elif "rent" in lower:
            category = "Rent"
        elif any(kw in lower for kw in ("bill", "electricity", "gas")):
            category = "Utilities"
        else:
            category = "Other"
        categories.setdefault(category, []).append(txn)
    return categories


def schedule_reminders(transactions: list) -> list:
    """
    Stub function to schedule reminders for important GST/UPI deadlines.

    Parameters
    ----------
    transactions : list
        List of transaction strings.

    Returns
    -------
    list
        List of reminder messages (stub implementation).
    """
    # In a real system, this might integrate with a calendar API.
    reminders: list[str] = []
    # Example: create a monthly summary reminder
    now = datetime.now().strftime("%Y-%m-%d")
    reminders.append(f"Generate monthly tax summary on {now}")
    return reminders


def main() -> None:
    """
    Main entry point for running the module standalone.
    """
    # Example usage of the stubs.
    example_file = "sample_statement.txt"
    txns = parse_upi_pdf(example_file)
    categorized = categorize_transactions(txns)
    for cat, items in categorized.items():
        print(f"{cat}: {len(items)} transactions")
    reminders = schedule_reminders(txns)
    print("Scheduled reminders:")
    for r in reminders:
        print(" -", r)


if __name__ == "__main__":
    main()
