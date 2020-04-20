
<?php
include'header.php';
?>
<!-- CSS For Slider Start-->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/1.19.0/TweenMax.min.js"></script>
   <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
  <style>
 


.accordion-slider {
  width: 100%;
  font-size: 0;
  background: #f5f5f5;
}

.accordion-slider .box.first-box {
  background: #000 url(img/slider/1.jpg) no-repeat center center;
  background-size: cover;
}

.accordion-slider .box.second-box {
  background: #000 url(img/slider/2.jpg) no-repeat center center;
  background-size: cover;
}

.accordion-slider .box.third-box {
  background: #000 url(img/slider/3.jpg) no-repeat center center;
  background-size: cover;
}

.accordion-slider .box {
  display: block;
  width: 33.333%;
  font-size: 18px;
  min-height: 400px;
  height: 100vh;
  position: relative;
  float: left;
}

.accordion-slider .box > .inner {
  position: absolute;
  top: 50%;
  -webkit-transform: translateY(-50%);
  transform: translateY(-50%);
}

.accordion-slider-title {
  color: #fff;
  opacity: 0;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-top: 0;
}

.accordion-slider-content {
  opacity: 0;
  width: 100%;
  max-width: 400px;
  position: relative;
  color: #fff;
}

@media screen and (max-width: 549px) {
  .accordion-slider-title,
  .accordion-slider-content {
    opacity: 1;
    text-align: center;
    width: 100%;
    max-width: 100%;
  }
  .site-footer {
    display: block;
  }
  .accordion-slider .box {
    float: none;
    width: 100%;
    text-align: center;
    min-height: 200px;
    height: 50vh;
  }
  .accordion-slider .box > .inner {
    width: 100%;
  }
}



#heading {
  font-family: 'Open Sans', sans-serif;
  color: #555;
  text-decoration: none;
  text-transform: uppercase;
  font-size: 40px;
  font-weight: 800;
  letter-spacing: -3px;
  line-height: 1;
  text-shadow: #EDEDED 3px 2px 0;
 
}

  </style>
  <!-- CSS For Slider End-->
  
  
    <!-- banner part start-->
    <section class="banner_part">
        <div class="container">
            <div class="row">
                <div class="col-lg-6">
                    <div class="banner_text">
                        <div class="banner_text_iner">
                            <h5>ARCHITECTURE + DESIGN</h5>
                            <h1>HEAVEN X LEATEST
                                PROJECT</h1>
                            <p>Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor
                                incididunt ut labore et dolore magna aliqua.</p>
                            <div class="banner_btn">
                                <a href="#" class="btn_1">learn more <span><img src="img/icon/left.svg" alt=""></span>
                                </a>
                            </div>
                        </div>
                        <div class="banner_text_iner">
                            <h5>DESIGN + ARCHITECTURE</h5>
                            <h1>HEAVEN X LEATEST
                                PROJECT</h1>
                            <p>Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor
                                incididunt ut labore et dolore magna aliqua.</p>
                            <div class="banner_btn">
                                <a href="#" class="btn_1">learn more <span><img src="img/icon/left.svg" alt=""></span>
                                </a>
                            </div>
                        </div>
                        <div class="banner_text_iner">
                            <h5>ARCHITECTURE + DESIGN</h5>
                            <h1>HEAVEN X LEATEST
                                PROJECT</h1>
                            <p>Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor
                                incididunt ut labore et dolore magna aliqua.</p>
                            <div class="banner_btn">
                                <a href="#" class="btn_1">learn more <span><img src="img/icon/left.svg" alt=""></span>
                                </a>
                            </div>
                        </div>
                    </div>
                    <div class="nav next"><a href="#"><span class="flaticon-left-arrow"></span></a></div>
                    <div class="nav prev"><a href="#"><span class="flaticon-right-arrow"></span></a></div>
                </div>
            </div>
        </div>
    </section>
    <!-- banner part start-->

    <!-- banner part start-->
    <div class="our_speciality">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="single_special_part border_left">
                        <img src="img/icon/special_1.svg" alt="">
                        <div class="single_special_text">
                            <h3>Inovative</h3>
                            <p>Living Over He god living Creature that appear place</p>
                        </div>
                    </div>
                    <div class="single_special_part border_left">
                        <img src="img/icon/special_2.svg" alt="">
                        <div class="single_special_text">
                            <h3>Inovative</h3>
                            <p>Living Over He god living Creature that appear place</p>
                        </div>
                    </div>
                    <div class="single_special_part border_left">
                        <img src="img/icon/special_3.svg" alt="">
                        <div class="single_special_text">
                            <h3>Inovative</h3>
                            <p>Living Over He god living Creature that appear place</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- banner part start-->

    <!-- about part start-->
    <div class="about_part section_bg">
        <div class="container-fluid">
            <div class="row justify-content-end">
                <div class="col-lg-4 col-md-6">
                    <div class="about_part_text">
                        <h2>About Us</h2>
                        <p>‘HIGH TECH’ is a company dedicated to Internet of things (IoT), which is making its marks across business and consumer sectors.
