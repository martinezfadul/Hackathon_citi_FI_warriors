import React from 'react'

const Carousel = () =>{
    return(
        <div>
            <div id="carouselExampleCaptions" className="carousel slide" data-bs-ride="carousel">
                <div className="carousel-indicators">
                    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
                    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
                </div>
                <div className="carousel-inner">
                    <div className="carousel-item active">
                    <img src="/Carrousel-Img/01.jpg" width="100%" height="600vw" alt="..."/>
                    <div className="carousel-caption d-none d-md-block">
                        <h1>DE MÉXICO A TU HOGAR</h1>
                        <p>Productos de calidad a buen precio, como si tú lo cosecharas</p>
                    </div>
                    </div>
                    <div className="carousel-item">
                    <img src="/Carrousel-Img/02.jpg" width="100%" height="600vw" alt="..."/>
                    <div className="carousel-caption d-none d-md-block">
                        <h5></h5>
                        <p></p>
                    </div>
                    </div>
                    <div className="carousel-item">
                    <img src="/Carrousel-Img/03.jpg" width="100%" height="600vw" alt="..."/>
                    <div className="carousel-caption d-none d-md-block">
                        <h5></h5>
                        <p></p>
                    </div>
                    </div>
                </div>
                <button className="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
                    <span className="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span className="visually-hidden">Previous</span>
                </button>
                <button className="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
                    <span className="carousel-control-next-icon" aria-hidden="true"></span>
                    <span className="visually-hidden">Next</span>
                </button>
                </div>

        </div>
    )
}

export default Carousel