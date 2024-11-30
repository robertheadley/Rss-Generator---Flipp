
# Rss-Generator---Flipp

This repository automates the process of generating an RSS feed from search results for Coca-Cola products (or other items) using data from the Flipp API. It dynamically fetches search results, processes them, and creates an RSS feed with product details, including images and prices.

---

## Features

- Fetches search results dynamically from the Flipp API.
- Processes the results to generate an RSS feed (`rss_feed.xml`).
- Automates the entire process using GitHub Actions.
- Schedules daily updates or runs on repository changes.

---

## Files and Structure

```
Rss-Generator---Flipp/
├── .github/
│   └── workflows/
│       └── rss_generator.yml     # GitHub Actions workflow file
├── generate_results.py           # Python script to fetch search results
├── generate_rss_feed.py          # Python script to generate the RSS feed
├── results.json                  # Dynamically generated search results
├── rss_feed.xml                  # Generated RSS feed
```

---

## How It Works

1. **Data Fetching**:
   - The `generate_results.py` script fetches search results for items (e.g., "Coke 24 Pack") using the Flipp API and saves them in `results.json`.

2. **RSS Feed Generation**:
   - The `generate_rss_feed.py` script processes `results.json` to create `rss_feed.xml`, an RSS feed containing product details, prices, and images.

3. **Automation**:
   - The GitHub Actions workflow (`rss_generator.yml`) runs automatically:
     - On every push to the `main` branch.
     - Daily at midnight UTC via a cron job.
   - The workflow generates `results.json` and `rss_feed.xml`, then commits and pushes the updates to the repository.

---

## Usage

### Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Rss-Generator---Flipp.git
   cd Rss-Generator---Flipp
   ```

2. Install Python dependencies:
   ```bash
   pip install requests
   ```

3. Run the scripts:
   - To fetch search results:
     ```bash
     python generate_results.py
     ```
   - To generate the RSS feed:
     ```bash
     python generate_rss_feed.py
     ```

4. The `results.json` and `rss_feed.xml` files will be generated in the repository folder.

---

### Automated Workflow
1. Push any changes to the `main` branch or let the scheduled workflow run automatically.
2. Navigate to the **Actions** tab in the GitHub repository to monitor the workflow execution.
3. The updated `results.json` and `rss_feed.xml` files will appear in the repository after a successful run.

---

## Configuration

### Search Query
To modify the search query, update the `PARAMS` dictionary in `generate_results.py`:
```python
PARAMS = {
    "locale": "en-us",
    "postal_code": "57106",
    "sid": "",
    "q": "Your Search Query Here"
}
```

### Schedule
To change the automation schedule, edit the `cron` field in `.github/workflows/rss_generator.yml`:
```yaml
schedule:
  - cron: "0 0 * * *"  # Runs daily at midnight UTC
```

---

## Requirements

- **Python**: Version 3.7 or later
- **GitHub Actions**: Enabled for the repository
- **Dependencies**: Install via `pip install requests`

---

## Troubleshooting

### Workflow Not Running
- Ensure the workflow file is located at `.github/workflows/rss_generator.yml`.
- Confirm the workflow is pushed to the `main` branch.
- Check the **Actions** tab for logs and error messages.

### API Errors
- Ensure you have a stable internet connection.
- Verify the Flipp API endpoint and parameters in `generate_results.py`.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---
