MOBILE OPTIMIZATION — what changed
==================================
1. Responsive CSS added to every page (breakpoints at 860px and 400px):
   - Multi-column grids collapse to 1 column (stats grid goes 4 -> 2 -> 1)
   - Headline sizes scale down fluidly (74px hero -> ~36-50px on phones)
   - Section/nav/footer padding tightened for small screens
   - Footer stacks and centers
2. Mobile hamburger menu: on screens under 860px the nav links tuck into
   a tap-to-open dropdown; the menu closes when you tap a link.
3. Custom illustrations added (in your cream/navy/orange palette) to the
   empty image slots: 3 on Home, 4 on Projects, 6 on Blogs. They are
   embedded in the files, so nothing external needs to load. To swap any
   of them for a real photo/screenshot later, open the page in your
   editor and use the image slot's Replace button.

HOW TO UPDATE YOUR REPO (from the GitHub app or web):
  Replace index.html, projects.html, blogs.html, tools.html, contact.html
  with the files in this folder (CNAME is unchanged, included for safety).
  Easiest on desktop web: open each file in the repo -> pencil icon ->
  paste new contents -> commit. Or upload all files at once via
  "Add file -> Upload files" on github.com (desktop site).
