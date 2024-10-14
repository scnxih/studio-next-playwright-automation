"""
Date: Feb 21, 2024
Description: This file referenced Cary related file.
"""
import math
import os
import time
from pytest_check import equal
from src.Pages.Common.tab_group import TabGroup
from src.Helper.helper import *

NODE_WIDTH_WITHOUT_PORTS_CONSTANT = 21  # Half of (NODE_WIDTH_AND_HEIGHT =42)
NODE_WIDTH_WITH_PORTS_CONSTANT = 28  # Half of (NODE_WIDTH_AND_HEIGHT =42) +  Half of  (PORT_WIDTH_AND_HEIGHT=13)
PORT_WIDTH_HEIGHT_CONSTANT = 6  # Half of  (PORT_WIDTH_AND_HEIGHT=13)


def select_node_in_flow_canvas(page, node_name):
    tab_group = TabGroup("", page)
    tab_group.click_tab_by_text(Helper.data_locale.FLOW)
    # Get the directory of the current script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Construct the relative path to functions.js
    functions_js_path = os.path.join(current_directory,
                                     "canvas_javascript.js")
    with open(functions_js_path, "r", encoding="utf-8") as js_file:
        js_functions = js_file.read()
        step_location = page.evaluate(js_functions + f'\nget_node_location("{node_name}")')
        x_coordinate = int(math.floor(float(step_location.split()[0])))
        y_coordinate = int(math.floor(float(step_location.split()[1])))

        execute_mouse_press_script = f"{js_functions}\nexecute_mouse_press({x_coordinate},{y_coordinate});"
        page.evaluate(execute_mouse_press_script)


def link_two_nodes_in_flow(page, node1_name, node2_name):
    # Get the directory of the current script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Construct the relative path to functions.js
    functions_js_path = os.path.join(current_directory,
                                     "canvas_javascript.js")
    with open(functions_js_path, "r", encoding="utf-8") as js_file:
        js_functions = js_file.read()
        #  node.Location gives the mid-value of the node, to reach the end of the node, we have to figure out first
        #  if the node has ports or not
        step1_info = page.evaluate(js_functions + f'\nget_node_shape_information("{node1_name}")')
        step1_shape_info = step1_info.upper()
        if step1_shape_info == "CIRCLE":
            flow_node_width_for_linking_nodes_in_canvas = NODE_WIDTH_WITHOUT_PORTS_CONSTANT
        else:
            flow_node_width_for_linking_nodes_in_canvas = NODE_WIDTH_WITH_PORTS_CONSTANT
        step1_location = page.evaluate(js_functions + f'\nget_node_location("{node1_name}")')

        # Needed to add padding for the coordinates in order for the drawing to work.  (December 11, 2023)
        # subtract 4 from x, and add 5 to y
        # The initial location is either the upper left corner of the node or center of node location. Unsure at this time
        x1_coordinate = int(math.floor(float(step1_location.split()[0]))) + flow_node_width_for_linking_nodes_in_canvas - 4
        y1_coordinate = int(math.floor(float(step1_location.split()[1]))) + 5

        step2_location = page.evaluate(js_functions + f'\nget_node_location("{node2_name}")')
        x2_coordinate = int(math.floor(float(step2_location.split()[0]))) - flow_node_width_for_linking_nodes_in_canvas - 4
        y2_coordinate = int(math.floor(float(step2_location.split()[1]))) + 5

        execute_mouse_move_script = (
            f"{js_functions}\nexecute_mouse_move({x1_coordinate}, " f"{y1_coordinate}, {x2_coordinate}, {y2_coordinate});"
        )

        page.evaluate(execute_mouse_move_script)
        time.sleep(1)
        select_node_in_flow_canvas(page, node2_name)


def open_context_menu_for_the_node_in_flow(page, node_name):
    """
    Definition handles opening the context menu for the selected step in the flow
    Args:
        page:
        node_name: name of the node whose context menu is being opened, The node name has unique to that open flow
    """
    # Get the directory of the current script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Construct the relative path to functions.js
    functions_js_path = os.path.join(current_directory,
                                     "canvas_javascript.js")
    with open(functions_js_path, "r", encoding="utf-8") as js_file:
        js_functions = js_file.read()
        step_location = page.evaluate(js_functions + f'\nget_node_location("{node_name}")')
        # logging.info(f"Node location '{step_location}'")
        x_coordinate = int(math.floor(float(step_location.split()[0])))
        y_coordinate = int(math.floor(float(step_location.split()[1])))
        execute_right_mouse_press_script = f"{js_functions}\nexecute_right_mouse_press({x_coordinate}, {y_coordinate});"
        page.evaluate(execute_right_mouse_press_script)

