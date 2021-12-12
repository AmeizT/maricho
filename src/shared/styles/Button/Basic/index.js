import styled from 'styled-components'

export const Button = styled.button.attrs({
    role: 'button',
    tabIndex: 0,
})`
    color: var(--gray-100);
    @media(prefers-color-scheme: dark){
        color: var(--gray-400);
    }
    transition: color background var(--ease-100);

    &:hover {
        color: var(--dark-900);
        @media(prefers-color-scheme: dark){
            color: var(--snow);
            background: var(--dark-400);
        }
    }
`

export const MaxButton = styled(Button) `
    width: 100%;
    height: auto;
`

export const SnoozeButton = styled(Button).attrs({
    disabled: "disabled",
}) ``

export const IconButton = styled(Button) `
    width: ${props => props.sizeX || '38px'};
    height: ${props => props.sizeY || '38px'};
    display: grid;
    place-items: center;
    border-radius: ${props => props.edge || 'var(--radius-sm)'};
    background: ${props => props.color};
`

export const LinkButton = styled(IconButton).attrs({
    as: "a",
}) `
`