# Usero PR checks demo

A one-page static site that [Usero PR checks](https://github.com/usero-feedback/pr-checks) measures on every pull
request.

- [`.github/workflows/pr.yml`](.github/workflows/pr.yml) checks out main and the pull request, serves each build on its own
  local port inside the job, and runs the action with the PR build as `head-url` and main as `base-url`. The browser applies
  the mobile network and CPU throttling, so the local pages load like they would on a phone.
- [Pull requests](https://github.com/usero-feedback/pr-checks-demo/pulls?q=is%3Apr) show the comments it posts: one PR
  swaps the hero image for a heavier one and gets flagged as an LCP regression, another changes nothing that affects loading
  and reports no significant change.

For a site with preview deployments (Cloudflare, Vercel, Netlify), point `head-url` and `base-url` at the previews instead.
The action's README has a recipe for each.
