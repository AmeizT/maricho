import styled from 'styled-components'

export const Card = styled.div `
    width: 100%;
    height: auto;
    margin: ${props => props.gap};
    padding: ${props => props.space};
`

export const Article = styled(Card).attrs({
    as: 'article',
    role: 'article',
})`
    background: var(--gray-100);
    @media(prefers-color-scheme: dark){
        background: var(--dark-500);
    }
`