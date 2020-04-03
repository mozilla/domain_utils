from domain_utils import get_ps_plus_1

def test_get_ps_plus_one_cloudfront():
    result = get_ps_plus_1('https://my.domain.cloudfront.net')
    assert result == 'domain.cloudfront.net'


def test_get_ps_plus_one_no_https():
    result = get_ps_plus_1('my.domain.cloudfront.net')
    assert result == 'domain.cloudfront.net'


def test_get_ps_plus_one_on_about_blank():
    result = get_ps_plus_1('about:blank')
    assert result == ''


def test_get_ps_plus_one_on_relative_url():
    result = get_ps_plus_1('/my/path/is.html')
    assert result == ''


def test_get_ps_plus_1_on_vanilla_public_suffix():
    assert get_ps_plus_1('http://www.google.com') == 'google.com'


def test_get_ps_plus_1_on_exotic_public_suffix():
    assert get_ps_plus_1('http://foo.bar.website.apartments') == 'website.apartments'


def test_get_ps_plus_1_on_data_url():
    assert get_ps_plus_1("data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAA") == ''


def test_get_ps_plus_1_on_fbsbx_example():
    # apps.fbsbx.com is on the public sufix list (Apr 2, 2020)
    assert get_ps_plus_1('http://foo.blah.apps.fbsbx.com') == 'blah.apps.fbsbx.com'
    assert get_ps_plus_1('http://foo.blah.www.fbsbx.com') == 'fbsbx.com'


def test_get_ps_plus_1_on_ip_addresses():
    assert get_ps_plus_1('http://192.168.1.1') == '192.168.1.1'
    assert get_ps_plus_1('http://127.0.0.1/foo.html') == '127.0.0.1'


def test_get_ps_plus_1_on_url_with_port():
    url = 'http://my.example.com:8080/path/to/webapp.htm?aced=1'
    result = get_ps_plus_1(url)
    assert result == 'example.com'
