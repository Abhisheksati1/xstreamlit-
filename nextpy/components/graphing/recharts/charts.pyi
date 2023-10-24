"""Stub file for charts.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, List, Literal, Optional, Union, overload
from nextpy.components.component import Component
from nextpy.components.graphing.recharts.recharts import RechartsCharts
from nextpy.core.vars import Var, BaseVar, ComputedVar
from nextpy.core.event import EventHandler, EventChain, EventSpec

class ChartBase(RechartsCharts):
    @overload
    @classmethod
    def create(cls, *children, data: Optional[Union[Var[List[Dict[str, Any]]], List[Dict[str, Any]]]] = None, sync_id: Optional[Union[Var[str], str]] = None, sync_method: Optional[Union[Var[Literal["index", "value"]], Literal["index", "value"]]] = None, width: Optional[Union[Var[Union[str, int]], Union[str, int]]] = None, height: Optional[Union[Var[Union[str, int]], Union[str, int]]] = None, layout: Optional[Union[Var[Literal["horizontal", "vertical"]], Literal["horizontal", "vertical"]]] = None, margin: Optional[Union[Var[Dict[str, Any]], Dict[str, Any]]] = None, stack_offset: Optional[Union[Var[Literal["expand", "none", "wiggle", "silhouette"]], Literal["expand", "none", "wiggle", "silhouette"]]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "ChartBase":  # type: ignore
        """Create a chart component.

        Args:
            *children: The children of the chart component.
            data: The source data, in which each element is an object.
            sync_id: If any two categorical charts(xt.line_chart, xt.area_chart, xt.bar_chart, xt.composed_chart) have the same sync_id, these two charts can sync the position GraphingTooltip, and the start_index, end_index of Brush.
            sync_method: When sync_id is provided, allows customisation of how the charts will synchronize GraphingTooltips and brushes. Using 'index' (default setting), other charts will reuse current datum's index within the data array. In cases where data does not have the same length, this might yield unexpected results. In that case use 'value' which will try to match other charts values, or a fully custom function which will receive tick, data as argument and should return an index. 'index' | 'value' | function
            width: The width of chart container. String or Integer
            height: The height of chart container.
            layout: The layout of area in the chart. 'horizontal' | 'vertical'
            margin: The sizes of whitespace around the chart.
            stack_offset: The type of offset function used to generate the lower and upper values in the series array. The four types are built-in offsets in d3-shape. 'expand' | 'none' | 'wiggle' | 'silhouette'
            **props: The properties of the chart component.

        Returns:
            The chart component wrapped in a responsive container.
        """
        ...

class AreaChart(ChartBase):
    @overload
    @classmethod
    def create(cls, *children, base_value: Optional[Union[Var[Union[int, Literal["dataMin", "dataMax", "auto"]]], Union[int, Literal["dataMin", "dataMax", "auto"]]]] = None, stack_offset: Optional[Union[Var[Literal["expand", "none", "wiggle", "silhouette"]], Literal["expand", "none", "wiggle", "silhouette"]]] = None, valid_children: Optional[List[str]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "AreaChart":  # type: ignore
        """Create a chart component.

        Args:
            *children: The children of the chart component.
            base_value: The base value of area. Number | 'dataMin' | 'dataMax' | 'auto'
            stack_offset: The type of offset function used to generate the lower and upper values in the series array. The four types are built-in offsets in d3-shape.
            valid_children: Valid children components
            **props: The properties of the chart component.

        Returns:
            The chart component wrapped in a responsive container.
        """
        ...

class BarChart(ChartBase):
    @overload
    @classmethod
    def create(cls, *children, bar_category_gap: Optional[Union[Var[Union[str, int]], Union[str, int]]] = None, bar_gap: Optional[Union[Var[Union[str, int]], Union[str, int]]] = None, bar_size: Optional[Union[Var[int], int]] = None, max_bar_size: Optional[Union[Var[int], int]] = None, stack_offset: Optional[Union[Var[Literal["expand", "none", "wiggle", "silhouette"]], Literal["expand", "none", "wiggle", "silhouette"]]] = None, reverse_stack_order: Optional[Union[Var[bool], bool]] = None, valid_children: Optional[List[str]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "BarChart":  # type: ignore
        """Create a chart component.

        Args:
            *children: The children of the chart component.
            bar_category_gap: The gap between two bar categories, which can be a percent value or a fixed value. Percentage | Number
            bar_gap: The gap between two bars in the same category, which can be a percent value or a fixed value. Percentage | Number
            bar_size: The width of all the bars in the chart. Number
            max_bar_size: The maximum width of all the bars in a horizontal BarChart, or maximum height in a vertical BarChart.
            stack_offset: The type of offset function used to generate the lower and upper values in the series array. The four types are built-in offsets in d3-shape.
            reverse_stack_order: If false set, stacked items will be rendered left to right. If true set, stacked items will be rendered right to left. (Render direction affects SVG layering, not x position.)
            valid_children: Valid children components
            **props: The properties of the chart component.

        Returns:
            The chart component wrapped in a responsive container.
        """
        ...

class LineChart(ChartBase):
    @overload
    @classmethod
    def create(cls, *children, valid_children: Optional[List[str]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "LineChart":  # type: ignore
        """Create a chart component.

        Args:
            *children: The children of the chart component.
            valid_children: Valid children components
            **props: The properties of the chart component.

        Returns:
            The chart component wrapped in a responsive container.
        """
        ...

class ComposedChart(ChartBase):
    @overload
    @classmethod
    def create(cls, *children, base_value: Optional[Union[Var[Union[int, Literal["dataMin", "dataMax", "auto"]]], Union[int, Literal["dataMin", "dataMax", "auto"]]]] = None, bar_category_gap: Optional[Union[Var[Union[str, int]], Union[str, int]]] = None, bar_gap: Optional[Union[Var[int], int]] = None, bar_size: Optional[Union[Var[int], int]] = None, reverse_stack_order: Optional[Union[Var[bool], bool]] = None, valid_children: Optional[List[str]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "ComposedChart":  # type: ignore
        """Create a chart component.

        Args:
            *children: The children of the chart component.
            base_value: The base value of area. Number | 'dataMin' | 'dataMax' | 'auto'
            bar_category_gap: The gap between two bar categories, which can be a percent value or a fixed value. Percentage | Number
            bar_gap: The gap between two bars in the same category, which can be a percent value or a fixed value. Percentage | Number
            bar_size: The width of all the bars in the chart. Number
            reverse_stack_order: If false set, stacked items will be rendered left to right. If true set, stacked items will be rendered right to left. (Render direction affects SVG layering, not x position.)
            valid_children: Valid children components
            **props: The properties of the chart component.

        Returns:
            The chart component wrapped in a responsive container.
        """
        ...

class PieChart(ChartBase):
    @overload
    @classmethod
    def create(cls, *children, valid_children: Optional[List[str]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "PieChart":  # type: ignore
        """Create a chart component.

        Args:
            *children: The children of the chart component.
            valid_children: Valid children components
            **props: The properties of the chart component.

        Returns:
            The chart component wrapped in a responsive container.
        """
        ...

class RadarChart(ChartBase):
    @overload
    @classmethod
    def create(cls, *children, cx: Optional[Union[Var[Union[int, str]], Union[int, str]]] = None, cy: Optional[Union[Var[Union[int, str]], Union[int, str]]] = None, start_angle: Optional[Union[Var[int], int]] = None, end_angle: Optional[Union[Var[int], int]] = None, inner_radius: Optional[Union[Var[Union[int, str]], Union[int, str]]] = None, outer_radius: Optional[Union[Var[Union[int, str]], Union[int, str]]] = None, valid_children: Optional[List[str]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "RadarChart":  # type: ignore
        """Create a chart component.

        Args:
            *children: The children of the chart component.
            cx: The The x-coordinate of center. If set a percentage, the final value is obtained by multiplying the percentage of width. Number | Percentage
            cy: The The y-coordinate of center. If set a percentage, the final value is obtained by multiplying the percentage of height. Number | Percentage
            start_angle: The angle of first radial direction line.
            end_angle: The angle of last point in the circle which should be startAngle - 360 or startAngle + 360. We'll calculate the direction of chart by 'startAngle' and 'endAngle'.
            inner_radius: The inner radius of first circle grid. If set a percentage, the final value is obtained by multiplying the percentage of maxRadius which is calculated by the width, height, cx, cy. Number | Percentage
            outer_radius: The outer radius of last circle grid. If set a percentage, the final value is obtained by multiplying the percentage of maxRadius which is calculated by the width, height, cx, cy. Number | Percentage
            valid_children: Valid children components
            **props: The properties of the chart component.

        Returns:
            The chart component wrapped in a responsive container.
        """
        ...

class RadialBarChart(ChartBase):
    @overload
    @classmethod
    def create(cls, *children, cx: Optional[Union[Var[Union[int, str]], Union[int, str]]] = None, cy: Optional[Union[Var[Union[int, str]], Union[int, str]]] = None, start_angle: Optional[Union[Var[int], int]] = None, end_angle: Optional[Union[Var[int], int]] = None, inner_radius: Optional[Union[Var[Union[int, str]], Union[int, str]]] = None, outer_radius: Optional[Union[Var[Union[int, str]], Union[int, str]]] = None, bar_category_gap: Optional[Union[Var[Union[int, str]], Union[int, str]]] = None, bar_gap: Optional[Union[Var[str], str]] = None, bar_size: Optional[Union[Var[int], int]] = None, valid_children: Optional[List[str]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "RadialBarChart":  # type: ignore
        """Create a chart component.

        Args:
            *children: The children of the chart component.
            cx: The The x-coordinate of center. If set a percentage, the final value is obtained by multiplying the percentage of width. Number | Percentage
            cy: The The y-coordinate of center. If set a percentage, the final value is obtained by multiplying the percentage of height. Number | Percentage
            start_angle: The angle of first radial direction line.
            end_angle: The angle of last point in the circle which should be startAngle - 360 or startAngle + 360. We'll calculate the direction of chart by 'startAngle' and 'endAngle'.
            inner_radius: The inner radius of first circle grid. If set a percentage, the final value is obtained by multiplying the percentage of maxRadius which is calculated by the width, height, cx, cy. Number | Percentage
            outer_radius: The outer radius of last circle grid. If set a percentage, the final value is obtained by multiplying the percentage of maxRadius which is calculated by the width, height, cx, cy. Number | Percentage
            bar_category_gap: The gap between two bar categories, which can be a percent value or a fixed value. Percentage | Number
            bar_gap: The gap between two bars in the same category, which can be a percent value or a fixed value. Percentage | Number
            bar_size: The size of each bar. If the barSize is not specified, the size of bar will be calculated by the barCategoryGap, barGap and the quantity of bar groups.
            valid_children: Valid children components
            **props: The properties of the chart component.

        Returns:
            The chart component wrapped in a responsive container.
        """
        ...

class ScatterChart(ChartBase):
    @overload
    @classmethod
    def create(cls, *children, valid_children: Optional[List[str]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "ScatterChart":  # type: ignore
        """Create a chart component.

        Args:
            *children: The children of the chart component.
            valid_children: Valid children components
            **props: The properties of the chart component.

        Returns:
            The chart component wrapped in a responsive container.
        """
        ...

class FunnelChart(RechartsCharts):
    @overload
    @classmethod
    def create(cls, *children, data: Optional[Union[Var[List[Dict[str, Any]]], List[Dict[str, Any]]]] = None, sync_id: Optional[Union[Var[str], str]] = None, sync_method: Optional[Union[Var[str], str]] = None, width: Optional[Union[Var[Union[str, int]], Union[str, int]]] = None, height: Optional[Union[Var[Union[str, int]], Union[str, int]]] = None, layout: Optional[Union[Var[str], str]] = None, margin: Optional[Union[Var[Dict[str, Any]], Dict[str, Any]]] = None, stack_offset: Optional[Union[Var[Literal["expand", "none", "wiggle", "silhouette"]], Literal["expand", "none", "wiggle", "silhouette"]]] = None, valid_children: Optional[List[str]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "FunnelChart":  # type: ignore
        """Create the component.

        Args:
            *children: The children of the component.
            data: The source data, in which each element is an object.
            sync_id: If any two categorical charts(xt.line_chart, xt.area_chart, xt.bar_chart, xt.composed_chart) have the same sync_id, these two charts can sync the position GraphingTooltip, and the start_index, end_index of Brush.
            sync_method: When sync_id is provided, allows customisation of how the charts will synchronize GraphingTooltips and brushes. Using 'index' (default setting), other charts will reuse current datum's index within the data array. In cases where data does not have the same length, this might yield unexpected results. In that case use 'value' which will try to match other charts values, or a fully custom function which will receive tick, data as argument and should return an index. 'index' | 'value' | function
            width: The width of chart container. String or Integer
            height: The height of chart container.
            layout: The layout of bars in the chart. centeric
            margin: The sizes of whitespace around the chart.
            stack_offset: The type of offset function used to generate the lower and upper values in the series array. The four types are built-in offsets in d3-shape. 'expand' | 'none' | 'wiggle' | 'silhouette'
            valid_children: Valid children components
            **props: The props of the component.

        Returns:
            The component.

        Raises:
            TypeError: If an invalid child is passed.
        """
        ...

class Treemap(RechartsCharts):
    @overload
    @classmethod
    def create(cls, *children, width: Optional[Union[Var[Union[str, int]], Union[str, int]]] = None, height: Optional[Union[Var[Union[str, int]], Union[str, int]]] = None, data: Optional[Union[Var[List[Dict[str, Any]]], List[Dict[str, Any]]]] = None, data_key: Optional[Union[Var[Union[str, int]], Union[str, int]]] = None, aspect_ratio: Optional[Union[Var[int], int]] = None, is_animation_active: Optional[Union[Var[bool], bool]] = None, animation_begin: Optional[Union[Var[int], int]] = None, animation_duration: Optional[Union[Var[int], int]] = None, animation_easing: Optional[Union[Var[Literal["ease", "ease-in", "ease-out", "ease-in-out", "linear"]], Literal["ease", "ease-in", "ease-out", "ease-in-out", "linear"]]] = None, on_blur: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_context_menu: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_double_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_focus: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_scroll: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_unmount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "Treemap":  # type: ignore
        """Create a chart component.

        Args:
            *children: The children of the chart component.
            width: The width of chart container. String or Integer
            height: The height of chart container.
            data: data of treemap. Array
            data_key: The key of a group of data which should be unique in a treemap. String | Number | Function
            aspect_ratio: The treemap will try to keep every single rectangle's aspect ratio near the aspectRatio given. Number
            is_animation_active: If set false, animation of area will be disabled.
            animation_begin: Specifies when the animation should begin, the unit of this option is ms.
            animation_duration: Specifies the duration of animation, the unit of this option is ms.
            animation_easing: The type of easing function. 'ease' | 'ease-in' | 'ease-out' | 'ease-in-out' | 'linear'
            **props: The properties of the chart component.

        Returns:
            The Treemap component wrapped in a responsive container.
        """
        ...