We are proud of being a part of this exciting trend with  IoT business, and willing to put ourselves at the forefront of innovation, consumed with imaginations and challenging spirit to advance its IoT technology.
If your need to materialize your potential ideas is where this trend goes, please contact us for partnership. We welcome this opportunity to be one you will be proud of.
</p>
                        <a href="about_us.php" class="btn_1">View more <span><img src="img/icon/left.svg" alt=""></span> </a>
                    </div>
                </div>
                <div class="col-lg-7 col-md-6">
                    <div class="about_img">
                        <img src="img/about_overlay.png" alt="#">
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- about part end-->


    <!-- service part start-->
    <section class="service_part">
	<center><h1 id="heading">Gallery</h1></center><br>
        <div class="container-fluid">
           
			
           <div class="accordion-slider clearfix">
  <div class="box first-box">
    <div class="inner">
      <h2 class="accordion-slider-title"> Photos</h2>
      <p class="accordion-slider-content"><a href="#"><button type="button" class="btn btn-primary">View Photos</button></a></p>
    </div>
  </div>
  <div class="box second-box">
    <div class="inner">
      <h2 class="accordion-slider-title"> Photos</h2>
      <p class="accordion-slider-content"><a href="#" ><button type="button" class="btn btn-primary">View Photos</button></a></p>
    </div>
  </div>
  <div class="box third-box">
    <div class="inner">
      <h2 class="accordion-slider-title"> Photos</h2>
      <p class="accordion-slider-content"><a href="#"><button type="button" class="btn btn-primary">View Photos</button></a></p>
    </div>
  </div>
</div>
        </div>
    </section>
    <!-- service part end-->
<div class="whole-wrap">
<center><h1 id="heading">Our Services</h1></center>
		<div class="container-fluid"style=" padding-left: 70px;
    padding-right: 70px;">
<div class="section-top-border">
				 
			
				<div class="row">
					<div class="col-md-3">
					
						<div class="single-defination">
						<center><img src="img/services/banner03.png"></center><br>
							<center><h4 class="mb-20">Service Provider</h4>
							<p>Our creative and total solution does not just end with the engineering achievements; our various front-end solution and UI/UX developers are one integral part of High Tech, providing the solution you can find in one place.
"Make connections"</p></center>
						</div>
					</div>
					<div class="col-md-3">
					
						<div class="single-defination">
						<center><img src="img/services/banner04.png"></center><br>
							<center><h4 class="mb-20">On-site Engineering</h4>
							<p>Engineering required for installing sensors on the structures such as cultural assets, buildings, bridges and tunnels, are based on our decades of efforts and patents earned by High Tech. We can customize our solution to any condition of your unique projects.
"Be there"</p></center>
						</div>
					</div>
					<div class="col-md-3">
					
						<div class="single-defination">
						<center><img src="img/services/banner01.png"></center><br>
							<center><h4 class="mb-20">Product Manufacturing</h4>
							<p>From the design on the paper to the manufacturing floor, our High Tech developers and engineers are the backbone of quality controls with instant response to better our overall service.