def click_on_canvas_in_flow(page):
    """
    Args:
        page:
    """
    # Get the directory of the current script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Construct the relative path to functions.js
    functions_js_path = os.path.join(current_directory,
                                     "canvas_javascript.js")
    with open(functions_js_path, "r", encoding="utf-8") as js_file:
        js_functions = js_file.read()
        x_coordinate = int(0)
        y_coordinate = int(0)
        execute_mouse_press_script = f"{js_functions}\nexecute_mouse_press({x_coordinate}, {y_coordinate});"
        page.evaluate(execute_mouse_press_script)

def open_context_menu_for_canvas_in_flow(page):
    """
    Definition handles opening the context menu for the background (canvas) in the flow
    Args:
        page:
    """
    # Get the directory of the current script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Construct the relative path to functions.js
    functions_js_path = os.path.join(current_directory,
                                     "canvas_javascript.js")
    with open(functions_js_path, "r", encoding="utf-8") as js_file:
        js_functions = js_file.read()
        x_coordinate = int(0)
        y_coordinate = int(0)
        execute_right_mouse_press_script = f"{js_functions}\nexecute_right_mouse_press({x_coordinate}, {y_coordinate});"
        page.evaluate(execute_right_mouse_press_script)


def select_input_port_node_in_flow(page, node_name):
    """
    Definition handles selecting the input port of the selected step in the flow
    Args:
        page:
        node_name: name of the node whose input port is selected [Note:- The node name has unique to that open flow]
    """

    # Get the directory of the current script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Construct the relative path to functions.js
    functions_js_path = os.path.join(current_directory,
                                     "canvas_javascript.js")
    with open(functions_js_path, "r", encoding="utf-8") as js_file:
        js_functions = js_file.read()
        step_location = page.evaluate(js_functions + f'\nget_node_location("{node_name}")')
        x_coordinate = int(math.floor(float(step_location.split()[0]))) - NODE_WIDTH_WITH_PORTS_CONSTANT
        y_coordinate = int(math.floor(float(step_location.split()[1])))
        execute_mouse_press_script = f"{js_functions}\nexecute_mouse_press({x_coordinate}, {y_coordinate});"
        page.evaluate(execute_mouse_press_script)


def select_output_port_node_in_flow(page, node_name):
    """
    Definition handles selecting the output port of the selected step in the flow
    Args:
        page:
        node_name: name of the node whose output port is selected [Note:- The node name has unique to that open flow]
    """
    # Get the directory of the current script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Construct the relative path to functions.js
    functions_js_path = os.path.join(current_directory,
                                     "canvas_javascript.js")
    with open(functions_js_path, "r", encoding="utf-8") as js_file:
        js_functions = js_file.read()
        step_location = page.evaluate(js_functions + f'\nget_node_location("{node_name}")')
        x_coordinate = int(math.floor(float(step_location.split()[0]))) + NODE_WIDTH_WITH_PORTS_CONSTANT
        y_coordinate = int(math.floor(float(step_location.split()[1])))
        execute_mouse_press_script = f"{js_functions}\nexecute_mouse_press({x_coordinate}, {y_coordinate});"
        page.evaluate(execute_mouse_press_script)


def open_context_menu_for_input_port_of_node_in_flow(page, port_number, node_name):
    """
    Definition handles opening the context menu of the input port of the selected step in the flow
    Args:
        page:
        port_number: The port number of the node in the flow, whose context is being opened, It starts with 1, 2, 3 etc.
        node_name: name of the node in the flow, whose input port is being selected, The node name has unique to that open flow
    """
    # Get the directory of the current script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Construct the relative path to functions.js
    functions_js_path = os.path.join(current_directory,
                                     "canvas_javascript.js")
    with open(functions_js_path, "r", encoding="utf-8") as js_file:
        js_functions = js_file.read()
        step_location = page.evaluate(js_functions + f'\nget_node_location("{node_name}")')
        # logging.info(f"Node location '{step_location}'")
        x_coordinate = int(math.floor(float(step_location.split()[0]))) - NODE_WIDTH_WITH_PORTS_CONSTANT
        if port_number == "1":
            input_port_coordinate = 0
        else:
            input_port_coordinate = PORT_WIDTH_HEIGHT_CONSTANT
        y_coordinate = int(math.floor(float(step_location.split()[1]))) + int(input_port_coordinate)
        execute_right_mouse_press_script = f"{js_functions}\nexecute_right_mouse_press({x_coordinate}, {y_coordinate});"
        page.evaluate(execute_right_mouse_press_script)


