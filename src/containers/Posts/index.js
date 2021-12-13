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
                <article key={post.id}><h3>{post.title}</h3></article>
            ))}
        </Box>
    )
}

export default Posts

