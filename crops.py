def crop(crop_name):
    crop_data = {
    "wheat":["https://cdn.pixabay.com/photo/2015/02/18/16/10/wheat-field-640960_960_720.jpg", "U.P., Punjab, Haryana, Rajasthan, M.P., bihar", "rabi","Sri Lanka, United Arab Emirates, Taiwan"],
    "paddy":["https://cdn.pixabay.com/photo/2014/10/22/18/43/rice-498688_960_720.jpg", "W.B., U.P., Andhra Pradesh, Punjab, T.N.", "kharif","Bangladesh, Saudi Arabia, Iran"],
    "barley":["https://cdn.pixabay.com/photo/2014/06/20/19/36/barley-373360_960_720.jpg", "Rajasthan, Uttar Pradesh, Madhya Pradesh, Haryana, Punjab", "rabi","Oman, UK, Qatar, USA"],
    "maize":["https://cdn.pixabay.com/photo/2014/03/25/16/23/corn-296956_960_720.png", "Karnataka, Andhra Pradesh, Tamil Nadu, Rajasthan, Maharashtra", "kharif", "Hong Kong, United Arab Emirates, France"],
    "bajra":["https://cdn.pixabay.com/photo/2013/11/01/18/21/pearl-millet-204098_960_720.jpg", "Rajasthan, Maharashtra, Haryana, Uttar Pradesh and Gujarat", "kharif", "Oman, Saudi Arabia, Israel, Japan"],
    "copra":["https://cdn.pixabay.com/photo/2016/07/06/20/56/coconut-1501334_960_720.jpg", "Kerala, Tamil Nadu, Karnataka, Andhra Pradesh, Orissa, West Bengal", "Veitnam, Bangladesh, Iran, Malaysia"],
    "cotton":["https://cdn.pixabay.com/photo/2013/04/03/12/31/clematis-vitalba-99887_960_720.jpg", "Punjab, Haryana, Maharashtra, Tamil Nadu, Madhya Pradesh, Gujarat", " China, Bangladesh, Egypt"],
    "masoor":["https://cdn.pixabay.com/photo/2016/08/28/22/07/sesame-1627005_960_720.jpg", "Uttar Pradesh, Madhya Pradesh, Bihar, West Bengal, Rajasthan", "rabi", "Pakistan, Cyprus,United Arab Emirates"],
    "gram":["https://cdn.pixabay.com/photo/2013/07/25/11/56/channa-166896_960_720.jpg", "Madhya Pradesh, Maharashtra, Rajasthan, Uttar Pradesh, Andhra Pradesh & Karnataka", "rabi", "Veitnam, Spain, Myanmar"],
    "groundnut":["https://cdn.pixabay.com/photo/2018/01/02/07/22/food-3055647_960_720.jpg", "Andhra Pradesh, Gujarat, Tamil Nadu, Karnataka, and Maharashtra", "kharif", "Indonesia, Jordan, Iraq"],
    "arhar":["https://cdn.pixabay.com/photo/2018/12/14/08/33/pigeon-peas-3874445_960_720.jpg", "Maharashtra, Karnataka, Madhya Pradesh and Andhra Pradesh", "kharif", "United Arab Emirates, USA, Chicago"],
    "sesamum":["https://cdn.pixabay.com/photo/2014/04/05/11/39/sesame-316590_960_720.jpg", "Maharashtra, Rajasthan, West Bengal, Andhra Pradesh, Gujarat", "rabi", "Iraq, South Africa, USA, Netherlands"],
    "jowar":["https://cdn.pixabay.com/photo/2018/08/22/22/46/field-3624849_960_720.jpg", "Maharashtra, Karnataka, Andhra Pradesh, Madhya Pradesh, Gujarat", "kharif", "Torronto, Sydney, New York"],
    "moong":["https://cdn.pixabay.com/photo/2013/07/25/12/03/chana-166987_960_720.jpg", "Rajasthan, Maharashtra, Andhra Pradesh", "rabi", "Qatar, United States, Canada"],
    "niger":["https://cdn.pixabay.com/photo/2016/11/19/15/27/bird-1839844_960_720.jpg", "Andha Pradesh, Assam, Chattisgarh, Gujarat, Jharkhand", "kharif", "United States of American,Argenyina, Belgium"],
    "rape":["https://cdn.pixabay.com/photo/2013/12/20/14/01/mustard-231302_960_720.jpg", "Rajasthan, Uttar Pradesh, Haryana, Madhya Pradesh, and Gujarat", "rabi", "Veitnam, Malaysia, Taiwan"],
    "jute":["https://cdn.pixabay.com/photo/2018/01/25/19/48/pepper-3106925_960_720.jpg", " West Bengal , Assam , Orissa , Bihar , Uttar Pradesh", "kharif", "JOrdan, United Arab Emirates, Taiwan"],
    "safflower":["https://cdn.pixabay.com/photo/2010/12/13/10/11/safflower-2423_960_720.jpg",  "Maharashtra, Karnataka, Andhra Pradesh, Madhya Pradesh, Orissa", "kharif", " Philippines, Taiwan, Portugal"],
    "soyabean":["https://cdn.pixabay.com/photo/2015/09/29/18/41/soy-964324_960_720.jpg",  "Madhya Pradesh, Maharashtra, Rajasthan, Madhya Pradesh and Maharashtra", "kharif", "Spain, Thailand, Singapore"],
    "urad":["https://www.boldsky.com/img/2018/12/xcoverimage-1544088609.png.pagespeed.ic.zeG4XwCeHo.jpg",  "Andhra Pradesh, Maharashtra, Madhya Pradesh, Tamil Nadu", "rabi", "United States, Canada, United Arab Emirates"],
    "ragi":["https://cdn.pixabay.com/photo/2016/09/26/21/18/millet-1697117_960_720.jpg",  "Maharashtra, Tamil Nadu and Uttarakhand", "kharif", "United Arab Emirates, New Zealand, Bahrain"],
    "sunflower":["https://cdn.pixabay.com/photo/2018/04/05/14/09/sun-flower-3292932_960_720.jpg",  "Karnataka, Andhra Pradesh, Maharashtra, Bihar, Orissa", "rabi", "Phillippines, United States, Bangladesh"],
    "sugarcane":["https://cdn.pixabay.com/photo/2014/04/03/11/35/sugarcane-311914_960_720.png","Uttar Pradesh, Maharashtra, Tamil Nadu, Karnataka, Andhra Pradesh" , "kharif", "Kenya, United Arab Emirates, United Kingdom"]
    }
    return crop_data[crop_name]