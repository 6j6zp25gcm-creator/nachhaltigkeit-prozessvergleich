# Publish this project on GitHub

The project includes 31 questions, 124 documented case answers, two PDFs and CSV/JSON downloads. No frontend build is needed.

## Upload the source

1. Create an empty repository named `nachhaltigkeit-prozessvergleich`.
2. Extract this archive. Upload the CONTENTS of the extracted project folder to the repository root, including `.github` and `.gitignore`. On macOS, press Command+Shift+. to display hidden files in Finder.
3. Commit the upload to the `main` branch.

Alternatively, use Git locally from the extracted project folder:

```sh
git init -b main
git add .
git commit -m "Publish sustainability process comparison"
git remote add origin https://github.com/YOUR_USERNAME/nachhaltigkeit-prozessvergleich.git
git push -u origin main
```

Replace YOUR_USERNAME with your GitHub username. Authentication is performed through your own Git client.

## Publish the webapp

1. In the repository, open Settings > Pages.
2. Under Build and deployment, choose Source: GitHub Actions.
3. Open Actions > Publish website > Run workflow and select main.
4. After the workflow succeeds, open the website URL shown in Settings > Pages.

Future pushes to main publish the contents of `dist/`. The workflow validates the committed questionnaire data before publishing. Regenerate data/PDFs locally when editing content; the workflow does not run the Python generators.

## Source and data

README.md describes generation and methodology. The original book PDFs and the previous hosting configuration are excluded from this export. This archive is a snapshot of the project source rather than a copy of its Git history.
