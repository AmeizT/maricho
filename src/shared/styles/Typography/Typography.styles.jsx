import styled from 'styled-components'

export const Typography = styled.p.attrs(props => ({
    as: props.variant,
})) `
    font-size: ${props => props.size};
    color: ${props => props.color};
    @media(prefers-color-scheme: dark){
        color: ${props => props.darkModeColor};
    }
`