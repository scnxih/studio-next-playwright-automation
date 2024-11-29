// get node coordinates
function get_node_location(node_name) {
    // Perform some operations to compute the value
    const elements = document.getElementsByClassName('sas_styles-Diagram_diagram-component');
    const nodeDataArray = elements[0].robot.diagram.model.nodeDataArray;
    const filteredNodes = nodeDataArray.filter(n => n.name === node_name);
    return filteredNodes[0].location;
}
////get input port coordinates
////added by Alice on 2024/11/28
//function get_input_port_location(node_name, input_port_number) {
//    // Perform some operations to compute the value
//    const elements = document.getElementsByClassName('sas_styles-Diagram_diagram-component');
//    const nodeDataArray = elements[0].robot.diagram.model.nodeDataArray;
//    const filteredNodes = nodeDataArray.filter(n => n.name === node_name);
//    const input_port_info = filteredNodes[0].inPorts[input_port_number]
//    return input_port_info.location;
//}
// do the select the node action
function execute_mouse_press(x_coordinate, y_coordinate) {
    document.getElementsByClassName('sas_styles-Diagram_diagram-component')[0].robot.mousePressAction(x_coordinate, y_coordinate);
}

//get node shape information
function get_node_shape_information(node_name) {
    const node_shape_info = document.getElementsByClassName('sas_styles-Diagram_diagram-component')[0].robot.diagram.model.nodeDataArray.filter(n=> n.name == node_name)[0].category;
    return node_shape_info;
}

// do the mouse move action from one node to another (linking)
function execute_mouse_move(x1_coordinate, y1_coordinate, x2_coordinate, y2_coordinate) {
    document.getElementsByClassName('sas_styles-Diagram_diagram-component')[0].robot.mouseMoveAction(x1_coordinate, y1_coordinate, x2_coordinate, y2_coordinate);
}

// do the right mouse click action to open context menu
function execute_right_mouse_press(x_coordinate, y_coordinate) {
    document.getElementsByClassName('sas_styles-Diagram_diagram-component')[0].robot.mouseDown(x_coordinate,y_coordinate,0,{button:2});
    document.getElementsByClassName('sas_styles-Diagram_diagram-component')[0].robot.mouseUp(x_coordinate,y_coordinate,100,{button:2});
}

//return node status of the node in the flow
function get_node_tooltip(node_name) {
    const node_status = document.getElementsByClassName('sas_styles-Diagram_diagram-component')[0].robot.diagram.model.nodeDataArray.filter(n=> n.name == node_name)[0].tooltip;
    return node_status;
}

//return the node count in the flow
function get_node_count(){
    const  node_count = document.getElementsByClassName('sas_styles-Diagram_diagram-component')[0].robot.diagram.model.nodeDataArray.length;
    return node_count;
}

//return the output port count of the specific step
function get_output_port_count(node_name){
    const output_port_count = document.getElementsByClassName('sas_styles-Diagram_diagram-component')[0].robot.diagram.model.nodeDataArray.filter(n=> n.name == node_name)[0].outPorts.ports.length;
    return output_port_count;
}

//return the input port count of the specific step
function get_input_port_count(node_name){
    const input_port_count = document.getElementsByClassName('sas_styles-Diagram_diagram-component')[0].robot.diagram.model.nodeDataArray.filter(n=> n.name == node_name)[0].inPorts.ports.length;
    return input_port_count;
}

//return input port is in expanded state or collapsed state (expanded state = true; collapsed state=false)
function get_input_port_expanded_or_collapsed_state(node_name){
    const input_port_expanded_or_collapsed_state = document.getElementsByClassName('sas_styles-Diagram_diagram-component')[0].robot.diagram.model.nodeDataArray.filter(n=> n.name == node_name)[0].inPorts.expanded;
    return input_port_expanded_or_collapsed_state;
}

//return output port is in expanded state or collapsed state (expanded state = true; collapsed state=false)
function get_output_port_expanded_or_collapsed_state(node_name){
    const output_port_expanded_or_collapsed_state = document.getElementsByClassName('sas_styles-Diagram_diagram-component')[0].robot.diagram.model.nodeDataArray.filter(n=> n.name == node_name)[0].outPorts.expanded;
    return output_port_expanded_or_collapsed_state;
}

//return output port color is blue(#addaff) or (#ffeaad) or transparent
function get_output_port_color(node_name, output_port_number){
    const output_port_color = document.getElementsByClassName('sas_styles-Diagram_diagram-component')[0].robot.diagram.model.nodeDataArray.filter(n=> n.name == node_name)[0].outPorts.ports[output_port_number].palette.body;
    return output_port_color;
}
