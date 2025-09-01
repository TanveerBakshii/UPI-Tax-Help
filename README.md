# UPI Tax Help

UPI Tax Help is an AI assistant designed to help individuals and small businesses manage their UPI and GST-related documents and reminders.

## Features

- 🗓 **Statement parsing** – Extract transactions from UPI/GST statements (PDF or text).
- 📊 **Categorisation** – Group transactions into categories like Food & Dining, Rent, Utilities, etc., using simple heuristics.
- ⏰ **Reminders** – Schedule monthly reminders to prepare tax summaries and pay GST dues.
- 📈 **Extensible** – Designed as a skeleton project; you can integrate with calendars, databases, or machine learning models.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/TanveerBakshii/UPI-Tax-Help.git
   cd UPI-Tax-Help
   ```

2. Ensure you have Python 3.8+ installed.

3. Install dependencies (once you add them):
   ```bash
   pip install -r requirements.txt
   ```

4. Place your UPI/GST statement file (e.g., `sample_statement.txt`) in the project directory.

5. Run the script:
   ```bash
   python app.py
   ```

## Project Structure

- `app.py` – Main script containing parsing, categorisation and reminder stubs.
- `README.md` – Project overview and usage instructions.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to extend functionality, fix bugs, or improve documentation.

## License

This project is provided under the MIT License. See [LICENSE](LICENSE) for more information.
