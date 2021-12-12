import styled from 'styled-components'

export const CharField = styled.input.attrs(props => ({
    type: 'text',
    placeholder: props.fieldName,
}))`
    width: ${props => props.size};
    height: ${props => props.sizeY || 'auto'};
    padding: ${props => props.space || 'var(--gap-sm)'};
    border-radius: var(--radius-sm);
    border: var(--border);
    color: var(--dark-900);
    background: var(--gray-100);
    @media(prefers-color-scheme: dark){
        border: var(--border-dark);
        color: var(--gray-300);
        background: var(--dark-700);
    }
    &:focus {
        border: var(--border-focus);
    }

`