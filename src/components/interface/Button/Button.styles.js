import styled from 'styled-components'

export const Button = styled.button.attrs({
    role: 'button',
    tabIndex: 0,
})``

export const MaxButton = styled(Button) `
    width: 100%;
    height: auto;
`

export const SnoozeButton = styled(Button).attrs({
    disabled: "disabled",
}) ``

export const IconButton = styled(Button) `
    width: ${props => props.sizeX || '42px'};
    height: ${props => props.sizeY || '42px'};
    display: grid;
    place-items: center;
    border-radius: ${props => props.edge || '50px'};
    background: ${props => props.color};
`

