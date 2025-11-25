import { Component, OnInit, HostListener, ElementRef, ViewChild, AfterViewInit } from '@angular/core';
import { gsap } from 'gsap';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit, AfterViewInit {
  @ViewChild('downloadLink', { static: false }) downloadLink!: ElementRef;
  @ViewChild('supportLink', { static: false }) supportLink!: ElementRef;
  @ViewChild('accountLink', { static: false }) accountLink!: ElementRef;
  @ViewChild('specialOffer', { static: false }) specialOffer!: ElementRef;
  @ViewChild('searchContainer', { static: false }) searchContainer!: ElementRef;
  @ViewChild('balanceLink', { static: false }) balanceLink!: ElementRef;

  isScrolled = false;
  games = ['Warcraft', 'Diablo', 'Overwatch', 'Hearthstone', 'StarCraft'];

  ngOnInit(): void {}

  ngAfterViewInit(): void {
    setTimeout(() => this.initAnimations(), 100);
  }

  @HostListener('window:scroll', ['$event'])
  onScroll(): void {
    this.isScrolled = window.scrollY > 50;
  }

  private initAnimations(): void {
    const topBar = document.querySelector('.header-top-bar');
    const navBar = document.querySelector('.header-nav-bar');
    const logo = document.querySelector('.top-bar-logo');
    const utilLinks = document.querySelectorAll('.util-link');
    const gameLinks = document.querySelectorAll('.nav-game-link');
    const allSpans = document.querySelectorAll('.header span');
    
    // Set initial visible state first - CRITICAL for visibility
    if (topBar) {
      gsap.set(topBar, { opacity: 1, y: 0, visibility: 'visible' });
    }
    if (navBar) {
      gsap.set(navBar, { opacity: 1, y: 0, visibility: 'visible' });
    }
    if (logo) {
      gsap.set(logo, { opacity: 1, scale: 1, visibility: 'visible' });
    }
    
    // Ensure all spans are visible
    allSpans.forEach((span) => {
      gsap.set(span, { opacity: 1, visibility: 'visible', display: 'inline-block' });
    });
    
    // Ensure all links are visible
    utilLinks.forEach((link) => {
      gsap.set(link, { opacity: 1, x: 0, visibility: 'visible' });
    });
    
    gameLinks.forEach((link) => {
      gsap.set(link, { opacity: 1, y: 0, visibility: 'visible' });
    });
    
    if (topBar && navBar) {
      const tl = gsap.timeline({ defaults: { ease: 'power3.out' } });
      
      // Top bar entrance (from slightly above)
      tl.from(topBar, {
        y: -30,
        opacity: 0,
        duration: 0.6,
        ease: 'power3.out'
      })
      // Logo animation
      .from(logo, {
        scale: 0.9,
        opacity: 0,
        duration: 0.5,
        ease: 'back.out(1.5)'
      }, '-=0.3')
      // Utility links
      .from(utilLinks, {
        x: -15,
        opacity: 0,
        duration: 0.4,
        stagger: 0.08,
        ease: 'power2.out'
      }, '-=0.2')
      // Nav bar entrance
      .from(navBar, {
        y: -20,
        opacity: 0,
        duration: 0.5,
        ease: 'power3.out'
      }, '-=0.1')
      // Game links
      .from(gameLinks, {
        y: -10,
        opacity: 0,
        duration: 0.4,
        stagger: 0.06,
        ease: 'power2.out'
      }, '-=0.3');

      // Logo icon continuous glow
      const logoIcon = document.querySelector('.logo-icon');
      if (logoIcon) {
        gsap.to(logoIcon, {
          opacity: 0.8,
          duration: 2,
          repeat: -1,
          yoyo: true,
          ease: 'sine.inOut'
        });
      }
    }
  }

  onGameHover(event: MouseEvent): void {
    const element = event.currentTarget as HTMLElement;
    const arrow = element.querySelector('.nav-arrow');
    
    gsap.to(element, {
      y: -2,
      duration: 0.3,
      ease: 'power2.out'
    });
    
    if (arrow) {
      gsap.to(arrow, {
        y: 2,
        duration: 0.3,
        ease: 'power2.out'
      });
    }
  }

  onGameLeave(event: MouseEvent): void {
    const element = event.currentTarget as HTMLElement;
    const arrow = element.querySelector('.nav-arrow');
    
    gsap.to(element, {
      y: 0,
      duration: 0.3,
      ease: 'power2.out'
    });
    
    if (arrow) {
      gsap.to(arrow, {
        y: 0,
        duration: 0.3,
        ease: 'power2.out'
      });
    }
  }

  onSearchFocus(): void {
    const container = this.searchContainer?.nativeElement;
    if (container) {
      gsap.to(container, {
        scale: 1.02,
        boxShadow: '0 0 20px rgba(0, 240, 255, 0.4)',
        duration: 0.3,
        ease: 'power2.out'
      });
    }
  }

  onSearchBlur(): void {
    const container = this.searchContainer?.nativeElement;
    if (container) {
      gsap.to(container, {
        scale: 1,
        boxShadow: '0 0 0px rgba(0, 240, 255, 0)',
        duration: 0.3,
        ease: 'power2.out'
      });
    }
  }
}

