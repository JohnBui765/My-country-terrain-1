# Vietnam 63

A practice app for Vietnam's 63 provincial-level units, grouped and numbered as in the
statistics table of the *Atlat Địa lí Việt Nam*. It is built for the iPhone: install it on the
Home Screen and it works offline, like a native app. It also runs on a laptop.

- **Regions I–VI in the Atlat's order**, each named in English and Vietnamese, with the
  provinces numbered 1–63 as in the table. The **Table** tab shows the table itself (area and
  2021 population); tap a row to find it on the map.
- **Labels never overlap.** Province names and capital names are placed around each other;
  whatever does not fit waits until you zoom in. Small provinces show their Atlat number.
- **Made for fingers:** pinch, double-tap to zoom in, two-finger tap to zoom out, flick to
  glide. If a tap could mean more than one small province, the map zooms in instead of guessing.
- **The neighbourhood** (China, Laos, Cambodia, Thailand, the East Sea and beyond) is drawn
  in general outline and fades into mist farther out. Hoàng Sa and Trường Sa are at their
  true positions.

The app is in English; province names are in Vietnamese.

## Put it online (GitHub Pages)

1. Create a new public repository, for example `vietnam63`.
2. Upload everything in this folder, keeping the `fonts`, `icons` and `tools` folders.
3. In the repository, open Settings, then Pages. Under "Build and deployment", choose
   "Deploy from a branch", branch `main`, folder `/ (root)`, and save.
4. After a minute the app is at `https://<your-username>.github.io/vietnam63/`.

## Install it

- **iPhone:** open the link in Safari, tap Share, then "Add to Home Screen".
- **Laptop:** open the link in Chrome or Edge and click the install icon in the address bar.

After the first visit it works without internet. If you installed an older version, remove it
from the Home Screen and add it again so iOS picks up the new icon and launch screen.

## Your progress

Progress is stored on each device separately. To move it, open Progress, then Details,
then "Back up progress", and use "Restore" on the other device. Progress saved by the
previous version is kept.

## After editing any file

Change `VERSION` at the top of `sw.js` (for example to `vn63-v3`). Otherwise installed
copies keep showing the cached version.

## Rebuilding the map data

The map data is embedded in `index.html`. `tools/build_data.py` rebuilds it from
`tools/vietnam63-base.json` (the provinces) and Natural Earth (the neighbours):

```sh
pip install shapely
npm pack world-atlas@2.0.2 && tar xzf world-atlas-2.0.2.tgz
python3 tools/build_data.py package
```

The Atlat table (regions, numbers, area, population) is written out in the script and checked
against the table's region totals. `tools/make_splash.py icons/icon-1024.png` remakes the
iPhone launch screens.

## Sources and licences

- Boundaries: district boundaries from OCHA ROAP and the Government of Viet Nam (2020),
  licensed CC BY 3.0 IGO, obtained through geoBoundaries (www.geoboundaries.org,
  William & Mary geoLab). Districts were merged into the 63 provinces and simplified
  to about 0.7 km.
- Regions, numbering, area and population: the statistics table of the Atlat Địa lí Việt Nam,
  quoting the Statistical Yearbook of Vietnam 2021 (Statistical Publishing House, 2022).
  English region names follow the General Statistics Office.
- Province codes: Decision 124/2004/QĐ-TTg. Boundary and status changes: Resolutions
  22/2003/QH11, 15/2008/QH12 and 175/2024/QH15. 2025 merger: Resolution 202/2025/QH15.
  Capitals: Atlat Địa lí Việt Nam.
- Neighbouring countries: Natural Earth 1:50m (public domain), via world-atlas. Biển Đông is
  labelled East Sea, the name Vietnam uses in English; it is also known internationally as
  the South China Sea.
- Typeface: Be Vietnam Pro, SIL Open Font License 1.1 (see `fonts/OFL.txt`).
