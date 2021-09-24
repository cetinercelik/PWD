var dataHeader = [
        {
            bigImage: "images/slide-1.jpg",
            title: "Minimal & Clean",
            author: "Templatestock"
        },
        {
            bigImage: "images/slide-2.jpg",
            title: "I'm A Creative Theme",
            author: "Templatestock"
        },
        {
            bigImage: "images/slide-3.jpg",
            title: "Achieve Success",
            author: "Templatestock"
        }
    ],
    loaderSVG = new SVGLoader(document.getElementById('loader'), {
        speedIn: 600,
        speedOut: 600,
        easingIn: mina.easeinout
    });
loaderSVG.show()