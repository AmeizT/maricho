import styled from 'styled-components'

export const Menu = styled.nav.attrs({
    role: 'listbox',
})`
    width: ${props => props.size};
    height: auto;
    display: none;
    position: ${props => props.pos || 'fixed'};
    top: ${props => props.posY || 'calc(var(--main-bar) - 10px)'};
    padding: ${props => props.space};
    border: var(--border);
    border-radius: var(--radius-sm);
    background: var(--snow);
    z-index: 1101;
    @media(prefers-color-scheme: dark){
        border: var(--border-dark);
        background: var(--dark-500);
    }

    &.active {
        display: flex;
    }

`