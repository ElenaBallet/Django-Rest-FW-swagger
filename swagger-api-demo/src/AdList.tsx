import {useEffect, useState} from "react";
import {Ad, AdService} from "./api";

function BookItem(props: Ad) {
    return <div>
        <b>{props.title}</b>
        <i>{props.authors_names.join(', ')}</i>
    </div>;
}

export default function AdList() {
    const [ads, setAd] = useState<Ad[] | undefined>();
    const loadAd = async () => {
        setAd(await AdService.adList());
    }
    useEffect(() => {
        loadAd();
    }, []);
    return (
        <div>
            <h1>Ads:</h1>
            {ads && ads.map(
                ads => {
                    return <BookItem {...ads}/>;
                })}
        </div>
    );
}