"QA comes second to none, a 5-star promise"</p></center>
						</div>
					</div>
						<div class="col-md-3">
						
						<div class="single-defination">
						<center><img src="img/services/banner02.png"></center><br>
							<center><h4 class="mb-20">Product Design to DevOps</h4>
							<p>Our passion to develop has been the source for our proud flagship of products such as wireless sensors, extremely low-power long-distance end-devices over the last decade. Always, being kept abreast with the latest technology, our innovation philosophy continues for the next decade.
"Be on the edge"</p></center>
						</div>
					</div>
				</div>
			</div>
			</div>
			</div>

    <!-- blog part start-->
    <section class="blog_part">
        <div class="container">
		
            <div class="row justify-content-between">
                <div class="col-lg-7">
                    <div class="section_tittle">
                        <h2>Blog Post</h2>
                        <p>According to the research firm Frost & Sullivan, the estimated size of
                            the orth American used test and measurement equipment market was $446.4</p>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-12">
                    <div class="blog_post_slider owl-carousel">
                        <div class="single_blog_post">
                            <div class="row">
                                <div class="col-lg-7">
                                    <div class="single_img">
                                        <a href="blog.html"><img src="img/blog/blog_1.png" alt="#"></a>

                                    </div>
                                </div>
                                <div class="col-lg-7">
                                    <div class="single_project_text">
                                        <div class="single_project_tittle">
                                            <h4> <a href="blog.html">john deo</a></h4>
                                            <p>Farmar x (ceo)</p>
                                            <span>May 02 2019</span>
                                        </div>
                                        <p>According to the research firm Frost & Sullivan all the estimated size
                                            of the North American used test and measurement equipment market was
                                            $446.4 million 2004 and is estimated to to $654.5 milliocompanies an
                                            governmentsprocured and mt instruments.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="single_blog_post">
                            <div class="row">
                                <div class="col-lg-7">
                                    <div class="single_img">
                                        <a href="blog.html"><img src="img/blog/blog_1.png" alt="#"></a>

                                    </div>
                                </div>
                                <div class="col-lg-7">
                                    <div class="single_project_text">
                                        <div class="single_project_tittle">
                                            <h4> <a href="blog.html">john deo</a></h4>
                                            <p>Farmar x (ceo)</p>
                                            <span>May 02 2019</span>
                                        </div>
                                        <p>According to the research firm Frost & Sullivan all the estimated size
                                            of the North American used test and measurement equipment market was
                                            $446.4 million 2004 and is estimated to to $654.5 milliocompanies an
                                            governmentsprocured and mt instruments.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="single_blog_post">
                            <div class="row">
                                <div class="col-lg-7">
                                    <div class="single_img">
                                        <a href="blog.html"><img src="img/blog/blog_1.png" alt="#"></a>

                                    </div>
                                </div>
                                <div class="col-lg-7">
                                    <div class="single_project_text">
                                        <div class="single_project_tittle">
                                            <h4> <a href="blog.html">john deo</a></h4>
                                            <p>Farmar x (ceo)</p>
                                            <span>May 02 2019</span>
                                        </div>
                                        <p>According to the research firm Frost & Sullivan all the estimated size
                                            of the North American used test and measurement equipment market was
                                            $446.4 million 2004 and is estimated to to $654.5 milliocompanies an
                                            governmentsprocured and mt instruments.</p>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>
                    <div class="slider-counter"></div>
                </div>
            </div>
        </div>
    </section>
    <!-- blog part end-->

    <!-- contact us part start-->
    <section class="contact_us">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="contact_us_iner">
                        <div class="row justify-content-around">
                            <div class="col-lg-4">
                                <div class="contact_us_left_text">
                                    <h4>HighTech</h4>
                                    <span>India</span>
                                    <p>Address</p>
                                    <p>Email: info@gmail.com <br>Phone no: 0000000000000</p>
                                </div>
                            </div>
                            <div class="col-lg-4">
                                <div class="contact_us_right_text">
                                    <h5>Call Directly;</h5>
                                    <h2>(0000000000000)</h2>
                                    <h5>Brand Office</h5>
                                    <span>Address</span>
                                    <h5>Working Hours:</h5>
                                    <p>Monday - Friday / 9.00 PM - 5.00 AM</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- contact us part end-->

    <!-- map us part start-->
    <section class="map_part">
        <div class="container-fluid">
            <div class="row">
                <div class="col-lg-12">
                    <div class="map_iner">
                        <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d15081.49178812641!2d72.9165003!3d19.0912881!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x9650bf3d68eaf334!2sSuprStart%20Ventures%20LLP%20-%20Digital%20Marketing%20Agency!5e0!3m2!1sen!2sin!4v1585127654130!5m2!1sen!2sin" width="100%" height="550" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- map us part end-->
	<!-- JS For Slider Start-->
