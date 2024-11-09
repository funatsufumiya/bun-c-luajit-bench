// #include <stdio.h>
// #include <stdlib.h>

// int myRandom() {
//     return rand() + 42;
// }

// NAPI version of above code

#include <node_api.h>
#include <stdlib.h>

napi_value MyRandom(napi_env env, napi_callback_info info) {
    napi_value result;
    int random = rand() + 42;
    napi_create_int32(env, random, &result);
    return result;
}

napi_value Init(napi_env env, napi_value exports) {
    napi_value fn;
    napi_create_function(env, NULL, 0, MyRandom, NULL, &fn);
    napi_set_named_property(env, exports, "myRandom", fn);
    return exports;
}

NAPI_MODULE(NODE_GYP_MODULE_NAME, Init)