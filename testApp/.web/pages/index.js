import { Fragment, useContext, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { Event, getAllLocalStorageItems, getRefValue, getRefValues, isTrue, preventDefault, refs, set_val, spreadArraysOrObjects, uploadFiles, useEventLoop } from "/utils/state"
import { ColorModeContext, EventLoopContext, initialEvents, StateContext } from "/utils/context.js"
import "focus-visible/dist/focus-visible"
import { Box, Button, Center, Heading, Input, Modal, ModalBody, ModalContent, ModalHeader, ModalOverlay, Text } from "@chakra-ui/react"
import { getEventURL } from "/utils/state.js"
import { motion } from "framer-motion"
import NextHead from "next/head"



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
  <Center sx={{"width": "100%", "height": "100vh"}}>
  <Box sx={{"padding": "2em", "shadow": "lg", "borderRadius": "lg"}}>
  <Heading>
  {`ChatGPT`}
</Heading>
  <Input onChange={(_e0) => addEvents([Event("state.set_user_input", {value:_e0.target.value})], (_e0))} placeholder={`Ask a question...`} sx={{"width": "100%"}} type={`text`}/>
  <motion.div className={`w-28 h-28 bg-blue-200 rounded-full`} whileHover={{"scale": 1.2}} whileTap={{"scale": 0.8}}/>
  <Button isLoading={state.processing} onClick={(_e) => addEvents([Event("state.get_response", {})], (_e))} sx={{"width": "100%"}}>
  {`Get Answer`}
</Button>
  <Text sx={{"color": "blue"}}>
  {state.assistant_response}
</Text>
</Box>
</Center>
  <NextHead>
  <title>
  {`ChatGPT App`}
</title>
  <meta content={`A Nextpy app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
