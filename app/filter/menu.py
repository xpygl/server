

menu_top = [
    {
        "label": "首页",
        "path": "/dashboard",
        "icon": 'el-icon-s-home',
        "meta": {
            "i18n": 'dashboard',
        },
        "parentId": 0
    }
]

first = [
    {
        "label": "用户管理",
        "path": '/userinfo',
        "meta": {
            "i18n": 'userinfo',
        },
        "icon": 'el-icon-user-solid',
        "children": [
            {
                "label": "用户管理",
                "path": 'user',
                "component": 'views/userinfo/user',
                "meta": {
                    "i18n": 'user',
                    "keepAlive": True
                },
                "icon": 'el-icon-user-solid',
                "children": []
            },
            {
                "label": "角色维护",
                "path": 'Role',
                "component": 'views/userinfo/role',
                "meta": {
                    "i18n": 'role',
                    "keepAlive": True
                },
                "icon": 'el-icon-setting',
                "children": []
            },
            {
                "label": "充值卡管理",
                "path": '/czcard',
                "component": 'views/userinfo/czcard',
                "meta": {
                    "i18n": 'czcard',
                    "keepAlive": True
                },
                "icon": 'el-icon-bank-card',
                "children": []
            },
            {
                "label": "安全管理",
                "path": 'pw',
                "component": 'views/userinfo/pw',
                "meta": {
                    "i18n": 'user',
                    "keepAlive": True
                },
                "icon": 'el-icon-setting',
                "children": []
            },
        ]
    },
    {
        "label": "店铺管理",
        "path": '/shopinfo',
        "meta": {
            "i18n": 'shopinfo',
        },
        "icon": 'el-icon-menu',
        "children": [
            {
                "label": "轮播图管理",
                "path": '/bannerHandler',
                "component": 'views/shopinfo/bannerHandler',
                "meta": {
                    "i18n": 'bannerHandler',
                    "keepAlive": False
                },
                "icon": 'el-icon-picture-outline-round',
                "children": []
            },
            {
                "label": "素材管理",
                "path": '/attachment',
                "component": 'views/shopinfo/attachment',
                "meta": {
                    "i18n": 'attachment',
                    "keepAlive": False
                },
                "icon": 'el-icon-picture',
                "children": []
            },
            {
                "label": "店铺参数",
                "path": 'Sysparams',
                "component": 'views/shopinfo/sysparams',
                "meta": {
                    "i18n": 'sysparams'
                },
                "icon": 'el-icon-setting',
                "children": []
            },
        ]
    },
    {
        "label": "商品管理",
        "path": '/goodsinfo',
        "meta": {
            "i18n": 'goodsinfo',
        },
        "icon": 'el-icon-s-goods',
        "children": [
            {
                "label": "商品管理",
                "path": '/goods',
                "component": 'views/goodsinfo/goods',
                "meta": {
                    "i18n": 'goods',
                    "keepAlive": True
                },
                "icon": 'el-icon-s-goods',
                "children": []
            },
            {
                "label": "分类管理",
                "path": '/category',
                "component": 'views/goodsinfo/category',
                "meta": {
                    "i18n": 'category',
                    "keepAlive": True
                },
                "icon": 'el-icon-menu',
                "children": []
            },
        ]
    },
    {
        "label": "主题管理",
        "path": '/themeinfo',
        "meta": {
            "i18n": 'themeinfo',
        },
        "icon": 'el-icon-menu',
        "children": [
            {
                "label": "热门分类管理",
                "path": '/hotcategory',
                "component": 'views/themeinfo/hotcategory',
                "meta": {
                    "i18n": 'hotcategory',
                    "keepAlive": True
                },
                "icon": 'el-icon-menu',
                "children": []
            },
            {
                "label": "热门分类管理1",
                "path": '/hotcategory1',
                "component": 'views/themeinfo/hotcategory1',
                "meta": {
                    "i18n": 'hotcategory1',
                    "keepAlive": True
                },
                "icon": 'el-icon-menu',
                "children": []
            },
            {
                "label": "推荐分类管理",
                "path": '/tjcategory',
                "component": 'views/themeinfo/tjcategory',
                "meta": {
                    "i18n": 'tjcategory',
                    "keepAlive": True
                },
                "icon": 'el-icon-menu',
                "children": []
            },
        ]
    },
    {
        "label": "订单管理",
        "path": '/orderinfo',
        "meta": {
            "i18n": 'orderinfo',
        },
        "icon": 'el-icon-s-order',
        "children": [
            {
                "label": "订单管理",
                "path": '/order',
                "component": 'views/orderinfo/order',
                "meta": {
                    "i18n": 'order',
                    "keepAlive": False
                },
                "icon": 'el-icon-s-order',
                "children": []
            },
        ]
    },
    {
        "label": "系统管理",
        "path": '/systemManagement',
        "meta": {
            "i18n": 'systemManagement',
        },
        "icon": 'el-icon-setting',
        "children": [
            {
                "label": "缓存管理",
                "path": 'Cache',
                "component": 'views/systemManagement/Cache',
                "meta": {
                    "i18n": 'Cache'
                },
                "icon": 'el-icon-setting',
                "children": []
            },
        ]
    }
]


all_menu = {
    "top" : menu_top,
    "first" : first
}
