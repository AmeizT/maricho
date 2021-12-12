import styled from 'styled-components'

export const Box = styled.div `
    width: 100%;
    height: auto;
    padding: ${props => props.space};
`

export const LayoutBox = styled(Box) `
    min-height: 100vh;
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: 1fr;

    @media only screen and (min-width: 1024px){
        grid-template-columns: 25% 45% 30%;
    }
`