import styled, {css} from 'styled-components'

export const Bar = styled.div `
    width: var(--max);
    height: ${props => props.sizeY || 'var(--main-bar)'};
    position: ${props => props.pos || 'fixed'};
    display: flex;
    align-items: center;
    ${props => props.over && css `
        top: 0;
        border-bottom: var(--border);
        @media(prefers-color-scheme: dark){
            border-bottom: var(--border-dark);
        }
    `}
    ${props => props.under && css `
        bottom: 0;
        border-top: var(--border);
        @media(prefers-color-scheme: dark){
            border-top: var(--border-dark);
        }
    `}
    background: var(--snow);
    @media(prefers-color-scheme: dark){
        background: var(--dark-500);
    }
    z-index: 1100;
    
`