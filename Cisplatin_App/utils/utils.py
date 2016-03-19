"""
General utilities that will be used throughout the site
"""

# A function for adding safe headers to a given response
def http_headers(response):
    # Add headers to avoid clickjacking
    response['X-Frame-Options'] = 'DENY'
    response['Content-Security-Policy'] = "frame-ancestors 'none'"

    # Stop any robots for indexing anything
    response['X-Robots-Tag'] = 'noindex'
    return response
