import { Component, OnInit, AfterViewInit, QueryList, ViewChildren, ViewChild, ElementRef } from '@angular/core';
import { Game } from '../game-card/game-card.component';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit, AfterViewInit {
  @ViewChildren('gameCardWrapper') gameCards!: QueryList<ElementRef>;
  @ViewChild('sectionTitle', { static: false }) sectionTitle!: ElementRef;

  games: Game[] = [
    {
      id: 1,
      title: 'World of Warcraft: Midnight',
      subtitle: 'World of Warcraft®: Midnight',
      description: 'Previsto para 2026: ¡Precompra hoy mismo para llevarte el futuro acceso anticipado a los hogares y más cosas!',
      image: 'https://images.unsplash.com/photo-1511512578047-dfb367046420?w=800&h=600&fit=crop',
      category: 'Rol multijugador masivo',
      color: '#f39c12',
      price: '179,00 PEN',
      badge: 'PREORDER',
      logo: 'W',
      animationDirection: 'left'
    },
    {
      id: 2,
      title: 'Diablo IV',
      subtitle: 'Lote de expansión de Diablo® IV',
      description: 'Experimenta la oscuridad definitiva en el RPG de acción más épico de Blizzard.',
      image: 'https://images.unsplash.com/photo-1542751371-adc38448a05e?w=800&h=600&fit=crop',
      category: 'RPG de acción',
      color: '#c0392b',
      price: '211,60 PEN',
      originalPrice: '529,00 PEN',
      discount: 60,
      badge: 'SALE',
      logo: 'D',
      animationDirection: 'right'
    },
    {
      id: 3,
      title: 'Call of Duty: Black Ops 7',
      subtitle: 'Call of Duty®: Black Ops 7 - Edición de Archivo',
      description: 'La experiencia definitiva de Call of Duty con contenido exclusivo y acceso anticipado.',
      image: 'https://images.unsplash.com/photo-1446776653964-20c1d3a81b06?w=800&h=600&fit=crop',
      category: 'Shooter de acción',
      color: '#3498db',
      price: '409,00 PEN',
      badge: 'NEW',
      logo: 'B7',
      animationDirection: 'left'
    },
    {
      id: 4,
      title: 'Overwatch 2',
      subtitle: 'Overwatch® 2',
      description: 'Únete a la batalla épica en el shooter de acción por equipos más popular del mundo.',
      image: 'https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=800&h=600&fit=crop',
      category: 'Acción por equipos',
      color: '#e74c3c',
      isFree: true,
      badge: 'FREE',
      logo: 'OW',
      animationDirection: 'right'
    },
    {
      id: 5,
      title: 'Hearthstone',
      subtitle: 'Hearthstone®',
      description: 'El juego de cartas estratégico más popular. Construye mazos y domina la arena.',
      image: 'https://images.unsplash.com/photo-1518709268805-4e9042af2176?w=800&h=600&fit=crop',
      category: 'Juego de cartas estratégico',
      color: '#9b59b6',
      isFree: true,
      badge: 'FREE',
      logo: 'HS',
      animationDirection: 'left'
    },
    {
      id: 6,
      title: 'Call of Duty: Warzone',
      subtitle: 'Call of Duty®: Warzone',
      description: 'Gratis para todos. La experiencia battle royale definitiva con millones de jugadores.',
      image: 'https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=800&h=600&fit=crop',
      category: 'Shooter de acción',
      color: '#1abc9c',
      isFree: true,
      badge: 'FREE',
      logo: 'WZ',
      animationDirection: 'right'
    },
    {
      id: 7,
      title: 'Diablo Immortal',
      subtitle: 'Diablo Immortal™',
      description: 'Lleva la oscuridad contigo. El RPG de acción de Blizzard ahora en móviles y PC.',
      image: 'https://images.unsplash.com/photo-1511512578047-dfb367046420?w=800&h=600&fit=crop',
      category: 'RPG de acción',
      color: '#8e44ad',
      isFree: true,
      badge: 'FREE',
      logo: 'DI',
      animationDirection: 'left'
    },
    {
      id: 8,
      title: 'Diablo II: Resurrected',
      subtitle: 'Diablo II: Resurrected™',
      description: '¡Ya disponible! El clásico RPG de acción remasterizado con gráficos modernos.',
      image: 'https://images.unsplash.com/photo-1542751371-adc38448a05e?w=800&h=600&fit=crop',
      category: 'RPG de acción',
      color: '#c0392b',
      price: '47,85 PEN',
      originalPrice: '145,00 PEN',
      discount: 67,
      badge: 'SALE',
      logo: 'D2',
      animationDirection: 'right'
    },
    {
      id: 9,
      title: 'Warcraft III: Reforged',
      subtitle: 'Warcraft® III: Reforged',
      description: 'Ya está disponible una nueva actualización principal con mejoras en los gráficos y funcionalidades.',
      image: 'https://images.unsplash.com/photo-1446776653964-20c1d3a81b06?w=800&h=600&fit=crop',
      category: 'Estrategia en tiempo real',
      color: '#16a085',
      price: '54,50 PEN',
      originalPrice: '109,00 PEN',
      discount: 50,
      badge: 'SALE',
      logo: 'W3',
      animationDirection: 'left'
    },
    {
      id: 10,
      title: 'StarCraft Remastered',
      subtitle: 'StarCraft® Remastered',
      description: 'El clásico de estrategia en tiempo real remasterizado. Domina la galaxia.',
      image: 'https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=800&h=600&fit=crop',
      category: 'Estrategia en tiempo real',
      color: '#2980b9',
      price: '27,50 PEN',
      originalPrice: '55,00 PEN',
      discount: 50,
      badge: 'SALE',
      logo: 'SC',
      animationDirection: 'right'
    }
  ];

  ngOnInit(): void {}

  ngAfterViewInit(): void {
    setTimeout(() => {
      this.initTitleAnimation();
      this.initCardAnimations();
    }, 100);
  }

  private initTitleAnimation(): void {
    if (!this.sectionTitle?.nativeElement) return;

    const title = this.sectionTitle.nativeElement;
    const text = title.textContent?.trim() || '';
    
    if (!text) return;
    
    title.innerHTML = text.split('').map((char: string) => {
      return `<span class="char" style="display: inline-block;">${char === ' ' ? '&nbsp;' : char}</span>`;
    }).join('');

    const chars = title.querySelectorAll('.char') as NodeListOf<HTMLElement>;
    
    if (chars.length === 0) return;
    
    gsap.from(chars, {
      opacity: 0,
      y: 20,
      duration: 0.6,
      ease: 'power2.out',
      stagger: {
        amount: 0.4,
        from: 'start'
      },
      scrollTrigger: {
        trigger: title,
        start: 'top 85%',
        toggleActions: 'play none none none',
        once: true
      }
    });

    chars.forEach((char: HTMLElement, index: number) => {
      const offset = (index * 0.1) % 1;
      const amplitude = 2 + (index % 3) * 0.3;
      
      gsap.to(char, {
        y: `+=${amplitude}`,
        rotation: `+=${0.5 + (index % 2) * 0.3}`,
        duration: 3 + (index * 0.1),
        repeat: -1,
        yoyo: true,
        ease: 'sine.inOut',
        delay: offset * 2
      });
    });
  }

  private initCardAnimations(): void {
    const cards = this.gameCards.toArray();
    
    cards.forEach((cardRef, index) => {
      if (!cardRef?.nativeElement) return;
      
      const card = cardRef.nativeElement;
      const game = this.games[index];
      const direction = game.animationDirection || (index % 2 === 0 ? 'right' : 'left');
      const xOffset = direction === 'left' ? -300 : 300;

      gsap.set(card, {
        opacity: 0,
        x: xOffset,
        y: 30,
        scale: 0.95
      });

      gsap.to(card, {
        opacity: 1,
        x: 0,
        y: 0,
        scale: 1,
        duration: 0.8,
        ease: 'power3.out',
        delay: index * 0.05,
        scrollTrigger: {
          trigger: card,
          start: 'top 90%',
          toggleActions: 'play none none reverse',
          once: true
        }
      });

      gsap.to(card, {
        y: '+=5',
        duration: 3 + (index * 0.2),
        repeat: -1,
        yoyo: true,
        ease: 'sine.inOut',
        delay: index * 0.1
      });
    });
  }
}

