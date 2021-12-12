import React, { Fragment, useEffect } from 'react'
import { IconContext } from 'react-icons'
import { Bar } from '../../shared/styles/Bar'
import { Article, Card } from '../../shared/styles/Card'
import { Typography } from '../../shared/styles/Typography'
import { MdMoreHoriz, MdOutlineBusinessCenter } from 'react-icons/md'
import { Container, Box, Stack, Group } from '../../shared/styles/Surfaces'
import { RiShareLine, RiHeart3Line, RiShareForwardLine } from 'react-icons/ri'

function Posts({ posts }){
    return (
        <Box role="feed" space="var(--main-bar) 0 0">
            {posts.map(post => (
                <Article
                gap="0 0 var(--gap-xs)" 
                space="var(--gap-md)"
                key={post.id} 
                aria-posinset={post.id} 
                aria-setsize="-1" 
                aria-label={post.title} 
                aria-labelledby={post.description}>
                    <Container direction="column">
                        <Stack>
                            <Group>
                                <Typography variant="a">{post.title}</Typography>
                            </Group>

                            <Group gap="0 0 0 auto">
                                <button>
                                    <IconContext.Provider value={{ size: 24 }}>
                                        <MdMoreHoriz />
                                    </IconContext.Provider>
                                </button>
                            </Group>
                        </Stack>

                        <Stack direction="column">
                            <Typography variant="span">
                                {post.currency === 'BTC' ? 
                                    `${'BTC'}${post.compensation}` : 
                                    
                                    post.currency === 'ETH' ? 
                                        `${'ETH'}${post.compensation}` :

                                    post.currency === 'ZAR' ? 
                                        `${new Intl.NumberFormat("en-ZA", {
                                            style: "currency",
                                            currency: "ZAR"
                                        }).format(post.compensation)}` :

                                    `${new Intl.NumberFormat("en-US", {
                                        style: "currency",
                                        currency: "USD"
                                    }).format(post.compensation)}`
                                }
                            </Typography>
                            <Typography>{post.description}</Typography>
                        </Stack>

                        <Bar pos="static" sizeY="0">
                            <Stack>
                                <Group>
                                    <Typography variant="span">{post.location}</Typography>
                                </Group>

                                <Group></Group>
                            </Stack>
                        </Bar>
                    </Container>
                </Article>
            ))}
        </Box>
    )
}

export default Posts

