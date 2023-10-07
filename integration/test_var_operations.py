"""Integration tests for var operations."""
from typing import Generator

import pytest
from selenium.webdriver.common.by import By

from dotreact.testing import AppHarness

# pyright: reportOptionalMemberAccess=false, reportGeneralTypeIssues=false, reportUnknownMemberType=false


def VarOperations():
    """App with var operations."""
    import dotreact as dr

    class VarOperationState(dr.State):
        int_var1: int = 10
        int_var2: int = 5
        int_var3: int = 7
        float_var1: float = 10.5
        float_var2: float = 5.5
        list1: list = [1, 2]
        list2: list = [3, 4]
        list3: list = ["first", "second", "third"]
        str_var1: str = "first"
        str_var2: str = "second"
        str_var3: str = "ThIrD"
        str_var4: str = "a long string"
        dict1: dict = {1: 2}
        dict2: dict = {3: 4}

        @dr.var
        def token(self) -> str:
            return self.get_token()

    app = dr.App(state=VarOperationState)

    @app.add_page
    def index():
        return dr.vstack(
            dr.input(id="token", value=VarOperationState.token, is_read_only=True),
            # INT INT
            dr.text(
                VarOperationState.int_var1 + VarOperationState.int_var2,
                id="int_add_int",
            ),
            dr.text(
                VarOperationState.int_var1 * VarOperationState.int_var2,
                id="int_mult_int",
            ),
            dr.text(
                VarOperationState.int_var1 - VarOperationState.int_var2,
                id="int_sub_int",
            ),
            dr.text(
                VarOperationState.int_var1**VarOperationState.int_var2,
                id="int_exp_int",
            ),
            dr.text(
                VarOperationState.int_var1 / VarOperationState.int_var2,
                id="int_div_int",
            ),
            dr.text(
                VarOperationState.int_var1 // VarOperationState.int_var3,
                id="int_floor_int",
            ),
            dr.text(
                VarOperationState.int_var1 % VarOperationState.int_var2,
                id="int_mod_int",
            ),
            dr.text(
                VarOperationState.int_var1 | VarOperationState.int_var2,
                id="int_or_int",
            ),
            dr.text(
                (VarOperationState.int_var1 > VarOperationState.int_var2).to_string(),
                id="int_gt_int",
            ),
            dr.text(
                (VarOperationState.int_var1 < VarOperationState.int_var2).to_string(),
                id="int_lt_int",
            ),
            dr.text(
                (VarOperationState.int_var1 >= VarOperationState.int_var2).to_string(),
                id="int_gte_int",
            ),
            dr.text(
                (VarOperationState.int_var1 <= VarOperationState.int_var2).to_string(),
                id="int_lte_int",
            ),
            dr.text(
                VarOperationState.int_var1 & VarOperationState.int_var2,
                id="int_and_int",
            ),
            dr.text(
                (VarOperationState.int_var1 | VarOperationState.int_var2).to_string(),
                id="int_or_int",
            ),
            dr.text(
                (VarOperationState.int_var1 == VarOperationState.int_var2).to_string(),
                id="int_eq_int",
            ),
            dr.text(
                (VarOperationState.int_var1 != VarOperationState.int_var2).to_string(),
                id="int_neq_int",
            ),
            # INT FLOAT OR FLOAT INT
            dr.text(
                VarOperationState.float_var1 + VarOperationState.int_var2,
                id="float_add_int",
            ),
            dr.text(
                VarOperationState.float_var1 * VarOperationState.int_var2,
                id="float_mult_int",
            ),
            dr.text(
                VarOperationState.float_var1 - VarOperationState.int_var2,
                id="float_sub_int",
            ),
            dr.text(
                VarOperationState.float_var1**VarOperationState.int_var2,
                id="float_exp_int",
            ),
            dr.text(
                VarOperationState.float_var1 / VarOperationState.int_var2,
                id="float_div_int",
            ),
            dr.text(
                VarOperationState.float_var1 // VarOperationState.int_var3,
                id="float_floor_int",
            ),
            dr.text(
                VarOperationState.float_var1 % VarOperationState.int_var2,
                id="float_mod_int",
            ),
            dr.text(
                (VarOperationState.float_var1 > VarOperationState.int_var2).to_string(),
                id="float_gt_int",
            ),
            dr.text(
                (VarOperationState.float_var1 < VarOperationState.int_var2).to_string(),
                id="float_lt_int",
            ),
            dr.text(
                (
                    VarOperationState.float_var1 >= VarOperationState.int_var2
                ).to_string(),
                id="float_gte_int",
            ),
            dr.text(
                (
                    VarOperationState.float_var1 <= VarOperationState.int_var2
                ).to_string(),
                id="float_lte_int",
            ),
            dr.text(
                (
                    VarOperationState.float_var1 == VarOperationState.int_var2
                ).to_string(),
                id="float_eq_int",
            ),
            dr.text(
                (
                    VarOperationState.float_var1 != VarOperationState.int_var2
                ).to_string(),
                id="float_neq_int",
            ),
            dr.text(
                (VarOperationState.float_var1 & VarOperationState.int_var2).to_string(),
                id="float_and_int",
            ),
            dr.text(
                (VarOperationState.float_var1 | VarOperationState.int_var2).to_string(),
                id="float_or_int",
            ),
            # INT, DICT
            dr.text(
                (VarOperationState.int_var1 | VarOperationState.dict1).to_string(),
                id="int_or_dict",
            ),
            dr.text(
                (VarOperationState.int_var1 & VarOperationState.dict1).to_string(),
                id="int_and_dict",
            ),
            dr.text(
                (VarOperationState.int_var1 == VarOperationState.dict1).to_string(),
                id="int_eq_dict",
            ),
            dr.text(
                (VarOperationState.int_var1 != VarOperationState.dict1).to_string(),
                id="int_neq_dict",
            ),
            # FLOAT FLOAT
            dr.text(
                VarOperationState.float_var1 + VarOperationState.float_var2,
                id="float_add_float",
            ),
            dr.text(
                VarOperationState.float_var1 * VarOperationState.float_var2,
                id="float_mult_float",
            ),
            dr.text(
                VarOperationState.float_var1 - VarOperationState.float_var2,
                id="float_sub_float",
            ),
            dr.text(
                VarOperationState.float_var1**VarOperationState.float_var2,
                id="float_exp_float",
            ),
            dr.text(
                VarOperationState.float_var1 / VarOperationState.float_var2,
                id="float_div_float",
            ),
            dr.text(
                VarOperationState.float_var1 // VarOperationState.float_var2,
                id="float_floor_float",
            ),
            dr.text(
                VarOperationState.float_var1 % VarOperationState.float_var2,
                id="float_mod_float",
            ),
            dr.text(
                (
                    VarOperationState.float_var1 > VarOperationState.float_var2
                ).to_string(),
                id="float_gt_float",
            ),
            dr.text(
                (
                    VarOperationState.float_var1 < VarOperationState.float_var2
                ).to_string(),
                id="float_lt_float",
            ),
            dr.text(
                (
                    VarOperationState.float_var1 >= VarOperationState.float_var2
                ).to_string(),
                id="float_gte_float",
            ),
            dr.text(
                (
                    VarOperationState.float_var1 <= VarOperationState.float_var2
                ).to_string(),
                id="float_lte_float",
            ),
            dr.text(
                (
                    VarOperationState.float_var1 == VarOperationState.float_var2
                ).to_string(),
                id="float_eq_float",
            ),
            dr.text(
                (
                    VarOperationState.float_var1 != VarOperationState.float_var2
                ).to_string(),
                id="float_neq_float",
            ),
            dr.text(
                (
                    VarOperationState.float_var1 & VarOperationState.float_var2
                ).to_string(),
                id="float_and_float",
            ),
            dr.text(
                (
                    VarOperationState.float_var1 | VarOperationState.float_var2
                ).to_string(),
                id="float_or_float",
            ),
            # FLOAT STR
            dr.text(
                VarOperationState.float_var1 | VarOperationState.str_var1,
                id="float_or_str",
            ),
            dr.text(
                VarOperationState.float_var1 & VarOperationState.str_var1,
                id="float_and_str",
            ),
            dr.text(
                (
                    VarOperationState.float_var1 == VarOperationState.str_var1
                ).to_string(),
                id="float_eq_str",
            ),
            dr.text(
                (
                    VarOperationState.float_var1 != VarOperationState.str_var1
                ).to_string(),
                id="float_neq_str",
            ),
            # FLOAT LIST
            dr.text(
                (VarOperationState.float_var1 | VarOperationState.list1).to_string(),
                id="float_or_list",
            ),
            dr.text(
                (VarOperationState.float_var1 & VarOperationState.list1).to_string(),
                id="float_and_list",
            ),
            dr.text(
                (VarOperationState.float_var1 == VarOperationState.list1).to_string(),
                id="float_eq_list",
            ),
            dr.text(
                (VarOperationState.float_var1 != VarOperationState.list1).to_string(),
                id="float_neq_list",
            ),
            # FLOAT DICT
            dr.text(
                (VarOperationState.float_var1 | VarOperationState.dict1).to_string(),
                id="float_or_dict",
            ),
            dr.text(
                (VarOperationState.float_var1 & VarOperationState.dict1).to_string(),
                id="float_and_dict",
            ),
            dr.text(
                (VarOperationState.float_var1 == VarOperationState.dict1).to_string(),
                id="float_eq_dict",
            ),
            dr.text(
                (VarOperationState.float_var1 != VarOperationState.dict1).to_string(),
                id="float_neq_dict",
            ),
            # STR STR
            dr.text(
                VarOperationState.str_var1 + VarOperationState.str_var2,
                id="str_add_str",
            ),
            dr.text(
                (VarOperationState.str_var1 > VarOperationState.str_var2).to_string(),
                id="str_gt_str",
            ),
            dr.text(
                (VarOperationState.str_var1 < VarOperationState.str_var2).to_string(),
                id="str_lt_str",
            ),
            dr.text(
                (VarOperationState.str_var1 >= VarOperationState.str_var2).to_string(),
                id="str_gte_str",
            ),
            dr.text(
                (VarOperationState.str_var1 <= VarOperationState.str_var2).to_string(),
                id="str_lte_str",
            ),
            dr.text(
                (
                    VarOperationState.float_var1 == VarOperationState.float_var2
                ).to_string(),
                id="str_eq_str",
            ),
            dr.text(
                (
                    VarOperationState.float_var1 != VarOperationState.float_var2
                ).to_string(),
                id="str_neq_str",
            ),
            dr.text(
                VarOperationState.str_var1.contains("fir").to_string(),
                id="str_contains",
            ),
            dr.text(
                VarOperationState.str_var1 | VarOperationState.str_var1, id="str_or_str"
            ),
            dr.text(
                VarOperationState.str_var1 & VarOperationState.str_var2,
                id="str_and_str",
            ),
            # STR, INT
            dr.text(
                VarOperationState.str_var1 * VarOperationState.int_var2,
                id="str_mult_int",
            ),
            dr.text(
                VarOperationState.str_var1 & VarOperationState.int_var2,
                id="str_and_int",
            ),
            dr.text(
                VarOperationState.str_var1 | VarOperationState.int_var2, id="str_or_int"
            ),
            dr.text(
                (VarOperationState.str_var1 == VarOperationState.int_var1).to_string(),
                id="str_eq_int",
            ),
            dr.text(
                (VarOperationState.str_var1 != VarOperationState.int_var1).to_string(),
                id="str_neq_int",
            ),
            # STR, LIST
            dr.text(
                VarOperationState.str_var1 | VarOperationState.list1, id="str_or_list"
            ),
            dr.text(
                (VarOperationState.str_var1 & VarOperationState.list1).to_string(),
                id="str_and_list",
            ),
            dr.text(
                (VarOperationState.str_var1 == VarOperationState.list1).to_string(),
                id="str_eq_list",
            ),
            dr.text(
                (VarOperationState.str_var1 != VarOperationState.list1).to_string(),
                id="str_neq_list",
            ),
            # STR, DICT
            dr.text(
                VarOperationState.str_var1 | VarOperationState.dict1, id="str_or_dict"
            ),
            dr.text(
                (VarOperationState.str_var1 & VarOperationState.dict1).to_string(),
                id="str_and_dict",
            ),
            dr.text(
                (VarOperationState.str_var1 == VarOperationState.dict1).to_string(),
                id="str_eq_dict",
            ),
            dr.text(
                (VarOperationState.str_var1 != VarOperationState.dict1).to_string(),
                id="str_neq_dict",
            ),
            # LIST, LIST
            dr.text(
                (VarOperationState.list1 + VarOperationState.list2).to_string(),
                id="list_add_list",
            ),
            dr.text(
                (VarOperationState.list1 & VarOperationState.list2).to_string(),
                id="list_and_list",
            ),
            dr.text(
                (VarOperationState.list1 | VarOperationState.list2).to_string(),
                id="list_or_list",
            ),
            dr.text(
                (VarOperationState.list1 > VarOperationState.list2).to_string(),
                id="list_gt_list",
            ),
            dr.text(
                (VarOperationState.list1 < VarOperationState.list2).to_string(),
                id="list_lt_list",
            ),
            dr.text(
                (VarOperationState.list1 >= VarOperationState.list2).to_string(),
                id="list_gte_list",
            ),
            dr.text(
                (VarOperationState.list1 <= VarOperationState.list2).to_string(),
                id="list_lte_list",
            ),
            dr.text(
                (VarOperationState.list1 == VarOperationState.list2).to_string(),
                id="list_eq_list",
            ),
            dr.text(
                (VarOperationState.list1 != VarOperationState.list2).to_string(),
                id="list_neq_list",
            ),
            dr.text(
                VarOperationState.list1.contains(1).to_string(), id="list_contains"
            ),
            dr.text(VarOperationState.list1.reverse().to_string(), id="list_reverse"),
            # LIST, INT
            dr.text(
                (VarOperationState.list1 * VarOperationState.int_var2).to_string(),
                id="list_mult_int",
            ),
            dr.text(
                (VarOperationState.list1 | VarOperationState.int_var1).to_string(),
                id="list_or_int",
            ),
            dr.text(
                (VarOperationState.list1 & VarOperationState.int_var1).to_string(),
                id="list_and_int",
            ),
            dr.text(
                (VarOperationState.list1 == VarOperationState.int_var1).to_string(),
                id="list_eq_int",
            ),
            dr.text(
                (VarOperationState.list1 != VarOperationState.int_var1).to_string(),
                id="list_neq_int",
            ),
            # LIST, DICT
            dr.text(
                (VarOperationState.list1 | VarOperationState.dict1).to_string(),
                id="list_or_dict",
            ),
            dr.text(
                (VarOperationState.list1 & VarOperationState.dict1).to_string(),
                id="list_and_dict",
            ),
            dr.text(
                (VarOperationState.list1 == VarOperationState.dict1).to_string(),
                id="list_eq_dict",
            ),
            dr.text(
                (VarOperationState.list1 != VarOperationState.dict1).to_string(),
                id="list_neq_dict",
            ),
            # DICT, DICT
            dr.text(
                (VarOperationState.dict1 | VarOperationState.dict2).to_string(),
                id="dict_or_dict",
            ),
            dr.text(
                (VarOperationState.dict1 & VarOperationState.dict2).to_string(),
                id="dict_and_dict",
            ),
            dr.text(
                (VarOperationState.dict1 == VarOperationState.dict2).to_string(),
                id="dict_eq_dict",
            ),
            dr.text(
                (VarOperationState.dict1 != VarOperationState.dict2).to_string(),
                id="dict_neq_dict",
            ),
            dr.text(
                VarOperationState.dict1.contains(1).to_string(), id="dict_contains"
            ),
            dr.text(VarOperationState.str_var3.lower(), id="str_lower"),
            dr.text(VarOperationState.str_var3.upper(), id="str_upper"),
            dr.text(VarOperationState.str_var4.split(" ").to_string(), id="str_split"),
            dr.text(VarOperationState.list3.join(""), id="list_join"),
            dr.text(VarOperationState.list3.join(","), id="list_join_comma"),
        )

    app.compile()


