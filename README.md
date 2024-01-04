A project showing integration between [Dagre](https://github.com/dagrejs/dagre), [Dagre-D3](https://github.com/dagrejs/dagre-d3),
[D3](https://d3js.org), [Htmx](https://htmx.org), [Hyperscript](https://hyperscript.org), [FastAPI](https://fastapi.tiangolo.com), 
and [NetworkX](https://networkx.org/documentation/stable/index.html).

- Dagre is used to define the structure of the graph on the frontend. 
- Dagre-D3 is used to render the Dagre graph structure as an SVG.
- Any additional interactions with the graph is implemented using D3. 
- Htmx is used to handle click events on the nodes of the graph. When the user clicks on the node, the `hx-get` attribute is used to send a `GET` request to the FastAPI backend, 
`hx-trigger` is used to specify the `GET` request is sent when the user clicks the node,
`hx-target` and `hx-swap` is used to specify where and how the returned html is to be inserted into the DOM.
- The backend uses FastAPI to handle the incoming requests from the frontend
and Jinja2 templates are for rendering the html on the server before sending the returned html back to the frontend where the html response is handled by htmx;
hence why the FastAPI endpoints are configured to use Jinja2 templates and return html. 
- NetworkX is used to define the structure of the graph and exporting the structure of the graph as a dictionary of dictionaries.
- The backend then translates the dictionary of dictionaries to json and then sends the information about the graph structure to the frontend in the intial page load.
- With that said, asides from the initial page load, all other interactions between the backend and the frontend occur through Htmx attributes and html repsonses.
