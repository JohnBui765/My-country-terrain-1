# Vietnam 63

A practice app for memorising Vietnam's 63 provincial-level units as they stood on
30 June 2025, the day before they were merged into 34. It works offline and can be
installed on a phone or laptop like a native app.

## Put it online (GitHub Pages)

1. Create a new public repository, for example `vietnam63`.
2. Upload everything in this folder, keeping the `fonts` and `icons` folders.
3. In the repository, open Settings, then Pages. Under "Build and deployment", choose
   "Deploy from a branch", branch `main`, folder `/ (root)`, and save.
4. After a minute the app is at `https://<your-username>.github.io/vietnam63/`.

## Install it

- **iPhone:** open the link in Safari, tap Share, then "Add to Home Screen".
- **Laptop:** open the link in Chrome or Edge and click the install icon in the address bar.

After the first visit it works without internet.

## Your progress

Progress is stored on each device separately. To move it, open Progress, then Details,
then "Back up progress", and use "Restore" on the other device.

## After editing any file

Change `VERSION` at the top of `sw.js` (for example to `vn63-v2`). Otherwise installed
copies keep showing the cached version.

## Sources and licences

- Boundaries: district boundaries from OCHA ROAP and the Government of Viet Nam (2020),
  licensed CC BY 3.0 IGO, obtained through geoBoundaries (www.geoboundaries.org,
  William & Mary geoLab). Districts were merged into the 63 provinces and simplified
  to about 0.7 km. Trường Sa is shown in an inset at 40% scale.
- Province list and codes: Quyết định 124/2004/QĐ-TTg. Regions: Nghị quyết 81/2023/QH15.
  Boundary and status changes: NQ 22/2003/QH11, NQ 15/2008/QH12, NQ 175/2024/QH15.
  2025 merger: NQ 202/2025/QH15. Capitals: Atlat Địa lí Việt Nam.
- Neighbouring countries: Natural Earth 1:50m (public domain), via world-atlas.
- Typeface: Be Vietnam Pro, SIL Open Font License 1.1 (see `fonts/OFL.txt`).
