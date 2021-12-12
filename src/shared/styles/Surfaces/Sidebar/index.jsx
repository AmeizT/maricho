import styled from 'styled-components'


export const SideBar = styled.aside `
    width: ${props => props.sizeX};
    height: ${props => props.sizeY || '100vh'};
    display: ${props => props.view || 'none'};
    flex-direction: column;
    padding: ${props => props.space || 'var(--main-bar) var(--gap-md)'};
    @media only screen and (min-width: 1024px){
        display: flex;
    }
`

export const ListBar = styled(SideBar).attrs({
    as: 'nav',
    role: 'listbox',
})`

`