<script>
jQuery(function($){
    var active;
    var boxes = $('.accordion-slider .box').length;
    var singleBoxWidth = (100 / boxes);
    var collapsedWidth = singleBoxWidth - ( singleBoxWidth / ( boxes - 1 ) );
    var openWidth = 100 - (collapsedWidth * ( boxes - 1 ) );

    function accordionSlider() {
        $('.accordion-slider .box').css('width', 100/boxes + '%' )
        $('.accordion-slider .box').on('mouseenter', function(){
            if ( !$(this).hasClass('active') && $(window).width() >= 550 ){
                //hide active elements
                if( active ){ 
                    TweenLite.to(active.find('.accordion-slider-title'), 0.3, {opacity:0, x:0, overwrite:'all'});
                    TweenLite.to(active.find('.accordion-slider-content'), 0.3, {opacity:0, x:0, overwrite:'all'});
                }
                    
                //introduce new active elements
                var others = $('.accordion-slider .box').not(this);
                active = $(this);
                $(this).addClass('active');
                others.removeClass('active');
                var tl = new TimelineLite();
                tl.to(others, 0.8, {ease: Back.easeOut.config(1.1),width:collapsedWidth + '%'}, 0)
                .to(active, 0.8, {ease: Back.easeOut.config(1.1),width:openWidth + '%'}, 0)
                .to(active.find('.accordion-slider-title'), 0.6, {ease: Back.easeOut.config(1.2),opacity:1, x:100}, 0.3)
                .to(active.find('.accordion-slider-content'), 0.6, {ease: Back.easeOut.config(1.2),x:100, opacity:1}, 0.4);
            }

        });
        $('.accordion-slider .box').on('mouseleave', function(){
            if ( $(window).width() >= 550 ){
                var all = $('.accordion-slider .box');
                var tl = new TimelineLite();
                tl.to(all, 0.8, {ease: Back.easeOut.config(1.1),width: 100/boxes + '%'}, 0)
                .to(active.find('.accordion-slider-title'), 0.3, {opacity:0, x:0, overwrite:'all'}, 0)
                .to(active.find('.accordion-slider-content'), 0.3, {opacity:0, x:0, overwrite:'all'}, 0)
                $(this).removeClass('active');
            }
        });
        if( $(window).width() < 550 ) {
            $('.accordion-slider-title, .accordion-slider-content').removeAttr('style');
            $('.accordion-slider .box').removeClass('active').css('width', '100%');
        }
            
    }

  accordionSlider()

  $(window).resize(function(){accordionSlider()});


});
</script>

<!-- JS For Slider END-->
<!-- JS For Aniomation Start-->
<script>
        window.sr = ScrollReveal();
        sr.reveal('.banner_part', {
          duration: 2000,
          origin:'bottom'
        });
        sr.reveal('.our_speciality', {
          duration: 2000,
          origin:'bottom',
          distance:'300px'
        });
        sr.reveal('.about_part', {
           duration: 2000,
          origin:'bottom',
          distance:'300px'
        });
        sr.reveal('.service_part', {
          duration: 2000,
          origin:'bottom',
          distance:'300px'
        });
        sr.reveal('.blog_part', {
          duration: 2000,
          origin:'bottom',
          distance:'300px'
        });
        sr.reveal('.contact_us', {
          duration: 2000,
          origin:'bottom',
          distance:'300px'
        });
        sr.reveal('.map_part', {
          duration: 2000,
          origin:'bottom',
          distance:'300px'
        });
    </script>
	<!-- JS For Aniomation END-->
   <?php
   include'footer.php';
   ?>