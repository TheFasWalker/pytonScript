# pytonScript
задача скрипта - считать адреса файлов и записать их в файл kitchensPhotos.json


Обязательная структура:
publick (родительская папка)
  001 (название внутренних папок должно соответствовать ID элемента из БД)
    additional( папка с файлами для "дополнительного слайдера")
    main(файлы для основного слайдера)

структура создаваемого файла
{
    "kitchensUrls": {
        "100": {
            "firstSlider": [
               "public/100/main/02.txt",
                "public/100/main/main1.txt",
                "public/100/main/main2.txt",
                "public/100/main/main3.txt"
            ],
            "additionalSlider": [
                "public/100/additional/01.txt",
                "public/100/additional/012.txt",
                "public/100/additional/013.txt",
                "public/100/additional/014.txt"
            ]
        },
        "101": {
            "firstSlider": [
                "public/101/main/02.txt"
            ],
            "additionalSlider": [
                "public/101/additional/01.txt"
            ]
        }
    }
}
