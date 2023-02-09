from service.ServiceCraigsListAll import ServiceCraigsListAll
from service.ServiceCraigsListOneAd import ServiceCraigsListOneAd

if __name__ == '__main__':
    service1 = ServiceCraigsListOneAd()
    service2 = ServiceCraigsListAll()

    # STEP 2
    service1.find()

    # STEP 3
    service2.set_more_info(ad_info=service1.one_ad)

    # Show Info for csv
    service2.show_info()
