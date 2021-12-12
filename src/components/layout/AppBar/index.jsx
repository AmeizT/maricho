import { CgMenuGridR } from 'react-icons/cg'
import { NavBar } from '../../../shared/styles/Bar'
import { BarContainer, Stack } from '../../../shared/styles/Surfaces'
import { List, ListItem } from '../../../shared/styles/Navigation'
import { IconContext } from 'react-icons/lib'
import { BiBell } from 'react-icons/bi'
import { RiTruckLine, RiPushpinLine } from 'react-icons/ri'
import { MdOutlineTipsAndUpdates, MdOutlineBolt, MdApps, MdStorefront, MdOutlineBusinessCenter, MdPersonOutline } from 'react-icons/md'
import { CharField } from '../../../shared/styles/Form'
import { IconButton, LinkButton } from '../../../shared/styles/Button'
import Link from 'next/link'

function AppBar(){
    return (
        <NavBar over>
            <BarContainer 
            cols="repeat(3, 1fr)" 
            space="0 var(--gap-md)" 
            dwSpace="0 var(--gap-max)">
                <Stack>1</Stack>

                <Stack dw>
                    <SearchArea />
                </Stack>

                <Stack dw>
                    <Navigation />
                </Stack>
            </BarContainer>
        </NavBar>
    )
}

function SearchArea(){
    return (
        <Stack size="100%">
            <CharField size="100%" fieldName="Search Maricho" />
        </Stack>
    )
}

function Navigation(){
    const navigation = [
        { pk: 1, name: "Menu", type: "button", badge: <MdApps /> },
        { pk: 2, name: "Messages", type: "button", badge: <BiBell /> },
        { pk: 3, name: "Runner", type: "link", to: "/runner", badge: <MdOutlineBolt /> },
        { pk: 4, name: "Fades", type: "link", to: "/fades", badge: <MdOutlineTipsAndUpdates /> },
        { pk: 5, name: "Account", type: "link", to: "/account", badge: <MdPersonOutline /> },
    ]
    return (
        <List pos="flex-end">
            {navigation.map(nav => (
                <ListItem key={nav.pk}>
                    {nav.type === 'button' ? 
                        <IconButton title={nav.name}>
                            <IconContext.Provider value={{ size: 24 }}>
                                {nav.badge}
                            </IconContext.Provider>
                        </IconButton> :

                        <Link href={nav.to} passHref>
                            <LinkButton title={nav.name}>
                                <IconContext.Provider value={{ size: 24 }}>
                                    {nav.badge}
                                </IconContext.Provider>
                            </LinkButton>
                        </Link>
                    }
                </ListItem>
            ))}
        </List>
    )
}

export default AppBar