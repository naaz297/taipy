# Copyright 2022 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

from taipy.gui import Gui


def test_tree_md(gui: Gui, helpers):
    gui._bind_var_val("value", "Item 1")
    md_string = "<|{value}|tree|lov=Item 1;Item 2;Item 3|>"
    expected_list = [
        "<TreeView",
        'defaultLov="[&quot;Item 1&quot;, &quot;Item 2&quot;, &quot;Item 3&quot;]"',
        'defaultValue="[&quot;Item 1&quot;]"',
        'updateVarName="_TpLv_value"',
        "value={_TpLv_value}",
    ]
    helpers.test_control_md(gui, md_string, expected_list)


def test_tree_expanded_md_1(gui: Gui, helpers):
    gui._bind_var_val("value", "Item 1")
    md_string = "<|{value}|tree|lov=Item 1;Item 2;Item 3|not expanded|>"
    expected_list = [
        "<TreeView",
        'defaultLov="[&quot;Item 1&quot;, &quot;Item 2&quot;, &quot;Item 3&quot;]"',
        'defaultValue="[&quot;Item 1&quot;]"',
        'updateVarName="_TpLv_value"',
        "value={_TpLv_value}",
        "expanded={false}",
    ]
    helpers.test_control_md(gui, md_string, expected_list)


def test_tree_expanded_md_2(gui: Gui, helpers):
    gui._bind_var_val("value", "Item 1")
    gui._bind_var_val("expa", ["Item1"])
    md_string = "<|{value}|tree|lov=Item 1;Item 2;Item 3|expanded={expa}|>"
    expected_list = [
        "<TreeView",
        'defaultLov="[&quot;Item 1&quot;, &quot;Item 2&quot;, &quot;Item 3&quot;]"',
        'defaultValue="[&quot;Item 1&quot;]"',
        'updateVarName="_TpLv_value"',
        "value={_TpLv_value}",
        'defaultExpanded="[&quot;Item1&quot;]"',
        "expanded={expa}",
        'updateVars="expanded=expa"',
    ]
    helpers.test_control_md(gui, md_string, expected_list)


def test_tree_html_1(gui: Gui, helpers):
    gui._bind_var_val("value", "Item 1")
    html_string = '<taipy:tree lov="Item 1;Item 2;Item 3">{value}</taipy:tree>'
    expected_list = [
        "<TreeView",
        'defaultLov="[&quot;Item 1&quot;, &quot;Item 2&quot;, &quot;Item 3&quot;]"',
        'defaultValue="[&quot;Item 1&quot;]"',
        'updateVarName="_TpLv_value"',
        "value={_TpLv_value}",
    ]
    helpers.test_control_html(gui, html_string, expected_list)


def test_tree_html_2(gui: Gui, helpers):
    gui._bind_var_val("value", "Item 1")
    html_string = '<taipy:tree lov="Item 1;Item 2;Item 3" value="{value}" />'
    expected_list = [
        "<TreeView",
        'defaultLov="[&quot;Item 1&quot;, &quot;Item 2&quot;, &quot;Item 3&quot;]"',
        'defaultValue="[&quot;Item 1&quot;]"',
        'updateVarName="_TpLv_value"',
        "value={_TpLv_value}",
    ]
    helpers.test_control_html(gui, html_string, expected_list)
