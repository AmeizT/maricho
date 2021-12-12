import React from 'react'
import AppBar from "../AppBar"
import Content from '../Content'
import BottomNavigation from '../Footer'
import { LayoutBox } from './Interface.styles'
import { SideBar, ListBar } from '../../../shared/styles/Surfaces'

export default function BaseLayout({ children }){
    return (
        <React.Fragment>
            <AppBar />
            <LayoutBox>
                <SideBar></SideBar>
                <Content>{ children }</Content>
                <ListBar></ListBar>
            </LayoutBox>
            <BottomNavigation />
        </React.Fragment>
    )
}