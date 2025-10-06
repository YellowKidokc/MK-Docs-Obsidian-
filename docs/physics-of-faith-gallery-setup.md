# Physics of Faith Visualizations Gallery Deployment Guide

This guide walks through preparing, populating, and deploying the
[physics-of-faith-visualizations](https://github.com/YellowKidokc/physics-of-faith-visualizations/)
static gallery to Cloudflare Pages. The workflow assumes you are working
on Windows with the batch and PowerShell helpers that live in that
repository, but the high-level structure applies everywhere.

## 1. Prepare the Gallery Workspace

1. Clone the repository and open a terminal with write permissions to
the project directory.
2. Run the elevated setup helper:

   ```bat
   run-admin-setup.bat
   ```

   The script scaffolds a `gallery/` directory that contains the working
   structure used by the other helpers:

   ```text
   gallery/
   ├── images/          # Regular single images
   ├── collections/     # Featured multi-image stories
   └── descriptions/    # Caption files (one per image)
   ```

If you do not have admin rights, launch the terminal as Administrator or
manually create the folders above before proceeding.

## 2. Add Content

### Regular Images

Use `add-image.bat` to copy an image into the gallery and generate its
caption stub:

```bat
add-image.bat "path\to\your\image.png" gallery
```

The helper will:

- Copy the source file into `gallery\images\`.
- Create a matching text file under `gallery\descriptions\` for your
  caption copy.
- Update the gallery JSON that powers the frontend grid.

### Featured Collections

Collections feed the "Featured" row at the top of the gallery. Create a
collection scaffold with:

```bat
new-collection.bat master-equation gallery
```

The command produces:

```text
gallery/collections/master-equation/
├── cover.jpg      # Supply a hero image that represents the collection
├── index.html     # Replace with your narrative or landing content
└── meta.json      # Update with collection metadata
```

Any images placed inside the new directory automatically appear as part
of the featured carousel once the gallery rebuilds.

## 3. Customise the Frontend

The primary HTML template you should use lives at
`physics-of-faith-gallery.html`. This file is intentionally lean compared
to the other variants in the repository (for example, in a Windows setup
you might see it at `B:\Cloud Accounts\OneDrive\Desktop\David Bible
Study\Marketing\HTML Claude\physics-of-faith-gallery.html`). Treat this
as the canonical layout for every gallery you publish.

1. Copy `physics-of-faith-gallery.html` into your `gallery/` directory and
   rename it to `index.html`.
2. Ensure the accompanying `styles.css` and `app.js` files sit alongside
   it so the responsive grid, featured strip, and lightbox continue to
   function:

   ```text
   gallery/
   ├── index.html   # Copied from physics-of-faith-gallery.html
   ├── styles.css   # Visual styling
   └── app.js       # Lightbox + polling logic
   ```

3. When you want another gallery (for example, to highlight a different
   theme), duplicate the same template into a new folder, point it at the
   relevant `images/` and `collections/` content, and repeat the process.

Update the HTML, CSS, or JavaScript to match your branding, analytics, or
copy needs, but keep the file and folder references above so the runtime
can load everything correctly.

## 4. Deploy with Cloudflare Pages

1. Push your changes to the `main` branch on GitHub.
2. In the Cloudflare dashboard, create a **Pages** project and connect it
   to the GitHub repository.
3. Use the following settings when prompted:

   | Setting               | Value                                   |
   | --------------------- | --------------------------------------- |
   | Project name          | `physics-of-faith-visualizations`       |
   | Production branch     | `main`                                  |
   | Build command         | *(leave empty — static site)*           |
   | Build output directory| `/`                                     |
   | Root directory        | `/`                                     |

4. Save and deploy. Cloudflare Pages will serve the site at
   `https://physics-of-faith-visualizations.pages.dev` once the build
   completes (typically under two minutes).

## 5. Keep the Gallery Fresh

- **Featured updates**: Add new collections with `new-collection.bat`,
  supply a `cover.jpg`, and drop supporting media into the folder.
- **Regular uploads**: Run `add-image.bat` for each new asset you want in
  the main scrolling grid.
- **Automatic refresh**: `app.js` contains a polling loop that rescans
  the image directory every 30 seconds so newly uploaded files appear
  without a manual page refresh.

## 6. Run an End-to-End Smoke Test

Before your launch, walk through the same automation that Cloudflare
Pages will execute so you can confirm every helper script, file type, and
lightbox interaction works from end to end:

1. **Start from a clean workspace.** Delete the existing `gallery/`
   folder if present, then rerun `run-admin-setup.bat` to rebuild the
   baseline structure.
2. **Verify regular uploads.** Use `add-image.bat` to ingest one PNG, one
   JPG, one SVG, and one HTML snippet (for example, a short animated
   visualization). After each run, confirm the file lands in
   `gallery/images/`, a matching caption file appears in
   `gallery/descriptions/`, and the gallery JSON (`gallery/data.json` in
   the upstream project) includes a new entry with a unique permalink.
3. **Verify featured collections.** Run `new-collection.bat demo-set
   gallery`, add a `cover.jpg`, drop at least one image or HTML page into
   the new directory, and refresh the gallery. The featured strip should
   now list **Demo Set** with working navigation into the collection.
4. **Check automatic refresh.** Launch a local static server from within
   the `gallery/` folder (`python -m http.server 8080` works on Windows
   if Python is installed), open `http://localhost:8080`, and leave the
   page running. Upload another asset with `add-image.bat`. Within ~30
   seconds the new card should appear without you reloading the page.
5. **Capture permanent links.** Right-click each new card and copy the
   link address. These URLs are the ones Cloudflare Pages will serve, so
   they are safe to share on your subdomain once you deploy.

If any step fails, note the helper script output, check whether the file
appeared in the target folder, and review the browser console for errors.
Those details make it easier to troubleshoot or to open an issue in the
GitHub repository.

## 7. Troubleshooting

| Issue                         | Checks                                                                                 |
| ----------------------------- | -------------------------------------------------------------------------------------- |
| Images do not display         | Confirm files live in `gallery/images/`, use supported formats (PNG/JPG/GIF/SVG/WebP),
|                               | and avoid spaces or special characters in filenames.                                  |
| Featured row is empty         | Verify each collection has a `cover.jpg` and a populated `meta.json`.                  |
| Cloudflare build fails        | Review build logs, confirm repo permissions, and keep assets below ~2&nbsp;MB.         |
| Local scripts need elevation  | Run the `.bat` files from an Administrator shell or create folders manually.           |

By following the steps above you can maintain a responsive, lightbox-enabled gallery that highlights flagship collections while automatically ingesting the latest visualizations.
