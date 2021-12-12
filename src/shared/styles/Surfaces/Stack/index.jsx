import { Container } from '../Container'
import styled, {css} from 'styled-components'

export const Stack = styled.div `
    width: ${props => props.size || 'auto'};
    height: auto;
    display: ${props => props.view || 'flex'};
    flex-direction: ${props => props.direction || 'row'};
    justify-content: ${props => props.pos};
    align-items: ${props => props.align};
    padding: ${props => props.space};
    @media only screen and (min-width: 1024px){
        padding: ${props => props.dwSpace};
    }
    ${props => props.mw && css `
        display: ${props => props.view || 'flex'};
        @media only screen and (min-width: 1024px){
            display: none;
        }
    `}
    ${props => props.dw && css `
        display: none;
        @media only screen and (min-width: 1024px){
            display: flex;
        }
    `}
`

export const Group = styled.div `
    display: flex;
    flex-flow: ${props => props.direction || 'row'};
    align-items: center;
    margin: ${props => props.gap};
`