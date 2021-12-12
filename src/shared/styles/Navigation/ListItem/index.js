import styled from 'styled-components'

export const ListItem = styled.li.attrs(props => ({
    role: "listitem",
}))`
    width: ${props => props.size};
    height: auto;
    padding: ${props => props.space};
    justify-content: ${props => props.float};
`