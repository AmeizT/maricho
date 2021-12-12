import styled from 'styled-components'

export const Item = styled.span `
    display: ${props => props.view || 'flex'};
    align-items: center;
    margin-left: ${props => props.space};
`