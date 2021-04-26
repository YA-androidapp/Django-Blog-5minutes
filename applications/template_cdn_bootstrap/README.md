# Template CDN Bootstrap

This is a simple  Django template that uses bootstrap from a CND


## Usage

Add `template_cdn_bootstrap` to your `INSTALLED_APPS` in your django `settings.py` file

Also if you want to see as an index page add

```python
path(
    '',
    include('template_cdn_bootstrap.urls')
    
)
```

To your `urls.py` file under the `urlpattenrs` list.