def open_context_menu_for_output_port_of_node_in_flow(page, port_number, node_name):
    """
    Definition handles opening the context menu of the output port of the selected step in the flow
    Args:
        page:
        port_number: The port number of the step in the flow, whose context is being opened, It starts with 1, 2, 3 etc.
        node_name: name of the node in the flow, whose input port is being selected, The node name has unique to that open flow
    """
    # Get the directory of the current script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Construct the relative path to functions.js
    functions_js_path = os.path.join(current_directory,
                                     "canvas_javascript.js")
    with open(functions_js_path, "r", encoding="utf-8") as js_file:
        js_functions = js_file.read()
        step_location = page.evaluate(js_functions + f'\nget_node_location("{node_name}")')
        # logging.info(f"Node location '{step_location}'")
        x_coordinate = int(math.floor(float(step_location.split()[0]))) + NODE_WIDTH_WITH_PORTS_CONSTANT
        if port_number == "1":
            output_port_coordinate = 0
        else:
            output_port_coordinate = PORT_WIDTH_HEIGHT_CONSTANT
        y_coordinate = int(math.floor(float(step_location.split()[1]))) + int(output_port_coordinate)
        execute_right_mouse_press_script = f"{js_functions}\nexecute_right_mouse_press({x_coordinate}, {y_coordinate});"
        page.evaluate(execute_right_mouse_press_script)
        execute_right_mouse_press_script = f"{js_functions}\nexecute_right_mouse_press({x_coordinate}, {y_coordinate});"
        page.evaluate(execute_right_mouse_press_script)


def validate_node_tooltip_of_the_node_in_flow(page, node_name, expected_node_tooltip):
    """
    Definition handles validating tool tip of the selected step in the flow
    Args:
        page:
        node_name: name of the node in the flow, whose tool tip is being validated, The step name has unique to that
                   open flow
        expected_node_tooltip: Expected tool tip text
    """
    # Get the directory of the current script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Construct the relative path to functions.js
    functions_js_path = os.path.join(current_directory,
                                     "canvas_javascript.js")
    with open(functions_js_path, "r", encoding="utf-8") as js_file:
        js_functions = js_file.read()
        actual_step_tooltip = page.evaluate(js_functions + f'\nget_node_tooltip("{node_name}")')
        equal(actual_step_tooltip, expected_node_tooltip)

def select_node_status_dialog_of_the_node_in_flow(page, node_name):
    """
    Definition handles selecting the status of the step in the flow
    Args:
        page:
        node_name: name of the step in the flow, whose status dialog is being selected, The step name has unique to the
                   open flow
    """
    # Get the directory of the current script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Construct the relative path to functions.js
    functions_js_path = os.path.join(current_directory,
                                     "canvas_javascript.js")
    with open(functions_js_path, "r", encoding="utf-8") as js_file:
        js_functions = js_file.read()
        flow_node_width_for_linking_nodes_in_canvas = NODE_WIDTH_WITHOUT_PORTS_CONSTANT
        step_location = page.evaluate(js_functions + f'\nget_node_location("{node_name}")')
        x_coordinate = int(math.floor(float(step_location.split()[0])))
        y_coordinate = int(math.floor(float(step_location.split()[1]))) + flow_node_width_for_linking_nodes_in_canvas
        execute_mouse_press_script = f"{js_functions}\nexecute_mouse_press({x_coordinate},{y_coordinate});"
        page.evaluate(execute_mouse_press_script)

def validate_the_flow_canvas_node_count_in_zero_state(page):
    """
    Definition handles validating the background(canvas) of the flow in zero state has no steps
    Args:
        page:
    """
    # Get the directory of the current script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Construct the relative path to functions.js
    functions_js_path = os.path.join(current_directory,
                                     "canvas_javascript.js")
    with open(functions_js_path, "r", encoding="utf-8") as js_file:
        js_functions = js_file.read()
        execute_mouse_press_script = f"{js_functions}\nget_node_count());"
        actual_node_count = page.evaluate(execute_mouse_press_script)
        equal(actual_node_count, 0)

def validate_count_of_nodes_in_flow(page, expected_node_count):
    """
    Definition handles validating the count of steps in the open flow
    Args:
        page:
        expected_node_count: Count of the nodes expected
    """
    # Get the directory of the current script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Construct the relative path to functions.js
    functions_js_path = os.path.join(current_directory,
                                     "canvas_javascript.js")
    with open(functions_js_path, "r", encoding="utf-8") as js_file:
        js_functions = js_file.read()
        execute_mouse_press_script = f"{js_functions}\nget_node_count();"
        actual_node_count = page.evaluate(execute_mouse_press_script)
        equal(actual_node_count, expected_node_count)

