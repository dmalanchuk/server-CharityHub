from string import Template

_cache_txt = {}


def get_email_text(code: str, path: str):
        if path not in _cache_txt:
            with open(path, "r", encoding="utf-8") as f:
                _cache_txt[path] = f.read()

        temp_str = _cache_txt[path].replace("{{ code }}", "${code}")
        template = Template(temp_str)

        return template.safe_substitute(code=code)

