<!DOCTYPE html>
<html lang="zxx">

<?php 
include 'sc_head.php';
?>

<?php
 $test = "123";
 $get_data_1 = "select * from customer " ;
 $result_1 = mysqli_query($mysqli , $get_data_1 );
 //$rs = mysqli_fetch_array($result_1);
 
?>


<body>
        <!-- Page Preloder -->
        <div id="preloder">
            <div class="loader"></div>
        </div>

        <?php 
include 'sc_nav.php';
?>
       

    <section class="hero">
        <div class="container">
            <div class="row">
                <div class="col-lg-3">
                    <div class="hero__categories">
                        <div class="hero__categories__all">
                            <i class="fa fa-bars"></i>
                            <span>All departments</span>
                        </div>
                        <ul>
                    
                            <li><a href="shop-grid-1.php">Back Pack</a></li>
                            <li><a href="shop-grid-2.php">Shoulder Bag</a></li>
                            <li><a href="shop-grid-3.php">Other Bags </a></li>
                          

                        </ul>
                    </div>
                </div>
                <div class="col-lg-9">
                    <div class="hero__search">
                        <div class="hero__search__form">
                            <form action="#">
                                <div class="hero__search__categories">
                                    All Categories
                                    <span class="arrow_carrot-down"></span>
                                </div>
                                <input type="text" placeholder="What do yo u need?">
                                <button type="submit" class="site-btn">SEARCH</button>
                            </form>
                        </div>
                        <div class="hero__search__phone">
                            <div class="hero__search__phone__icon">
                                <i class="fa fa-phone"></i>
                            </div>
                            <div class="hero__search__phone__text">
                                <h5>+66 00.000.000</h5>
                                <span>support 24/7 time</span>
                            </div>
                        </div>
                    </div>
                    <div class="hero__item set-bg" data-setbg="img/Bag/B7.jpg"style="background-image: url(&quot;C:/xampp/htdocs/Test/img/Bag\B7.jpg&quot;);">
                        <div class="hero__text">
                            <h2>Genuine Bag <br />100%</h2>
                            <p>Free Pickup and Delivery Available</p>
                            <a href="#" class="primary-btn">SHOP NOW</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
<!-- Categories Section Begin -->
<section class="categories">
    <div class="container">
        <div class="row">
            <div class="categories__slider owl-carousel">
                <div class="col-lg-3">
                    <div class="categories__item set-bg" data-setbg="img/Bag/B2.jpg">
                        <h5><a href="#">Crossbody Bag</a></h5>
                    </div>
                </div>
                <div class="col-lg-3">
                    <div class="categories__item set-bg" data-setbg="img/Bag/B3.jpg">
                        <h5><a href="#">Fanny Pack</a></h5>
                    </div>
                </div>
                <div class="col-lg-3">
                    <div class="categories__item set-bg" data-setbg="img/Bag/B4.jpg">
                        <h5><a href="#">Waist Bag</a></h5>
                    </div>
                </div>
                <div class="col-lg-3">
                    <div class="categories__item set-bg" data-setbg="img/Bag/B5.jpg">
                        <h5><a href="#">Waterproof Bag</a></h5>
                    </div>
                </div>
                <div class="col-lg-3">
                    <div class="categories__item set-bg" data-setbg="img/Bag/B6.jpg">
                        <h5><a href="#">School Bag</a></h5>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
<!-- Categories Section End -->

    <!-- Js Plugins -->
    <script src="js/jquery-3.3.1.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/jquery.nice-select.min.js"></script>
    <script src="js/jquery-ui.min.js"></script>
    <script src="js/jquery.slicknav.js"></script>
    <script src="js/mixitup.min.js"></script>
    <script src="js/owl.carousel.min.js"></script>
    <script src="js/main.js"></script>



</body>

</html>