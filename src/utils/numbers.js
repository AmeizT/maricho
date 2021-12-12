export function currencyUSD(wage){
    new Intl.NumberFormat("en-US", {
        style: "currency",
        currency: "USD"
    }).format(wage)


}