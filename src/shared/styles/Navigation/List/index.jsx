import styled from 'styled-components'

export const List = styled.ul.attrs(props => ({
    role: props.role || 'toolbar',
})) `
    justify-content: ${props => props.pos};
    flex-direction: ${props => props.dir};
`