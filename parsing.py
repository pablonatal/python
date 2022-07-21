proxy_url = "http://user:pass@proxy.yourproxy.org:8080"
proxy_support = urllib2.ProxyHandler({'http': proxy_url})
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)
src = urllib2.urlopen(url)