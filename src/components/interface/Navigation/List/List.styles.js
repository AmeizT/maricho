import styled from 'styled-components'

export const List = styled.ul.attrs(props => ({
    role: props.role || 'toolbar',
})) `
    justify-content: ${props => props.pos};
    flex-direction: ${props => props.dir};
`

export const ListItem = styled.li.attrs({
    role: "listitem",
})`
    width: ${props => props.size};
    height: auto;
    padding: ${props => props.space};
    justify-content: ${props => props.float};
`