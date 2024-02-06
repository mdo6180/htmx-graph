from whitehouse.default import *
from whitehouse.utils import format_html
from whitehouse.custom import Template
from whitehouse.base import Component


class IndexTemplate(Template):
    def __init__(
        self, 
        children: Union[str, 'Component', List['Component']], 
        json_data,
        headers:  Union[str, 'Component', List['Component']] = [], 
    ):
        super().__init__(
            html([
                head([
                    title("DAG"),
                    meta({"charset": "utf-8"}),
                    link({"rel": "stylesheet", "type": "text/css", "href": "/static/css/home.css"}),
                    link({"rel": "icon", "type": "image/x-icon", "href": "/static/img/favicon.ico"}),
                    script("", {"src": "/static/js/htmx.min.js", "type": "text/javascript"}),
                    script("", {"src": "/static/js/_hyperscript_w9y.min.js", "type": "text/javascript"}),
                    script("", {"src": "/static/js/d3.v6.min.js", "type": "text/javascript"}),
                    script("", {"src": "/static/js/dagre.min.js", "type": "text/javascript"}),
                    script("", {"src": "/static/js/dagre-d3.min.js", "type": "text/javascript"}),
                    link({"rel": "stylesheet", "type": "text/css", "href": "/static/css/index.css"}),
                    *headers
                ]),
                body([
                    div([
                            a([img({"src": "/static/img/dag-black.svg", "alt": "home"})], {"href": "/", "class": "dag-icon"}),
                            h1("Anacostia Pipeline", {"class": "title"}),
                            div([
                                button("Nodes", {"class": "dropbtn"}),
                                div([
                                    div(node["label"], 
                                        {"hx-get": node["endpoint"], "hx-target": "#page_content", "hx-swap": "innerHTML", "hx-trigger": "click"}
                                    ) for node in json_data["nodes"] 
                                ], {"class": "dropdown-content"})
                            ], {"class": "dropdown"}),
                        ], {"class": "toolbar"}),
                    div([*children], {"id": "page_content"})
                ])
            ])
        )