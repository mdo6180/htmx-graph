var scriptTag = document.querySelector('script[src="/static/js/dag.js"]');

var graph_data = scriptTag.getAttribute('graph-data');
graph_data = graph_data.replace(/'/g, '"');
graph_data = JSON.parse(graph_data);

var nodes = graph_data.nodes;
var edges = graph_data.edges;

// Create a new directed graph 
var g = new dagre.graphlib.Graph({ directed: true, compound: false, multigraph: false });

// Set an object for the graph label
g.setGraph({});

// Add nodes to the graph. 
// Note: the order of when the nodes are declared does not determine the layout of the graph.
nodes.forEach(function(node) {
    g.setNode(
        node.id, 
        { 
            label: node.label, 
            width: node.width, 
            height: node.height, 
            endpoint: node.endpoint,
            progress_endpoint: node.progress_endpoint
        }
    );
});

// Add edges to the graph.
edges.forEach(function(edge) {
    g.setEdge(
        edge.source, 
        edge.target, 
        {
            name: edge.source, 
            arrowhead: "vee",
            endpoint: edge.endpoint
        }
    );
});

var svg = d3.select("svg");
var inner = svg.select("g");

// Set up zoom support
var zoom = d3.zoom().on("zoom", (event) => {
    inner.attr("transform", event.transform);
});
svg.call(zoom);

// Create the renderer
var render = new dagreD3.render();

// Run the renderer. This is what draws the final graph.
render(inner, g);

// select node containers
const node_container = inner.selectAll(".node");

// apply HTMX attributes to the entire node container
node_container.attr("hx-get", (v) => { return g.node(v).endpoint; })
                .attr("hx-trigger", "click")
                .attr("hx-target", "#graph")
                .attr("hx-swap", "outerHTML");

// apply SVG attributes to the rect element
const rect = inner.selectAll("rect");
rect.attr("rx", 10);
rect.attr("ry", 10);

const text = inner.selectAll(".node .label g text");
text.append("tspan")
    .attr("space", "preserve")
    .attr("dy", "1em")
    .attr("x", "1")
    .attr("hx-get", (v) => { return g.node(v).progress_endpoint; })
    .attr("hx-target", "this")
    .attr("hx-trigger", "load, every 1s")
    .attr("hx-swap", "innerHTML");

const arrowhead = inner.selectAll(".edgePath defs marker");
arrowhead.attr("fill", "#333");

const edge = inner.selectAll(".edgePath path.path");
edge.attr("stroke", "#333")
edge.attr("stroke-width", "1.5");
edge.attr("_", (e) => { 
    return `
    on load
        -- create global variables to store the edge's line and arrowhead
        set global ${g.edge(e).name}_path to me
        set global ${g.edge(e).name}_arrowhead to the next <marker/> 

        -- listen for a 'done' event, change the color of the line and arrowhead to the color specified in the data packet
        eventsource event_stream from ${g.edge(e).endpoint} 
            on done as string
                set ${g.edge(e).name}_path @stroke to it 
                set ${g.edge(e).name}_arrowhead @fill to it
            end
            on close as string
                log it
                call event_stream.close()
            end
        end
    end`; 
});

var initialScale = 1;

// Center the graph horizontally in the svg container
// Question: what happens if the width of the svg container is smaller than the width of the graph?
svg.call(zoom.transform, d3.zoomIdentity.translate((svg.attr("width") - g.graph().width * initialScale) / 2, 20).scale(initialScale));

// Center the graph vertically in the svg container by shrinking the height of the svg container
// svg.attr('height', g.graph().height * initialScale + 40);