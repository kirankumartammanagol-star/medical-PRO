import React from 'react';

const footer = {
    quickLinks: [
        { label: 'Browse Jobs', href: '#jobs' },
        { label: 'For Hospitals', href: '#employers' },
        { label: 'Platform Features', href: '#features' },
        { label: 'Resources', href: '#resources' },
        { label: 'Privacy Policy', href: '#' },
        { label: 'Terms of Service', href: '#' },
        { label: 'Contact Us', href: '#contact' },
    ],
    specializations: ['Cardiology', 'Neurology', 'Orthopedics', 'Pediatrics', 'Oncology', 'Radiology', 'Emergency Medicine'],
    social: [
        {
            name: 'LinkedIn',
            href: '#',
            icon: (
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                    <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z" />
                    <rect x="2" y="9" width="4" height="12" /><circle cx="4" cy="4" r="2" />
                </svg>
            ),
        },
        {
            name: 'Twitter',
            href: '#',
            icon: (
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                    <path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z" />
                </svg>
            ),
        },
        {
            name: 'Instagram',
            href: '#',
            icon: (
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
                    <rect x="2" y="2" width="20" height="20" rx="5" ry="5" />
                    <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z" />
                    <line x1="17.5" y1="6.5" x2="17.51" y2="6.5" />
                </svg>
            ),
        },
        {
            name: 'YouTube',
            href: '#',
            icon: (
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                    <path d="M22.54 6.42a2.78 2.78 0 0 0-1.95-1.96C18.88 4 12 4 12 4s-6.88 0-8.59.46a2.78 2.78 0 0 0-1.95 1.96A29 29 0 0 0 1 12a29 29 0 0 0 .46 5.58A2.78 2.78 0 0 0 3.41 19.6C5.12 20 12 20 12 20s6.88 0 8.59-.4a2.78 2.78 0 0 0 1.95-1.95A29 29 0 0 0 23 12a29 29 0 0 0-.46-5.58z" />
                    <polygon fill="white" points="9.75 15.02 15.5 12 9.75 8.98 9.75 15.02" />
                </svg>
            ),
        },
    ],
};

const Footer = () => (
    <footer className="bg-slate-900 text-white" id="contact" aria-label="Site footer">
        {/* Top section */}
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12">
            {/* Brand */}
            <div className="lg:col-span-1">
                <div className="flex items-center gap-3 mb-5">
                    <div className="w-10 h-10 rounded-xl flex items-center justify-center bg-gradient-to-br from-sky-500 to-teal-400 shadow-lg">
                        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                            <path d="M12 2L12 22M2 12L22 12" stroke="white" strokeWidth="3.5" strokeLinecap="round" />
                        </svg>
                    </div>
                    <span className="font-bold text-lg">
                        HealthCareer <span className="gradient-text">Pro</span>
                    </span>
                </div>
                <p className="text-slate-400 text-sm leading-relaxed mb-6">
                    India's #1 AI-powered healthcare recruitment platform connecting 50,000+ professionals with verified hospitals.
                </p>
                {/* Social links */}
                <div className="flex gap-3">
                    {footer.social.map((s) => (
                        <a
                            key={s.name}
                            href={s.href}
                            className="w-10 h-10 rounded-xl bg-slate-800 flex items-center justify-center text-slate-400 hover:bg-sky-500 hover:text-white transition-all duration-200 hover:-translate-y-1"
                            aria-label={`Visit our ${s.name} page`}
                        >
                            {s.icon}
                        </a>
                    ))}
                </div>
            </div>

            {/* Quick Links */}
            <div>
                <h3 className="font-bold text-white mb-5 text-sm uppercase tracking-wider">Quick Links</h3>
                <ul className="space-y-3" role="list">
                    {footer.quickLinks.map((link) => (
                        <li key={link.label}>
                            <a
                                href={link.href}
                                className="text-slate-400 hover:text-sky-400 transition-colors text-sm flex items-center gap-2 group"
                            >
                                <span className="w-1.5 h-1.5 rounded-full bg-sky-500 opacity-0 group-hover:opacity-100 transition-opacity" aria-hidden="true"></span>
                                {link.label}
                            </a>
                        </li>
                    ))}
                </ul>
            </div>

            {/* Specializations */}
            <div>
                <h3 className="font-bold text-white mb-5 text-sm uppercase tracking-wider">Browse By Specialty</h3>
                <ul className="space-y-3" role="list">
                    {footer.specializations.map((s) => (
                        <li key={s}>
                            <a href="#" className="text-slate-400 hover:text-sky-400 transition-colors text-sm flex items-center gap-2 group">
                                <span className="w-1.5 h-1.5 rounded-full bg-teal-500 opacity-0 group-hover:opacity-100 transition-opacity" aria-hidden="true"></span>
                                {s}
                            </a>
                        </li>
                    ))}
                </ul>
            </div>

            {/* Contact / Newsletter */}
            <div>
                <h3 className="font-bold text-white mb-5 text-sm uppercase tracking-wider">Stay Updated</h3>
                <p className="text-slate-400 text-sm mb-4">Get the latest healthcare job alerts and platform updates.</p>
                <div className="flex gap-2 mb-6">
                    <input
                        type="email"
                        placeholder="Your email"
                        className="flex-1 px-4 py-2.5 rounded-xl bg-slate-800 border border-slate-700 text-white text-sm placeholder-slate-500 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500 transition-colors"
                        aria-label="Email address for newsletter"
                    />
                    <button
                        className="btn-ripple px-4 py-2.5 bg-gradient-to-r from-sky-500 to-teal-400 text-white rounded-xl text-sm font-semibold hover:shadow-lg transition-all duration-200"
                        aria-label="Subscribe to newsletter"
                    >
                        Go
                    </button>
                </div>

                <div className="space-y-2 text-sm text-slate-400">
                    <div className="flex items-center gap-2">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                            <path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z" stroke="#0EA5E9" strokeWidth="2" />
                            <circle cx="12" cy="10" r="3" stroke="#0EA5E9" strokeWidth="2" />
                        </svg>
                        <span>Mumbai, Maharashtra, India</span>
                    </div>
                    <div className="flex items-center gap-2">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                            <path d="M3 8l7.89 5.26a2 2 0 0 0 2.22 0L21 8M5 19h14a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2z" stroke="#0EA5E9" strokeWidth="2" />
                        </svg>
                        <span>hello@healthcareerpro.in</span>
                    </div>
                </div>
            </div>
        </div>

        {/* Bottom bar */}
        <div className="border-t border-slate-800">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-5 flex flex-col sm:flex-row items-center justify-between gap-3">
                <p className="text-slate-500 text-sm">© 2026 HealthCareer Pro. All rights reserved.</p>
                <div className="flex items-center gap-2">
                    <span className="w-2 h-2 bg-green-500 rounded-full animate-pulse" aria-hidden="true"></span>
                    <span className="text-slate-400 text-xs">All systems operational</span>
                </div>
                <div className="flex gap-1">
                    <span className="text-xs text-slate-500">Made with</span>
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="#EF4444" className="mx-1" aria-hidden="true">
                        <path d="M12 21.593C-4.667 11.538 4.2 0 12 0c7.8 0 16.667 11.538 0 21.593z" />
                    </svg>
                    <span className="text-xs text-slate-500">for Healthcare</span>
                </div>
            </div>
        </div>
    </footer>
);

export default Footer;
