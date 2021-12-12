import styled from 'styled-components'

export const Container = styled.div `
    width: 100%;
    height: auto;
    display: ${props => props.view || 'flex'};
    flex-direction: ${props => props.direction || 'row'};
    align-items: ${props => props.align};
    padding: ${props => props.space};
    @media only screen and (min-width: 1024px){
        padding: ${props => props.dwSpace};
    }
`

export const BarContainer = styled(Container) `
    display: grid;
    grid-template-columns: ${props => props.cols};
    grid-template-rows: 1fr;
    @media only screen and (min-width: 1024px){
        grid-template-columns: 25% 45% 30%;
    }
`