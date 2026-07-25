import React, { useState, useEffect } from 'react';

import AuthModal from './AuthModal';

const Navbar = () => {
    const [scrolled, setScrolled] = useState(false);
    const [menuOpen, setMenuOpen] = useState(false);
    const [authOpen, setAuthOpen] = useState(false);
    const [authTab, setAuthTab] = useState('login');

    useEffect(() => {
        const handleScroll = () => setScrolled(window.scrollY > 20);
        window.addEventListener('scroll', handleScroll);
        return () => window.removeEventListener('scroll', handleScroll);
    }, []);

    const openAuth = (tab) => { setAuthTab(tab); setAuthOpen(true); setMenuOpen(false); };

    const navLinks = ['Home', 'Jobs', 'Employers', 'Features', 'Resources', 'About', 'Contact'];

    return (
        <>
            <nav
                className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${scrolled ? 'glass shadow-lg shadow-sky-100/50 py-3' : 'bg-transparent py-4'
                    }`}
                role="navigation"
                aria-label="Main navigation"
            >
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="flex items-center justify-between h-14">

                        {/* Logo */}
                        <a href="#" className="flex items-center gap-2.5 flex-shrink-0" aria-label="HealthCareer Pro Home">
                            <div className="w-9 h-9 rounded-xl flex items-center justify-center bg-gradient-to-br from-sky-500 to-teal-400 shadow-lg pulse-glow">
                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                                    <path d="M12 2L12 22M2 12L22 12" stroke="white" strokeWidth="3.5" strokeLinecap="round" />
                                </svg>
                            </div>
                            <span className="font-bold text-base text-slate-900 whitespace-nowrap">
                                HealthCareer <span className="gradient-text">Pro</span>
                            </span>
                        </a>

                        {/* Desktop Nav */}
                        <ul className="hidden lg:flex items-center gap-6 xl:gap-8" role="list">
                            {navLinks.map((link) => (
                                <li key={link}>
                                    <a
                                        href={`#${link.toLowerCase()}`}
                                        className="text-slate-600 hover:text-sky-500 font-medium text-sm transition-colors duration-200 relative group whitespace-nowrap"
                                    >
                                        {link}
                                        <span className="absolute -bottom-0.5 left-0 w-0 h-0.5 bg-gradient-to-r from-sky-500 to-teal-400 group-hover:w-full transition-all duration-300 rounded-full" />
                                    </a>
                                </li>
                            ))}
                        </ul>

                        {/* Auth Buttons */}
                        <div className="hidden lg:flex items-center gap-2 flex-shrink-0">
                            <button
                                onClick={() => openAuth('login')}
                                className="px-4 py-2 text-sm font-semibold text-slate-700 hover:text-sky-600 transition-colors duration-200 rounded-xl hover:bg-sky-50"
                                aria-label="Login"
                            >
                                Login
                            </button>
                            <button
                                onClick={() => openAuth('signup')}
                                className="btn-ripple px-5 py-2 text-sm font-semibold text-white bg-gradient-to-r from-sky-500 to-teal-400 rounded-xl hover:shadow-lg hover:shadow-sky-200 hover:-translate-y-0.5 transition-all duration-300"
                                aria-label="Sign Up"
                            >
                                Sign Up
                            </button>
                        </div>

                        {/* Mobile Hamburger */}
                        <button
                            className="lg:hidden p-2 rounded-xl hover:bg-sky-50 transition-colors duration-200"
                            onClick={() => setMenuOpen(!menuOpen)}
                            aria-label={menuOpen ? 'Close menu' : 'Open menu'}
                            aria-expanded={menuOpen}
                        >
                            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                                {menuOpen
                                    ? <path d="M6 18L18 6M6 6l12 12" stroke="#0F172A" strokeWidth="2" strokeLinecap="round" />
                                    : <path d="M4 6h16M4 12h16M4 18h16" stroke="#0F172A" strokeWidth="2" strokeLinecap="round" />
                                }
                            </svg>
                        </button>
                    </div>
                </div>

                {/* Mobile Menu */}
                <>
                    {menuOpen && (
                        <div
                            className="lg:hidden glass border-t border-white/30"
                        >
                            <div className="max-w-7xl mx-auto px-4 py-4">
                                <ul className="flex flex-col gap-1" role="list">
                                    {navLinks.map((link) => (
                                        <li key={link}>
                                            <a
                                                href={`#${link.toLowerCase()}`}
                                                className="flex items-center py-2.5 px-3 text-slate-700 hover:text-sky-500 hover:bg-sky-50 font-medium transition-all duration-200 rounded-xl text-sm"
                                                onClick={() => setMenuOpen(false)}
                                            >
                                                {link}
                                            </a>
                                        </li>
                                    ))}
                                    <li className="flex gap-3 pt-3 mt-1 border-t border-slate-100">
                                        <button
                                            onClick={() => openAuth('login')}
                                            className="flex-1 text-center py-2.5 border border-slate-200 text-slate-700 rounded-xl text-sm font-semibold hover:border-sky-300 transition-colors"
                                        >
                                            Login
                                        </button>
                                        <button
                                            onClick={() => openAuth('signup')}
                                            className="flex-1 text-center py-2.5 bg-gradient-to-r from-sky-500 to-teal-400 text-white rounded-xl text-sm font-semibold"
                                        >
                                            Sign Up
                                        </button>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    )}
                </>
            </nav>

            {/* Auth Modal */}
            <AuthModal isOpen={authOpen} onClose={() => { setAuthOpen(false); }} initialTab={authTab} />
        </>
    );
};

export default Navbar;