def validate_input_port_count_for_node_in_flow(page, node_name, expected_input_port_count):
    """
    Definition handles validating the input port count of selected step in the open flow
    Args:
        page:
        node_name: Name of the node whose input port count is being validated
        expected_input_port_count: Expected count of the input port
    """
    current_directory = os.path.dirname(os.path.abspath(__file__))
    functions_js_path = os.path.join(current_directory,
                                     "canvas_javascript.js")
    with open(functions_js_path, "r", encoding="utf-8") as js_file:
        js_functions = js_file.read()
        actual_input_port_count = page.evaluate(js_functions + f'\nget_input_port_count("{node_name}")')
        equal(int(actual_input_port_count), int(expected_input_port_count))

def validate_output_port_count_for_node_in_flow(page, node_name, expected_output_port_count):
    """
    Definition handles validating the output port count of selected step in the open flow
    Args:
        page:
        node_name: Name of the node whose output port count is being validated
        expected_output_port_count: Expected count of the output port
    """
    current_directory = os.path.dirname(os.path.abspath(__file__))
    functions_js_path = os.path.join(current_directory,
                                     "canvas_javascript.js")
    with open(functions_js_path, "r", encoding="utf-8") as js_file:
        js_functions = js_file.read()
        actual_output_port_count = page.evaluate(js_functions + f'\nget_output_port_count("{node_name}")')
        equal(int(actual_output_port_count), int(expected_output_port_count))


def validate_input_port_is_in_expanded_state_for_node_in_flow(page, node_name):
    """
    Definition handles validating the input port is in expanded state of selected step in the open flow
    Args:
        page:
        node_name: Name of the node whose input port  is being validated
    """
    current_directory = os.path.dirname(os.path.abspath(__file__))
    functions_js_path = os.path.join(current_directory,
                                     "canvas_javascript.js")
    with open(functions_js_path, "r", encoding="utf-8") as js_file:
        js_functions = js_file.read()
        actual_input_port_state = page.evaluate(js_functions + f'\nget_input_port_expanded_or_collapsed_state("{node_name}")')
        equal(int(actual_input_port_state), 1)

def validate_output_port_is_in_expanded_state_for_node_in_flow(page, node_name):
    """
    Definition handles validating the output port is in expanded state of selected step in the open flow
    Args:
        page:
        node_name: Name of the step whose output port  is being validated
    """
    current_directory = os.path.dirname(os.path.abspath(__file__))
    functions_js_path = os.path.join(current_directory,
                                     "canvas_javascript.js")
    with open(functions_js_path, "r", encoding="utf-8") as js_file:
        js_functions = js_file.read()
        actual_output_port_state = page.evaluate(js_functions + f'\nget_output_port_expanded_or_collapsed_state("{node_name}")')
        equal(int(actual_output_port_state), 1)

def validate_input_port_is_in_collapsed_state_for_node_in_flow(page, node_name):
    """
    Definition handles validating the input port is in collapsed state of selected step in the open flow
    Args:
        page:
        node_name: Name of the node whose input port  is being validated
    """
    current_directory = os.path.dirname(os.path.abspath(__file__))
    functions_js_path = os.path.join(current_directory,
                                     "canvas_javascript.js")
    with open(functions_js_path, "r", encoding="utf-8") as js_file:
        js_functions = js_file.read()
        actual_input_port_state = page.evaluate(js_functions + f'\nget_input_port_expanded_or_collapsed_state("{node_name}")')
        equal(int(actual_input_port_state), 0)

def validate_output_port_is_in_collapsed_state_for_node_in_flow(page, node_name):
    """
    Definition handles validating the output port is in collapsed state of selected step in the open flow
    Args:
        page:
        node_name: Name of the node whose output port  is being validated
    """
    current_directory = os.path.dirname(os.path.abspath(__file__))
    functions_js_path = os.path.join(current_directory,
                                     "canvas_javascript.js")
    with open(functions_js_path, "r", encoding="utf-8") as js_file:
        js_functions = js_file.read()
        actual_output_port_state = page.evaluate(js_functions + f'\nget_output_port_expanded_or_collapsed_state("{node_name}")')
        equal(int(actual_output_port_state), 0)

def validate_output_port_color_for_node_in_flow(page, port_number, node_name, expected_port_color):
    """
    Definition handles validating the output port color of selected step in the open flow
    Args:
        page:
        port_number: Number of the port whose color is being validated
        node_name: Name of the node whose input port  is being validated
        expected_port_color: Expected port color text
    """
    current_directory = os.path.dirname(os.path.abspath(__file__))
    functions_js_path = os.path.join(current_directory,
                                     "canvas_javascript.js")
    with open(functions_js_path, "r", encoding="utf-8") as js_file:
        js_functions = js_file.read()
        actual_port_color = page.evaluate(js_functions + f'\nget_output_port_color("{node_name}", "{port_number}")')
        equal(actual_port_color, expected_port_color)
