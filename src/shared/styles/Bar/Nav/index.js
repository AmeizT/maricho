import { Bar } from '../Base'
import styled from 'styled-components'

export const NavBar = styled(Bar).attrs(props => ({
    as: "header",
    role: "banner",
}))``