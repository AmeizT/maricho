import '../shared/sass/app.scss'
import { BaseLayout } from '../components/layout'

function App({ Component, pageProps }){
    return (
        <BaseLayout>
            <Component {...pageProps} />
        </BaseLayout>
    )
}

export default App