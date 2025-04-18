from string import Template

from config import BASE_URL, TEMPLATES_DIR

sitemap_xml = f"""<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
<url>
<loc>{BASE_URL}</loc>
<lastmod>2025-04-18</lastmod>
<changefreq>monthly</changefreq>
<priority>1</priority>
</url>
</urlset>"""


robots_txt = "User-agent: *\nDisallow: /"

mainpage_html = Template((TEMPLATES_DIR / "main.html").read_text())
error_404_html = (TEMPLATES_DIR / "404.html").read_text()
error_500_html = (TEMPLATES_DIR / "500.html").read_text()
