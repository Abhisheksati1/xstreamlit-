import { Fragment, useContext, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { Event, getAllLocalStorageItems, getRefValue, getRefValues, isTrue, preventDefault, refs, spreadArraysOrObjects, uploadFiles, useEventLoop } from "/utils/state"
import { ColorModeContext, EventLoopContext, initialEvents, StateContext } from "/utils/context.js"
import "focus-visible/dist/focus-visible"
import "gridjs/dist/theme/mermaid.css"
import { Box, Center, Container, Heading, Highlight, HStack, Image, Link, Menu, MenuButton, MenuDivider, MenuItem, MenuList, Modal, ModalBody, ModalContent, ModalHeader, ModalOverlay, Spacer, Table, Tbody, Td, Text, Th, Thead, Tr, VStack } from "@chakra-ui/react"
import { getEventURL } from "/utils/state.js"
import NextLink from "next/link"
import { InlineMath } from "react-katex"
import { Grid as DataTableGrid } from "gridjs-react"
import { Area as RechartsArea, Bar as RechartsBar, Line as RechartsLine, ResponsiveContainer as RechartsResponsiveContainer, XAxis as RechartsXAxis, YAxis as RechartsYAxis } from "recharts"
import dynamic from "next/dynamic"
import { HexColorPicker } from "react-colorful"
import { HamburgerIcon } from "@chakra-ui/icons"
import NextHead from "next/head"

const RechartsLineChart = dynamic(() => import('recharts').then((mod) => mod.LineChart), { ssr: false });
const RechartsAreaChart = dynamic(() => import('recharts').then((mod) => mod.AreaChart), { ssr: false });
const RechartsBarChart = dynamic(() => import('recharts').then((mod) => mod.BarChart), { ssr: false });


export default function Component() {
  const state = useContext(StateContext)
  const router = useRouter()
  const [ colorMode, toggleColorMode ] = useContext(ColorModeContext)
  const focusRef = useRef();
  
  // Main event loop.
  const [addEvents, connectError] = useContext(EventLoopContext)

  // Set focus to the specified element.
  useEffect(() => {
    if (focusRef.current) {
      focusRef.current.focus();
    }
  })

  // Route after the initial page hydration.
  useEffect(() => {
    const change_complete = () => addEvents(initialEvents())
    router.events.on('routeChangeComplete', change_complete)
    return () => {
      router.events.off('routeChangeComplete', change_complete)
    }
  }, [router])


  return (
    <Fragment>
  <Fragment>
  {isTrue(connectError !== null) ? (
  <Fragment>
  <Modal isOpen={connectError !== null}>
  <ModalOverlay>
  <ModalContent>
  <ModalHeader>
  {`Connection Error`}
</ModalHeader>
  <ModalBody>
  <Text>
  {`Cannot connect to server: `}
  {(connectError !== null) ? connectError.message : ''}
  {`. Check if server is reachable at `}
  {getEventURL().href}
</Text>
</ModalBody>
</ModalContent>
</ModalOverlay>
</Modal>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  <HStack alignItems={`flex-start`} sx={{"transition": "left 0.5s, width 0.5s", "position": "relative", "left": isTrue(state.sidebar_displayed) ? `0px` : `-20em`}}>
  <Box sx={{"minWidth": "20em", "height": "100%", "position": "sticky", "top": "0px", "borderRight": "1px solid #F4F3F6"}}>
  <VStack sx={{"height": "100dvh"}}>
  <HStack sx={{"width": "100%", "borderBottom": "1px solid #F4F3F6", "padding": "1em"}}>
  <Image src={`/icon.svg`} sx={{"height": "2em"}}/>
  <Spacer/>
  <Link as={NextLink} href={`https://github.com/dot-agent`}>
  <Center sx={{"boxShadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.14)", "bg": "transparent", "borderRadius": "0.375rem", "_hover": {"bg": "#F5EFFE"}}}>
  <Image src={`/github.svg`} sx={{"height": "3em", "padding": "0.5em"}}/>
</Center>
</Link>
</HStack>
  <VStack alignItems={`flex-start`} sx={{"width": "100%", "overflowY": "auto", "padding": "1em"}}>
  <Link as={NextLink} href={`/`} sx={{"width": "100%"}}>
  <HStack sx={{"bg": isTrue((state.router.page.path === "/home") || (((state.router.page.path === "/") && "Home") === "Home")) ? `#F5EFFE` : `transparent`, "color": isTrue((state.router.page.path === "/home") || (((state.router.page.path === "/") && "Home") === "Home")) ? `#1A1060` : `black`, "borderRadius": "0.375rem", "boxShadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.14)", "width": "100%", "paddingX": "1em"}}>
  <Image src={`/logo.svg`} sx={{"height": "2.5em", "padding": "0.5em"}}/>
  <Text>
  {`Home`}
</Text>
</HStack>
</Link>
  <Link as={NextLink} href={`/dashboard`} sx={{"width": "100%"}}>
  <HStack sx={{"bg": isTrue((state.router.page.path === "/dashboard") || (((state.router.page.path === "/") && "Dashboard") === "Home")) ? `#F5EFFE` : `transparent`, "color": isTrue((state.router.page.path === "/dashboard") || (((state.router.page.path === "/") && "Dashboard") === "Home")) ? `#1A1060` : `black`, "borderRadius": "0.375rem", "boxShadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.14)", "width": "100%", "paddingX": "1em"}}>
  <Image src={`/github.svg`} sx={{"height": "2.5em", "padding": "0.5em"}}/>
  <Text>
  {`Dashboard`}
</Text>
</HStack>
</Link>
  <Link as={NextLink} href={`/my_app`} sx={{"width": "100%"}}>
  <HStack sx={{"bg": isTrue((state.router.page.path === "/my_app") || (((state.router.page.path === "/") && "my_app") === "Home")) ? `#F5EFFE` : `transparent`, "color": isTrue((state.router.page.path === "/my_app") || (((state.router.page.path === "/") && "my_app") === "Home")) ? `#1A1060` : `black`, "borderRadius": "0.375rem", "boxShadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.14)", "width": "100%", "paddingX": "1em"}}>
  <Image src={`/github.svg`} sx={{"height": "2.5em", "padding": "0.5em"}}/>
  <Text>
  {`my_app`}
</Text>
</HStack>
</Link>
  <Link as={NextLink} href={`/settings`} sx={{"width": "100%"}}>
  <HStack sx={{"bg": isTrue((state.router.page.path === "/settings") || (((state.router.page.path === "/") && "Settings") === "Home")) ? `#F5EFFE` : `transparent`, "color": isTrue((state.router.page.path === "/settings") || (((state.router.page.path === "/") && "Settings") === "Home")) ? `#1A1060` : `black`, "borderRadius": "0.375rem", "boxShadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.14)", "width": "100%", "paddingX": "1em"}}>
  <Image src={`/github.svg`} sx={{"height": "2.5em", "padding": "0.5em"}}/>
  <Text>
  {`Settings`}
</Text>
</HStack>
</Link>
</VStack>
  <Spacer/>
  <HStack sx={{"width": "100%", "borderTop": "1px solid #F4F3F6", "padding": "1em"}}>
  <Link as={``} onClick={(_e) => addEvents([Event("state.toggle_sidebar_displayed", {})], (_e))} sx={{"transform": isTrue(!state.sidebar_displayed) ? `rotate(180deg)` : ``, "transition": "transform 0.5s, left 0.5s", "position": "relative", "left": isTrue(state.sidebar_displayed) ? `0px` : `20.5em`, "backgroundColor": "white", "border": "1px solid #F4F3F6", "borderRadius": "0.375rem"}}>
  <Center sx={{"bg": "transparent", "borderRadius": "0.375rem", "_hover": {"bg": "#F5EFFE"}}}>
  <Image src={`/paneleft.svg`} sx={{"height": "2em", "padding": "0.5em"}}/>
</Center>
</Link>
  <Spacer/>
  <Link as={NextLink} href={`https://docs.dotagent.dev/nextpy/getting-started/introduction/`}>
  <Text>
  {`Docs`}
</Text>
</Link>
  <Link as={NextLink} href={`https://dotagent.dev/blog/`}>
  <Text>
  {`Blog`}
</Text>
</Link>
</HStack>
</VStack>
</Box>
  <Box sx={{"paddingTop": "5em", "paddingX": "2em"}}>
  <Box sx={{"width": isTrue(state.sidebar_displayed) ? `calc(90vw - 20em)` : `90vw`, "min-width": "20em", "alignItems": "flex-start", "boxShadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.14)", "borderRadius": "0.375rem", "padding": "1em", "marginBottom": "2em"}}>
  <Container>
  <Highlight query={["st.table"]} styles={{"px": "2", "py": "1", "rounded": "full", "bg": "grey"}}>
  {`St.table`}
</Highlight>
  <Table colorScheme={`teal`} variant={`striped`}>
  <Thead>
  <Tr>
  <Th>
  {`Name`}
</Th>
  <Th>
  {`Age`}
</Th>
  <Th>
  {`Location`}
</Th>
</Tr>
</Thead>
  <Tbody>
  <Tr>
  <Td>
  {`John`}
</Td>
  <Td>
  {`30`}
</Td>
  <Td>
  {`New York`}
</Td>
</Tr>
  <Tr>
  <Td>
  {`Jane`}
</Td>
  <Td>
  {`31`}
</Td>
  <Td>
  {`San Francisco`}
</Td>
</Tr>
  <Tr>
  <Td>
  {`Joe`}
</Td>
  <Td>
  {`32`}
</Td>
  <Td>
  {`Los Angeles`}
</Td>
</Tr>
</Tbody>
</Table>
  <Highlight query={["st.latex "]} styles={{"px": "2", "py": "1", "rounded": "full", "bg": "grey"}}>
  {`St.latex`}
</Highlight>
  <InlineMath>
  {state.eq}
</InlineMath>
  <Highlight query={["st.dataframe \n"]} styles={{"px": "2", "py": "1", "rounded": "full", "bg": "grey"}}>
  {`St.dataframe`}
</Highlight>
  <DataTableGrid columns={state.data.columns} data={state.data.data} pagination={true} search={true} sort={false}/>
  <Highlight query={["st.chart"]} styles={{"px": "2", "py": "1", "rounded": "full", "bg": "grey"}}>
  {`St.areachart`}
</Highlight>
  <RechartsResponsiveContainer height={300} width={`40%`}>
  <RechartsAreaChart data={state.data_list} height={`100%`} width={`100%`}>
  <RechartsArea dataKey={`x`} fill={`#8884d8`} stroke={`#8884d8`}/>
  <RechartsXAxis dataKey={`y`}/>
  <RechartsYAxis/>
</RechartsAreaChart>
</RechartsResponsiveContainer>
  <Heading>
  {`Hii`}
</Heading>
  <RechartsResponsiveContainer height={`100%`} minHeight={100} minWidth={200} width={`100%`}>
  <RechartsLineChart data={state.data2} height={`100%`} width={`100%`}>
  <RechartsLine dataKey={`pv`} stroke={`#8884d8`}/>
  <RechartsLine dataKey={`uv`} stroke={`#82ca9d`}/>
  <RechartsXAxis dataKey={`name`}/>
  <RechartsYAxis/>
</RechartsLineChart>
</RechartsResponsiveContainer>
  <Text>
  {`Hello`}
</Text>
  <Highlight query={["st.colorpicker"]} styles={{"px": "2", "py": "1", "rounded": "full", "bg": "grey"}}>
  {`St.colorpicker`}
</Highlight>
  <Text>
  {`Color: `}
  {state.color}
</Text>
  <HexColorPicker onChange={(_e0) => addEvents([Event("state.set_color", {value:_e0})], (_e0))}/>
  <RechartsResponsiveContainer height={`100%`} minHeight={100} minWidth={200} width={`100%`}>
  <RechartsBarChart data={state.data2} height={`100%`} width={`100%`}>
  <RechartsBar dataKey={`uv`} fill={`#8884d8`} stroke={`#8884d8`}/>
  <RechartsXAxis dataKey={`name`}/>
  <RechartsYAxis/>
</RechartsBarChart>
</RechartsResponsiveContainer>
</Container>
</Box>
</Box>
  <Spacer/>
  <Box sx={{"position": "fixed", "right": "1.5em", "top": "1.5em", "zIndex": "500"}}>
  <Menu>
  <MenuButton sx={{"width": "3em", "height": "3em", "backgroundColor": "white", "border": "1px solid #F4F3F6", "borderRadius": "0.375rem"}}>
  <HamburgerIcon sx={{"size": "4em", "color": "black"}}/>
</MenuButton>
  <MenuList>
  <MenuItem sx={{"_hover": {"bg": "#F5EFFE"}}}>
  <Link as={NextLink} href={`/`} sx={{"width": "100%"}}>
  {`Home`}
</Link>
</MenuItem>
  <MenuDivider/>
  <MenuItem sx={{"_hover": {"bg": "#F5EFFE"}}}>
  <Link as={NextLink} href={`https://github.com/dot-agent`} sx={{"width": "100%"}}>
  {`About`}
</Link>
</MenuItem>
  <MenuItem sx={{"_hover": {"bg": "#F5EFFE"}}}>
  <Link as={NextLink} href={`mailto:anurag@dotagent.ai`} sx={{"width": "100%"}}>
  {`Contact`}
</Link>
</MenuItem>
</MenuList>
</Menu>
</Box>
</HStack>
  <NextHead>
  <title>
  {`my_app`}
</title>
  <meta content={`A Nextpy app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
  <meta content={`width=device-width, shrink-to-fit=no, initial-scale=1`} name={`viewport`}/>
</NextHead>
</Fragment>
  )
}
