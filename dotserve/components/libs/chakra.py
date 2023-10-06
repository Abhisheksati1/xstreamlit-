"""Components that are based on Chakra-UI."""

from dotserve.components.component import Component


class ChakraComponent(Component):
    """A component that wraps a Chakra component."""

    library = "@chakra-ui/react"