@pytest.fixture(scope="session")
def var_operations(tmp_path_factory) -> Generator[AppHarness, None, None]:
    """Start VarOperations app at tmp_path via AppHarness.

    Args:
        tmp_path_factory: pytest tmp_path_factory fixture

    Yields:
        running AppHarness instance
    """
    with AppHarness.create(
        root=tmp_path_factory.mktemp("var_operations"),
        app_source=VarOperations,  # type: ignore
    ) as harness:
        assert harness.app_instance is not None, "app is not running"
        yield harness


@pytest.fixture
def driver(var_operations: AppHarness):
    """Get an instance of the browser open to the var operations app.

    Args:
        var_operations: harness for VarOperations app

    Yields:
        WebDriver instance.
    """
    driver = var_operations.frontend()
    try:
        token_input = driver.find_element(By.ID, "token")
        assert token_input
        # wait for the backend connection to send the token
        token = var_operations.poll_for_value(token_input)
        assert token is not None

        yield driver
    finally:
        driver.quit()


def test_var_operations(driver, var_operations: AppHarness):
    """Test that the var operations produce the right results.

    Args:
        driver: selenium WebDriver open to the app
        var_operations: AppHarness for the var operations app
    """
    tests = [
        # int, int
        ("int_add_int", "15"),
        ("int_mult_int", "50"),
        ("int_sub_int", "5"),
        ("int_exp_int", "100000"),
        ("int_div_int", "2"),
        ("int_floor_int", "1"),
        ("int_mod_int", "0"),
        ("int_gt_int", "true"),
        ("int_lt_int", "false"),
        ("int_gte_int", "true"),
        ("int_lte_int", "false"),
        ("int_and_int", "5"),
        ("int_or_int", "10"),
        ("int_eq_int", "false"),
        ("int_neq_int", "true"),
        # int, float
        ("float_add_int", "15.5"),
        ("float_mult_int", "52.5"),
        ("float_sub_int", "5.5"),
        ("float_exp_int", "127628.15625"),
        ("float_div_int", "2.1"),
        ("float_floor_int", "1"),
        ("float_mod_int", "0.5"),
        ("float_gt_int", "true"),
        ("float_lt_int", "false"),
        ("float_gte_int", "true"),
        ("float_lte_int", "false"),
        ("float_eq_int", "false"),
        ("float_neq_int", "true"),
        ("float_and_int", "5"),
        ("float_or_int", "10.5"),
        # int, dict
        ("int_or_dict", "10"),
        ("int_and_dict", '{"1":2}'),
        ("int_eq_dict", "false"),
        ("int_neq_dict", "true"),
        # float, float
        ("float_add_float", "16"),
        ("float_mult_float", "57.75"),
        ("float_sub_float", "5"),
        ("float_exp_float", "413562.49323606625"),
        ("float_div_float", "1.9090909090909092"),
        ("float_floor_float", "1"),
        ("float_mod_float", "5"),
        ("float_gt_float", "true"),
        ("float_lt_float", "false"),
        ("float_gte_float", "true"),
        ("float_lte_float", "false"),
        ("float_eq_float", "false"),
        ("float_neq_float", "true"),
        ("float_and_float", "5.5"),
        ("float_or_float", "10.5"),
        # float, str
        ("float_or_str", "10.5"),
        ("float_and_str", "first"),
        ("float_eq_str", "false"),
        ("float_neq_str", "true"),
        # float, list
        ("float_or_list", "10.5"),
        ("float_and_list", "[1,2]"),
        ("float_eq_list", "false"),
        ("float_neq_list", "true"),
        # float, dict
        ("float_or_dict", "10.5"),
        ("float_and_dict", '{"1":2}'),
        ("float_eq_dict", "false"),
        ("float_neq_dict", "true"),
        # str, str
        ("str_add_str", "firstsecond"),
        ("str_gt_str", "false"),
        ("str_lt_str", "true"),
        ("str_gte_str", "false"),
        ("str_lte_str", "true"),
        ("str_eq_str", "false"),
        ("str_neq_str", "true"),
        ("str_and_str", "second"),
        ("str_or_str", "first"),
        ("str_contains", "true"),
        ("str_lower", "third"),
        ("str_upper", "THIRD"),
        ("str_split", '["a","long","string"]'),
        # str, int
        ("str_mult_int", "firstfirstfirstfirstfirst"),
        ("str_and_int", "5"),
        ("str_or_int", "first"),
        ("str_eq_int", "false"),
        ("str_neq_int", "true"),
        # str, list
        ("str_and_list", "[1,2]"),
        ("str_or_list", "first"),
        ("str_eq_list", "false"),
        ("str_neq_list", "true"),
        # str, dict
        ("str_or_dict", "first"),
        ("str_and_dict", '{"1":2}'),
        ("str_eq_dict", "false"),
        ("str_neq_dict", "true"),
        # list, list
        ("list_add_list", "[1,2,3,4]"),
        ("list_gt_list", "false"),
        ("list_lt_list", "true"),
        ("list_gte_list", "false"),
        ("list_lte_list", "true"),
        ("list_eq_list", "false"),
        ("list_neq_list", "true"),
        ("list_and_list", "[3,4]"),
        ("list_or_list", "[1,2]"),
        ("list_contains", "true"),
        ("list_reverse", "[2,1]"),
        ("list_join", "firstsecondthird"),
        ("list_join_comma", "first,second,third"),
        # list, int
        ("list_mult_int", "[1,2,1,2,1,2,1,2,1,2]"),
        ("list_or_int", "[1,2]"),
        ("list_and_int", "10"),
        ("list_eq_int", "false"),
        ("list_neq_int", "true"),
        # list, dict
        ("list_and_dict", '{"1":2}'),
        ("list_or_dict", "[1,2]"),
        ("list_eq_dict", "false"),
        ("list_neq_dict", "true"),
        # dict, dict
        ("dict_or_dict", '{"1":2}'),
        ("dict_and_dict", '{"3":4}'),
        ("dict_eq_dict", "false"),
        ("dict_neq_dict", "true"),
        ("dict_contains", "true"),
    ]

    for tag, expected in tests:
        assert driver.find_element(By.ID, tag).text == expected
