import styled from 'styled-components'

export const Container = styled.div `

`

export const Stack = styled(Container) `

`

export const Wrapper = styled.section `

`

export const Box = styled.div.attrs({
    as: props.turn,
}) `

`

export const Grid = styled.div `
    display: grid;
    grid-template-columns: ${props => props.col};
    grid-template-rows: ${props => props.row};
`

export const Segment = styled.span `
    display: ${props => props.view || 'block'};
`