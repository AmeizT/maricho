import styled, {css} from 'styled-components'

export const Bridge = styled.a.attrs({
    role: 'link',
    href: props.to,
}) `
    width: ${props => props.size};
    display: ${props => props.view || 'block'};
    align-items: center;
    padding: var(--gap-sm);
    color: var(--dark-900);
    text-transform: capitalize;
    font-size: ${props => props.font};
    transition: color var(--ease-100);
    @media(prefers-color-scheme: dark){
        color: var(--snow);
    };
    ${props => props.withBorder && css `
        border-bottom: var(--border);
        @media(prefers-color-scheme: dark){
            border-bottom: var(--border-dark);
        }
    `};
    & :hover {
        ${props => props.hover && css `
            color: var(--dark-700);
            @media(prefers-color-scheme: dark){
                color: var(--gray-500);
            }
        `}

        ${props => props.highlight && css `
            background: var(--gray-100);
            @media(prefers-color-scheme: dark){
                background: var(--dark-400);
            }
        `}
    }
`

export const Referrer = styled(Bridge).attrs({
    rel: 'noreferrer',
    target: '_blank',
})`

`