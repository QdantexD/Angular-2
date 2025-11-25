import { Component, OnInit, ElementRef, ViewChild, AfterViewInit } from '@angular/core';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

@Component({
  selector: 'app-hero-section',
  templateUrl: './hero-section.component.html',
  styleUrls: ['./hero-section.component.scss']
})
export class HeroSectionComponent implements OnInit, AfterViewInit {
  @ViewChild('heroContent', { static: false }) heroContent!: ElementRef;
  @ViewChild('word1', { static: false }) word1!: ElementRef;
  @ViewChild('word2', { static: false }) word2!: ElementRef;
  @ViewChild('word3', { static: false }) word3!: ElementRef;
  @ViewChild('word4', { static: false }) word4!: ElementRef;
  @ViewChild('heroSubtitle', { static: false }) heroSubtitle!: ElementRef;
  @ViewChild('heroButtons', { static: false }) heroButtons!: ElementRef;

  ngOnInit(): void {}

  ngAfterViewInit(): void {
    setTimeout(() => this.initAnimations(), 100);
  }

  private initAnimations(): void {
    if (!this.word1?.nativeElement) return;

    const words = [
      this.word1.nativeElement,
      this.word2.nativeElement,
      this.word3.nativeElement,
      this.word4.nativeElement
    ].filter(w => w);

    const tl = gsap.timeline();

    // Animate words with dramatic entrance
    words.forEach((word, index) => {
      gsap.set(word, {
        opacity: 0,
        y: 80,
        scale: 0.5,
        rotationX: -90
      });

      tl.to(word, {
        opacity: 1,
        y: 0,
        scale: 1,
        rotationX: 0,
        duration: 1,
        ease: 'back.out(2)',
        delay: index * 0.15
      }, index === 0 ? 0 : '-=0.7');
    });

    // Subtitle animation
    if (this.heroSubtitle?.nativeElement) {
      tl.from(this.heroSubtitle.nativeElement, {
        opacity: 0,
        y: 30,
        duration: 0.8,
        ease: 'power2.out'
      }, '-=0.5');
    }

    // Buttons animation
    if (this.heroButtons?.nativeElement) {
      tl.from(this.heroButtons.nativeElement.children, {
        opacity: 0,
        y: 20,
        scale: 0.9,
        duration: 0.6,
        stagger: 0.15,
        ease: 'back.out(1.5)'
      }, '-=0.4');
    }

    // Continuous glow pulse on main title
    if (this.word3?.nativeElement) {
      gsap.to(this.word3.nativeElement, {
        textShadow: '0 0 20px rgba(0, 240, 255, 1), 0 0 40px rgba(0, 240, 255, 0.8), 0 0 60px rgba(0, 240, 255, 0.6)',
        duration: 2,
        repeat: -1,
        yoyo: true,
        ease: 'sine.inOut'
      });
    }

    // Parallax effect
    if (this.heroContent?.nativeElement) {
      gsap.to(this.heroContent.nativeElement, {
        y: -60,
        scrollTrigger: {
          trigger: this.heroContent.nativeElement,
          start: 'top top',
          end: 'bottom top',
          scrub: 1
        }
      });
    }
  }
}

