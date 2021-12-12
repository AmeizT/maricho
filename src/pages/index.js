import axios from 'axios'
import React, { Component, Fragment } from 'react'
import Posts from '../containers/Posts'

export async function getStaticProps(){
    try {
        const res = await axios('http://127.0.0.1:8000/api/feed/')
        const posts = res.data
   
        if (!posts) {
            return {
            notFound: true,
            }
        }

        return { 
            props: {
                posts
            },

            revalidate: 1,
        }
    } catch(err){
        console.log('no data')
        return { 
            props: {
                err: "no data",
            }
        }
    }
}

class Feed extends Component {
    render() {
        return (
            <Fragment>
                <Posts posts={this.props.posts} />
            </Fragment>
        )
    }
}

export default Feed
