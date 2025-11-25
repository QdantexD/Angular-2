import { Component, Input, OnInit, ElementRef, ViewChild, AfterViewInit } from '@angular/core';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

export interface Game {
  id: number;
  title: string;
  subtitle?: string;
  description: string;
  image: string;
  category: string;
  color: string;
  price?: string;
  originalPrice?: string;
  discount?: number;
  badge?: 'NEW' | 'PREORDER' | 'FREE' | 'SALE';
  logo?: string;
  isFree?: boolean;
  animationDirection?: 'left' | 'right';
}

@Component({
  selector: 'app-game-card',
  templateUrl: './game-card.component.html',
  styleUrls: ['./game-card.component.scss']
})
export class GameCardComponent implements OnInit, AfterViewInit {
  @Input() game!: Game;
  @ViewChild('card', { static: false }) cardRef!: ElementRef;
  @ViewChild('image', { static: false }) imageRef!: ElementRef;

  ngOnInit(): void {}

  ngAfterViewInit(): void {
    this.initAnimations();
  }

  private initAnimations(): void {
    if (!this.cardRef?.nativeElement) return;

    const card = this.cardRef.nativeElement;
    const direction = this.game.animationDirection || (this.game.id % 2 === 0 ? 'right' : 'left');
    const xOffset = direction === 'left' ? -400 : 400;
    const parallaxSpeed = 0.15 + (this.game.id % 3) * 0.1;

    gsap.set(card, {
      opacity: 0,
      x: xOffset,
      y: 50,
      scale: 0.9,
      rotationY: direction === 'left' ? -20 : 20
    });

    // Entrance animation
    gsap.to(card, {
      opacity: 1,
      x: 0,
      y: 0,
      scale: 1,
      rotationY: 0,
      duration: 1,
      ease: 'power3.out',
      scrollTrigger: {
        trigger: card,
        start: 'top 85%',
        toggleActions: 'play none none reverse',
        once: true
      }
    });

    // Smooth Parallax Effect - Individual card parallax
    gsap.to(card, {
      y: -80 * parallaxSpeed,
      scrollTrigger: {
        trigger: card,
        start: 'top bottom',
        end: 'bottom top',
        scrub: 2
      }
    });

    // Image parallax - subtle movement
    if (this.imageRef?.nativeElement) {
      gsap.to(this.imageRef.nativeElement, {
        y: -40 * parallaxSpeed,
        scrollTrigger: {
          trigger: card,
          start: 'top bottom',
          end: 'bottom top',
          scrub: 2
        }
      });

      card.addEventListener('mouseenter', () => {
        gsap.to(card, {
          y: -15,
          scale: 1.05,
          rotationY: 0,
          rotationX: 0,
          duration: 0.4,
          ease: 'power2.out'
        });
        gsap.to(this.imageRef.nativeElement, {
          scale: 1.2,
          duration: 0.4,
          ease: 'power2.out'
        });
      });

      card.addEventListener('mouseleave', () => {
        gsap.to(card, {
          y: 0,
          scale: 1,
          duration: 0.4,
          ease: 'power2.out'
        });
        gsap.to(this.imageRef.nativeElement, {
          scale: 1,
          duration: 0.4,
          ease: 'power2.out'
        });
      });
    }

    // Continuous floating animation
    gsap.to(card, {
      y: '+=8',
      rotationZ: (direction === 'left' ? -1 : 1) * 1.5,
      duration: 4 + (this.game.id * 0.1),
      repeat: -1,
      yoyo: true,
      ease: 'sine.inOut'
    });
  }
}

