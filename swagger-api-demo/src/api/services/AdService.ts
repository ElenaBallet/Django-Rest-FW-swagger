/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Ad } from '../models/Ad';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class AdService {

    /**
     * @returns Ad
     * @throws ApiError
     */
    public static adList(): CancelablePromise<Array<Ad>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/ad',
        });
    }

}
